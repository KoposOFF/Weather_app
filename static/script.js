$(document).ready(function() {
    var cities = {{ cities | tojson | safe }};
    $("#city").autocomplete({
        source: cities,
        minLength: 2 // Минимальное количество символов для начала автозаполнения
    });
});
