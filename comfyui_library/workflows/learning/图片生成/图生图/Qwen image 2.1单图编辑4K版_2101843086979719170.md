---
key: 图片生成/图生图/Qwen image 2.1单图编辑4K版_2101843086979719170.json
name: Qwen image 2.1单图编辑4K版_2101843086979719170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1单图编辑4K版_2101843086979719170.json
hash: e564f5e2e77d8dc0
coverage: 0.888889
learned_at: 2026-10-21 00:42:56
nodes: [CLIPLoader, BatchImagesNode, QwenImage21Cache, KSampler, VAELoader, CLIPLoader, ComfySwitchNode, TextGenerateLTX2Prompt, EmptyLatentImage, ResolutionSelector, KOOK_ImageCompression, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, VAEDecode, SaveImage, UNETLoader, TextEncodeQwenImage21, KSampler, easy showAnything, LoraLoaderModelOnly, EmptyLatentImage, VAEDecode, PreviewImage, KOOK_SaveJPGImage, LoadImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.30000000000000004, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 1, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image 2.1单图编辑4K版_2101843086979719170.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1单图编辑4K版_2101843086979719170.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `CLIPLoader`
- `BatchImagesNode`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAELoader`
- `CLIPLoader`
- `ComfySwitchNode`
- `TextGenerateLTX2Prompt`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `KOOK_ImageCompression`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `VAEDecode` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `KOOK_SaveJPGImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `999`
- `steps` = `1`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.30000000000000004`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`CLIPLoader`、`BatchImagesNode`、`QwenImage21Cache`、`KSampler`、`VAELoader`、`TextGenerateLTX2Prompt`、`EmptyLatentImage`、`ResolutionSelector`、`KOOK_ImageCompression`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`VAEDecode`、`SaveImage`、`UNETLoader`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`KOOK_SaveJPGImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
