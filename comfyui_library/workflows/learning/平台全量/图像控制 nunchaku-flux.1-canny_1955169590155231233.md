---
key: 平台全量/图像控制 nunchaku-flux.1-canny_1955169590155231233.json
name: 图像控制 nunchaku-flux.1-canny_1955169590155231233
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/图像控制 nunchaku-flux.1-canny_1955169590155231233.json
hash: ae865630f6b87d2b
coverage: 0.722222
learned_at: 2026-11-14 01:53:35
nodes: [FluxGuidance, CLIPTextEncode, DualCLIPLoader, PreviewImage, NunchakuFluxLoraLoader, Image Comparer (rgthree), InstructPixToPixConditioning, CLIPTextEncode, Prompts Everywhere, LoadImage, NunchakuFluxDiTLoader, Note, VAELoader, PreviewImage, Anything Everywhere, AIO_Preprocessor, KSampler (Efficient), SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 910160214287452, "steps": 20}
---

# 平台全量/图像控制 nunchaku-flux.1-canny_1955169590155231233.json

> 来源文件 `comfyui_library/workflows/平台全量/图像控制 nunchaku-flux.1-canny_1955169590155231233.json`

## 结构

**生成流程**：Model → Condition → Sampling → Output → Other

**节点**（18 个）：
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `PreviewImage`
- `NunchakuFluxLoraLoader` ★核心
- `Image Comparer (rgthree)`
- `InstructPixToPixConditioning`
- `CLIPTextEncode` ★核心
- `Prompts Everywhere`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `Note`
- `VAELoader`
- `PreviewImage`
- `Anything Everywhere`
- `AIO_Preprocessor`
- `KSampler (Efficient)` ★核心
- `SaveImage`

## 关键参数

- `seed` = `910160214287452`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **72%**（13/18）

**有卡**：`FluxGuidance`、`CLIPTextEncode`、`DualCLIPLoader`、`NunchakuFluxLoraLoader`、`InstructPixToPixConditioning`、`Prompts Everywhere`、`LoadImage`、`NunchakuFluxDiTLoader`、`VAELoader`、`AIO_Preprocessor`、`KSampler (Efficient)`、`SaveImage`

**用到的条目**：VAELoader、CLIPTextEncode、LoadImage、FluxGuidance、KSampler (Efficient)、NunchakuFluxLoraLoader、DualCLIPLoader、NunchakuFluxDiTLoader
