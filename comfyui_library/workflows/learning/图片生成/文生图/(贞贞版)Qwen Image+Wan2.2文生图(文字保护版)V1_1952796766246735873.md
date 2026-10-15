---
key: 图片生成/文生图/(贞贞版)Qwen Image+Wan2.2文生图(文字保护版)V1_1952796766246735873.json
name: (贞贞版)Qwen Image+Wan2.2文生图(文字保护版)V1_1952796766246735873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/(贞贞版)Qwen Image+Wan2.2文生图(文字保护版)V1_1952796766246735873.json
hash: 8a780fd823497f62
coverage: 0.931818
learned_at: 2026-10-15 22:26:05
nodes: [CLIPLoader, ModelSamplingAuraFlow, VAELoader, CLIPTextEncode, KSampler, CLIPTextEncode, VAELoader, InpaintModelConditioning, ModelSamplingSD3, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, CLIPLoader, UNETLoader, InvertMask, LoraLoaderModelOnly, SaveImage, VAEDecode, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, PreviewImage, BBoxesToSAM2, easy showAnything, LayerMask: LoadSAM2Model, LayerUtility: PurgeVRAM, CR Prompt Text, KSampler, DownloadAndLoadQwenModel, LayerMask: SAM2UltraV2, LayerUtility: PurgeVRAM, MaskPreview+, MaskToImage, PreviewImage, INPAINT_ExpandMask, SaveImage, VAEDecode, LoadImage, QwenVLDetection, CLIPTextEncode, CLIPTextEncode, CR Prompt Text, EmptySD3LatentImage, JWInteger, JWInteger]
patterns: []
missing: []
parameters: {"cfg": 3.5, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 436504485801433, "steps": 20}
---

# 图片生成/文生图/(贞贞版)Qwen Image+Wan2.2文生图(文字保护版)V1_1952796766246735873.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/(贞贞版)Qwen Image+Wan2.2文生图(文字保护版)V1_1952796766246735873.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `InpaintModelConditioning`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `InvertMask`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `BBoxesToSAM2`
- `easy showAnything`
- `LayerMask: LoadSAM2Model`
- `LayerUtility: PurgeVRAM`
- `CR Prompt Text`
- `KSampler` ★核心
- `DownloadAndLoadQwenModel`
- `LayerMask: SAM2UltraV2`
- `LayerUtility: PurgeVRAM`
- `MaskPreview+`
- `MaskToImage`
- `PreviewImage`
- `INPAINT_ExpandMask`
- `SaveImage`
- `VAEDecode` ★核心
- `LoadImage`
- `QwenVLDetection`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `EmptySD3LatentImage`
- `JWInteger`
- `JWInteger`

## 关键参数

- `seed` = `436504485801433`
- `steps` = `20`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **93%**（41/44）

**有卡**：`CLIPLoader`、`ModelSamplingAuraFlow`、`VAELoader`、`CLIPTextEncode`、`KSampler`、`InpaintModelConditioning`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`UNETLoader`、`InvertMask`、`SaveImage`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`BBoxesToSAM2`、`LayerMask: LoadSAM2Model`、`CR Prompt Text`、`DownloadAndLoadQwenModel`、`LayerMask: SAM2UltraV2`、`MaskPreview+`、`MaskToImage`、`INPAINT_ExpandMask`、`LoadImage`、`QwenVLDetection`、`EmptySD3LatentImage`、`JWInteger`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
