document.addEventListener("DOMContentLoaded", () => {
  let recentContainer = document.getElementById("recentContainer");
  fetch("/api/get_recent")
    .then(res => res.json())
    .then(res => res.data)
    .then(res => {
      recentContainer.innerHTML = "";
      Object.entries(res).forEach(([index, data]) => {
        recentContainer.innerHTML += videoCard(data.title, data.duration, data.tags, data.download);
      });
    })
})



function videoCard(title, duration, tags, downloadLink) {
  return `<div class="ui column">
<div class="ui card">
        <video class="player ui placeholder" playsinline controls data-poster="/path/to/poster.jpg" controlslist="nodownload">
          <source src="${downloadLink}" type="video/mp4" />
    </video>
    <div class="content">
      <a class="header">${title}</a>
      <div class="meta">
        <span class="date">${duration}</span>
      </div>
      <div class="description">
        <span><b>Tags:</b>${tags}</span>
      </div>
    </div>
    <div class="extra content">
      <a href="/download?url=${downloadLink}" download>
        <i class="download icon"></i>
        Download
      </a>
    </div>
  </div>
</div>
` 
}
