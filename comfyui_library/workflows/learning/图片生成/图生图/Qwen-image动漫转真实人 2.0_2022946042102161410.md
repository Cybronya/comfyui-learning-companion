---
key: 图片生成/图生图/Qwen-image动漫转真实人 2.0_2022946042102161410.json
name: Qwen-image动漫转真实人 2.0_2022946042102161410
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image动漫转真实人 2.0_2022946042102161410.json
hash: 1f8651c4208a3f2f
coverage: 0.641026
learned_at: 2026-10-23 11:18:38
nodes: [CFGNorm, KSampler, UNETLoader, SetNode, GetNode, SetNode, Note, Note, easy int, GetNode, GetNode, SetNode, LoadImage, Florence2Run, DownloadAndLoadFlorence2Model, ImageScaleToTotalPixels, easy cleanGpuUsed, GetNode, PrimitiveString, ShowText|pysssss, Text Concatenate, Note, PrimitiveString, SeedVR2VideoUpscaler, VAEEncode, ModelSamplingAuraFlow, VAELoader, CLIPLoader, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, SaveImage, LayerUtility: PurgeVRAM V2, VAEDecode, SetNode, LoraLoaderModelOnly, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2TorchCompileSettings, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 438569037208469, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-image动漫转真实人 2.0_2022946042102161410.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image动漫转真实人 2.0_2022946042102161410.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `CFGNorm`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `Note`
- `Note`
- `easy int`
- `GetNode`
- `GetNode`
- `SetNode`
- `LoadImage`
- `Florence2Run`
- `DownloadAndLoadFlorence2Model`
- `ImageScaleToTotalPixels`
- `easy cleanGpuUsed`
- `GetNode`
- `PrimitiveString`
- `ShowText|pysssss`
- `Text Concatenate`
- `Note`
- `PrimitiveString`
- `SeedVR2VideoUpscaler`
- `VAEEncode` ★核心
- `ModelSamplingAuraFlow`
- `VAELoader`
- `CLIPLoader`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `SaveImage`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2TorchCompileSettings`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `438569037208469`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **64%**（25/39）

**有卡**：`CFGNorm`、`KSampler`、`UNETLoader`、`easy int`、`LoadImage`、`Florence2Run`、`DownloadAndLoadFlorence2Model`、`ImageScaleToTotalPixels`、`easy cleanGpuUsed`、`Text Concatenate`、`SeedVR2VideoUpscaler`、`VAEEncode`、`ModelSamplingAuraFlow`、`VAELoader`、`CLIPLoader`、`TextEncodeQwenImageEdit`、`TextEncodeQwenImageEditPlus`、`SaveImage`、`LayerUtility: PurgeVRAM V2`、`VAEDecode`、`LoraLoaderModelOnly`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2TorchCompileSettings`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
