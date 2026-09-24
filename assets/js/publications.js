(function () {
    var section = document.getElementById('publications');
    if (!section) return;

    var input = section.querySelector('#publication-search');
    var noResults = section.querySelector('#publication-no-results');
    var status = section.querySelector('#publication-search-status');
    var entries = Array.from(section.querySelectorAll('.publication-entry')).map(function (element) {
        return {
            element: element,
            text: element.textContent.toLowerCase().replace(/\s+/g, ' ')
        };
    });

    function filterPublications() {
        var query = input.value.trim().toLowerCase();
        var terms = query.split(/\s+/).filter(Boolean);
        var count = 0;

        entries.forEach(function (entry) {
            var matches = terms.every(function (term) {
                return entry.text.includes(term);
            });
            entry.element.hidden = !matches;
            if (matches) count += 1;
        });

        noResults.hidden = entries.length === 0 || count > 0;
        status.textContent = query ? count + ' matching publication' + (count === 1 ? '.' : 's.') : '';
        // Recheck lazy images when filtering brings a paper into view.
        window.dispatchEvent(new Event('scroll'));
    }

    input.addEventListener('input', filterPublications);
    filterPublications();
})();
