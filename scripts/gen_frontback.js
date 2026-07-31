export const meta = {
  name: 'gen-frontback',
  description: 'Generate real front-matter, appendices, and capstone pages (replace stubs) in house style',
  phases: [{ title: 'Write' }],
}

const ROOT = 'E:/Projects/Books/SensorAI'
const BOOK = 'Building Sensory AI'

// up = relative prefix to book root from the page's own directory.
const SPECS = [
  { path: 'front-matter/foreword.html', up: '../', title: 'Foreword',
    brief: 'A warm 450-650 word foreword. Open on the idea that most AI meets the world through text and pixels, while sensory AI starts earlier, at a device that measures reality imperfectly. Argue why perceiving the physical world through inertial, vibration, radar, lidar, depth, thermal, RF, tactile, and biomedical sensing is now a first-class AI discipline, and why treating sensors as instruments with noise, bias, drift, and failure modes (not clean arrays) is the book\'s core stance. Note the 2023-2026 shift to sensor and time-series foundation models. End by welcoming the reader to a single connected build from raw sample to trustworthy deployed decision. No headings needed beyond the h1; 2-4 flowing paragraphs. You may add one short epigraph blockquote at the top.' },
  { path: 'front-matter/fm-what-this-book-covers.html', up: '../', title: 'What This Book Covers',
    brief: 'Describe the scope. State the central thesis: sensory intelligence is inferring hidden state from noisy physical measurements and acting on it reliably, organized around six verbs (measure, clean, represent, infer, fuse, deploy). Summarize the fourteen-part arc in a compact list or short paragraphs: foundations and sensor physics; classical signal processing and state estimation; deep learning and foundation models for sensor time series; agentic sensing; motion and inertial; biosignals and wearables; industrial and infrastructure; radar/lidar/depth/thermal/event/RF; fusion and world models; tactile and embodied; edge and TinyML; trust, safety, evaluation; applications and frontier. Mention the full modality spectrum and that every idea is built from scratch then shown with the modern library. 500-800 words.' },
  { path: 'front-matter/fm-who-should-read.html', up: '../', title: 'Who Should Read This Book',
    brief: 'Explain the triple audience: advanced undergraduates, graduate students and instructors, and practicing researchers and engineers (IoT, wearables, robotics, autonomous systems, industrial monitoring, medical devices, environmental sensing). Explain the level-tag system: every chapter and section is tagged [F] foundational, [C] core, [A] advanced, [R] research frontier, so each reader finds their depth in one book. State prerequisites plainly: Python and basic calculus, linear algebra, and probability are assumed; everything else (signals, sampling, estimation, a deep-learning refresher) is developed in Part I and the appendices, so no prior signal-processing or ML course is strictly required. 450-650 words.' },
  { path: 'front-matter/fm-how-to-use.html', up: '../', title: 'How to Use This Book',
    brief: 'A practical guide. Explain the level tags and that a one-semester course reads only [F]/[C] sections while [A]/[R] are self-contained and skippable. Give reading paths as a list: first-course/undergraduate; graduate deep-learning-for-sensing; IoT/edge; robotics/autonomous systems; health/wearables; industrial/cyber-physical; researcher/frontier survey (name the relevant Parts for each, consistent with the book plan). Explain tiered labs (about 30 Core Labs plus lighter Mini-Labs) and that a shorter-course consolidation guide exists. Mention the callout system (key-insight, practical-example, library-shortcut, warning, exercise, self-check, research-frontier, lab) so readers can read deep or skim. Link to the Contents. 500-750 words.' },
  { path: 'front-matter/copyright.html', up: '../', title: 'Copyright',
    brief: 'A concise copyright/edition page. Title: Building Sensory AI: Machine Perception of the Physical World. First Edition, 2026. Copyright (c) 2026 Alexander Apartsin and Yehudit Aperstein. All rights reserved. Part of the Hands-On AI Science series. Include a short standard "no warranty / for educational purposes / code provided as-is under a permissive spirit" disclaimer, a line that trademarks and product names belong to their owners, and a placeholder line "ISBN / ASIN: to be assigned." Keep it short and formal, not flowery. Link to About the Series and About the Authors.' },
  { path: 'capstone/index.html', up: '../', title: 'Capstone: End-to-End Sensory AI System',
    brief: 'An overview page for the capstone (the full-book synthesis). Explain that the capstone walks the six verbs end to end on one chosen system: select an application and sensing stack, define measurement and task, build acquisition and preprocessing, train a classical baseline and a modern or foundation model, evaluate generalization/uncertainty/robustness with leakage-safe protocols, deploy or simulate deployment, and produce a final technical and responsible-use report. List the capstone options (wearable activity and anomaly monitoring; industrial predictive maintenance; smart-building occupancy; radar/lidar/depth perception prototype; multi-sensor mobile-robot fusion; environmental early-warning network; sensor-language monitoring agent). State the concrete deliverables and a rubric-style checklist. Link to Chapter 72 (part-14-applications-systems-and-frontiers/module-72-frontier-research-and-the-end-to-end-capstone/index.html) as the in-text capstone chapter. 600-900 words.' },
  { path: 'appendices/index.html', up: '../', title: 'Appendices',
    brief: 'A landing page listing the ten appendices A-J with a one-to-two sentence description each and a link. The links (each a subdirectory index) are: appendix-a-math-reference/index.html Mathematical and Signal-Processing Reference; appendix-b-deep-learning-refresher/index.html Deep Learning Refresher for Sequences and Tensors; appendix-c-sensor-hardware/index.html Sensor Hardware Guide; appendix-d-toolchain/index.html The Sensory AI Toolchain; appendix-e-datasets-benchmarks/index.html Sensor Datasets and Benchmarks; appendix-f-evaluation-metrics/index.html Evaluation Metrics Reference; appendix-g-synthetic-data/index.html Synthetic Data and Simulation Resources; appendix-h-course-syllabi/index.html Course Syllabi; appendix-i-solutions/index.html Solutions to Selected Exercises; appendix-j-notation-glossary/index.html Notation and Glossary. Use a simple list or the section-card-grid pattern. Short intro paragraph.' },
  { path: 'appendices/appendix-a-math-reference/index.html', up: '../../', title: 'Appendix A. Mathematical and Signal-Processing Reference',
    brief: 'A compact but real reference. Cover, with short definitions and key formulas in KaTeX: sampling and the Nyquist theorem; the Fourier transform and DFT/FFT; convolution and LTI filters; probability (random variables, expectation, variance, Gaussian, Bayes rule); estimation (MLE, MAP, bias-variance); state-space models and the Kalman filter equations; basic optimization (gradient descent); and information theory (entropy, mutual information). Use display math \\[...\\] and inline \\(...\\). Organize under h2 subsections. This is a refresher, not a course; keep each topic to a tight paragraph plus its key equation(s). 900-1400 words.' },
  { path: 'appendices/appendix-b-deep-learning-refresher/index.html', up: '../../', title: 'Appendix B. Deep Learning Refresher for Sequences and Tensors',
    brief: 'A sensor-oriented deep-learning refresher. Cover: tensors and shapes for sensor windows (batch, channels, time); automatic differentiation and backprop at a high level; the training loop, loss functions, optimizers (SGD, Adam), learning-rate schedules; regularization (dropout, weight decay, early stopping, augmentation); the core layers (linear, 1D convolution, recurrence, attention, and state-space layers) and when each fits time series; normalization; and practical training recipes for multivariate sensor data. Include one short PyTorch code block (a minimal 1D-CNN or training loop) with a caption below it. 900-1400 words.' },
  { path: 'appendices/appendix-c-sensor-hardware/index.html', up: '../../', title: 'Appendix C. Sensor Hardware Guide',
    brief: 'A practical hardware reference. Briefly describe each sensor family, what it measures, typical sampling rates, and gotchas: IMUs (accelerometer, gyroscope, magnetometer); vibration and acoustic sensors; biosensors (ECG, PPG, EEG, EMG); radar (FMCW/mmWave); lidar; depth cameras (stereo, structured light, ToF); thermal/IR; event cameras; RF/Wi-Fi front-ends (CSI); tactile sensors; environmental sensors. Then cover compute: microcontrollers, NPUs and edge accelerators, and data-acquisition considerations (clocks, synchronization, buses). Use a table where it helps. 900-1300 words.' },
  { path: 'appendices/appendix-d-toolchain/index.html', up: '../../', title: 'Appendix D. The Sensory AI Toolchain',
    brief: 'A curated tools reference, grouped, with a one-line purpose each: core (Python, NumPy, SciPy, pandas, Polars, PyTorch, PyTorch Lightning, scikit-learn); time series (sktime, aeon, tsai, GluonTS, Nixtla); state estimation (filterpy, GTSAM); foundation models and SSL (HuggingFace, uni2ts, granite-tsfm, momentfm, Chronos, mamba-ssm); 3D and perception (Open3D, MMDetection3D, OpenPCDet, Pointcept, gsplat, nerfstudio); biosignals (NeuroKit2, MNE-Python, Braindecode, WFDB); radar and event (OpenRadar, Metavision/Tonic, snnTorch/Lava); robotics and sim (ROS 2, Isaac Sim, CARLA, MuJoCo); edge (ONNX Runtime, LiteRT/TF-Lite-Micro, ExecuTorch, microTVM, Edge Impulse); uncertainty and evaluation (MAPIE, TorchCP, TSInterpret, OpenOOD); ops (MLflow, Weights & Biases, Flower, River, FastAPI, Docker). Use grouped lists with links where well known. 700-1100 words.' },
  { path: 'appendices/appendix-e-datasets-benchmarks/index.html', up: '../../', title: 'Appendix E. Sensor Datasets and Benchmarks',
    brief: 'A curated datasets table by modality/task, with columns like Dataset, Modality, Task, and Notes/pitfalls (leakage, subject/device split, domain shift). Cover HAR (UCI-HAR, WISDM, PAMAP2, Opportunity, Capture-24), biosignals (PhysioNet, PTB-XL, MIMIC-IV-ECG, PPG-DaLiA, WESAD, TUH-EEG, SleepEDF, emg2qwerty), industrial (C-MAPSS/N-CMAPSS, CWRU, MIMII/MIMII-DG, DCASE, SWaT/WADI/HAI), autonomous (KITTI/SemanticKITTI, nuScenes, Waymo, Argoverse 2, Occ3D, K-Radar/RADIal/View-of-Delft, DSEC/Prophesee), RF (Widar3.0), tactile (TacBench/Touch-and-Go), sensor networks (METR-LA, PEMS-BAY), and forecasting (Monash TSF, GIFT-Eval). Add a short note on leakage-safe splitting. 800-1200 words with a table.' },
  { path: 'appendices/appendix-f-evaluation-metrics/index.html', up: '../../', title: 'Appendix F. Evaluation Metrics Reference',
    brief: 'A metrics reference with brief definitions and formulas in KaTeX where useful. Cover: classification (accuracy, precision, recall, F1, ROC-AUC, PR-AUC, balanced accuracy); detection (mAP, IoU); forecasting (MAE, RMSE, MAPE, sMAPE, CRPS); anomaly detection (precision-recall under alert budgets, the point-adjust pitfall); calibration and uncertainty (ECE, Brier score, conformal coverage and interval width); tracking (MOTA, MOTP); localization (ATE, RPE); remaining useful life (RMSE, scoring functions); and fairness and operational/field-reliability metrics. Note the difference between task metrics and operational metrics. 800-1200 words.' },
  { path: 'appendices/appendix-g-synthetic-data/index.html', up: '../../', title: 'Appendix G. Synthetic Data and Simulation Resources',
    brief: 'A reference on synthetic sensor data. Cover: physics-based sensor simulators and noise models; digital twins; domain randomization and sim-to-real; simulators and engines (Isaac Sim/Lab, CARLA, Gazebo, MuJoCo); neural-field and Gaussian-splatting re-simulation for lidar and camera; controllable fault injection; and validation protocols for synthetic-from-real pipelines (how to check a synthetic set actually transfers). Explain when synthetic data helps (rare events, labels, privacy) and its failure modes. 700-1000 words.' },
  { path: 'appendices/appendix-h-course-syllabi/index.html', up: '../../', title: 'Appendix H. Course Syllabi',
    brief: 'Concrete course tracks as week-by-week tables. Provide: a 14-week undergraduate Sensory AI course; a 14-week graduate Cyber-Physical and Foundation-Model Sensing course; a 7-week IoT/Edge AI professional course; a 14-week Robotics Sensor Fusion and Embodied AI seminar; and a 7-week Health/Wearable AI short course. For at least the first two, give a week/topic/lab table mapping to the book\'s parts and chapters. Keep tables compact. 800-1200 words.' },
  { path: 'appendices/appendix-i-solutions/index.html', up: '../../', title: 'Appendix I. Solutions to Selected Exercises',
    brief: 'An overview page for worked solutions. Explain that selected exercises from across the book have worked solutions (derivations, coding solutions, and system-design answers), that solutions are chosen to reinforce the most transferable ideas, and give 3-5 representative worked mini-solutions as examples (e.g. a leakage-safe split rationale, a Kalman-gain derivation sketch, a conformal-coverage check, a why-averaging-fixes-noise-but-not-bias explanation). Note that a full solutions set accompanies the instructor materials. 600-900 words.' },
  { path: 'appendices/appendix-j-notation-glossary/index.html', up: '../../', title: 'Appendix J. Notation and Glossary',
    brief: 'Two parts. First, a Notation table: the book\'s consistent symbols (signal x(t) or x[n], hidden state s, observation y, measurement model x = h(s) + noise eta, estimate s-hat, belief p(s|x), time t, and common ML symbols). Second, a Glossary: alphabetical short definitions of 25-40 key terms used across the book (aliasing, bias, drift, calibration, leakage, Kalman filter, conformal prediction, foundation model, self-supervised learning, sensor fusion, SLAM, TinyML, domain shift, test-time adaptation, micro-Doppler, occupancy, world model, RUL, and so on). Use a table for notation and a definition list or table for the glossary. 900-1400 words.' },
]

const SCHEMA = { type: 'object', additionalProperties: false,
  properties: { path: { type: 'string' }, words: { type: 'number' }, wrote: { type: 'boolean' }, notes: { type: 'string' } },
  required: ['path', 'wrote'] }

function prompt(s) {
  return `You are writing one non-chapter page for the textbook "${BOOK}: Machine Perception of the Physical World" (a Hands-On AI Science series book). Authors: Alexander Apartsin and Yehudit Aperstein.

WRITE THE FILE with the Write tool to: ${ROOT}/${s.path}
Overwrite whatever is there (it is a placeholder stub).

CONTENT BRIEF for "${s.title}":
${s.brief}

EXACT PAGE STRUCTURE (this page is reached via the prefix "${s.up}" to the book root):

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<meta content="${s.title}. ${BOOK}." name="description"/>
<title>${s.title} | ${BOOK}</title>
<link href="${s.up}styles/book.css" rel="stylesheet"/>
<link href="${s.up}styles/pygments.css" rel="stylesheet"/>
<link href="${s.up}vendor/katex/katex.min.css" rel="stylesheet"/>
<script defer src="${s.up}vendor/katex/katex.min.js"></script>
<script defer onload="renderMathInElement(document.body, {delimiters:[{left:'$$',right:'$$',display:true},{left:'\\\\[',right:'\\\\]',display:true},{left:'\\\\(',right:'\\\\)',display:false}],throwOnError:false});" src="${s.up}vendor/katex/contrib/auto-render.min.js"></script>
<link href="${s.up}vendor/prism/prism-theme.css" rel="stylesheet"/>
<script defer src="${s.up}vendor/prism/prism-bundle.min.js"></script>
<script defer src="${s.up}scripts/book.js"></script>
</head>
<body>
<a class="skip-link" href="#main-content">Skip to main content</a>
<header class="chapter-header">
<nav class="header-nav">
<a class="book-title-link" href="${s.up}index.html">${BOOK}</a>
<a class="toc-link" href="${s.up}toc.html" title="Table of Contents"><span class="toc-icon">&#9776;</span> Contents</a>
</nav>
<h1>${s.title}</h1>
</header>
<main class="content" id="main-content">
... YOUR CONTENT (h2 subsections, paragraphs, tables, KaTeX math, and at most one small code block with a caption below it where the brief calls for it) ...
</main>
<footer>
<p class="footer-title">${BOOK}: Machine Perception of the Physical World</p>
<p>&#169; 2026 Alexander Apartsin &amp; Yehudit Aperstein &#183; <a href="${s.up}toc.html">Contents</a></p>
</footer>
</body>
</html>

HARD RULES:
- NO em-dashes or double hyphens anywhere. Use commas, colons, semicolons, parentheses, or separate sentences.
- Do not use the words honestly, frankly, candidly.
- Inline math uses \\(...\\); display math uses $$...$$ or \\[...\\]. Never bare single-$ math.
- Real, specific, correct content. Match the confident, plain, example-driven voice of the book. No placeholders, no "TODO", no "lorem".
- Use tables (<table>) where the brief asks for tabular reference material.
- Any link you write must be either an external https URL or a same-site link built from the "${s.up}" prefix; do not invent internal paths beyond those named in the brief.

After writing, return the structured summary.`
}

phase('Write')
const results = await pipeline(
  SPECS,
  (s) => agent(prompt(s), { schema: SCHEMA, label: s.path.split('/').pop().replace('.html','').replace('index', s.title.split('.')[0].replace('Appendix ','app-')), phase: 'Write', effort: 'high' })
)

return { requested: SPECS.length, wrote: results.filter(Boolean).filter(r => r.wrote !== false).length, pages: results.filter(Boolean).map(r => r.path) }
