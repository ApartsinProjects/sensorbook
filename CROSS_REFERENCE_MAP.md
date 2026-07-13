# Cross-Reference Map — Building Sensory AI

Progressive-depth concepts that appear in multiple chapters at increasing depth. Each row
lists where a concept is introduced and where it is revisited, so authors link forward and
back instead of re-teaching. Keep in sync when the plan changes.

| Concept | Introduced | Revisited / deepened |
|---|---|---|
| Aleatoric vs epistemic uncertainty | Ch 4 (primer) | Ch 18 (calibration/conformal), Ch 49 (propagation), Ch 66 (shift) |
| Leakage-safe splits (subject/device/site) | Ch 5 | Ch 12, 26, 28, 37, 38, 65 |
| Kalman / Bayesian filtering | Ch 9 | Ch 10-11 (nonlinear, factor graphs), Ch 49 (multi-sensor), Ch 55 (twin+EKF) |
| Factor graphs / GTSAM | Ch 11 | Ch 49 (fusion), Ch 52 (SLAM/VIO) |
| Self-supervised learning | Ch 17 | Ch 19-20 (foundation models), Ch 42 (lidar SSL) |
| State-space models (Mamba) | Ch 16 | Ch 19 (TSFM backbones), App B |
| Foundation models | Ch 19 (time series) | Ch 20 (sensor/wearable), Ch 21-22 (language/agents), Ch 29-33, 36-37, 41, 56, 58 |
| Conformal prediction | Ch 18 | Ch 66 (shift), Ch 72 (frontier) |
| Occupancy / world models | Ch 43 (occupancy) | Ch 53 (world models) |
| Gaussian splatting / neural fields | Ch 51 | Ch 52 (GS-SLAM), Ch 55 (synthetic data) |
| Missing-modality robustness | Ch 48 | Ch 50 (deep fusion), Ch 33 (wearable), Ch 68 (safety) |
| Multimodal / cross-attention fusion | Ch 48-50 | Ch 43 (BEV), Ch 57 (robot perception), Ch 33 |
| Test-time adaptation / domain shift | Ch 66 | Ch 26 (personalization), Ch 32 (subject transfer), Ch 45 (thermal DA) |
| Edge quantization / on-device | Ch 59 | Ch 61 (TinyML), Ch 62 (continual), Ch 63 (batteryless), Ch 20 (on-device FM) |
| Biometric privacy / regulation | Ch 34 | Ch 70 (responsible AI), Ch 25 (location), Ch 47 (RF) |
| Sensor spoofing / functional safety | Ch 68 | Ch 25 (GPS), Ch 44 (radar), Ch 42 (lidar), Ch 71.3 (vehicles) |
| Anomaly detection | Ch 12 (classical) | Ch 37-38 (industrial/ICS), Ch 22 (agentic), Ch 18 (conformal) |
| Micro-Doppler / range-Doppler | Ch 44 | Ch 33 (health radar), Ch 71.6 (security) |
| RUL / prognostics | Ch 36 | Ch 19 (FM embeddings), Ch 71.3 (fleet PdM) |

## Notes
- Cross-references are inserted as inline hyperlinks by the Cross-Reference Architect (Agent #13).
- When a Part or Chapter is renumbered, update this table and run the Book Restructuring Protocol.
