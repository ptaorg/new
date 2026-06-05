#!/usr/bin/env node
const fs=require('fs');
const targets=['timeline.html','shizuoka-incident.html','guideline.html','compliance.html','documents.html','contact.html','board-responses.html'];
const count=(re,s)=>{const m=s.match(re);return m?m.length:0};
let failed=false;
for(const file of targets){
 if(!fs.existsSync(file)){console.log(`SKIP ${file}`);continue}
 const html=fs.readFileSync(file,'utf8');
 const checks={
  canonical:count(/<link\s+[^>]*rel=["']canonical["'][^>]*>/gi,html),
  ogImage:count(/<meta\s+[^>]*property=["']og:image["'][^>]*>/gi,html),
  twitterCard:count(/<meta\s+[^>]*name=["']twitter:card["'][^>]*>/gi,html),
  twitterImage:count(/<meta\s+[^>]*name=["']twitter:image["'][^>]*>/gi,html),
  twitterImageAlt:count(/<meta\s+[^>]*name=["']twitter:image:alt["'][^>]*>/gi,html),
  h1:count(/<h1\b/gi,html),
  siteJs:count(/<script\s+[^>]*src=["'][^"']*js\/site\.js[^"']*["'][^>]*>/gi,html)
 };
 const warn=[];
 if(checks.canonical!==1)warn.push(`canonical=${checks.canonical}`);
 if(checks.ogImage<1)warn.push('og:image missing');
 if(checks.twitterCard<1)warn.push('twitter:card missing');
 if(checks.twitterImage<1)warn.push('twitter:image missing');
 if(checks.twitterImageAlt<1)warn.push('twitter:image:alt missing');
 if(checks.h1<1)warn.push('h1 missing');
 if(checks.siteJs<1)warn.push('site.js missing');
 if(warn.length){failed=true;console.log(`NG ${file}: ${warn.join(', ')}`)}else console.log(`OK ${file}`);
}
if(failed)process.exit(1);
