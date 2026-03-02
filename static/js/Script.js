//Start Camera (Ask permission to use camera)
const video = document.getElementById("video");

navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    });

    //Capture Image from Camera 
function capture() {
    const canvas = document.getElementById("canvas");
    const context = canvas.getContext("2d");

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0);

    const imageData = canvas.toDataURL("image/png");

    //Send image to backend for prediction
    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ image: imageData })
    })

    //Show result on frontend
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText =
         "Emotion: " + data.emotion 
        //  + 
        //  " | Confidence: " + data.confidence + "%"
         ;
    });
}

//Upload Image function
function uploadImage() {
    const fileInput = document.getElementById("upload");
    const file = fileInput.files[0];
    const reader = new FileReader();

    reader.onload = function() {
        fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ image: reader.result })
        })
        .then(res => res.json())
        .then(data => {
            document.getElementById("result").innerText = "Emotion: " + data.emotion;
        });
    };

    reader.readAsDataURL(file);
}