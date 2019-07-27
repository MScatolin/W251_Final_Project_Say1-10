Possible Comercial uses:
  * Separating speech when multiple people are talking
  * Improve speech-to-text inference (particularly in in noisy environments)
  * Biometric security: digits recognition

Bibliographic Review
 * Visual units and confusion modelling for automatic lip-reading, June 2015. Dominic Howell, Stephen Cox, Barry Theobald
   * 2 datasets of 1 speaker. First only 211 single words (picked to be relevant). Second had 3000 sentences.
   * Use of weighted finite state transducer and phoneme based 
  
 * LIPNET: END-TO-END SENTENCE-LEVEL LIPREADING, December 2016. Yannis M. Assael, Brendan Shillingford, Shimon Whiteson, Nando de Freitas
   * First ANN based model that takes a sentence approach (other than songle words)
   * 95.2% on GRID corpus.
   
 * Lip Reading Sentences in the Wild, December 2017, Joon Son Chung, Andrew Senior, Oriol Vinyals, Andrew Zisserman
   * Limited corpus recognitiion using encoder-decoder architecture with attention.

 * Survey on automatic lip-reading in the era of deep learning, July 2018, Adriana Fernandez-Lopez, Federico M. Sukno. 
   * Survey on several papers on lip-reading using deep learning. Usefull to compare results.
  
 * LARGE-SCALE VISUAL SPEECH RECOGNITION, October 2018. Brendan Shillingford, Yannis Assael, Matthew W. Hoffman, Thomas Paine, Cían Hughes, Utsav Prabhu, Hank Liao, Hasim Sak, Kanishka Rao, Lorrayne Bennett, Marie Mulville, Ben Coppin, Ben Laurie, Andrew Senior, Nando de Freitas
   * Largest database (3886 hours) with open sentence. They were able to achieve WER 40.9% using only video, halving the existing state of the art model.

 * datasets:
   * http://www.robots.ox.ac.uk/~vgg/data/lip_reading/lrw1.html
     * looks promissing, 500 words already classified with 800 to 1000 examples. Need to verifiy if digits are available. Need authorization for usage, which may not be taken in feasible time.
     
   
   
 
