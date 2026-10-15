---
key: 图片生成/文生图/图像控制 nunchaku-flux.1-depth 深度图控制_1955175871537713153.json
name: 图像控制 nunchaku-flux.1-depth 深度图控制_1955175871537713153
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/图像控制 nunchaku-flux.1-depth 深度图控制_1955175871537713153.json
hash: d7b18583458b11fc
coverage: 0.578947
learned_at: 2026-10-10 20:59:41
nodes: [CLIPTextEncode, DualCLIPLoader, PreviewImage, NunchakuFluxLoraLoader, Seed Everywhere, PreviewImage, Image Comparer (rgthree), Prompts Everywhere, FluxGuidance, CLIPTextEncode, NunchakuFluxDiTLoader, LoadImage, InstructPixToPixConditioning, VAELoader, Anything Everywhere, AIO_Preprocessor, KSampler (Efficient), SaveImage, Note]
patterns: []
missing: [KSampler (Efficient), Prompts Everywhere, Seed Everywhere]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 860855444243422, "steps": 20}
discoveries: [核心节点 `KSampler (Efficient)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `Prompts Everywhere` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/图像控制 nunchaku-flux.1-depth 深度图控制_1955175871537713153.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/图像控制 nunchaku-flux.1-depth 深度图控制_1955175871537713153.json`

## 结构

**节点**（19 个）：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `PreviewImage`
- `NunchakuFluxLoraLoader`
- `Seed Everywhere`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Prompts Everywhere`
- `FluxGuidance`
- `CLIPTextEncode`
- `NunchakuFluxDiTLoader`
- `LoadImage`
- `InstructPixToPixConditioning`
- `VAELoader`
- `Anything Everywhere`
- `AIO_Preprocessor`
- `KSampler (Efficient)`
- `SaveImage`
- `Note`

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `860855444243422`
- `steps` = `20`

## 知识

覆盖率 **58%**（11/19）

**有卡**：`CLIPTextEncode`、`DualCLIPLoader`、`PreviewImage`、`NunchakuFluxLoraLoader`、`Seed Everywhere`、`Image Comparer (rgthree)`、`Prompts Everywhere`、`FluxGuidance`、`NunchakuFluxDiTLoader`

**缺卡**（3）：`KSampler (Efficient)`、`Prompts Everywhere`、`Seed Everywhere`

## 学习发现

- 核心节点 `KSampler (Efficient)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `Prompts Everywhere` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明
