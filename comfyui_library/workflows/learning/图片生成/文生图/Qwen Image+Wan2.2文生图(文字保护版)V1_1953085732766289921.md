---
key: 图片生成/文生图/Qwen Image+Wan2.2文生图(文字保护版)V1_1953085732766289921.json
name: Qwen Image+Wan2.2文生图(文字保护版)V1_1953085732766289921.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image+Wan2.2文生图(文字保护版)V1_1953085732766289921.json
hash: 4fee8eade4ff0771
coverage: 0.75
learned_at: 2026-10-07 23:11:35
nodes: [CLIPLoader, ModelSamplingAuraFlow, VAELoader, CLIPTextEncode, KSampler, CLIPTextEncode, VAELoader, InpaintModelConditioning, ModelSamplingSD3, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, CLIPLoader, UNETLoader, InvertMask, LoraLoaderModelOnly, SaveImage, VAEDecode, LayerUtility: PurgeVRAM, PreviewImage, BBoxesToSAM2, easy showAnything, LayerMask: LoadSAM2Model, LayerUtility: PurgeVRAM, CR Prompt Text, KSampler, DownloadAndLoadQwenModel, LayerMask: SAM2UltraV2, LayerUtility: PurgeVRAM, MaskPreview+, MaskToImage, PreviewImage, INPAINT_ExpandMask, SaveImage, VAEDecode, LoadImage, QwenVLDetection, CLIPTextEncode, CLIPTextEncode, CR Prompt Text, EmptySD3LatentImage, JWInteger, JWInteger, LoraLoaderModelOnly]
patterns: []
missing: [LayerMask: LoadSAM2Model, LayerMask: SAM2UltraV2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CR Prompt Text, CR Prompt Text, MaskPreview+]
parameters: {"cfg": 3.5, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 436504485801433, "steps": 20}
discoveries: [次要节点 `LayerMask: LoadSAM2Model` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: SAM2UltraV2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `MaskPreview+` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen Image+Wan2.2文生图(文字保护版)V1_1953085732766289921.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1953085732766289921.json`

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
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `436504485801433`
- `steps` = `20`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **75%**（33/44）

**有卡**：`CLIPLoader`、`ModelSamplingAuraFlow`、`VAELoader`、`CLIPTextEncode`、`KSampler`、`InpaintModelConditioning`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`UNETLoader`、`InvertMask`、`SaveImage`、`VAEDecode`、`BBoxesToSAM2`、`DownloadAndLoadQwenModel`、`MaskToImage`、`INPAINT_ExpandMask`、`LoadImage`、`QwenVLDetection`、`EmptySD3LatentImage`、`JWInteger`

**缺卡**（8）：`LayerMask: LoadSAM2Model`、`LayerMask: SAM2UltraV2`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`CR Prompt Text`、`CR Prompt Text`、`MaskPreview+`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 学习发现

- 次要节点 `LayerMask: LoadSAM2Model` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: SAM2UltraV2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `MaskPreview+` 仅有 SaveImage 的通用知识，没有该节点自己的说明
