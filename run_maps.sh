for file in /data/Twitter\ dataset/geoTwitter20-*.zip; do 
	echo $file
	./src/map.py --input_path="$file" &
	
done
