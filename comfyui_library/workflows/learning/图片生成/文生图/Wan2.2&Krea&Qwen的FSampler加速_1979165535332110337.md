---
key: 图片生成/文生图/Wan2.2&Krea&Qwen的FSampler加速_1979165535332110337.json
name: Wan2.2&Krea&Qwen的FSampler加速_1979165535332110337
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2&Krea&Qwen的FSampler加速_1979165535332110337.json
hash: ec85fbbb708d41f8
coverage: 0.934783
learned_at: 2026-10-15 22:27:35
nodes: [FluxGuidance, ModelSamplingFlux, VAELoader, DualCLIPLoader, CLIPLoader, VAELoader, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, UNETLoader, UNETLoader, UNETLoader, CLIPTextEncode, CLIPLoader, VAELoader, CLIPTextEncode, UNETLoader, VAEDecode, SaveImage, SDXLEmptyLatentSizePicker+, LoraLoaderModelOnly, ModelSamplingAuraFlow, CLIPTextEncode, CLIPTextEncode, SDXLEmptyLatentSizePicker+, VAEDecode, LayerUtility: PurgeVRAM V2, SaveImage, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, String Literal, easy seed, SDXLEmptyLatentSizePicker+, FSampler, String Literal, FSampler, easy seed, FSamplerAdvanced, FSamplerAdvanced, VAEDecode, String Literal, PreviewImage, PreviewImage, easy seed, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 0, "height": 1, "width": "1280x768 (1.67)"}
---

# 图片生成/文生图/Wan2.2&Krea&Qwen的FSampler加速_1979165535332110337.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2&Krea&Qwen的FSampler加速_1979165535332110337.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（46 个）：
- `FluxGuidance`
- `ModelSamplingFlux`
- `VAELoader`
- `DualCLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SDXLEmptyLatentSizePicker+` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SDXLEmptyLatentSizePicker+` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `SaveImage`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `String Literal`
- `easy seed`
- `SDXLEmptyLatentSizePicker+` ★核心
- `FSampler` ★核心
- `String Literal`
- `FSampler` ★核心
- `easy seed`
- `FSamplerAdvanced` ★核心
- `FSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `String Literal`
- `PreviewImage`
- `PreviewImage`
- `easy seed`
- `PreviewImage`

## 关键参数

- `width` = `1280x768 (1.67)`
- `height` = `1`
- `batch_size` = `0`

## 知识

覆盖率 **93%**（43/46）

**有卡**：`FluxGuidance`、`ModelSamplingFlux`、`VAELoader`、`DualCLIPLoader`、`CLIPLoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`UNETLoader`、`VAEDecode`、`SaveImage`、`SDXLEmptyLatentSizePicker+`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`LayerUtility: PurgeVRAM V2`、`String Literal`、`easy seed`、`FSampler`、`FSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、FluxGuidance、FSampler
