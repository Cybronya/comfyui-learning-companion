---
key: 图片生成/文生图/Qwen-Image+Krea-refiner_1952978061257076737.json
name: Qwen-Image+Krea-refiner_1952978061257076737.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image+Krea-refiner_1952978061257076737.json
hash: 40a212c319c24f9c
coverage: 0.84375
learned_at: 2026-10-07 23:11:26
nodes: [CLIPTextEncode, FluxGuidance, ModelSamplingFlux, KSamplerSelect, RandomNoise, ModelSamplingAuraFlow, CLIPTextEncode, UNETLoader, CLIPLoader, VAELoader, KSampler, LayerUtility: PurgeVRAM V2, BasicGuider, DualCLIPLoader, UNETLoader, LayerUtility: PurgeVRAM V2, SamplerCustomAdvanced, VAELoader, ImageScaleBy, VAEEncode, VAEDecode, BasicScheduler, CLIPTextEncode, QwenImageModelLoader, easy seed, SDXLEmptyLatentSizePicker+, RH_QwenImageGenerator, SaveImage, VAEDecode, SaveImage, String Literal, SaveImage]
patterns: []
missing: [LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, String Literal, SDXLEmptyLatentSizePicker+, easy seed]
parameters: {"batch_size": 0, "cfg": 4, "denoise": 1, "height": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 964801033311783, "steps": 20, "width": "1280x768 (1.67)"}
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen-Image+Krea-refiner_1952978061257076737.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1952978061257076737.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ModelSamplingFlux`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `BasicGuider`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM V2`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `ImageScaleBy`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `QwenImageModelLoader`
- `easy seed`
- `SDXLEmptyLatentSizePicker+` ★核心
- `RH_QwenImageGenerator`
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImage`
- `String Literal`
- `SaveImage`

## 关键参数

- `seed` = `964801033311783`
- `steps` = `20`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1280x768 (1.67)`
- `height` = `1`
- `batch_size` = `0`

## 知识

覆盖率 **84%**（27/32）

**有卡**：`CLIPTextEncode`、`FluxGuidance`、`ModelSamplingFlux`、`KSamplerSelect`、`RandomNoise`、`ModelSamplingAuraFlow`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`BasicGuider`、`DualCLIPLoader`、`SamplerCustomAdvanced`、`ImageScaleBy`、`VAEEncode`、`VAEDecode`、`BasicScheduler`、`QwenImageModelLoader`、`RH_QwenImageGenerator`、`SaveImage`

**缺卡**（5）：`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`String Literal`、`SDXLEmptyLatentSizePicker+`、`easy seed`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、FluxGuidance、KSamplerSelect

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
