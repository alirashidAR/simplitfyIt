document.getElementById("generateBtn").addEventListener("click", async function () {
  const text = document.getElementById("text").value;
  const way = document.getElementById("way").value;
  const inputs = document.getElementById("inputs").value;
  const voiceType = document.getElementById("type").value; 
  const resultContainer = document.getElementById("result");

  if (text && way && inputs) {
    const statusMessages = ["Making you summar...", "Working on it...", "Almost there..."];
    let messageIndex = 0;

    
    const intervalId = setInterval(() => {
      resultContainer.innerHTML = `<p>${statusMessages[messageIndex]}</p>`;
      messageIndex = (messageIndex + 1) % statusMessages.length;
    }, 1000);

    try {
      const response = await fetch("http://127.0.0.1:8000/generate_final_video?" +
        new URLSearchParams({
          text: text,
          way: way,
          inputs: inputs,
          type: voiceType  
        }), {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          }
      });

      clearInterval(intervalId);  

      if (response.ok) {
        const videoBlob = await response.blob();
        const videoUrl = URL.createObjectURL(videoBlob);

        
        resultContainer.innerHTML = "";
        
        const downloadLink = document.createElement("a");
        downloadLink.href = videoUrl;
        downloadLink.download = "generated_video.mp4";
        downloadLink.textContent = "Download your video";
        resultContainer.appendChild(downloadLink);

        // Optional: Display the video in a video element
        const videoElement = document.createElement("video");
        videoElement.src = videoUrl;
        videoElement.controls = true;
        videoElement.style.width = "100%";
        resultContainer.appendChild(videoElement);

      } else {
        resultContainer.innerHTML = "<p>Error generating video.</p>";
      }
    } catch (error) {
      clearInterval(intervalId);
      resultContainer.innerHTML = "<p>Error generating video.</p>";
    }

  } else {
    resultContainer.innerHTML = "<p>Please fill in all fields.</p>";
  }
});
