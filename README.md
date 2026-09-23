# Recamán — Python in Motion

A 60-second cinematic, audiovisual interpretation of **Recamán's sequence**.
It turns 180 algorithmic decisions into semicircular motion, temporal depth,
live code highlighting, evolving color, and a through-composed piano score.

**Live demo after deployment:**
`https://YOUR-USERNAME.github.io/recaman-cinematic-reel/`

> Audio starts only after pressing the **گوش کن** button. This is required by
> modern browser autoplay policies.

## What this project contains

- A responsive 9:16 canvas experience designed for Instagram Reels
- 180 Recamán moves in exactly 60 seconds
- Constant visual pacing locked to the Web Audio clock
- True semicircular paths with smooth zoom-out
- A cinematic 2.5D depth reveal and camera orbit
- Three synchronized VS Code-style Python panels
- An original browser-generated piano miniature with a three-second fade
- A local Vazirmatn font for reliable Persian rendering
- Executable Python reference implementations and tests
- Automatic GitHub Pages deployment through GitHub Actions

## Run locally

No build step and no JavaScript dependencies are required.

```bash
python -m http.server 8000
```

Then open <http://localhost:8000> and press **گوش کن**.

Opening `index.html` directly also works in most browsers, but a local server is
recommended because it matches the GitHub Pages environment more closely.

## Deploy to GitHub Pages

1. Create a public repository named `recaman-cinematic-reel`.
2. Upload the **contents** of this folder to the repository root.
3. Open **Settings → Pages** in the repository.
4. Under **Build and deployment**, set **Source** to **GitHub Actions**.
5. Push to `main`, or run the workflow manually from the **Actions** tab.
6. Wait for the `Deploy GitHub Pages` workflow to finish.

Your page will be available at:

```text
https://YOUR-USERNAME.github.io/recaman-cinematic-reel/
```

The included workflow follows GitHub's official static Pages deployment flow:
checkout, configure Pages, upload the static artifact, and deploy it.

For Persian step-by-step instructions, see
[`DEPLOYMENT_FA.md`](DEPLOYMENT_FA.md).

## Push with Git

Replace `YOUR-USERNAME` with your GitHub username:

```bash
git init
git add .
git commit -m "Publish Recamán cinematic reel"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/recaman-cinematic-reel.git
git push -u origin main
```

## Project structure

```text
.
├── .github/workflows/pages.yml  # Automatic Pages deployment
├── python/                      # Executable reference implementation
│   ├── recaman.py               # Sequence and jump trace
│   ├── score.py                 # 60-second score event model
│   └── camera.py                # Temporal depth and perspective projection
├── tests/test_reference.py      # Standard-library unit tests
├── licenses/OFL-Vazirmatn.txt   # Font license
├── DEPLOYMENT_FA.md             # Persian publishing guide
├── LICENSE                      # Project license
├── Vazirmatn-Bold.ttf           # Local Persian typeface
└── index.html                   # Complete audiovisual experience
```

## Verify the Python reference

Python 3.10 or newer is recommended. No third-party packages are needed.

```bash
python -m unittest discover -s tests -v
python python/recaman.py --steps 180
python python/score.py
```

## Timing model

- Tempo: 60 BPM
- Grid: 15 bars × 12 triplet slots
- Visual moves: 180
- Total duration: 60 seconds
- Final fade: seconds 57–60

The browser uses one `AudioContext` clock for both animation and sound, so the
last musical event and the last visual move resolve together.

## Recording a Reel

1. Open the live page in Chrome or Edge.
2. Set a 9:16 viewport, ideally 1080 × 1920 or 540 × 960.
3. Enable system-audio capture in the recorder.
4. Start recording, press **گوش کن**, and keep the tab active for 60 seconds.
5. Export at 1080 × 1920, H.264, 30 or 60 fps.

## Technical notes

The experience is implemented with Canvas 2D, CSS, and the Web Audio API. It
uses no prerecorded music and no external JavaScript framework. Recamán values
shape expression and accents; the musical notes themselves come from a
through-composed harmonic plan, avoiding a random “one number = one note”
mapping.

## Credits and licenses

- Project code: [MIT License](LICENSE)
- Vazirmatn font: SIL Open Font License 1.1; see
  [`licenses/OFL-Vazirmatn.txt`](licenses/OFL-Vazirmatn.txt)
- Vazirmatn project: <https://github.com/rastikerdar/vazirmatn>

The piano texture is synthesized in the browser. No third-party audio recording
is included in this repository.

