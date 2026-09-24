# Checks the generated site before GitHub Pages receives it.
require "cgi"
require "pathname"
require "uri"

root = Pathname.new(ARGV.fetch(0, "_site")).expand_path
required = %w[index.html blog/index.html showcase/index.html
              projects/index.html 404.html feed.xml sitemap.xml assets/css/global.css
              assets/css/blog.css assets/js/common.js assets/js/blog.js
              assets/images/empty_300x200.png assets/css/images/loading.gif]
errors = required.reject { |path| root.join(path).file? }.map { |path| "Missing output: #{path}" }

Dir.glob(root.join("**/*.html").to_s).each do |file|
  html = File.read(file, encoding: "UTF-8")
  if html.match?(/<head[\s>]/i)
    icon_tags = html.scan(/<link\b[^>]*>/i).select { |tag| tag.match?(/rel=["'](?:icon|shortcut icon|apple-touch-icon)["']/i) }
    expected_icon = "/assets/img/railway-favicon.jpg"
    unless icon_tags.size == 3 && icon_tags.all? { |tag| tag.include?(expected_icon) }
      errors << "#{Pathname.new(file).relative_path_from(root)}: missing or inconsistent site icon"
    end
  end
  html.scan(/(?:href|src|data-src)\s*=\s*["']([^"']*)["']/i).flatten.each do |raw|
    href = CGI.unescapeHTML(raw).split(/[?#]/, 2).first.to_s
    next if href.empty? || href.start_with?("//") || href.match?(/\A[a-z][a-z0-9+.-]*:/i)
    path = URI::DEFAULT_PARSER.unescape(href)
    target = path.start_with?("/") ? root.join(path.delete_prefix("/")) : Pathname.new(file).dirname.join(path)
    next if target.file? || target.join("index.html").file? || Pathname.new("#{target}.html").file?
    errors << "#{Pathname.new(file).relative_path_from(root)}: missing local link #{raw}"
  end
end

%w[.git .obsidian .tools _verification vendor templates bin docs Gemfile Gemfile.lock].each do |path|
  errors << "Development file leaked into output: #{path}" if root.join(path).exist?
end
abort errors.uniq.join("\n") unless errors.empty?
puts "Generated pages, local links, and deployment contents are valid."
