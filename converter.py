import os, subprocess

directory = '.'

for filename in os.listdir(directory):
    if filename.lower().endswith(".heic"): 
        print('Converting %s...' % os.path.join(directory, filename))
        subprocess.run(["magick", "%s" % filename, "%s" % (filename[0:-5] + '.jpg')])
        os.popen("rm {}".format(os.path.join(directory, filename)))
        continue
    elif filename.lower().endswith(".mov"):
        print("Video")
        print('Converting %s...' % os.path.join(directory, filename))
        some_command = "ffmpeg -i {} -qscale 0 {} > /dev/null".format(filename, filename[0:-4] + '.mp4')
        p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()  
        p_status = p.wait()
        os.popen("rm {}".format(os.path.join(directory, filename)))
        continue
        
        
        
