---
key: 图片生成/文生图/Wan2.2&Krea&Qwen的FSampler加速_1979165535332110337.json
name: Wan2.2&Krea&Qwen的FSampler加速_1979165535332110337
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2&Krea&Qwen的FSampler加速_1979165535332110337.json
hash: ec85fbbb708d41f8
coverage: 0.673913
learned_at: 2026-10-10 20:59:14
nodes: [FluxGuidance, ModelSamplingFlux, VAELoader, DualCLIPLoader, CLIPLoader, VAELoader, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, UNETLoader, UNETLoader, UNETLoader, CLIPTextEncode, CLIPLoader, VAELoader, CLIPTextEncode, UNETLoader, VAEDecode, SaveImage, SDXLEmptyLatentSizePicker+, LoraLoaderModelOnly, ModelSamplingAuraFlow, CLIPTextEncode, CLIPTextEncode, SDXLEmptyLatentSizePicker+, VAEDecode, LayerUtility: PurgeVRAM V2, SaveImage, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, String Literal, easy seed, SDXLEmptyLatentSizePicker+, FSampler, String Literal, FSampler, easy seed, FSamplerAdvanced, FSamplerAdvanced, VAEDecode, String Literal, PreviewImage, PreviewImage, easy seed, PreviewImage]
patterns: []
missing: [LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, String Literal, String Literal, String Literal, SDXLEmptyLatentSizePicker+, SDXLEmptyLatentSizePicker+, SDXLEmptyLatentSizePicker+, easy seed, easy seed, easy seed]
parameters: {"batch_size": 0, "height": 1, "width": "1280x768 (1.67)"}
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明, 核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明, 核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Wan2.2&Krea&Qwen的FSampler加速_1979165535332110337.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2&Krea&Qwen的FSampler加速_1979165535332110337.json`

## 结构

**节点**（46 个）：
- `FluxGuidance`
- `ModelSamplingFlux`
- `VAELoader`
- `DualCLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `UNETLoader`
- `UNETLoader`
- `UNETLoader`
- `CLIPTextEncode`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode`
- `UNETLoader`
- `VAEDecode`
- `SaveImage`
- `SDXLEmptyLatentSizePicker+`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `SDXLEmptyLatentSizePicker+`
- `VAEDecode`
- `LayerUtility: PurgeVRAM V2`
- `SaveImage`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `String Literal`
- `easy seed`
- `SDXLEmptyLatentSizePicker+`
- `FSampler`
- `String Literal`
- `FSampler`
- `easy seed`
- `FSamplerAdvanced`
- `FSamplerAdvanced`
- `VAEDecode`
- `String Literal`
- `PreviewImage`
- `PreviewImage`
- `easy seed`
- `PreviewImage`

## 关键参数

- `batch_size` = `0`
- `height` = `1`
- `width` = `1280x768 (1.67)`

## 知识

覆盖率 **67%**（31/46）

**有卡**：`FluxGuidance`、`ModelSamplingFlux`、`VAELoader`、`DualCLIPLoader`、`CLIPLoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`UNETLoader`、`VAEDecode`、`SaveImage`、`SDXLEmptyLatentSizePicker+`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`LayerUtility: PurgeVRAM V2`

**缺卡**（12）：`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`String Literal`、`String Literal`、`String Literal`、`SDXLEmptyLatentSizePicker+`、`SDXLEmptyLatentSizePicker+`、`SDXLEmptyLatentSizePicker+`、`easy seed`、`easy seed`、`easy seed`

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明
- 核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明
- 核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
