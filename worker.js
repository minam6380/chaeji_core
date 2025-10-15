export default {
  async fetch(request, env) {
    if (request.method !== 'POST') return new Response('Only POST', { status: 405 });

    try {
      const body = await request.json();
      const { title, start, end, location = '', desc = '' } = body || {};
      if (!title || !start || !end) {
        return new Response(JSON.stringify({ status: 'ERROR', message: 'MISSING_FIELDS' }), {
          status: 400, headers: { 'Content-Type': 'application/json' }
        });
      }

      const res = await fetch(env.APPS_SCRIPT_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          secret: env.SHARED_SECRET, title, start, end, location, desc
        })
      });

      const text = await res.text();
      return new Response(text, { status: res.status, headers: { 'Content-Type': 'application/json' } });
    } catch (e) {
      return new Response(JSON.stringify({ status: 'ERROR', message: String(e) }), {
        status: 500, headers: { 'Content-Type': 'application/json' }
      });
    }
  }
};
