---
key: 图片生成/文生图/图像控制 nunchaku-flux.1-depth 深度图控制_1955175871537713153.json
name: 图像控制 nunchaku-flux.1-depth 深度图控制_1955175871537713153
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/图像控制 nunchaku-flux.1-depth 深度图控制_1955175871537713153.json
hash: d7b18583458b11fc
coverage: 0.736842
learned_at: 2026-10-15 22:28:24
nodes: [CLIPTextEncode, DualCLIPLoader, PreviewImage, NunchakuFluxLoraLoader, Seed Everywhere, PreviewImage, Image Comparer (rgthree), Prompts Everywhere, FluxGuidance, CLIPTextEncode, NunchakuFluxDiTLoader, LoadImage, InstructPixToPixConditioning, VAELoader, Anything Everywhere, AIO_Preprocessor, KSampler (Efficient), SaveImage, Note]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 860855444243422, "steps": 20}
---

# 图片生成/文生图/图像控制 nunchaku-flux.1-depth 深度图控制_1955175871537713153.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/图像控制 nunchaku-flux.1-depth 深度图控制_1955175871537713153.json`

## 结构

**生成流程**：Model → Condition → Sampling → Output → Other

**节点**（19 个）：
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `PreviewImage`
- `NunchakuFluxLoraLoader` ★核心
- `Seed Everywhere`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Prompts Everywhere`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `NunchakuFluxDiTLoader`
- `LoadImage`
- `InstructPixToPixConditioning`
- `VAELoader`
- `Anything Everywhere`
- `AIO_Preprocessor`
- `KSampler (Efficient)` ★核心
- `SaveImage`
- `Note`

## 关键参数

- `seed` = `860855444243422`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **74%**（14/19）

**有卡**：`CLIPTextEncode`、`DualCLIPLoader`、`NunchakuFluxLoraLoader`、`Seed Everywhere`、`Prompts Everywhere`、`FluxGuidance`、`NunchakuFluxDiTLoader`、`LoadImage`、`InstructPixToPixConditioning`、`VAELoader`、`AIO_Preprocessor`、`KSampler (Efficient)`、`SaveImage`

**用到的条目**：VAELoader、CLIPTextEncode、LoadImage、FluxGuidance、KSampler (Efficient)、Seed Everywhere、NunchakuFluxLoraLoader、DualCLIPLoader
