// 讓「存到照片」頁面在連著相機 Wi-Fi（沒有網路）時也打得開：先用快取，有網路時順便更新快取
const CACHE = "ps135-saver-v2";
const FILES = ["./", "./index.html"];
self.addEventListener("install", e => e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES)).then(() => self.skipWaiting())));
self.addEventListener("activate", e => e.waitUntil(
  caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim())));
self.addEventListener("fetch", e => {
  if (e.request.method !== "GET") return;
  e.respondWith(caches.open(CACHE).then(async c => {
    const hit = await c.match(e.request, { ignoreSearch: true });
    const net = fetch(e.request).then(r => { if (r.ok) c.put(e.request, r.clone()); return r; }).catch(() => null);
    return hit || (await net) || new Response("離線中，這一頁還沒存在手機上", { status: 503, headers: { "Content-Type": "text/plain; charset=utf-8" } });
  }));
});
