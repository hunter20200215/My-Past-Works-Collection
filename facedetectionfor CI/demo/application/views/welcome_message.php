<?php
defined('BASEPATH') OR exit('No direct script access allowed');
?><!DOCTYPE html>
<html lang="en">
<head>
  <script src="detect/js/face-api.js"></script>
  <script src="detect/js/commons.js"></script>
  <script src="detect/js/faceDetectionControls.js"></script>
  <link rel="stylesheet" href="detect/styles.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.css">
  <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js"></script>
</head>
<body>
  <div id="navbar"></div>
  <div class="center-content page-container">

  <div  style=font-size:30px id="detect-count"></div>
    <div style="position: relative" class="margin">
      <video onloadedmetadata="onPlay(this)" id="inputVideo" autoplay muted playsinline></video>
      <canvas id="overlay" />
    </div>

  
  </body>

  <script>
    let forwardTimes = []
    let predictedAges = []
    let withBoxes = true

    function onChangeHideBoundingBoxes(e) {
      withBoxes = !$(e.target).prop('checked')
    }

    function updateTimeStats(timeInMs) {
      forwardTimes = [timeInMs].concat(forwardTimes).slice(0, 60)
      const avgTimeInMs = forwardTimes.reduce((total, t) => total + t) / forwardTimes.length
      $('#time').val(`${Math.round(avgTimeInMs)} ms`)
      $('#fps').val(`${faceapi.round(1000 / avgTimeInMs)}`)
    }
    function interpolateAgePredictions(ages) {
      count = 0;

        predictedAges = [ages].concat(predictedAges).slice(0, 10);
        avgPredictedAge = predictedAges.reduce((total, a) => total + a) / predictedAges.length;
   
      return avgPredictedAge
    }



    async function onPlay() {
      const videoEl = $('#inputVideo').get(0)

      if(videoEl.paused || videoEl.ended || !isFaceDetectionModelLoaded())
        return setTimeout(() => onPlay())


      const options = getFaceDetectorOptions()

      const ts = Date.now()
   
      const resulta = await faceapi.detectAllFaces(videoEl, options).withFaceExpressions()

      var result = await faceapi.detectAllFaces(videoEl, options)
        .withAgeAndGender()
        .withFaceExpressions()

        updateTimeStats(Date.now() - ts)

      if (result) {
        const canvas = $('#overlay').get(0)
        const dims = faceapi.matchDimensions(canvas, videoEl, true)

        const resizedResult = faceapi.resizeResults(result, dims)
        if (withBoxes) {
          faceapi.draw.drawDetections(canvas, resizedResult)
        }

		$('#detect-count').html("Detect Count =" + result.length);      
        resizedResult.forEach(result => {
          const { age, gender, genderProbability, expressions } = result


          var maxValue = 0;
          var faceExpName, faceExpValue;
          for (exp in expressions) {
            if (expressions[exp] > maxValue) {
              maxValue = expressions[exp];
              faceExpName = exp;
              faceExpValue = maxValue;
            }
          }
         
          var interpolatedAge = interpolateAgePredictions(age);
          
          if (age >=18){
            tag='adult';}
            else{
              tag='Child';
            }
          
          new faceapi.draw.DrawTextField(
            [
             
            `${gender} (${faceapi.round(genderProbability)})`, 
            `${tag}`, 
            `${faceapi.round(age, 0)} years`,
              
              
            `${faceExpName}`             
            ],
            result.detection.box.bottomLeft
          ).draw(canvas)
        })
      }

      setTimeout(() => onPlay() )
    }

    

    async function run() {

      await changeFaceDetector(TINY_FACE_DETECTOR)
      await faceapi.loadFaceExpressionModel('/')
      await faceapi.nets.ageGenderNet.load('/')
      changeInputSize(608)
      const stream = await navigator.mediaDevices.getUserMedia({ video: {} })
      const videoEl = $('#inputVideo').get(0)
      videoEl.srcObject = stream
    }

    function updateResults() {}

    $(document).ready(function() {
     
      initFaceDetectionControls()
      run()
    })

  </script>
</body>
</html>