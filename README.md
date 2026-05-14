# SciNeM-suite

This repository brings together the main pieces of the **SciNeM** stack for heterogeneous information network (HIN) mining,.

| Component | Path | Role |
|-----------|------|------|
| **SciNeM (frontend)** | [`SciNeM-frontend/`](SciNeM-frontend/) | Web application: run (constrained) metapath queries, explore and visualise results. |
| **SciNeM-workflows (backend)** | [`SciNeM-backend/`](SciNeM-backend/) | Spark workflows invoked by the UI: entity ranking (HRank), similarity join and search (LSH), community detection, path searching, and HIN transformation. |
| **Atrapos** | [`Atrapos/`](Atrapos/) | Research prototype that speeds up batches of metapath queries using **sparse matrix multiplication**, an **overlap tree (OTree)** index, and **caching** of intermediate results. |

---

## Clone this repository

```bash
git clone --recursive https://github.com/athenarc/SciNeM-suite.git
cd SciNeM-suite
```

If you already cloned without submodules:

```bash
git submodule update --init --recursive
```

To refresh submodules to their tracked commits after pulling suite changes:

```bash
git submodule update --init --recursive
```

---

## SciNeM-frontend

SciNeM is an open-source data science tool for exploring and analysing HINs. It provides a web UI for constrained metapath-based analyses (e.g. random-walk–style ranking, top‑*k* similar pairs, similarity to a query entity, communities) and scales via Spark on clusters.

**Tech stack:** Java/Spring (JHipster), React, MongoDB.

**Where to look next:** full installation (Ubuntu, Spark, MongoDB), development (`./mvnw`, `npm start`), and production builds are documented in [`SciNeM-frontend/README.md`](SciNeM-frontend/README.md). The UI expects workflow code on disk; in a full deployment that path typically points at a checkout of SciNeM-workflows (see `Constants.java` in that project).

---

## SciNeM-backend

It contains the **SciNeM-workflows** Spark jobs used by the SciNeM application: ranking, similarity join/search, community detection, path searching, and related configuration (`config.properties`, `analysis/analysis.sh`, JSON configs).

**Tech stack:** Python, Apache Spark.

**Where to look next:** HDFS/local paths, `config.json` parameters, and analysis types are described in [`SciNeM-backend/README.md`](SciNeM-backend/README.md).

---

## Atrapos

Atrapos targets the expensive step shared by many HIN mining methods: enumerating node pairs connected under a given **metapath**, often for **many queries** in one query session. It implements:

- **Sparse matrix multiplication** strategies, including sequential and dynamic-programming–style multiplication, with options such as dense/sparse/MNC-style behaviour (see the local README for flags).
- The **OTree** algorithm, which exploits **overlaps between metapaths** to avoid redundant work.
- **Caching** of partial results and configurable cache size, combined with the tree structure, to reuse computation across queries.

Input formats (node attribute tables, sorted edge lists for relations, query files, constraints) and build/run instructions (`make`, `./run …`) are documented in [`Atrapos/README.md`](Atrapos/README.md).

---

## How to cite

### SciNeM

```bibtex
@inproceedings{chatzopoulos2021scinem,
  title={SciNeM: A Scalable Data Science Tool for Heterogeneous Network Mining.},
  author={Chatzopoulos, Serafeim and Vergoulis, Thanasis and Deligiannis, Panagiotis and Skoutas, Dimitrios and Dalamagas, Theodore and Tryfonopoulos, Christos},
  booktitle={EDBT},
  pages={654--657},
  year={2021}
}
```

### Atrapos

```bibtex
@inproceedings{chatzopoulos2023atrapos,
  title={Atrapos: Real-time evaluation of metapath query workloads},
  author={Chatzopoulos, Serafeim and Vergoulis, Thanasis and Skoutas, Dimitrios and Dalamagas, Theodore and Tryfonopoulos, Christos and Karras, Panagiotis},
  booktitle={Proceedings of the ACM Web Conference 2023},
  pages={2487--2498},
  year={2023}
}
```
