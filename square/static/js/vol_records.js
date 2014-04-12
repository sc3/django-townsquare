//Attempt to create a typeahead field with prefetched JSON data


var volrecords = new Bloodhound(
{
<<<<<<< HEAD
	
	datumTokenizer: Bloodhound.tokenizers.obj.whitespace('dates'),
	queryTokenizer: Bloodhound.tokenizers.whitespace,
	//limit: 100,
	prefetch:
	{
		
		url: '../data/vol.json',
		
		//Necessary when dealing with arrays of strings or nested JSON objects
		filter: function(data)
		{
			
			return $.map(list, function(signup_date)
			{
				return {dates:signup_date};
			});
		
		}
		
	}
	
=======

	datumTokenizer: Bloodhound.tokenizers.whitespace('first_name'),
	queryTokenizer: Bloodhound.tokenizers.whitespace,
	//limit: 100,
	
	prefetch:
	{

		url: '../api/v1/volunteers/?format=json',

		//Necessary when dealing with arrays of strings or nested JSON objects
		filter: function(url)
		{

			return $.map(url, function()
			{
				return this.first_name;
				console.log('Ninjas');
			});
			
			$.get();
			console.log(first_name);

		}
		
		
		
		/*filter: function(data)
		{
			
			var dataset = [];
			
			for(i=0; i<data.length; i++)
			{
				
				dataset.push({
					name: data[i].first_name //+ " " + data[i].last_name
				});
				
				console.log([i]);
			}
			
			
			return dataset;
			console.log('dead Teemos');
			
		}*/

	}

>>>>>>> api_rawstrap
});



//Starting processing/loading of "local" and "prefetch"
volrecords.initialize();


$('#volrec .typeahead').typeahead(null,
{
<<<<<<< HEAD
	
	name: 'vol-records',
	displayKey: 'dates',
	
	
	//'ttAdapter' wraps the suggestion engine in an apdapter compatible with the ta plugin
	source: volrecords.ttAdapter()
	
});
	
=======

	name: 'vol-records',
	displayKey: 'first_name',

	//'ttAdapter' wraps the suggestion engine in an apdapter compatible with the ta plugin
	source: volrecords.ttAdapter()

});

>>>>>>> api_rawstrap
