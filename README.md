# Final project for W251 -  Deep Learning in the Cloud and at the Edge 
## UC Berkeley - Master of Information and Data Science Program

#### Authors: 
[Marcus Chen](https://github.com/fa-mc),
[Marcelo Queiroz](https://github.com/MScatolin),
[Sylvia Yang](https://github.com/teleserv),
[Wei Wang](https://github.com/vivi11130704)

This repo contains the code we developed for our final work of the W251 course.

The goal here were to train a deep learning model to do lipreading of a digit dataset [zero,...,nine] without the audio or any other context. 

In the [Articles and References](https://github.com/MScatolin/W251_Final_Project_Say1-10/tree/master/Articles_n_References) directory you will find the articles we used to base this work.

In the [Downloader](https://github.com/MScatolin/W251_Final_Project_Say1-10/tree/master/Downloader) directory you will find the scripts we developed to download and prepare the dataset to use in LipNet model

The [LipNet](https://github.com/MScatolin/W251_Final_Project_Say1-10/tree/master/LipNet) directory was forked from the original code so we could update Tensorflow and Python code to the use in our training machines.

In [Data_examples](https://github.com/MScatolin/W251_Final_Project_Say1-10/tree/master/data_examples) some files of the used training corpus after processed are available.

In [docker](https://github.com/MScatolin/W251_Final_Project_Say1-10/tree/master/docker) we stored code to build the container for our still in progress attempt to implement the final model into the edge device NVIDIA Jetson TX2.

In [images](https://github.com/MScatolin/W251_Final_Project_Say1-10/tree/master/images) there are some resources used in for documentation here.




Navigate the directories for more detailed explanations and tutorials.

Thanks for accesing this code, and feell free to reach any of us out for questions and suggestions. 




Special thanks to:
* [Muhammad Rizki](https://github.com/rizkiarm) for the work on the LipNet model, our main resource here.
* the Multimedia Systems Department of Gdansk University of Technology who publically provided the [MODALITY Corpus](http://www.modality-corpus.org/)


#### See the whitepaper and the slide deck in this dicrectory for more information.
