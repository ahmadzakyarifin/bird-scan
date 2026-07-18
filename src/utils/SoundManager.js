class SoundManager {
  constructor() {
    this.audioCtx = null;
  }

  init() {
    if (!this.audioCtx) {
      this.audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (this.audioCtx.state === 'suspended') {
      this.audioCtx.resume();
    }
  }

  playClick() {
    this.init();
    if (!this.audioCtx) return;
    
    const osc = this.audioCtx.createOscillator();
    const gainNode = this.audioCtx.createGain();
    
    // Suara click yang lebih "kedap" (deep thud / dull drop)
    osc.type = 'sine';
    osc.frequency.setValueAtTime(150, this.audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(300, this.audioCtx.currentTime + 0.08);
    
    gainNode.gain.setValueAtTime(0, this.audioCtx.currentTime);
    gainNode.gain.linearRampToValueAtTime(0.6, this.audioCtx.currentTime + 0.01);
    gainNode.gain.exponentialRampToValueAtTime(0.001, this.audioCtx.currentTime + 0.15);
    
    osc.connect(gainNode);
    gainNode.connect(this.audioCtx.destination);
    
    osc.start();
    osc.stop(this.audioCtx.currentTime + 0.15);
  }

  playHover() {
    this.init();
    if (!this.audioCtx) return;

    // A gentle "whoosh" sound using a low-frequency oscillator and noise
    const osc = this.audioCtx.createOscillator();
    const gainNode = this.audioCtx.createGain();
    
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(150, this.audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(50, this.audioCtx.currentTime + 0.2);
    
    gainNode.gain.setValueAtTime(0, this.audioCtx.currentTime);
    gainNode.gain.linearRampToValueAtTime(0.05, this.audioCtx.currentTime + 0.1);
    gainNode.gain.linearRampToValueAtTime(0, this.audioCtx.currentTime + 0.3);
    
    osc.connect(gainNode);
    gainNode.connect(this.audioCtx.destination);
    
    osc.start();
    osc.stop(this.audioCtx.currentTime + 0.3);
  }

  playCloudSound() {
    this.init();
    if (!this.audioCtx) return;

    // Suara angin yang sangat "kedap" menggunakan lowpass filter pada white noise
    const bufferSize = this.audioCtx.sampleRate * 2; // 2 seconds
    const buffer = this.audioCtx.createBuffer(1, bufferSize, this.audioCtx.sampleRate);
    const data = buffer.getChannelData(0);
    for (let i = 0; i < bufferSize; i++) {
      data[i] = Math.random() * 2 - 1;
    }
    
    const noiseSource = this.audioCtx.createBufferSource();
    noiseSource.buffer = buffer;
    
    // Lowpass filter memotong frekuensi tinggi, menyisakan gemuruh rendah yang kedap
    const filter = this.audioCtx.createBiquadFilter();
    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(200, this.audioCtx.currentTime); 
    filter.frequency.linearRampToValueAtTime(80, this.audioCtx.currentTime + 1.5);
    
    const gainNode = this.audioCtx.createGain();
    gainNode.gain.setValueAtTime(0, this.audioCtx.currentTime);
    gainNode.gain.linearRampToValueAtTime(0.5, this.audioCtx.currentTime + 0.5);
    gainNode.gain.linearRampToValueAtTime(0, this.audioCtx.currentTime + 1.5);
    
    noiseSource.connect(filter);
    filter.connect(gainNode);
    gainNode.connect(this.audioCtx.destination);
    
    noiseSource.start();
    noiseSource.stop(this.audioCtx.currentTime + 1.5);
  }

  playBirdChirp() {
    this.init();
    if (!this.audioCtx) return;

    const playChirp = () => {
      const osc = this.audioCtx.createOscillator();
      const gainNode = this.audioCtx.createGain();
      
      osc.type = 'sine';
      osc.frequency.setValueAtTime(2500, this.audioCtx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(4000, this.audioCtx.currentTime + 0.1);
      osc.frequency.exponentialRampToValueAtTime(2000, this.audioCtx.currentTime + 0.2);
      
      gainNode.gain.setValueAtTime(0, this.audioCtx.currentTime);
      gainNode.gain.linearRampToValueAtTime(0.03, this.audioCtx.currentTime + 0.05);
      gainNode.gain.exponentialRampToValueAtTime(0.001, this.audioCtx.currentTime + 0.2);
      
      osc.connect(gainNode);
      gainNode.connect(this.audioCtx.destination);
      
      osc.start();
      osc.stop(this.audioCtx.currentTime + 0.2);
    }
    
    // Dua kicauan pendek
    playChirp();
    setTimeout(() => { if (this.audioCtx) playChirp(); }, 250);
  }
}

export const soundManager = new SoundManager();
