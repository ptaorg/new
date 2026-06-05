#!/usr/bin/env node
const fs=require('fs');
const targets=['timeline.html','shizuoka-incident.html','guideline.html','compliance.html'];
const IMG='https://ptaorg.com/assets/og-image-popc-en.png';
const ALT='PTA適正化推進委員会';
function beforeHead(html,frag){if(!/<\/head>/i.test(html))throw new Error('missing head');return html.replace(/<\/head>/i,frag+'\n</head>')}
function canonical(html,file){const href=`https://ptaorg.com/${file}`;const re=/<link\s+[^>]*rel=["']canonical["'][^>]*>\s*/gi;let seen=false;const found=html.match(re)||[];if(!found.length)return html.replace(/<title\b[^>]*>[\s\S]*?<\/title>/i,m=>m+`\n  <link rel="canonical" href="${href}">`);return html.replace(re,()=>{if(!seen){seen=true;return `  <link rel="canonical" href="${href}">\n`}return ''})}
function ensure(html,re,line,afterRe){if(re.test(html))return html;if(afterRe&&afterRe.test(html))return html.replace(afterRe,m=>m+'\n'+line);return beforeHead(html,line)}
for(const file of targets){
 if(!fs.existsSync(file)){console.log('SKIP '+file);continue}
 const before=fs.readFileSync(file,'utf8');let h=before;
 h=canonical(h,file);
 h=ensure(h,/<meta\s+[^>]*property=["']og:image["'][^>]*>/i,`  <meta property="og:image" content="${IMG}">`,/<meta\s+[^>]*property=["']og:url["'][^>]*>/i);
 h=ensure(h,/<meta\s+[^>]*name=["']twitter:image["'][^>]*>/i,`  <meta name="twitter:image" content="${IMG}">`,/<meta\s+[^>]*name=["']twitter:card["'][^>]*>/i);
 h=ensure(h,/<meta\s+[^>]*name=["']twitter:image:alt["'][^>]*>/i,`  <meta name="twitter:image:alt" content="${ALT}">`,/<meta\s+[^>]*name=["']twitter:image["'][^>]*>/i);
 h=ensure(h,/href=["'][^"']*css\/refine\.css[^"']*["']/i,'  <link href="css/refine.css?v=refine1" rel="stylesheet">',/<link\s+[^>]*href=["'][^"']*css\/style\.css[^"']*["'][^>]*>/i);
 if(h!==before){fs.writeFileSync(file,h,'utf8');console.log('UPDATED '+file)}else console.log('OK '+file)
}
