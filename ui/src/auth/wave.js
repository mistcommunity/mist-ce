export const waves = [];
const duration = 300;

function up() {
  waves.forEach(wave => {
    wave.up();
  });
}

export function Wave(x, y, color, opacity) {
  waves.push(this);
  this.element = document.createElement('div');
  this.element.style.left = `calc(${x}px - 2000px)`;
  this.element.style.top = `calc(${y}px - 2000px)`;
  this.element.style.backgroundColor = color;
  this.element.style.opacity = opacity;
  this.element.setAttribute('touch-action', 'none');
  this.element.setAttribute('class', 'wave');
  this.element.addEventListener('up', up);

  document.body.appendChild(this.element);

  this.scale = this.element.animate([{ transform: 'scale(0)' }, { transform: 'scale(1)' }], {
    duration,
    easing: 'cubic-bezier(0.3, 0.2, 1.0, 0.2)',
    fill: 'forwards',
  });
}
Wave.prototype = {
  up() {
    this.up = () => {};
    this.opacity = this.element.animate([{ opacity: 0.66 }, { opacity: 0 }], {
      duration,
      fill: 'forwards',
    });
    this.opacity.onfinish = () => {
      this.element.remove();
      waves.splice(waves.indexOf(this), 1);
    };
  },
};

document.body.addEventListener('up', up);
