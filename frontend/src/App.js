import React, { useEffect, useState } from "react";

function App() {
  const [clients, setClients] = useState([]);
  const [ventes, setVentes] = useState([]);

  useEffect(() => {
    
    fetch("http://localhost:8000/clients/")
      .then(res => res.json())
      .then(data => {
        setClients(data);

        
        const ventesPromises = data.map(client =>
          fetch(`http://localhost:8000/ventes/client/${client.id}?page=1`)
            .then(res => res.json())
            .then(v => v) 
        );

        
        Promise.all(ventesPromises)
          .then(allVentes => {
            
            setVentes(allVentes.flat());
          })
          .catch(err => console.error("Erreur ventes:", err));
      })
      .catch(err => console.error("Erreur clients:", err));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>LittleBill - Tableau de bord</h1>

      <section>
        <h2>👥 Clients</h2>
        <ul>
          {clients.map((c) => (
            <li key={c.id}>{c.name} ({c.email})</li>
          ))}
        </ul>
      </section>

      <section>
        <h2>💰 Ventes</h2>
        <ul>
          {ventes.map((v, i) => (
            <li key={i}>{v.produit} - {v.montant}€ (Client {v.client_id})</li>
          ))}
        </ul>
      </section>
    </div>
  );
}

export default App;
