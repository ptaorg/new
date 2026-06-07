/* PTA適正化推進委員会 — site.js v49 wrapper */
document.write('<script src="/js/site-v48-original.js?v=48"><\/script>');
document.addEventListener('DOMContentLoaded',function(){
  var cards=document.querySelectorAll('.parent-page .pdf-section .pdf-card');
  var pdfs=['/assets/pdf/pta-membership-inquiry.pdf','/assets/pdf/pta-withdrawal-notice.pdf','/assets/pdf/personal-data-deletion-request.pdf'];
  var labels=['PDFを開く','PDFを開く','PDFを開く'];
  cards.forEach(function(card,i){var a=card.querySelector('a.pdf-btn');if(a&&pdfs[i]){a.href=pdfs[i];a.removeAttribute('target');a.removeAttribute('rel');a.textContent=labels[i];}});
});
