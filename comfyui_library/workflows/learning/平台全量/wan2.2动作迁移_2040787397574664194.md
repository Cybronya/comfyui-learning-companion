---
key: 平台全量/wan2.2动作迁移_2040787397574664194.json
name: wan2.2动作迁移_2040787397574664194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2动作迁移_2040787397574664194.json
hash: cfe4095e109a6bbf
coverage: 0.928571
learned_at: 2026-11-14 01:19:44
nodes: [UnetLoaderGGUF, VAELoader, CLIPVisionLoader, ImageScale, PixelPerfectResolution, ModelSamplingSD3, ImageScale, PrimitiveInt, PrimitiveInt, CreateVideo, easy cleanGpuUsed, KSampler, DWPreprocessor, DWPreprocessor, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, CLIPLoader, TrimVideoLatent, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveVideo, WanAnimateToVideo, VHS_LoadVideo, VAEDecode, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 228711624086090, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/wan2.2动作迁移_2040787397574664194.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2动作迁移_2040787397574664194.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `UnetLoaderGGUF` ★核心
- `VAELoader`
- `CLIPVisionLoader`
- `ImageScale`
- `PixelPerfectResolution`
- `ModelSamplingSD3`
- `ImageScale`
- `PrimitiveInt`
- `PrimitiveInt`
- `CreateVideo`
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `DWPreprocessor`
- `DWPreprocessor`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `CLIPLoader`
- `TrimVideoLatent`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveVideo`
- `WanAnimateToVideo`
- `VHS_LoadVideo`
- `VAEDecode` ★核心
- `LoadImage`

## 关键参数

- `seed` = `228711624086090`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（26/28）

**有卡**：`UnetLoaderGGUF`、`VAELoader`、`CLIPVisionLoader`、`ImageScale`、`PixelPerfectResolution`、`ModelSamplingSD3`、`CreateVideo`、`easy cleanGpuUsed`、`KSampler`、`DWPreprocessor`、`CLIPTextEncode`、`CLIPVisionEncode`、`CLIPLoader`、`TrimVideoLatent`、`LoraLoaderModelOnly`、`SaveVideo`、`WanAnimateToVideo`、`VHS_LoadVideo`、`VAEDecode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、CLIPVisionEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
