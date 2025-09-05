'use client';

import { useEffect, useState } from 'react';

export default function HealthStatusPage() {
  const [status, setStatus] = useState('Loading...');
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchHealth = async () => {
      try {
        const res = await fetch('http://localhost:8000/api/health');
        if (!res.ok) throw new Error(`Error: ${res.status}`);
        const data = await res.json();
        setStatus(data.status);
      } catch (err) {
        setError('Failed to fetch health check');
        setStatus('Unavailable');
      }
    };

    fetchHealth();
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>API Health Status</h1>
      <p>Status: {status}</p>
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}

