# Building Sensory AI: Machine Perception of the Physical World

**Hands-On AI Science Series — comprehensive book plan (2026 edition)**
**Working subtitle:** *From Physical Signals to Perceiving, Fusing, and Deploying Machines*
**Target length:** 14 parts · 72 chapters · 400+ sections · 72 labs · exercises, application studies, appendices, and capstone
**Positioning:** a single self-contained volume that works as an undergraduate textbook, a graduate course text, and a working reference manual for researchers and engineers building AI on real sensors.

---

## Who This Book Is For (three audiences, one book)

The book is written to serve three readers at once, using an explicit layering system so each can find their level without a separate volume:

- **Undergraduate students.** Every prerequisite is developed in-book: signals, sampling, probability, estimation, linear algebra, optimization, and a deep-learning refresher are all included (Part I and the appendices), so no prior signal-processing or ML course is strictly required. Foundational sections are marked **[F]**.
- **Graduate students and instructors.** Core method chapters go to research depth, each closing with current literature and open problems. Core material is marked **[C]**, advanced material **[A]**.
- **Researchers and engineers.** The book doubles as a field manual: every chapter names the current state-of-the-art models, the datasets and benchmarks used to evaluate them, the production tools, and the failure modes. Frontier material is marked **[R]** and concentrated in Part V and the frontier chapter, but appears as "Frontier" boxes throughout.

**Level tags** appear on every chapter and every section: **[F]** foundational · **[C]** core · **[A]** advanced · **[R]** research frontier. A reader can traverse only **[F]**/**[C]** for a first course, or follow the **[R]** thread for a frontier survey.

## Book Positioning

*Building Sensory AI* is about AI systems that perceive the physical world through the full spectrum of sensing, not just RGB cameras and microphones: inertial sensors, vibration, radar, lidar, depth, thermal, magnetic, pressure, tactile, RF/Wi-Fi, event cameras, biosignals, environmental sensors, and industrial telemetry, while also integrating cameras and audio when they help. The focus is the complete sensing chain: sensor physics, calibration, synchronization, uncertainty, edge constraints, data quality, representation learning, sensor fusion, deployment, safety, and trustworthy operation.

The book fills the gap between signal processing, embedded systems, IoT, robotics perception, and machine learning. It treats sensors as measurement instruments with biases, noise, drift, and failure modes, not as clean arrays handed to a neural network. It is also the first textbook to integrate the 2023-2026 shift to **foundation models and self-supervised pretraining for sensor and time-series data**, and to **agentic, language-interfaced sensing**, alongside the durable classical foundations.

## Central Thesis

Sensory intelligence is the ability to infer hidden state from noisy physical measurements, and to act on that inference reliably under real-world constraints. The book is organized around six verbs:

1. **Measure** — understand what sensors actually observe, and what they miss.
2. **Clean** — calibrate, denoise, synchronize, and validate signals.
3. **Represent** — learn features and representations, from handcrafted to self-supervised foundation models.
4. **Infer** — estimate state, detect events, classify behavior, forecast, predict failure, quantify uncertainty.
5. **Fuse** — combine sensors, modalities, and time into coherent world models.
6. **Deploy** — run reliable sensory AI under power, latency, privacy, and safety constraints, and keep it trustworthy in the field.

## What Readers Will Build

- sensor data loaders for time series, event streams, point clouds, and telemetry;
- calibration, synchronization, and leakage-safe dataset pipelines;
- classical filters, including Kalman, particle, and factor-graph estimators;
- feature-based and deep classifiers, forecasters, and anomaly detectors;
- self-supervised encoders and fine-tuned sensor/time-series **foundation models**;
- IMU motion estimation, localization, and human activity recognition;
- ECG/PPG/EEG/EMG biosignal models with patient-level validation;
- radar, lidar, depth, thermal, event, and Wi-Fi perception pipelines;
- multimodal fusion, SLAM, world-model, and digital-twin systems;
- edge, TinyML, streaming, on-device continual, and federated deployments;
- conformal-prediction uncertainty, test-time adaptation, and safety monitors;
- production monitoring dashboards and a full end-to-end capstone system.

## How Each Chapter Is Structured

A consistent template lets all three audiences navigate:

1. **Learning objectives and prerequisites** (with pointers back to earlier chapters/appendices).
2. **Motivation and a real-world failure story** (why the naive approach breaks).
3. **Core sections** (5-7), building from intuition to method to math.
4. **Frontier box** — the current SOTA models/methods and where the research is moving **[R]**.
5. **Hands-on lab** — runnable, dataset-backed, with a starter repo.
6. **Exercises** — conceptual, derivation, and coding, tagged by level.
7. **Deployment notes / pitfalls** and **further reading**.

Running threads that recur across chapters: **leakage-safe evaluation**, **uncertainty and calibration**, **sensor failure modes**, **privacy and biometric ethics**, and **the classical-vs-foundation-model tradeoff**.

## Scope, Levels, and Size Discipline

The book is deliberately large because it is meant to be a *reference* as much as a course text. Three mechanisms keep that size from overwhelming any single reader:

- **Level gating.** A one-semester course reads only **[F]**/**[C]** sections; **[A]** and **[R]** sections are self-contained and skippable. Roughly half the total section count is **[A]**/**[R]**.
- **Tiered labs.** Not all 72 labs are equal. About **30 are "Core Labs"** (full, graded, dataset-backed, one per key competency) and the rest are lighter **"Mini-Labs"** (a focused exercise, ~1 hour). Instructors pick a lab spine; the Core Labs alone form a complete practical course.
- **A shorter-course consolidation guide** (see the end of this plan) lists chapters that can be merged or skipped for a leaner path, so the same book supports a 7-week module and a two-semester sequence.

The applications part (Part XIV) is written as integrative **"playbook" chapters** by design: they are intentionally shorter than the method chapters, reusing techniques already taught rather than introducing new ones.

## Running Tools and Datasets

**Core stack:** Python, NumPy, SciPy, pandas, Polars, PyTorch, PyTorch Lightning, scikit-learn, statsmodels; time series: sktime, aeon, tsai, tslib, GluonTS, Nixtla; state estimation: filterpy, GTSAM; SSL/foundation models: HuggingFace, uni2ts (Moirai), granite-tsfm (IBM TTM), momentfm, mamba-ssm, Chronos/AutoGluon-TS; 3D/perception: Open3D, MMDetection3D, OpenPCDet, Pointcept, gsplat, nerfstudio; biosignals: NeuroKit2, MNE-Python, Braindecode, WFDB; radar/event: OpenRadar, Metavision/Tonic, snnTorch/Lava; robotics/sim: ROS 2, Isaac Sim/Lab, CARLA, MuJoCo; edge: ONNX Runtime, LiteRT/TF-Lite-Micro, ExecuTorch, microTVM, Edge Impulse; uncertainty/eval: MAPIE, TorchCP, Fortuna, TSInterpret, OpenOOD; ops: MLflow/W&B, Flower, Docker, FastAPI, River.

**Representative datasets:** UCI-HAR, WISDM, PAMAP2, Opportunity, MHEALTH, Capture-24, UK Biobank accelerometry; PhysioNet, PTB-XL, MIMIC-IV-ECG, CODE-15, PPG-DaLiA, WESAD, TUH-EEG, SleepEDF, emg2qwerty; NASA C-MAPSS/N-CMAPSS, PRONOSTIA/FEMTO, CWRU, MIMII/MIMII-DG, DCASE machine-condition, SWaT/WADI/HAI, Tennessee Eastman, SKAB; KITTI/SemanticKITTI, nuScenes, Waymo Open, Argoverse 2, Occ3D, K-Radar/RADIal/View-of-Delft, DSEC/Prophesee-1Mpx, FLIR/LLVIP, Widar3.0; Open X-Embodiment, DROID, TacBench/Touch-and-Go; METR-LA/PEMS-BAY, smart-building energy sets; forecasting: Monash TSF, LOTSA, GIFT-Eval.

*(All named models, papers, datasets, and version numbers are verified with the `bibtest` skill at drafting time; the plan names them to fix scope, not as final citations.)*

---

# Front Matter

## F1. Why This Book Exists
Most AI textbooks assume the measurement process is solved: data arrives clean, labeled, and IID. Sensory AI starts earlier, before labels, before models, before features, with a device that measures the world imperfectly. This book teaches how to build AI systems that respect that physical reality, and how to ride the shift from bespoke per-sensor models to pretrained foundation models without losing the classical rigor that keeps deployed systems safe.

## F2. What This Book Covers
Sensor physics and measurement models; signal conditioning; time-series representation learning; state estimation; anomaly detection and forecasting; foundation models and self-supervised learning for sensors; multimodal and probabilistic fusion; world models and spatial AI; radar/lidar/depth/thermal/event/RF sensing; tactile and embodied sensing; edge, TinyML, streaming, and federated deployment; uncertainty, robustness, safety, and responsible practice; and applications across industry, healthcare, robotics, vehicles, smart environments, and the frontier.

## F3. Who Should Read This Book
Engineers and researchers who build AI systems connected to physical devices: IoT, wearables, robotics, autonomous systems, industrial monitoring, medical devices, environmental sensing, and cyber-physical systems, plus the students and instructors of the courses that train them.

## F4. How to Use This Book (reading paths)
- **First course / undergraduate (one semester):** Parts I-IV, plus selected chapters from VI, VII/VIII, and XIII. Follow **[F]**/**[C]** sections.
- **Graduate deep-learning-for-sensing:** Parts III-V, X, XIII; **[C]**/**[A]**/**[R]**.
- **IoT / edge AI track:** Parts I, II, IV, VIII, XII, XIII.
- **Robotics / autonomous systems track:** Parts I, III, IX, X, XI, XIII.
- **Health / wearables track:** Parts I, II, IV, VII, XII (privacy), XIII.
- **Industrial / cyber-physical track:** Parts I-III, VIII, XII, XIII.
- **Researcher / frontier survey:** Part V end-to-end, plus every "Frontier" box and Chapter 71.

## F5. Notation, Prerequisites, and Self-Containment
A single notation table; a "what you need and where to get it" map. Prerequisites (calculus, linear algebra, basic Python) are light; everything else (signals, probability, estimation, deep learning) is built in Part I and Appendices A-C. Basic electronics and DSP are helpful but introduced as needed.

---

# Part I · Foundations of Sensory AI  *(measure)*

**Part goal:** establish sensory AI as inference from noisy measurements, and equip every reader with the shared mathematical and engineering vocabulary.

## Chapter 1. What Is Sensory AI?  **[F]**
1.1 Sensors as imperfect windows into the world
1.2 Physical-world AI vs digital/text AI: why measurement changes everything
1.3 Measurement, state, event, action: the four quantities
1.4 A taxonomy of modalities and task families
1.5 From raw signal to decision: the sensing chain
1.6 Sampling, latency, bandwidth, power, cost, and privacy as first-class constraints
1.7 The 2023-2026 shift: from bespoke pipelines to foundation models and agentic sensing
1.8 Book map: measure, clean, represent, infer, fuse, deploy
**Lab 1:** survey a dozen sensor datasets; classify each by sampling rate, dimensionality, modality, task, noise source, label cost, and deployment constraint.

## Chapter 2. Sensor Physics and Measurement Models  **[F]**
2.1 Direct and indirect observables
2.2 Resolution, sensitivity, dynamic range
2.3 Noise sources and signal-to-noise ratio
2.4 Bias, drift, hysteresis, saturation
2.5 Transfer functions and response time
2.6 Cross-sensitivity and environmental coupling
2.7 Measurement models as the bridge to AI
**Lab 2:** simulate bias, drift, saturation, and colored noise; quantify their effect on a classifier and an anomaly detector.

## Chapter 3. Signals, Sampling, Time, and Synchronization  **[F]**
3.1 Sampling, aliasing, and the Nyquist limit
3.2 Event-driven vs clock-driven sensing
3.3 Clocks, timestamps, and multi-sensor synchronization
3.4 Missing samples, jitter, and packet loss
3.5 Quantization and compression
3.6 Streaming buffers, windows, and framing
3.7 Acquisition protocols and metadata
**Lab 3:** build a streaming ingestion pipeline with windowing, missing-data markers, and cross-sensor time alignment.

## Chapter 4. Probability, Estimation, and Uncertainty Primer  **[F]**
4.1 Random variables, distributions, and moments for signals
4.2 Estimators, bias-variance, and maximum likelihood
4.3 Bayesian inference and priors
4.4 Aleatoric vs epistemic uncertainty (introduced early, used everywhere)
4.5 Information, entropy, and mutual information
4.6 Hypothesis testing and detection theory
4.7 Monte Carlo and sampling basics
**Lab 4:** estimate sensor noise models from data and propagate uncertainty through a simple pipeline.

## Chapter 5. Sensor Data Engineering and Leakage-Safe Datasets  **[F][C]**
5.1 Formats for telemetry, waveforms, event streams, and point clouds
5.2 Window construction and labeling
5.3 Leakage in sensor datasets (the field's most common error)
5.4 Device, user, site, session, and machine splits
5.5 Normalization and per-device calibration
5.6 Annotation quality, weak labels, and label delay
5.7 Reproducible, versioned sensor pipelines and data contracts
**Lab 5:** build leakage-safe subject- and device-disjoint splits for human activity recognition; measure the accuracy gap vs a naive random split.

---

# Part II · Classical Signal Processing and Feature Engineering  *(clean, represent)*

**Part goal:** build durable foundations that still power, and often beat, deep models on real sensor systems.

## Chapter 6. Filtering and Denoising Sensor Signals  **[F][C]**
6.1 Moving averages and exponential smoothing
6.2 FIR and IIR filters
6.3 Low-pass, high-pass, band-pass, notch
6.4 Frequency-domain filtering
6.5 Robust filtering for outliers and spikes
6.6 Filter design for real-time, low-latency systems
6.7 Delay vs noise-reduction tradeoffs
**Lab 6:** design filters for accelerometer and vibration signals; quantify latency vs noise reduction.

## Chapter 7. Spectral and Time-Frequency Analysis  **[C]**
7.1 DFT/FFT and spectral leakage
7.2 Spectrograms and the STFT
7.3 Wavelets and multiresolution analysis
7.4 Empirical mode decomposition and the Hilbert-Huang transform
7.5 Cepstral and envelope analysis (bearings, machines)
7.6 Power spectral density and coherence
7.7 Choosing a representation for a modality
**Lab 7:** compare spectrogram, wavelet, and envelope features on machine-fault vibration data.

## Chapter 8. Feature Engineering and Dimensionality Reduction  **[C]**
8.1 Time-domain features
8.2 Frequency- and time-frequency features
8.3 Statistical, shape, and entropy features
8.4 Domain-specific feature libraries (tsfresh, catch22)
8.5 Feature selection
8.6 PCA, ICA, and manifold methods (UMAP, t-SNE) for sensors
8.7 When handcrafted features still beat deep learning
**Lab 8:** build a feature-based activity/condition classifier; compare against a small neural baseline and analyze where each wins.

---

# Part III · State Estimation and Classical Inference  *(infer)*

**Part goal:** the probabilistic backbone of sensing that fusion, tracking, and safety all build on.

## Chapter 9. Bayesian Filtering and the Kalman Family  **[C]**
9.1 Hidden state and observation models
9.2 Recursive Bayesian estimation
9.3 The linear Kalman filter
9.4 Tuning process and measurement noise
9.5 Observability and divergence
9.6 Smoothing vs filtering
9.7 Failure modes and diagnostics
**Lab 9:** implement a Kalman filter for noisy position tracking; extend it to sensor dropout.

## Chapter 10. Nonlinear and Particle Filtering  **[C][A]**
10.1 Extended Kalman filter
10.2 Unscented Kalman filter and sigma points
10.3 Particle filters and importance sampling
10.4 Resampling and degeneracy
10.5 Rao-Blackwellization
10.6 Robust and adaptive filtering
10.7 Choosing an estimator
**Lab 10:** track a nonlinear system with EKF, UKF, and a particle filter; compare accuracy and cost.

## Chapter 11. Factor Graphs and Smoothing  **[A]**
11.1 From filters to factor graphs
11.2 MAP estimation and nonlinear least squares
11.3 Incremental smoothing (iSAM2) and GTSAM
11.4 Loop closure and marginalization
11.5 Robust cost functions
11.6 Uncertainty from the information matrix
11.7 Why modern SLAM and VIO use this
**Lab 11:** build a factor-graph pose estimator fusing odometry and landmark measurements with GTSAM.

## Chapter 12. Classical Anomaly and Change Detection  **[C]**
12.1 Point, contextual, and collective anomalies
12.2 Statistical process control
12.3 Residuals and thresholds
12.4 Change-point detection (CUSUM, BOCPD)
12.5 Isolation Forest, LOF, one-class SVM
12.6 Evaluation without complete labels (and the point-adjust trap)
12.7 Alert fatigue and threshold economics
**Lab 12:** build a telemetry anomaly detector; analyze precision-recall under different alert budgets and a leakage-safe protocol.

---

# Part IV · Deep Learning for Sensor Time Series  *(represent, infer)*

**Part goal:** move from features to neural representation learning for multivariate sensor streams.

## Chapter 13. Neural Representations for Sensor Streams  **[C]**
13.1 Sensor windows as tensors; channel and axis structure
13.2 1D convolutions and temporal pooling
13.3 Multiresolution and dilated features
13.4 Learned vs fixed filterbanks
13.5 Normalization and augmentation for sensors
13.6 Inductive biases for time series
13.7 Debugging and inspecting learned filters
**Lab 13:** train a 1D CNN for human activity recognition; visualize learned filters.

## Chapter 14. Recurrent and Temporal Convolutional Models  **[C]**
14.1 RNNs, GRUs, LSTMs
14.2 Temporal convolutional networks
14.3 Dilations and receptive fields
14.4 Sequence-to-label and sequence-to-sequence
14.5 Streaming/stateful inference
14.6 Irregular and asynchronous sampling
14.7 Practical training recipes
**Lab 14:** compare LSTM and TCN on a multivariate sensor task, including a streaming variant.

## Chapter 15. Transformers for Sensor Data  **[C][A]**
15.1 Attention over time and channels
15.2 Patchification of sensor streams
15.3 Positional encoding for time and sensor identity
15.4 Long-context and efficient attention
15.5 Channel-independent vs channel-mixing designs
15.6 Masked sensor modeling
15.7 Compute-efficient deployment
**Lab 15:** train a patch transformer for sensor classification; compare with CNN/TCN baselines.

## Chapter 16. State-Space Models: Mamba, S4, and Linear-Time Sequences  **[A][R]**
16.1 Why quadratic attention hurts on long sensor sequences
16.2 Structured state-space models (S4, S5)
16.3 Selective state spaces (Mamba)
16.4 Time-series SSM variants (SiMBA, TimeMachine, Bi-Mamba)
16.5 SSMs vs transformers: accuracy, latency, memory, on-device fit
16.6 Hybrid SSM-attention architectures
16.7 When to reach for an SSM
**Lab 16:** benchmark a Mamba-style model vs a transformer on long-horizon sensor sequences (accuracy vs latency vs memory).

## Chapter 17. Self-Supervised and Contrastive Sensor Learning  **[A][R]**
17.1 Why labels are scarce in sensing
17.2 Contrastive learning with sensor augmentations
17.3 Masked reconstruction (MAE for time series)
17.4 Temporal predictive coding and TS2Vec
17.5 Relative and relational objectives (RelCon)
17.6 Cross-device, cross-user, cross-modal pretraining
17.7 Probing and evaluating learned representations
**Lab 17:** pretrain a contrastive/masked encoder on unlabeled sensor windows; fine-tune with few labels and measure the label-efficiency curve.

## Chapter 18. Uncertainty, Calibration, and Conformal Prediction  **[A][R]**
18.1 Aleatoric vs epistemic uncertainty revisited
18.2 Calibration and temperature scaling for time series
18.3 Deep ensembles, MC-dropout, Bayesian and evidential DL
18.4 Conformal prediction: split, weighted, and the exchangeability problem
18.5 Adaptive conformal inference (ACI) and conformal PID under drift
18.6 Abstention, fallback, and safety margins
18.7 Reporting uncertainty to downstream systems
**Lab 18:** compare split conformal vs ACI on a drifting sensor stream; verify coverage and interval width.

---

# Part V · Foundation Models and Agentic Sensing  *(represent, infer)* — **the modern core**

**Part goal:** teach the pretrain-once, adapt-anywhere paradigm that reshaped sensor and time-series AI in 2023-2026, and the language-interfaced, agentic layer on top of it.

## Chapter 19. Time-Series Foundation Models  **[R]**
19.1 What makes a model a "foundation" model for time series
19.2 Pretraining corpora and tokenization (patching vs value tokenization)
19.3 Model families: TimesFM, Chronos/Chronos-Bolt, Moirai/Moirai-MoE, MOMENT, Time-MoE, TTM/TinyTimeMixers, Lag-Llama, Toto, UniTS, Timer
19.4 Zero-shot and few-shot forecasting, classification, imputation, anomaly detection
19.5 Foundation-model embeddings as features for downstream tasks
19.6 The evaluation crisis: leakage, non-stationarity, and honest benchmarking (GIFT-Eval, Monash, LOTSA)
19.7 When a foundation model helps and when a small model wins
**Lab 19:** apply a pretrained TSFM zero-shot to a new sensor dataset; compare against a tuned task-specific model and a fair-baseline check.

## Chapter 20. Sensor and Wearable Foundation Models  **[R]**
20.1 From time-series FMs to raw multi-sensor FMs
20.2 Large sensor models: Google LSM and LSM-2 (adaptive/inherited masking, learning from incomplete data)
20.3 Apple-style wearable biosignal foundation models (PPG/ECG/accelerometer SSL at scale)
20.4 Motion/HAR foundation models
20.5 Handling missingness, multi-rate, and multi-device inputs
20.6 Personalization and adaptation of a pretrained sensor FM
20.7 Compute, privacy, and on-device constraints
**Lab 20:** fine-tune a pretrained sensor encoder for a new wearable task with limited labels; evaluate cross-user generalization.

## Chapter 21. Multimodal Sensor-Language Models and Sensor Reasoning  **[R]**
21.1 Aligning sensor representations with language
21.2 Sensor-to-text: captioning and describing signals
21.3 Sensor question answering (SensorQA, SensorBench, OpenSQA)
21.4 LLM-based reasoning over sensor streams (LLaSA, SensorLLM, HARGPT, LLMSense)
21.5 Prompting and retrieval over sensor context
21.6 Grounding, hallucination, and verification for physical signals
21.7 Evaluation of sensor-language systems
**Lab 21:** build a sensor-QA prototype that answers natural-language questions over an activity/telemetry stream, with a grounding check.

## Chapter 22. LLM Agents for Sensing and Operations  **[R]**
22.1 From single-shot inference to agentic sensing loops
22.2 Anomaly explanation and root-cause reasoning with LLMs
22.3 Log/telemetry reasoning and industrial copilots (Argos, AgentFM, CALM)
22.4 Tool use: agents that call detectors, filters, and forecasters
22.5 Multi-agent recursion-of-thought for RCA
22.6 Guardrails, calibrated confidence, and human-in-the-loop
22.7 Cost, latency, and reliability of agentic pipelines
**Lab 22:** build an agent that monitors a sensor stream, invokes a detector tool, and produces an explained, uncertainty-tagged alert.

---

# Part VI · Motion, Location, and Inertial Intelligence  *(infer)*

**Part goal:** IMU, GNSS, RF positioning, motion estimation, activity, and neuromotor interfaces.

## Chapter 23. Inertial Sensors and Motion Signals  **[C]**
23.1 Accelerometers, gyroscopes, magnetometers
23.2 Coordinate frames and orientation
23.3 Gravity separation and linear acceleration
23.4 IMU calibration (bias, scale, misalignment)
23.5 Step detection and gait analysis
23.6 IMU failure and saturation modes
23.7 Preprocessing for orientation-aware models
**Lab 23:** build an IMU preprocessing pipeline for orientation-aware activity recognition.

## Chapter 24. Orientation Estimation and Dead Reckoning  **[C][A]**
24.1 Quaternions and rotation representations
24.2 Complementary and Mahony/Madgwick filters
24.3 Attitude and heading reference systems
24.4 Inertial navigation and drift
24.5 Zero-velocity updates and pedestrian dead reckoning
24.6 Learned inertial odometry (IONet-style)
24.7 Evaluation of trajectory estimates
**Lab 24:** implement orientation estimation and compare a complementary filter with a learned inertial-odometry model.

## Chapter 25. Localization, GNSS, and RF Positioning  **[C]**
25.1 GPS/GNSS basics and error sources
25.2 Wi-Fi, Bluetooth, and UWB positioning
25.3 Fingerprinting vs geometric methods
25.4 Map matching
25.5 GNSS-inertial fusion
25.6 Localization metrics
25.7 Privacy and spoofing risks of location data
**Lab 25:** fuse GNSS and inertial readings for a smoother, drift-corrected trajectory.

## Chapter 26. Human Activity and Behavior Recognition  **[C]**
26.1 Activity taxonomies and label hierarchies
26.2 Wearable placement and sensor choice
26.3 Segmentation and transition states
26.4 User personalization and adaptation
26.5 Continual learning for changing behavior
26.6 Fairness across users, bodies, and demographics
26.7 Applications: fitness, healthcare, safety, accessibility
**Lab 26:** build user-independent vs user-adapted HAR models; compare generalization on held-out subjects.

## Chapter 27. Gesture, Pose, and Neuromotor Interfaces  **[C][R]**
27.1 Touch, pressure, capacitive, and proximity sensing
27.2 IMU gestures and low-latency inference
27.3 Wearable hand/body pose sensing
27.4 Surface EMG for gesture and typing (Meta neuromotor wristband, emg2qwerty)
27.5 Cross-user, calibration-free neuromotor decoding
27.6 Multimodal interaction
27.7 Human factors, usability, and latency budgets
**Lab 27:** train a gesture/neuromotor classifier and optimize it for low-latency, cross-user interaction.

---

# Part VII · Health, Biosignals, and Wearable AI  *(infer)*

**Part goal:** sensory AI for physiological data under strict reliability, validation, and ethics constraints.

## Chapter 28. Biosignal Foundations  **[C]**
28.1 ECG, PPG, EEG, EMG, respiration, EDA
28.2 Physiological noise and motion artifacts
28.3 Electrode and optical measurement issues
28.4 Event detection in biosignals
28.5 Clinical labels and reference standards
28.6 Patient-level splits and leakage
28.7 Regulatory and safety context (overview)
**Lab 28:** detect heartbeats in ECG/PPG; compare signal quality under motion artifacts.

## Chapter 29. ECG and Cardiac AI  **[C][A]**
29.1 ECG morphology and leads
29.2 Arrhythmia and AFib detection at scale
29.3 Hidden-diagnosis ECG (LVEF, age/sex, hyperkalemia)
29.4 Beat-level vs record-level classification
29.5 Deep ECG models and ECG foundation models
29.6 Explainability and false-alarm triage
29.7 Clinical validation design
**Lab 29:** train an arrhythmia classifier with patient-level evaluation; probe an ECG foundation-model embedding.

## Chapter 30. PPG and Wearable Cardiovascular Sensing  **[C][R]**
30.1 PPG physics and the pulse waveform
30.2 AFib screening on consumer wearables (Apple/Fitbit heart studies)
30.3 SpO2, heart rate, and HRV
30.4 Cuffless and continuous blood-pressure estimation
30.5 Sleep staging and stress from PPG
30.6 Motion robustness and signal-quality gating
30.7 Fairness across skin tones and the calibration problem
**Lab 30:** build a PPG heart-rate/AFib pipeline with signal-quality gating; audit performance across subgroups.

## Chapter 31. EEG, Neural Signals, and Brain-Computer Interfaces  **[A][R]**
31.1 Brain signals, montages, and frequency bands
31.2 Artifact removal and spectral features
31.3 Motor imagery and SSVEP BCIs
31.4 EEG foundation models (LaBraM, EEGPT, BIOT, CBraMod)
31.5 Invasive BCI: speech and handwriting decoding (Neuralink, Synchron, cortical arrays)
31.6 Non-invasive language/speech decoding
31.7 Subject adaptation, safety, and interpretability
**Lab 31:** build a motor-imagery classifier with subject-independent evaluation; probe an EEG foundation model.

## Chapter 32. EMG and Neuromuscular AI  **[C][A]**
32.1 Surface vs intramuscular EMG
32.2 Spectral and envelope features
32.3 Gesture and prosthetic control
32.4 Fatigue and effort estimation
32.5 Cross-session and cross-subject transfer
32.6 Artifact and crosstalk handling
32.7 Real-time control loops
**Lab 32:** build an sEMG gesture model with subject-independent evaluation and a real-time control demo.

## Chapter 33. Continuous and Contactless Health Monitoring  **[C][R]**
33.1 Longitudinal, irregular, and sparse monitoring
33.2 Missingness-as-signal and personalized baselines
33.3 Multimodal wearable fusion (PPG + accel + temp + EDA)
33.4 Contactless vitals: mmWave radar for heart/respiration/sleep apnea
33.5 Camera-based rPPG and privacy tradeoffs
33.6 Continuous glucose monitoring and digital biomarkers
33.7 Longitudinal drift and responsible deployment
**Lab 33:** build a wearable anomaly detector that learns a personal baseline and flags deviations; add a contactless-vitals comparison.

## Chapter 34. Clinical Validation, Regulation, and Biometric Privacy  **[C]**
34.1 SaMD and the FDA framework
34.2 Predetermined change control plans (PCCP) for learning models
34.3 Clinical trial and prospective validation design
34.4 Biometric leakage and re-identification from physiological signals
34.5 Consent, data governance, and de-identification
34.6 Fairness and equity in health sensing
34.7 Documentation: datasheets, model cards, and audit trails
**Lab 34:** write a validation-and-privacy plan for a wearable health model, including a re-identification risk check.

---

# Part VIII · Industrial, Energy, and Infrastructure Sensor AI  *(infer, deploy)*

**Part goal:** predictive maintenance, condition monitoring, and cyber-physical anomaly detection at industrial scale.

## Chapter 35. Industrial Sensing Systems  **[C]**
35.1 Machines, processes, and telemetry
35.2 SCADA, PLCs, and historian data
35.3 Vibration, acoustic, thermal, and electrical signals
35.4 Operating regimes and regime segmentation
35.5 Maintenance records and label delay
35.6 Data quality in industrial systems
35.7 Safety-critical constraints
**Lab 35:** explore industrial logs and segment operating regimes before modeling.

## Chapter 36. Predictive Maintenance and Prognostics  **[C][A]**
36.1 Failure modes and degradation
36.2 Remaining useful life and prediction horizons
36.3 Survival analysis and hazard models
36.4 Sequence models for degradation
36.5 Foundation-model embeddings for RUL
36.6 Uncertainty-aware RUL and maintenance decision economics
36.7 Fleet-scale deployment
**Lab 36:** build an RUL predictor on C-MAPSS/N-CMAPSS; compare regression metrics against maintenance utility.

## Chapter 37. Condition Monitoring and Anomaly Detection  **[C][R]**
37.1 Supervised vs unsupervised condition monitoring
37.2 Acoustic and vibration anomaly detection
37.3 First-shot and domain-generalized anomalous sound detection (DCASE)
37.4 Reconstruction- and forecasting-based detection
37.5 Foundation-model reconstruction for anomalies
37.6 Domain shift across machines and sites
37.7 Honest evaluation (TSB-AD, point-adjust pitfalls)
**Lab 37:** build a first-shot machine-condition anomaly detector on MIMII-DG; evaluate cross-machine generalization.

## Chapter 38. Cyber-Physical Anomaly Detection and ICS Security  **[A][R]**
38.1 Physical process invariants
38.2 Attacks vs faults
38.3 Reconstruction and forecasting residuals
38.4 Graph-based process modeling (GNNs)
38.5 Root-cause localization
38.6 Adversarial robustness of detectors and the transductive-leakage trap
38.7 Security-operations integration
**Lab 38:** train an ICS anomaly detector on SWaT/WADI/HAI with a leakage-safe protocol; test under simulated faults and attacks.

## Chapter 39. Energy, Buildings, and Environmental Sensors  **[C]**
39.1 Smart meters and load disaggregation
39.2 HVAC and building telemetry
39.3 Air/water/soil quality monitoring
39.4 Spatial sensor networks
39.5 Forecasting and control
39.6 Missing and faulty sensors
39.7 Sustainability applications
**Lab 39:** build a building-energy anomaly + forecasting pipeline with weather covariates.

---

# Part IX · Radar, Lidar, Depth, Thermal, Event, and RF Sensing  *(measure, infer)*

**Part goal:** active and non-RGB sensing for autonomy, robotics, security, health, and industrial perception.

## Chapter 40. Depth and 3D Sensing Fundamentals  **[C]**
40.1 Stereo, structured light, and time-of-flight
40.2 Depth maps and point clouds
40.3 Calibration and coordinate frames
40.4 Point-cloud preprocessing and registration
40.5 3D representations (voxels, points, meshes, SDFs)
40.6 Depth uncertainty
40.7 Applications in robotics and AR
**Lab 40:** load, register, downsample, and segment point clouds with Open3D.

## Chapter 41. Monocular Depth Foundation Models  **[R]**
41.1 From per-dataset regression to zero-shot metric depth
41.2 Depth Anything v1/v2 and video depth
41.3 Metric depth and camera-agnostic models (Metric3D v2, UniDepth)
41.4 Diffusion-based depth (Marigold)
41.5 Sensor-prompted depth (lidar-guided)
41.6 Evaluation and zero-shot transfer
41.7 Using depth FMs inside a sensing stack
**Lab 41:** run a monocular depth foundation model zero-shot; fuse its output with a sparse depth sensor.

## Chapter 42. Point Clouds and Lidar AI  **[C][A]**
42.1 Lidar measurement principles
42.2 Point-cloud representations; voxelization and pillars
42.3 Sparse-convolution backbones (CenterPoint, VoxelNeXt)
42.4 Point transformers (Point Transformer v3)
42.5 3D detection, segmentation, and tracking
42.6 Self-supervised lidar pretraining (ALSO, LISO)
42.7 Weather, domain shift, and deployment constraints
**Lab 42:** build a point-cloud detection/segmentation pipeline on a public dataset subset with OpenPCDet/Pointcept.

## Chapter 43. BEV Perception and 3D Occupancy  **[A][R]**
43.1 Bird's-eye-view as a shared representation
43.2 Camera-to-BEV lifting and BEVFormer-style attention
43.3 BEV multi-sensor fusion (BEVFusion)
43.4 3D semantic occupancy prediction (Occ3D, SurroundOcc, TPVFormer)
43.5 Self-supervised and Gaussian occupancy (GaussianOcc)
43.6 Occupancy world models (developed further in Ch 53)
43.7 Benchmarks and metrics
**Lab 43:** train a BEV or occupancy model on an Occ3D benchmark subset; evaluate under a missing-sensor condition.

## Chapter 44. Radar AI  **[C][R]**
44.1 Radar basics: range, Doppler, angle
44.2 FMCW/mmWave signal chain
44.3 Range-Doppler and micro-Doppler representations
44.4 4D imaging radar detection and occupancy (RadarOcc, RCBEVDet)
44.5 Radar-camera-lidar fusion (weather robustness)
44.6 Radar for human and health sensing
44.7 Automotive, security, and healthcare deployment
**Lab 44:** classify micro-Doppler signatures or detect objects in range-Doppler maps (K-Radar/RADIal/VoD subset).

## Chapter 45. Thermal, Infrared, and Multispectral Sensing  **[C]**
45.1 Thermal radiation, emissivity, and calibration
45.2 Human detection and monitoring
45.3 Industrial thermal inspection
45.4 RGB-thermal domain adaptation (D3T, causal multiplexing)
45.5 Visible-to-thermal translation
45.6 Privacy-preserving thermal perception
45.7 Multispectral fusion
**Lab 45:** build a thermal anomaly/pedestrian detector with an RGB→thermal domain-adaptation step.

## Chapter 46. Event-Based and Neuromorphic Sensing  **[A][R]**
46.1 Event cameras and asynchronous sensing
46.2 Event representations (voxel grids, time surfaces)
46.3 Event-to-video and recurrent vision transformers (E2VID, RVT)
46.4 Spiking neural networks
46.5 Neuromorphic hardware (Loihi 2, Speck)
46.6 Event-frame-IMU fusion
46.7 Low-latency, low-power edge advantages and limits
**Lab 46:** process an event-camera stream (DSEC/Prophesee) and build an event-based classifier or tracker.

## Chapter 47. RF and Wireless Sensing  **[A][R]**
47.1 Channel state information (CSI) fundamentals
47.2 Device-free human activity and presence
47.3 Wi-Fi pose and vital-sign sensing (DensePose-from-WiFi, WiPose)
47.4 Through-wall and multi-person sensing
47.5 Standardization (IEEE 802.11bf)
47.6 Robustness across layouts and environments
47.7 Privacy implications of ubiquitous RF sensing
**Lab 47:** build a Wi-Fi CSI activity-recognition model (Widar3.0) and test cross-environment generalization.

---

# Part X · Sensor Fusion, World Models, and Spatial AI  *(fuse)*

**Part goal:** combine measurements into coherent state estimates and predictive world representations.

## Chapter 48. Foundations of Sensor Fusion  **[C]**
48.1 Why fusion works: complementary and redundant sensors
48.2 Early, middle, and late fusion
48.3 Temporal alignment and calibration between sensors
48.4 Fusion under missing modalities
48.5 Confidence-weighted combination
48.6 Evaluation of fused systems
48.7 Design patterns and anti-patterns
**Lab 48:** build early, late, and attention-based fusion for a multimodal activity dataset.

## Chapter 49. Probabilistic and Bayesian Fusion  **[C][A]**
49.1 Bayesian fusion and covariance
49.2 Multi-sensor Kalman filtering
49.3 Occupancy grids
49.4 Data association (JPDA, MHT) and tracking
49.5 Factor-graph fusion (GTSAM), applying the estimator from Ch 11 to multi-sensor fusion
49.6 Uncertainty propagation
49.7 Consistency checks and fault detection
**Lab 49:** fuse two noisy sensors with different error profiles; visualize posterior uncertainty and detect an injected fault.

## Chapter 50. Deep Multimodal Fusion and Missing-Modality Robustness  **[A][R]**
50.1 Modality-specific encoders
50.2 Cross-attention and transformer fusion
50.3 Gated fusion and mixture-of-experts
50.4 Missing-modality training and graceful degradation
50.5 Contrastive multimodal pretraining
50.6 Fusion interpretability
50.7 Deployment tradeoffs
**Lab 50:** train a cross-attention/MoE fusion model; measure degradation with each sensor removed.

## Chapter 51. Neural Fields and Gaussian Splatting for Sensing  **[A][R]**
51.1 Neural radiance fields and signed distance fields
51.2 3D Gaussian splatting basics
51.3 Sensor re-simulation (lidar and camera) from reconstructed scenes
51.4 Joint lidar-camera splatting (SplatAD)
51.5 Synthetic data generation for rare events
51.6 Real-time reconstruction constraints
51.7 Validation of synthetic-from-real pipelines
**Lab 51:** reconstruct a scene with Gaussian splatting and re-simulate a sensor view for augmentation.

## Chapter 52. SLAM and Spatial AI  **[A][R]**
52.1 Visual-inertial odometry
52.2 Classical SLAM (ORB-SLAM3, DROID-SLAM)
52.3 Neural SLAM (NICE-SLAM)
52.4 Gaussian-splatting SLAM (MonoGS, SplaTAM, Photo-SLAM)
52.5 Lidar-inertial-camera SLAM (Gaussian-LIC)
52.6 Dynamic-scene and semantic mapping
52.7 Evaluation and benchmarks
**Lab 52:** run a visual-inertial or Gaussian-splatting SLAM system and evaluate trajectory/map quality.

## Chapter 53. World Models and Predictive Sensing  **[R]**
53.1 What a world model is and why sensing needs one
53.2 Latent state-space and recurrent world models (DreamerV3)
53.3 Joint-embedding predictive architectures (I-JEPA, V-JEPA 2)
53.4 Generative interactive world models (Genie)
53.5 Planning and control in latent space
53.6 Predictive sensing and anticipation
53.7 Evaluation of world models (physical-reasoning benchmarks)
**Lab 53:** train a small latent world model on a sensor sequence and use it for prediction/anomaly anticipation.

## Chapter 54. Graph Neural Networks for Sensor Networks  **[A]**
54.1 Sensors as nodes and relations
54.2 Spatial, process, and dynamic graphs
54.3 Spatiotemporal GNNs (DCRNN, Graph WaveNet, BigST)
54.4 Message passing for fault localization
54.5 Scalability to large networks
54.6 Traffic, energy, water, and industrial grids
54.7 Interpretability
**Lab 54:** build a spatiotemporal GNN for sensor-network forecasting or anomaly localization (METR-LA/PEMS-BAY).

## Chapter 55. Digital Twins, Synthetic Data, and Physics-Informed ML  **[A][R]**
55.1 Predictive models of sensor dynamics
55.2 Simulation and synthetic sensor data
55.3 Domain randomization and sim-to-real
55.4 Physics-informed neural networks (PINNs) and inverse problems
55.5 Hybrid mechanistic + data-driven models
55.6 Digital twins coupled with state estimators (EKF)
55.7 Validation of synthetic data and twins
**Lab 55:** generate synthetic sensor sequences with controllable faults; train a detector that transfers to real data.

---

# Part XI · Tactile, Embodied, and Robotic Sensing  *(fuse, deploy)*

**Part goal:** the sensing that makes robots and embodied agents perceive and act.

## Chapter 56. Tactile Sensing and Electronic Skin  **[A][R]**
56.1 Why touch is the missing modality
56.2 Camera-based tactile sensors (GelSight, DIGIT, DIGIT 360)
56.3 Capacitive, piezoresistive, and e-skin arrays
56.4 Tactile representations and features
56.5 Tactile foundation models (Sparsh, UniTouch, T3)
56.6 Visuo-tactile fusion
56.7 Slip, contact, and material inference
**Lab 56:** train a tactile classifier for contact/material recognition and fuse it with vision (TacBench/Touch-and-Go).

## Chapter 57. Proprioception, Exteroception, and Robot Perception  **[A]**
57.1 Body-state sensing (encoders, force/torque, IMU)
57.2 Exteroceptive fusion for navigation
57.3 Detection and tracking in the perception stack
57.4 Proprioception-exteroception fusion
57.5 Failure detection and recovery
57.6 Latency and real-time constraints
57.7 ROS 2 perception integration
**Lab 57:** build a small robot perception pipeline in simulation/ROS 2 fusing IMU, depth, and lidar.

## Chapter 58. Vision-Language-Action and Embodied Foundation Models  **[R]**
58.1 From perception to action: the VLA idea
58.2 RT-1/RT-2 and web-scale knowledge transfer
58.3 Open generalist policies (Octo, OpenVLA)
58.4 Flow-matching and open-world VLAs (π0/π0.5)
58.5 Humanoid and general robot foundation models (GR00T, Gemini Robotics)
58.6 Sim-to-real and Open X-Embodiment data
58.7 Evaluation, safety, and generalization
**Lab 58:** fine-tune or evaluate an open VLA policy on a manipulation benchmark subset (LIBERO/CALVIN).

---

# Part XII · Edge, Embedded, Streaming, and Federated Sensor AI  *(deploy)*

**Part goal:** run sensory AI where the data is produced, under power, memory, and privacy limits.

## Chapter 59. Edge AI Fundamentals and Model Optimization  **[C][A]**
59.1 Why sensory AI runs on-device
59.2 CPU, GPU, NPU, DSP, MCU tradeoffs
59.3 Memory, power, and thermal limits
59.4 Quantization (int8, int4, and hardware-native 2/4-bit)
59.5 Pruning and sparsity
59.6 Hardware-aware NAS
59.7 Edge-cloud partitioning and the deployment lifecycle
**Lab 59:** quantize and prune a sensor classifier for edge inference; measure latency/size/accuracy tradeoffs.

## Chapter 60. Streaming Inference and Online Learning  **[C][A]**
60.1 Windowed and stateful inference
60.2 Backpressure and data loss
60.3 Online normalization and feature extraction
60.4 Online learning (River) and incremental models
60.5 Concept-drift detection (ADWIN, DDM) and adaptation
60.6 Streaming evaluation and prequential metrics
60.7 Incident handling
**Lab 60:** build a streaming inference service with drift detection, online metrics, and adaptive retraining.

## Chapter 61. TinyML and Microcontroller Sensor AI  **[A]**
61.1 TinyML design constraints
61.2 Feature extraction on microcontrollers
61.3 Quantized networks and TinyNAS/MCUNet
61.4 Runtimes: LiteRT/TF-Lite-Micro, microTVM, ExecuTorch
61.5 Wake-up cascades and always-on sensing
61.6 Firmware integration and testing on hardware
61.7 Field update and rollback; MLPerf Tiny
**Lab 61:** deploy a motion classifier to an MCU (or a faithful embedded simulation) and benchmark it.

## Chapter 62. On-Device Continual Learning  **[A][R]**
62.1 Why static deployment is obsolete
62.2 Catastrophic forgetting on the edge
62.3 Latent and quantized replay
62.4 Few-shot class-incremental learning (TinyOL)
62.5 Energy budgets for on-device training
62.6 Personalization on-device
62.7 Safety of self-updating models
**Lab 62:** implement latent-replay continual learning for a wearable model under a memory/energy budget.

## Chapter 63. Batteryless and Intermittent Sensing  **[R]**
63.1 Energy harvesting and power constraints
63.2 Intermittent computing and checkpointing
63.3 Energy-adaptive inference
63.4 Charging-aware scheduling (CARTOS)
63.5 Batteryless intelligence tradeoffs
63.6 Systems and reliability constraints
63.7 Sustainability and the zero-power frontier
**Lab 63:** simulate energy-adaptive inference of a pretrained model under an intermittent power trace.

## Chapter 64. Federated and Privacy-Preserving Sensor AI  **[A][R]**
64.1 Why raw sensor data may not leave the device
64.2 Federated learning (FedAvg family) and non-IID sensors
64.3 Personalization and local adaptation
64.4 Differential privacy and secure aggregation
64.5 Split and split-federated learning
64.6 Multimodal and cross-device federation
64.7 Federated evaluation, security, and failure modes
**Lab 64:** simulate federated training across users/devices for a wearable model; add differential privacy and measure the utility cost.

---

# Part XIII · Trust, Safety, Evaluation, and Operations  *(deploy)*

**Part goal:** make sensory AI measurable, robust, safe, and accountable in the field.

## Chapter 65. Evaluation Protocols and Leakage-Safe Benchmarking  **[C]**
65.1 Task metrics vs operational metrics
65.2 User/site/device/session splits
65.3 Time-aware cross-validation
65.4 Rare-event and imbalanced evaluation
65.5 Robustness to missing and faulty sensors
65.6 Calibration and uncertainty metrics
65.7 Reproducibility and field-validation protocols
**Lab 65:** write an evaluation harness that reports standard metrics plus device/site/generalization breakdowns.

## Chapter 66. Distribution Shift, OOD, and Test-Time Adaptation  **[A][R]**
66.1 Covariate, label, and concept shift in sensing (builds on the uncertainty tools of Ch 18)
66.2 OOD and novelty detection
66.3 Domain generalization for sensors (DIVERSIFY)
66.4 Test-time training and adaptation (TENT, CoTTA)
66.5 Optimization-free TTA for cross-person HAR
66.6 Monitoring risk during adaptation
66.7 Benchmarks (HAROOD, BenchHAR, WILDS)
**Lab 66:** evaluate a HAR model under subject/device shift; add test-time adaptation and measure the recovery.

## Chapter 67. Interpretability and Root-Cause Analysis for Time Series  **[A]**
67.1 Attribution for time series (Integrated Gradients, SHAP-TS)
67.2 Temporal saliency and its pitfalls
67.3 Counterfactual sensor explanations (TSEvo, MASCOTS)
67.4 Concept- and prototype-based explanations
67.5 Root-cause graphs
67.6 Human-review tooling (TSInterpret, Captum)
67.7 Explanation faithfulness and benchmarks (XTSC-Bench)
**Lab 67:** explain an anomaly alert with temporal attribution and nearest similar historical events; test faithfulness.

## Chapter 68. Robustness, Sensor Spoofing, and Functional Safety  **[A][R]**
68.1 Sensor failure and degradation modes
68.2 Adversarial and physical spoofing (lidar, radar/MadRadar, GPS, IMU, audio)
68.3 Redundancy, voting, and safety envelopes
68.4 Runtime monitoring and assurance
68.5 Functional-safety standards (ISO 26262, ISO 21448/SOTIF, ISO/PAS 8800, IEC 61508)
68.6 Safety cases for ML perception
68.7 Reliability-engineering patterns
**Lab 68:** stress-test a fusion model under sensor dropout, bias drift, and spoofing; add a runtime safety monitor.

## Chapter 69. MLOps for Sensor Fleets  **[C][A]**
69.1 Data contracts for sensors
69.2 Model versioning and deployment
69.3 Monitoring drift and data quality
69.4 Proxy monitoring under delayed ground truth
69.5 Retraining triggers and fleet management
69.6 Logging under privacy constraints
69.7 Incident response
**Lab 69:** build a sensor-AI monitoring dashboard with drift alerts, proxy metrics, and model-version tracking.

## Chapter 70. Responsible Sensory AI and Regulation  **[C]**
70.1 Surveillance, consent, and proportionality
70.2 Location and biometric privacy
70.3 Fairness across users, bodies, and environments
70.4 Security of physical-world AI
70.5 Dataset governance (datasheets, dataset cards)
70.6 Regulation: EU AI Act (biometrics/emotion as high-risk), GDPR, FDA
70.7 Documentation and accountability
**Lab 70:** produce a responsible-use, privacy, and compliance checklist for a wearable, industrial, or smart-building system.

---

# Part XIV · Applications, Systems, and Frontiers

**Part goal:** show how the pieces combine in real domains, and where research is heading.

## Chapter 71. Domain Playbooks: Wearables, Robotics, Vehicles, Smart Spaces, Environment, Security  **[C][A]**
71.1 Wearables and personal sensing (fitness, fall detection, sleep, stress)
71.2 Robotics and autonomous systems (perception stack, sim-to-real, recovery)
71.3 Vehicles and mobility (multimodal suites, cabin monitoring, fleet PdM, safety cases)
71.4 Smart spaces and ambient intelligence (occupancy, non-camera sensing, placement)
71.5 Environmental and climate sensing (spatial interpolation, early warning, citizen sensing)
71.6 Defense, security, and critical infrastructure (perimeter sensing, spoofing, triage, ethics)
71.7 Cross-domain lessons and reusable system blueprints
**Lab 71:** pick one domain; design an end-to-end system blueprint (sensing → modeling → evaluation → deployment → privacy).

## Chapter 72. Frontier Research and the End-to-End Capstone  **[R]**
72.1 Sensor and time-series foundation models: open problems
72.2 Universal encoders and cross-modal physical AI
72.3 Neural fields, differentiable sensors, and inverse sensing
72.4 World models for physical AI
72.5 Agentic and self-improving sensing systems
72.6 Open research problems and evaluation gaps
72.7 Capstone: select an application and sensing stack; define measurement and task; build acquisition and preprocessing; train a classical baseline and a modern/foundation model; evaluate generalization, uncertainty, and robustness; deploy or simulate deployment; produce a final technical and responsible-use report
**Capstone options:** wearable activity + anomaly monitoring · industrial predictive maintenance · smart-building occupancy inference · radar/lidar/depth perception prototype · multi-sensor mobile-robot fusion · environmental early-warning network · sensor-language monitoring agent.

---

# Appendices

## Appendix A. Mathematical and Signal-Processing Reference
Sampling and Fourier analysis, filtering, probability and estimation, state-space models, Bayesian inference, optimization, information theory, and uncertainty.

## Appendix B. Deep Learning Refresher for Sequences and Tensors
Tensors, autodiff, training dynamics, regularization, attention, convolutions, recurrence, state-space layers, and training recipes, sensor-oriented throughout.

## Appendix C. Sensor Hardware Guide
IMUs, vibration and acoustic sensors, biosensors, radar, lidar, depth, thermal, event cameras, RF/Wi-Fi front-ends, tactile sensors, environmental sensors, microcontrollers, NPUs/edge accelerators, and data-acquisition boards.

## Appendix D. The Sensory AI Toolchain
PyTorch/Lightning, time-series libraries (sktime/aeon/tsai/GluonTS/Nixtla), foundation-model hubs (uni2ts, granite-tsfm, momentfm, Chronos, mamba-ssm), 3D/perception (Open3D, MMDetection3D, OpenPCDet, Pointcept, gsplat/nerfstudio), biosignals (NeuroKit2, MNE, Braindecode, WFDB), robotics/sim (ROS 2, Isaac Sim, CARLA, MuJoCo), edge (ONNX/LiteRT/ExecuTorch/microTVM/Edge Impulse), uncertainty/eval (MAPIE, TorchCP, TSInterpret, OpenOOD), and ops (MLflow/W&B, Flower, River, FastAPI).

## Appendix E. Sensor Datasets and Benchmarks
Curated tables by modality, task, sampling rate, license, subject/device split, and known pitfalls (leakage, point-adjust, domain shift), spanning HAR, biosignals, industrial, autonomous-driving, radar/lidar/event, RF, tactile, sensor-network, and forecasting corpora.

## Appendix F. Evaluation Metrics Reference
Classification, detection, forecasting, anomaly detection, calibration, conformal coverage, tracking, localization, RUL, fairness, and operational/field-reliability metrics.

## Appendix G. Synthetic Data and Simulation Resources
Digital twins, physics engines, domain randomization, Gaussian-splatting/neural-field re-simulation, sensor noise simulators, and validation protocols.

## Appendix H. Course Syllabi
- 14-week undergraduate *Sensory AI* course.
- 14-week graduate *Cyber-Physical and Foundation-Model Sensing* course.
- 7-week IoT/Edge AI professional course.
- 14-week Robotics Sensor Fusion and Embodied AI seminar.
- 7-week Health/Wearable AI short course.

## Appendix I. Solutions to Selected Exercises
Worked derivations, coding solutions, and system-design answers.

## Appendix J. Notation and Glossary
Unified symbol table and a glossary of sensing, signal-processing, estimation, and ML terms.

---

# Suggested 14-Week Course Track (undergraduate/graduate hybrid)

| Week | Topics | Lab |
|---|---|---|
| 1 | Sensory AI overview, measurement, the six verbs | Dataset survey |
| 2 | Sensor physics, sampling, noise, calibration | Noise and drift simulation |
| 3 | Filtering, spectral/time-frequency, features | Vibration feature lab |
| 4 | State estimation and classical anomaly detection | Kalman + telemetry anomaly |
| 5 | CNN/TCN/RNN and transformers for sensors | Activity recognition |
| 6 | State-space models and self-supervised learning | Mamba vs transformer; contrastive pretraining |
| 7 | Foundation models and agentic sensing | Zero-shot TSFM + sensor-QA |
| 8 | IMU, localization, activity, neuromotor | Trajectory smoothing / gesture |
| 9 | Biosignals and wearable AI | ECG or PPG classifier with patient splits |
| 10 | Industrial, predictive maintenance, CPS security | RUL + ICS anomaly (leakage-safe) |
| 11 | Radar/lidar/depth/thermal/event/RF | Point-cloud or radar or Wi-Fi lab |
| 12 | Fusion, world models, SLAM, digital twins | Cross-attention fusion / world model |
| 13 | Edge, TinyML, streaming, federated | Quantized streaming inference |
| 14 | Trust, safety, evaluation; capstone | Capstone demo |

---

# Consolidation Guide for Shorter Courses

The full 14 parts are a two-semester or reference sequence. To build a leaner path, apply these merges and cuts (coverage is preserved by dropping to **[F]**/**[C]** sections and folding closely related chapters):

- **Merge** Ch 23-24 (inertial sensing + orientation) into one lecture; Ch 9-11 (Kalman → nonlinear → factor graphs) into a two-lecture estimation block; Ch 40-41 (depth fundamentals + depth foundation models) into one.
- **Treat as optional / frontier-survey only** (assign as reading, skip labs): Ch 16 (state-space models), Ch 46-47 (event/neuromorphic, RF/Wi-Fi), Ch 51 (neural fields/splatting), Ch 53 (world models), Ch 56-58 (tactile/embodied/VLA), Ch 62-63 (on-device continual, batteryless).
- **Pick one domain chapter** from each application cluster rather than all: one of the biosignal chapters (29-33), one industrial chapter (36-38), one active-sensing chapter (42-47).
- **Minimum viable "Sensory AI 101"** (7 weeks): Ch 1-5, 6+8, 9, 12, 13-15, 26, one biosignal or industrial chapter, 48, 59-60, 65, 70. Core Labs only.

---

# Distinctive Features

- Treats sensors as physical measurement systems with noise, bias, drift, and failure modes, not clean data sources.
- The first sensor-AI textbook to fully integrate the **foundation-model and self-supervised shift** (time-series and wearable FMs, state-space models) alongside durable classical methods, with explicit guidance on when each wins.
- Adds the **agentic, language-interfaced sensing** layer (sensor-language models, LLM operations agents) missing from every prior text.
- Unifies signal processing, state estimation, deep learning, foundation models, fusion, world models, edge AI, and MLOps in one arc.
- Covers the full modality spectrum, including radar, lidar, depth, thermal, **event**, **RF/Wi-Fi**, and **tactile** sensing, not just IMU and audio.
- Foregrounds **leakage-free evaluation, uncertainty (conformal prediction), robustness, sensor spoofing, functional-safety standards, and responsible practice** as first-class engineering concerns.
- Triple-audience design: undergraduate textbook, graduate course text, and researcher/engineer field manual, via explicit level tags, reading paths, and per-chapter frontier boxes.
- Every chapter is hands-on: runnable labs on public datasets, level-tagged exercises, deployment notes, and a full end-to-end capstone.
