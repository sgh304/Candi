const updateSelects = () => {
    // Updates all selection dropdowns for the current state
    updateOfficeSelect();
    updatePartySelect();
}

const updateOfficeSelect = () => {
    // Updates the office selection dropdown for the current state
    state = $('select[name="state"]').val();
    $.get('api/office/', {state: state}, (offices) => {
        $('select[name="office"]').children().remove();
        $('select[name="office"]').append($('<option>', {value: 'ALL'}).text('All'));
        offices.forEach((office) => {
            $('select[name="office"]').append($('<option>', {value: office}).text(office));
        })
    })
}

const updatePartySelect = () => {
    // Updates the party selection dropdown for the current state
    state = $('select[name="state"]').val();
    $.get('api/party/', {state: state}, (parties) => {
        $('select[name="party"]').children().remove();
        $('select[name="party"]').append($('<option>', {value: 'ALL'}).text('All'));
        parties.forEach((party) => {
            $('select[name="party"]').append($('<option>', {value: party}).text(party));
        })
    })
}

const run = () => {
    // Performs an AJAX request and updates the response data on the page
    state = $('select[name="state"]').val();
    office = $('select[name="office"]').val();
    party = $('select[name="party"]').val();

    $.get('api/candidate/', {state: state, office: office, party: party}, function(data) {
        $('#response').show();
        $('#response--url').text(window.location.origin + '/' + this.url);
        $('#response--data').text(JSON.stringify(data, null, 2));
    })
}