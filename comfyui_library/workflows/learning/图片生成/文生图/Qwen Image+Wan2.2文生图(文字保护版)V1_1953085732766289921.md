---
key: 图片生成/文生图/Qwen Image+Wan2.2文生图(文字保护版)V1_1953085732766289921.json
name: Qwen Image+Wan2.2文生图(文字保护版)V1_1953085732766289921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image+Wan2.2文生图(文字保护版)V1_1953085732766289921.json
hash: 4fee8eade4ff0771
coverage: 0.75
learned_at: 2026-10-10 20:58:55
nodes: [CLIPLoader, ModelSamplingAuraFlow, VAELoader, CLIPTextEncode, KSampler, CLIPTextEncode, VAELoader, InpaintModelConditioning, ModelSamplingSD3, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, CLIPLoader, UNETLoader, InvertMask, LoraLoaderModelOnly, SaveImage, VAEDecode, LayerUtility: PurgeVRAM, PreviewImage, BBoxesToSAM2, easy showAnything, LayerMask: LoadSAM2Model, LayerUtility: PurgeVRAM, CR Prompt Text, KSampler, DownloadAndLoadQwenModel, LayerMask: SAM2UltraV2, LayerUtility: PurgeVRAM, MaskPreview+, MaskToImage, PreviewImage, INPAINT_ExpandMask, SaveImage, VAEDecode, LoadImage, QwenVLDetection, CLIPTextEncode, CLIPTextEncode, CR Prompt Text, EmptySD3LatentImage, JWInteger, JWInteger, LoraLoaderModelOnly]
patterns: []
missing: [LayerMask: LoadSAM2Model, LayerMask: SAM2UltraV2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CR Prompt Text, CR Prompt Text, MaskPreview+]
parameters: {"cfg": 3.5, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 436504485801433, "steps": 20}
discoveries: [次要节点 `LayerMask: LoadSAM2Model` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: SAM2UltraV2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `MaskPreview+` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen Image+Wan2.2文生图(文字保护版)V1_1953085732766289921.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image+Wan2.2文生图(文字保护版)V1_1953085732766289921.json`

## 结构

**节点**（44 个）：
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `VAELoader`
- `CLIPTextEncode`
- `KSampler`
- `CLIPTextEncode`
- `VAELoader`
- `InpaintModelConditioning`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `CLIPLoader`
- `UNETLoader`
- `InvertMask`
- `LoraLoaderModelOnly`
- `SaveImage`
- `VAEDecode`
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `BBoxesToSAM2`
- `easy showAnything`
- `LayerMask: LoadSAM2Model`
- `LayerUtility: PurgeVRAM`
- `CR Prompt Text`
- `KSampler`
- `DownloadAndLoadQwenModel`
- `LayerMask: SAM2UltraV2`
- `LayerUtility: PurgeVRAM`
- `MaskPreview+`
- `MaskToImage`
- `PreviewImage`
- `INPAINT_ExpandMask`
- `SaveImage`
- `VAEDecode`
- `LoadImage`
- `QwenVLDetection`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptySD3LatentImage`
- `JWInteger`
- `JWInteger`
- `LoraLoaderModelOnly`

## 关键参数

- `cfg` = `3.5`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `seed` = `436504485801433`
- `steps` = `20`

## 知识

覆盖率 **75%**（33/44）

**有卡**：`CLIPLoader`、`ModelSamplingAuraFlow`、`VAELoader`、`CLIPTextEncode`、`KSampler`、`InpaintModelConditioning`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`UNETLoader`、`InvertMask`、`SaveImage`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`PreviewImage`、`BBoxesToSAM2`、`easy showAnything`、`LayerMask: LoadSAM2Model`、`CR Prompt Text`、`DownloadAndLoadQwenModel`、`LayerMask: SAM2UltraV2`、`MaskPreview+`、`MaskToImage`、`INPAINT_ExpandMask`

**缺卡**（8）：`LayerMask: LoadSAM2Model`、`LayerMask: SAM2UltraV2`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`CR Prompt Text`、`CR Prompt Text`、`MaskPreview+`

## 学习发现

- 次要节点 `LayerMask: LoadSAM2Model` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: SAM2UltraV2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `MaskPreview+` 仅有 SaveImage 的通用知识，没有该节点自己的说明
