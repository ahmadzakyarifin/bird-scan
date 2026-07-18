const fs = require('fs');
let svg = fs.readFileSync('public/islands/map-outline.svg', 'utf8');

// Remove existing fills and strokes
svg = svg.replace(/fill="[^"]*"/g, '');
svg = svg.replace(/stroke="[^"]*"/g, '');
svg = svg.replace(/stroke-width="[^"]*"/g, '');

// Add our own line style to the <g id="admin1"> group
svg = svg.replace('<g id="admin1">', '<g id="admin1" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" opacity="0.4">');

fs.writeFileSync('public/islands/map-outline.svg', svg);
console.log('SVG Cleaned!');
