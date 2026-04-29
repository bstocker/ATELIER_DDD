```mermaid
flowchart LR
    CL["SD-CL-01<br/>Prescription Clinique et Validation<br/><b>Coeur stratégique</b>"]
    PREA["SD-LB-02<br/>Gestion des Échantillons et Conformité Pré-analytique<br/>Support"]
    PRIO["SD-LB-03<br/>Priorisation et Ordonnancement des Analyses<br/><b>Coeur stratégique</b>"]
    ANA["SD-LB-04<br/>Analyse Biologique et Validation des Résultats<br/><b>Coeur stratégique</b>"]
    TH["SD-TH-05<br/>Adaptation Thérapeutique et Collaboration Pluridisciplinaire<br/><b>Coeur stratégique</b>"]
    TR["SD-GV-06<br/>Traçabilité, Sécurité et Conformité Réglementaire<br/>Support"]
    EX["SD-OR-07<br/>Gestion des Exceptions et Astreintes<br/>Support"]
    INT["SD-TE-08<br/>Intégration et Interopérabilité des Systèmes<br/>Générique"]

    CL -->|"Demande validée + contexte clinique"| PRIO
    PRIO -->|"Priorité + ordre de traitement"| PREA
    PREA -->|"Échantillon conforme"| ANA
    ANA -->|"Résultat interprété + recommandations"| TH
    TH -->|"Décision thérapeutique"| CL

    EX -.->|"Cas particulier ou astreinte"| PRIO
    EX -.->|"Escalade biologique"| ANA

    TR -.->|"Traçabilité du circuit"| CL
    TR -.->|"Traçabilité du circuit"| PREA
    TR -.->|"Traçabilité du circuit"| PRIO
    TR -.->|"Traçabilité du circuit"| ANA
    TR -.->|"Traçabilité du circuit"| TH

    INT -.->|"Échanges SIL / DPI / analyseurs"| CL
    INT -.->|"Échanges SIL / DPI / analyseurs"| PRIO
    INT -.->|"Échanges SIL / DPI / analyseurs"| ANA
```
