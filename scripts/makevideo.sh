# script to create movie from multiple png files
# taken in choronoligcal order

# start at 0
count=0
# take all files named shot - something ordered by date
for f in `ls -rt *.jpg`
# for f in `find . -name "*.jpg" -exec ls -r {} \;`

do
  # get the index in 0000 format
  printf -v counts "%04d" $count
    # link file to a frame_0000  named symbolic link
    ln -s $f frame_$counts.jpg
    # increment counter
  count=`expr $count + 1`
done
# create movie
# slowed down by factor 5
# ffmpeg -f image2 -i frame_%04d.png -vcodec mpeg4 -vf "setpts=5*PTS" movie.mp4
ffmpeg -framerate 500 -i frame_%04d.jpg ../movie.mp4
# remove the links
rm frame_*