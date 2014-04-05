//Attempt to create a typeahead field with prefetched JSON data


var volrecords = new Bloodhound(
{

	datumTokenizer: Bloodhound.tokenizers.obj.whitespace('objects'),
	queryTokenizer: Bloodhound.tokenizers.whitespace,
	//limit: 100,
	
	prefetch:
	{

		url: '../api/v1/volunteers/?format=json',

		//Necessary when dealing with arrays of strings or nested JSON objects
		/*filter: function(data)
		{

			return $.map(list, function(signup_date)
			{
				return {dates:signup_date};
			});

		}*/

	}

});



//Starting processing/loading of "local" and "prefetch"
volrecords.initialize();


$('#volrec .typeahead').typeahead(null,
{

	name: 'vol-records',
	displayKey: 'objects',


	//'ttAdapter' wraps the suggestion engine in an apdapter compatible with the ta plugin
	source: volrecords.ttAdapter()

});

