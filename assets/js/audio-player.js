// Swaps each native <audio controls> for a player styled by site.css (.audio-player).
// Without this script the browser's own controls still work.
// Used by evanapplegate.com and veryexpensivemaps.com. The file's length is only fetched once the player is near
// the screen, not on page load.
document.querySelectorAll('audio[controls]').forEach((audio) => {
  const clock = (s) => (isFinite(s) ? Math.floor(s / 60) + ':' + String(Math.floor(s % 60)).padStart(2, '0') : '0:00');

  const player = document.createElement('div');
  player.className = 'audio-player';
  player.innerHTML =
    '<button type="button" class="audio-player__toggle" aria-label="Play">' +
    '<svg class="audio-player__play" viewBox="0 0 12 12" aria-hidden="true"><path d="M2.5 1l8.5 5-8.5 5z"/></svg>' +
    '<svg class="audio-player__pause" viewBox="0 0 12 12" aria-hidden="true"><path d="M2 1h3v10H2zM7 1h3v10H7z"/></svg>' +
    '</button>' +
    '<span class="audio-player__time">0:00</span>' +
    '<input class="audio-player__seek" type="range" min="0" max="100" step="0.1" value="0" aria-label="Seek">' +
    '<span class="audio-player__time">0:00</span>';
  const [toggle, current, seek, total] = player.children;

  const showDuration = () => {
    if (!isFinite(audio.duration)) return;
    seek.max = audio.duration;
    total.textContent = clock(audio.duration);
  };
  const showProgress = () => {
    current.textContent = clock(audio.currentTime);
    seek.value = audio.currentTime;
    seek.style.setProperty('--progress', (audio.duration ? (audio.currentTime / audio.duration) * 100 : 0) + '%');
  };
  const showState = () => {
    player.classList.toggle('is-playing', !audio.paused);
    toggle.setAttribute('aria-label', audio.paused ? 'Play' : 'Pause');
  };

  toggle.addEventListener('click', () => (audio.paused ? audio.play() : audio.pause()));
  seek.addEventListener('input', () => {
    audio.currentTime = seek.value;
    showProgress();
  });
  audio.addEventListener('loadedmetadata', showDuration);
  audio.addEventListener('durationchange', showDuration);
  audio.addEventListener('timeupdate', showProgress);
  ['play', 'pause', 'ended'].forEach((e) => audio.addEventListener(e, showState));

  audio.controls = false;
  audio.after(player);
  new IntersectionObserver((entries, io) => {
    if (entries[0].isIntersecting) {
      io.disconnect();
      audio.preload = 'metadata';
    }
  }, { rootMargin: '400px' }).observe(player);
  showDuration();
});
