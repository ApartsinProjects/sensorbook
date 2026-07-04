# Building Sensor AI: From Signals to Intelligent Sensing Systems

**Hands-On AI Science Series — detailed book plan**  
**Working subtitle:** *From Signals to Intelligent Sensing Systems*  
**Target length:** 11 parts · 52 chapters · 280+ sections · labs, projects, appendices, and capstone  
**Audience:** advanced undergraduates, graduate students, applied researchers, embedded/IoT engineers, robotics engineers, industrial AI engineers, healthcare AI engineers  
**Prerequisites:** Python, NumPy/PyTorch basics, probability, linear algebra; basic electronics and signal processing helpful but introduced as needed  

## Book Positioning

*Building Sensor AI* is about AI systems that perceive the physical world through sensors other than ordinary cameras and microphones, while also integrating cameras/audio when needed. It covers inertial sensors, vibration, radar, lidar, depth, thermal, magnetic, pressure, biosignals, environmental sensors, industrial telemetry, smart buildings, vehicles, wearables, and robotics. The focus is not only model architecture, but the complete sensing chain: sensor physics, calibration, synchronization, uncertainty, edge constraints, data quality, sensor fusion, deployment, and trustworthy operation.

The book fills a gap between signal processing, embedded systems, IoT, robotics perception, and machine learning. It treats sensors as measurement instruments with biases, noise, drift, and failure modes, not as clean arrays handed to a neural network.

## Central Thesis

Sensor intelligence is the ability to infer hidden state from noisy physical measurements. The book is organized around five verbs:

1. **Measure** — understand what sensors actually observe and what they miss.
2. **Clean** — calibrate, denoise, synchronize, and validate signals.
3. **Infer** — estimate state, detect events, classify behavior, predict failures.
4. **Fuse** — combine multiple sensors and modalities into coherent world models.
5. **Deploy** — run reliable sensor AI under power, latency, privacy, and safety constraints.

## What Readers Will Build

Readers will build:

- sensor data loaders for time series, event streams, point clouds, and telemetry;
- calibration and synchronization pipelines;
- classical filters including Kalman and particle filters;
- vibration and anomaly detectors;
- wearable activity recognition models;
- IMU-based motion estimation;
- radar/lidar object detection examples;
- multimodal sensor fusion networks;
- edge inference pipelines;
- digital-twin simulation data generators;
- production monitoring dashboards for deployed sensor AI.

---

# Front Matter

## F1. Why This Book Exists
Most AI textbooks assume the measurement process is already solved. Sensor AI starts earlier: before labels, before models, before features, there is a device that measures the world imperfectly. This book teaches how to build AI systems that respect that physical reality.

## F2. What This Book Covers
Sensor physics, signal conditioning, time-series modeling, state estimation, anomaly detection, multimodal fusion, edge AI, deployment, and applications in industry, healthcare, robotics, vehicles, and smart environments.

## F3. Who Should Read This Book
Engineers and researchers who build AI systems connected to physical devices: IoT, wearables, robotics, autonomous systems, industrial monitoring, medical devices, environmental sensing, and cyber-physical systems.

## F4. How to Use This Book
Recommended paths:

- **IoT/edge AI path:** Parts I, II, III, VI, IX, X.
- **Robotics/autonomous systems path:** Parts I, II, IV, VII, VIII, X.
- **Industrial monitoring path:** Parts I, II, V, VI, IX, X.
- **Healthcare/wearables path:** Parts I, II, III, V, XI.
- **Research path:** all parts plus appendices and capstone.

## F5. Running Tools and Datasets
Core stack: Python, NumPy, SciPy, pandas, Polars, PyTorch, PyTorch Lightning, tsfresh, sktime, river, filterpy, Open3D, ROS 2, PyTorch Geometric, ONNX Runtime, TensorFlow Lite, Edge Impulse, MLflow/W&B, Docker, FastAPI.

Representative datasets: UCI HAR, WISDM, PAMAP2, MHEALTH, PhysioNet signals, NASA turbofan degradation, MIMII/DCASE machine condition datasets, KITTI, nuScenes, Waymo Open Dataset, Oxford Radar RobotCar, OPPORTUNITY, smart-building energy datasets, CMAPSS, SWaT/WADI industrial control datasets.

---

# Part I · Foundations of Sensor Intelligence

**Part goal:** establish sensor AI as inference from noisy measurements.

## Chapter 1. What Is Sensor AI?
### Sections
1.1 Sensors as imperfect windows into the world  
1.2 Measurement, state, event, and action  
1.3 Sensor types and task families  
1.4 From raw signal to decision  
1.5 Sampling, latency, bandwidth, power, and cost  
1.6 Why physical constraints matter for AI  
1.7 Book map: measure, clean, infer, fuse, deploy  

### Lab 1
Explore several sensor datasets and classify each by sampling rate, dimensionality, task type, noise source, and deployment constraint.

## Chapter 2. Sensor Physics and Measurement Models
### Sections
2.1 What sensors measure: direct and indirect observables  
2.2 Resolution, sensitivity, dynamic range  
2.3 Noise sources and signal-to-noise ratio  
2.4 Bias, drift, hysteresis, saturation  
2.5 Transfer functions and response time  
2.6 Cross-sensitivity and environmental effects  
2.7 Measurement models as the bridge to AI  

### Lab 2
Simulate sensor bias, drift, saturation, and noise; show how each affects classification and anomaly detection.

## Chapter 3. Sampling, Time, and Data Acquisition
### Sections
3.1 Sampling rate and aliasing  
3.2 Event-driven versus clock-driven sensors  
3.3 Time stamps, clocks, and synchronization  
3.4 Missing samples and packet loss  
3.5 Quantization and compression  
3.6 Streaming buffers and windows  
3.7 Acquisition protocols and metadata  

### Lab 3
Build a streaming sensor ingestion pipeline with windowing, missing-data markers, and time alignment.

## Chapter 4. Sensor Data Engineering
### Sections
4.1 Data formats for telemetry and sensor logs  
4.2 Window construction and labeling  
4.3 Leakage in sensor datasets  
4.4 Device, user, site, and machine splits  
4.5 Normalization and per-device calibration  
4.6 Annotation quality and weak labels  
4.7 Reproducible sensor pipelines  

### Lab 4
Create leakage-safe train/test splits for human activity recognition by user and device.

---

# Part II · Classical Signal Processing and State Estimation

**Part goal:** build durable foundations that still power real sensor systems.

## Chapter 5. Filtering and Denoising Sensor Signals
### Sections
5.1 Moving averages and exponential smoothing  
5.2 FIR and IIR filters  
5.3 Low-pass, high-pass, band-pass, notch filters  
5.4 Frequency-domain filtering  
5.5 Wavelet denoising  
5.6 Robust filtering for outliers  
5.7 Filter design for real-time systems  

### Lab 5
Design filters for accelerometer and vibration signals and evaluate delay versus noise reduction.

## Chapter 6. Feature Engineering for Sensor AI
### Sections
6.1 Time-domain features  
6.2 Frequency-domain features  
6.3 Time-frequency features  
6.4 Statistical and shape features  
6.5 Domain-specific features  
6.6 Feature selection and dimensionality reduction  
6.7 When handcrafted features beat deep learning  

### Lab 6
Build a feature-based activity recognition classifier and compare features across activities.

## Chapter 7. State Estimation and Kalman Filtering
### Sections
7.1 Hidden state and observation models  
7.2 Bayesian filtering  
7.3 Linear Kalman filter  
7.4 Extended and unscented Kalman filters  
7.5 Particle filters  
7.6 Smoothing versus filtering  
7.7 Failure modes and tuning  

### Lab 7
Implement a Kalman filter for noisy position tracking and extend it to sensor dropout.

## Chapter 8. Classical Anomaly and Change Detection
### Sections
8.1 Point anomalies, contextual anomalies, collective anomalies  
8.2 Statistical process control  
8.3 Thresholds and residuals  
8.4 Change-point detection  
8.5 Isolation Forest, LOF, one-class SVM  
8.6 Evaluation without complete labels  
8.7 Alert fatigue and threshold economics  

### Lab 8
Build an anomaly detector for machine telemetry and analyze precision-recall under different alert budgets.

---

# Part III · Deep Learning for Sensor Time Series

**Part goal:** move from features to neural representation learning for multivariate sensor streams.

## Chapter 9. Neural Representations for Sensor Streams
### Sections
9.1 Sensor windows as tensors  
9.2 Channel structure and sensor axes  
9.3 1D convolutions  
9.4 Temporal pooling  
9.5 Multiresolution features  
9.6 Learned versus fixed filterbanks  
9.7 Input normalization and augmentation  

### Lab 9
Train a 1D CNN for human activity recognition and inspect learned filters.

## Chapter 10. Recurrent and Temporal Convolutional Models
### Sections
10.1 RNNs, GRUs, and LSTMs  
10.2 Temporal convolutional networks  
10.3 Dilations and receptive fields  
10.4 Sequence-to-label and sequence-to-sequence tasks  
10.5 Streaming state  
10.6 Handling irregular sampling  
10.7 Practical training recipes  

### Lab 10
Compare LSTM and TCN models for multivariate sensor classification.

## Chapter 11. Transformers for Sensor Data
### Sections
11.1 Attention over time and channels  
11.2 Patchification of sensor streams  
11.3 Positional encoding for time and sensor identity  
11.4 Long-context attention  
11.5 Masked sensor modeling  
11.6 Foundation models for time series and sensors  
11.7 Compute-efficient transformer deployment  

### Lab 11
Fine-tune a transformer on a sensor classification dataset and compare with CNN/TCN baselines.

## Chapter 12. Self-Supervised and Contrastive Sensor Learning
### Sections
12.1 Why labels are scarce in sensor AI  
12.2 Contrastive learning with augmentations  
12.3 Temporal predictive learning  
12.4 Masked reconstruction  
12.5 Cross-device and cross-user pretraining  
12.6 Representation probing  
12.7 Transfer learning across sensor tasks  

### Lab 12
Pretrain an encoder with contrastive learning on unlabeled sensor windows, then fine-tune with few labels.

## Chapter 13. Uncertainty and Reliability in Sensor Models
### Sections
13.1 Aleatoric versus epistemic uncertainty  
13.2 Calibration  
13.3 Ensembles and MC dropout  
13.4 Out-of-distribution detection  
13.5 Abstention and fallback logic  
13.6 Safety margins  
13.7 Reporting uncertainty to downstream systems  

### Lab 13
Add uncertainty-aware abstention to an activity recognition model and evaluate coverage-risk tradeoff.

---

# Part IV · Motion, Location, and Inertial Intelligence

**Part goal:** cover IMU, GPS, motion estimation, localization, and navigation.

## Chapter 14. Inertial Sensors and Motion Signals
### Sections
14.1 Accelerometers, gyroscopes, magnetometers  
14.2 Coordinate frames and orientation  
14.3 Gravity separation  
14.4 Sensor calibration  
14.5 Step detection and gait analysis  
14.6 Gesture recognition  
14.7 IMU failure modes  

### Lab 14
Build an IMU preprocessing pipeline for orientation-aware activity recognition.

## Chapter 15. Localization and Tracking
### Sections
15.1 GPS and GNSS basics  
15.2 Dead reckoning  
15.3 Wi-Fi, Bluetooth, UWB localization  
15.4 Map matching  
15.5 Multi-sensor tracking  
15.6 Tracking metrics  
15.7 Privacy risks of location data  

### Lab 15
Fuse GPS and inertial readings for a smoother trajectory estimate.

## Chapter 16. Human Activity and Behavior Recognition
### Sections
16.1 Activity taxonomies  
16.2 Wearable placement and sensor choice  
16.3 Segmentation and transition states  
16.4 User personalization  
16.5 Continual learning for changing behavior  
16.6 Fairness across users and bodies  
16.7 Applications in fitness, healthcare, safety, and accessibility  

### Lab 16
Build a user-independent and user-adapted activity recognition model and compare generalization.

## Chapter 17. Gesture, Pose, and Interaction Sensors
### Sections
17.1 Touch, pressure, capacitive, and proximity sensing  
17.2 IMU gestures  
17.3 Wearable hand and body sensors  
17.4 EMG for gesture recognition  
17.5 Multimodal interaction  
17.6 Low-latency inference  
17.7 Human factors and usability  

### Lab 17
Train a small gesture classifier and optimize it for low-latency interaction.

---

# Part V · Health, Biosignals, and Wearable AI

**Part goal:** cover sensor AI for physiological data under strict reliability and ethics constraints.

## Chapter 18. Biosignal Foundations
### Sections
18.1 ECG, PPG, EEG, EMG, respiration  
18.2 Physiological noise and artifacts  
18.3 Electrode and optical measurement issues  
18.4 Event detection in biosignals  
18.5 Clinical labels and reference standards  
18.6 Patient-level splits and leakage  
18.7 Regulatory and safety context  

### Lab 18
Detect heartbeats in ECG/PPG and compare signal quality under motion artifacts.

## Chapter 19. ECG and Cardiac AI
### Sections
19.1 ECG morphology  
19.2 Arrhythmia detection  
19.3 Beat-level versus record-level classification  
19.4 Deep ECG models  
19.5 Explainability for clinical review  
19.6 False alarms and triage  
19.7 Clinical validation design  

### Lab 19
Train an ECG arrhythmia classifier and produce patient-level evaluation.

## Chapter 20. EEG, EMG, and Neuro-Sensor AI
### Sections
20.1 Brain and muscle signals  
20.2 Frequency bands and spectral features  
20.3 Brain-computer interfaces  
20.4 EMG gesture and fatigue detection  
20.5 Artifact removal  
20.6 Subject adaptation  
20.7 Safety and interpretability  

### Lab 20
Build an EMG gesture recognition model with subject-independent evaluation.

## Chapter 21. Wearable Health Monitoring
### Sections
21.1 Continuous monitoring and irregular data  
21.2 Sleep, activity, stress, and recovery  
21.3 Multimodal wearable fusion  
21.4 Personalized baselines  
21.5 Longitudinal drift  
21.6 Missingness as signal  
21.7 Responsible deployment and user feedback  

### Lab 21
Build a wearable anomaly detector that learns a personal baseline and flags deviations.

---

# Part VI · Industrial, Energy, and Infrastructure Sensor AI

**Part goal:** teach predictive maintenance, industrial monitoring, and cyber-physical anomaly detection.

## Chapter 22. Industrial Sensing Systems
### Sections
22.1 Machines, processes, and telemetry  
22.2 SCADA, PLCs, and historian data  
22.3 Vibration, acoustic, thermal, and electrical signals  
22.4 Operational states and regimes  
22.5 Maintenance records and label delay  
22.6 Data quality in industrial systems  
22.7 Safety-critical constraints  

### Lab 22
Explore industrial sensor logs and segment operating regimes before modeling.

## Chapter 23. Predictive Maintenance
### Sections
23.1 Failure modes and degradation  
23.2 Remaining useful life  
23.3 Survival analysis and hazard models  
23.4 Sequence models for degradation  
23.5 Unsupervised condition monitoring  
23.6 Maintenance decision economics  
23.7 Deployment in fleets  

### Lab 23
Build a remaining-useful-life predictor and compare regression metrics with maintenance utility.

## Chapter 24. Cyber-Physical Anomaly Detection
### Sections
24.1 Physical process invariants  
24.2 Attacks versus faults  
24.3 Reconstruction-based detection  
24.4 Forecasting residuals  
24.5 Graph-based process modeling  
24.6 Root-cause analysis  
24.7 Security operations integration  

### Lab 24
Train an anomaly detector on industrial control data and test it under simulated faults and attacks.

## Chapter 25. Energy, Buildings, and Environmental Sensors
### Sections
25.1 Smart meters and energy load  
25.2 HVAC and building telemetry  
25.3 Air quality and environmental monitoring  
25.4 Spatial sensor networks  
25.5 Forecasting and control  
25.6 Missing and faulty sensors  
25.7 Sustainability applications  

### Lab 25
Build a building energy anomaly and forecasting pipeline with weather covariates.

---

# Part VII · Radar, Lidar, Depth, Thermal, and Event Sensors

**Part goal:** cover active and non-RGB sensing for autonomy, robotics, security, and industrial perception.

## Chapter 26. Depth and 3D Sensing
### Sections
26.1 Stereo, structured light, time-of-flight  
26.2 Depth maps and point clouds  
26.3 Calibration and coordinate frames  
26.4 Point cloud preprocessing  
26.5 3D object detection basics  
26.6 Depth uncertainty  
26.7 Applications in robotics and AR  

### Lab 26
Load, visualize, downsample, and segment point clouds using Open3D.

## Chapter 27. Lidar AI
### Sections
27.1 Lidar measurement principles  
27.2 Point cloud representations  
27.3 Voxelization and pillars  
27.4 PointNet-style models  
27.5 3D detection and tracking  
27.6 Weather and domain shift  
27.7 Lidar deployment constraints  

### Lab 27
Build a small point-cloud classification or detection pipeline using a public dataset subset.

## Chapter 28. Radar AI
### Sections
28.1 Radar basics: range, Doppler, angle  
28.2 FMCW radar signal chain  
28.3 Range-Doppler maps  
28.4 Radar object detection  
28.5 Micro-Doppler signatures  
28.6 Radar-camera-lidar fusion  
28.7 Radar in automotive, security, and healthcare  

### Lab 28
Classify micro-Doppler signatures or detect objects in range-Doppler maps.

## Chapter 29. Thermal and Infrared Sensing
### Sections
29.1 Thermal radiation and emissivity  
29.2 Thermal cameras and calibration  
29.3 Human detection and monitoring  
29.4 Industrial thermal inspection  
29.5 Domain shift from temperature and environment  
29.6 Privacy-preserving perception  
29.7 Fusion with RGB and other sensors  

### Lab 29
Build a thermal anomaly detector for equipment or scene monitoring.

## Chapter 30. Event-Based and Neuromorphic Sensors
### Sections
30.1 Event cameras and asynchronous sensing  
30.2 Event streams and voxel grids  
30.3 Spiking representations  
30.4 Event-based object recognition  
30.5 Low-latency tracking  
30.6 Fusion with frame cameras and IMUs  
30.7 Edge advantages and limitations  

### Lab 30
Process an event-camera stream and build a simple event-based classifier or tracker.

---

# Part VIII · Sensor Fusion and World Models

**Part goal:** combine measurements into coherent state estimates and predictive representations.

## Chapter 31. Foundations of Sensor Fusion
### Sections
31.1 Why fusion works  
31.2 Early, middle, and late fusion  
31.3 Complementary and redundant sensors  
31.4 Temporal alignment  
31.5 Calibration between sensors  
31.6 Fusion under missing modalities  
31.7 Evaluation of fused systems  

### Lab 31
Build early, late, and attention-based fusion models for a multimodal activity dataset.

## Chapter 32. Probabilistic Fusion
### Sections
32.1 Bayesian fusion  
32.2 Covariance and confidence  
32.3 Multi-sensor Kalman filtering  
32.4 Occupancy grids  
32.5 SLAM intuition  
32.6 Data association  
32.7 Uncertainty propagation  

### Lab 32
Fuse two noisy sensors with different error profiles and visualize posterior uncertainty.

## Chapter 33. Deep Multimodal Sensor Fusion
### Sections
33.1 Modality-specific encoders  
33.2 Cross-attention fusion  
33.3 Gated fusion and mixture-of-experts  
33.4 Missing-modality training  
33.5 Contrastive multimodal pretraining  
33.6 Fusion interpretability  
33.7 Deployment tradeoffs  

### Lab 33
Train a cross-attention fusion model and test it with one sensor removed.

## Chapter 34. Sensor World Models and Digital Twins
### Sections
34.1 Predictive models of sensor dynamics  
34.2 Latent state-space models  
34.3 Simulation and synthetic sensor data  
34.4 Domain randomization  
34.5 Sim-to-real transfer  
34.6 World models for planning and control  
34.7 Validation of synthetic data  

### Lab 34
Create synthetic sensor sequences with controllable faults and train a detector that transfers to real data.

## Chapter 35. Graph Sensor Networks
### Sections
35.1 Sensors as nodes and relations  
35.2 Spatial graphs and process graphs  
35.3 Graph neural networks for sensor data  
35.4 Dynamic graphs  
35.5 Message passing for fault localization  
35.6 Traffic, energy, water, and industrial networks  
35.7 Scalability and interpretability  

### Lab 35
Build a graph neural network for sensor network forecasting or anomaly localization.

---

# Part IX · Edge, Embedded, and Streaming Sensor AI

**Part goal:** run sensor AI where the data is produced.

## Chapter 36. Edge AI Fundamentals
### Sections
36.1 Why sensor AI often runs on-device  
36.2 CPU, GPU, NPU, DSP, MCU tradeoffs  
36.3 Memory, power, and thermal limits  
36.4 Quantization and pruning  
36.5 Streaming feature extraction  
36.6 Edge-cloud partitioning  
36.7 Deployment lifecycle  

### Lab 36
Convert and quantize a sensor classifier for edge inference and measure latency/size/accuracy.

## Chapter 37. Streaming Inference Systems
### Sections
37.1 Windowed inference  
37.2 Stateful models  
37.3 Backpressure and data loss  
37.4 Real-time thresholds  
37.5 Online normalization  
37.6 Streaming evaluation  
37.7 Incident handling  

### Lab 37
Build a streaming inference service for sensor events with online metrics.

## Chapter 38. TinyML and Microcontroller Sensor AI
### Sections
38.1 TinyML design constraints  
38.2 Feature extraction on microcontrollers  
38.3 Quantized neural networks  
38.4 Wake-up cascades  
38.5 Firmware integration  
38.6 Testing on embedded hardware  
38.7 Field update and rollback  

### Lab 38
Deploy a simple motion classifier to a microcontroller or simulate the embedded pipeline.

## Chapter 39. Federated and Privacy-Preserving Sensor AI
### Sections
39.1 Why raw sensor data may not leave the device  
39.2 Federated learning  
39.3 Personalization and local adaptation  
39.4 Differential privacy  
39.5 Secure aggregation  
39.6 Federated evaluation  
39.7 Limitations and failure modes  

### Lab 39
Simulate federated training across users/devices for a wearable activity model.

---

# Part X · Evaluation, Trust, Safety, and Operations

**Part goal:** make sensor AI measurable and dependable in the field.

## Chapter 40. Evaluation Protocols for Sensor AI
### Sections
40.1 Task metrics and operational metrics  
40.2 User/site/device splits  
40.3 Time-aware evaluation  
40.4 Rare event evaluation  
40.5 Robustness to missing and faulty sensors  
40.6 Calibration and uncertainty metrics  
40.7 Field validation protocols  

### Lab 40
Write an evaluation harness that reports standard metrics plus device/site/generalization breakdowns.

## Chapter 41. Interpretability and Root-Cause Analysis
### Sections
41.1 Feature attribution for time series  
41.2 Saliency over sensors and time  
41.3 Counterfactual sensor explanations  
41.4 Prototype and example-based explanations  
41.5 Root-cause graphs  
41.6 Human review tools  
41.7 Explanation pitfalls  

### Lab 41
Explain an anomaly detection alert using temporal attribution and nearest similar historical events.

## Chapter 42. Robustness, Fault Tolerance, and Safety
### Sections
42.1 Sensor failure modes  
42.2 Missing modality resilience  
42.3 Redundancy and fallback  
42.4 Safety envelopes  
42.5 Adversarial sensor attacks  
42.6 Validation for safety-critical domains  
42.7 Reliability engineering patterns  

### Lab 42
Stress-test a fusion model under sensor dropout, bias drift, and adversarial perturbations.

## Chapter 43. MLOps for Sensor AI
### Sections
43.1 Data contracts for sensors  
43.2 Model versioning and deployment  
43.3 Monitoring drift and data quality  
43.4 Retraining triggers  
43.5 Fleet management  
43.6 Logging under privacy constraints  
43.7 Incident response  

### Lab 43
Build a sensor AI monitoring dashboard with drift alerts and model-version tracking.

## Chapter 44. Responsible Sensor AI
### Sections
44.1 Surveillance and consent  
44.2 Location and biometric privacy  
44.3 Fairness across users and environments  
44.4 Security of physical-world AI  
44.5 Dataset governance  
44.6 Regulatory considerations  
44.7 Documentation and accountability  

### Lab 44
Create a responsible-use and deployment checklist for a wearable, industrial, or smart-building sensor system.

---

# Part XI · Applications and Future Directions

**Part goal:** show how the pieces combine in real domains and where research is heading.

## Chapter 45. Wearables and Personal Sensing
### Sections
45.1 Fitness and wellness  
45.2 Fall detection  
45.3 Sleep monitoring  
45.4 Stress and fatigue  
45.5 Personalization  
45.6 Privacy and user trust  
45.7 Product case study  

### Lab 45
Design a wearable AI product blueprint with sensing, modeling, evaluation, and privacy controls.

## Chapter 46. Robotics and Autonomous Systems
### Sections
46.1 Perception stack overview  
46.2 Proprioception and exteroception  
46.3 Sensor fusion for navigation  
46.4 Object detection and tracking  
46.5 Sim-to-real  
46.6 Failure recovery  
46.7 Robotics case study  

### Lab 46
Build a small robot perception pipeline in simulation or ROS 2 using IMU/depth/lidar inputs.

## Chapter 47. Vehicles and Mobility
### Sections
47.1 Automotive sensor suites  
47.2 Radar, lidar, camera, IMU, GPS fusion  
47.3 Driver and cabin monitoring  
47.4 Road condition sensing  
47.5 Predictive maintenance for fleets  
47.6 Validation and safety cases  
47.7 Mobility case study  

### Lab 47
Design a multimodal vehicle sensing system and evaluate failure cases under weather and sensor dropout.

## Chapter 48. Smart Spaces and Ambient Intelligence
### Sections
48.1 Smart homes, buildings, factories, hospitals  
48.2 Occupancy and activity sensing  
48.3 Privacy-preserving sensing  
48.4 Sensor placement  
48.5 Multi-room and multi-zone models  
48.6 Human-centered automation  
48.7 Ambient intelligence case study  

### Lab 48
Build an occupancy or activity inference model from non-camera sensors.

## Chapter 49. Environmental and Climate Sensor AI
### Sections
49.1 Air, water, soil, and weather sensors  
49.2 Spatial interpolation  
49.3 Sensor networks and missing nodes  
49.4 Remote and edge deployments  
49.5 Early warning systems  
49.6 Citizen sensing  
49.7 Climate adaptation applications  

### Lab 49
Build a spatial-temporal pollution or weather sensor model with uncertainty maps.

## Chapter 50. Defense, Security, and Critical Infrastructure
### Sections
50.1 Perimeter sensing  
50.2 Intrusion and anomaly detection  
50.3 Sensor deception and spoofing  
50.4 Multi-sensor alert triage  
50.5 Human-machine teaming  
50.6 Legal and ethical boundaries  
50.7 Critical infrastructure case study  

### Lab 50
Design a multi-sensor anomaly triage system with explicit false-alarm management.

## Chapter 51. Frontier Research in Sensor AI
### Sections
51.1 Sensor foundation models  
51.2 Universal time-series encoders  
51.3 Neural fields and physical sensing  
51.4 Differentiable sensors  
51.5 Self-supervised multimodal physical AI  
51.6 Sensor AI and world models  
51.7 Open research problems  

### Lab 51
Replicate a small self-supervised sensor foundation-model experiment with masked reconstruction or contrastive learning.

## Chapter 52. Capstone: End-to-End Sensor AI System
### Sections
52.1 Select an application and sensing stack  
52.2 Define measurement and task  
52.3 Build acquisition and preprocessing  
52.4 Train baseline and modern model  
52.5 Evaluate generalization and robustness  
52.6 Deploy or simulate deployment  
52.7 Produce final technical and responsible-use report  

### Capstone Options
- Wearable activity and anomaly monitoring.
- Industrial predictive maintenance system.
- Multi-sensor smart-building occupancy inference.
- Radar/lidar/depth perception prototype.
- Sensor fusion system for mobile robotics.
- Environmental sensor network early-warning system.

---

# Appendices

## Appendix A. Mathematical and Signal Processing Reference
Sampling, Fourier analysis, filtering, probability, state-space models, Bayesian inference, optimization, and uncertainty.

## Appendix B. Sensor Hardware Guide
IMUs, vibration sensors, biosensors, radar, lidar, depth, thermal, environmental sensors, microcontrollers, edge accelerators, data acquisition boards.

## Appendix C. PyTorch, ROS 2, and Edge Deployment Primer
Practical setup for sensor datasets, streaming models, ROS topics, ONNX/TFLite export, and embedded inference.

## Appendix D. Sensor Datasets and Benchmarks
Curated table of datasets by modality, task, sampling rate, license, subject/device split, and known pitfalls.

## Appendix E. Evaluation Metrics Reference
Classification, detection, forecasting, anomaly detection, calibration, tracking, localization, RUL, field reliability, and operational metrics.

## Appendix F. Synthetic Data and Simulation Resources
Digital twins, physics engines, domain randomization, sensor noise simulators, validation protocols.

## Appendix G. Course Syllabi
Tracks:
- 14-week undergraduate Sensor AI course.
- 14-week graduate Cyber-Physical AI course.
- 7-week IoT/Edge AI professional course.
- 14-week Robotics Sensor Fusion seminar.

## Appendix H. Solutions to Selected Exercises
Worked derivations, coding solutions, and system design answers.

---

# Suggested 14-Week Course Track

| Week | Topics | Lab |
|---|---|---|
| 1 | Sensor AI overview and measurement | Dataset survey |
| 2 | Sampling, noise, calibration | Noise and drift simulation |
| 3 | Filtering and features | Sensor filtering lab |
| 4 | Classical ML and anomaly detection | Industrial anomaly baseline |
| 5 | CNN/TCN/RNN sensor models | Activity recognition |
| 6 | Transformers and self-supervised learning | Masked sensor modeling |
| 7 | State estimation | Kalman filtering |
| 8 | IMU and localization | Trajectory smoothing |
| 9 | Biosignals/wearables | ECG or EMG classifier |
| 10 | Industrial and infrastructure AI | Predictive maintenance |
| 11 | Radar/lidar/depth/thermal | Point-cloud or radar lab |
| 12 | Sensor fusion | Cross-attention fusion |
| 13 | Edge deployment and MLOps | Quantized streaming inference |
| 14 | Capstone presentations | Final demo |

---

# Distinctive Features

- Treats sensors as physical measurement systems, not only data sources.
- Unifies signal processing, state estimation, deep learning, sensor fusion, edge AI, and MLOps.
- Covers major real-world sensing domains: wearables, health, industry, robotics, vehicles, smart spaces, environment, and security.
- Emphasizes leakage-free evaluation, robustness, uncertainty, and sensor failure modes.
- Designed for both academic courses and applied cyber-physical AI development.
