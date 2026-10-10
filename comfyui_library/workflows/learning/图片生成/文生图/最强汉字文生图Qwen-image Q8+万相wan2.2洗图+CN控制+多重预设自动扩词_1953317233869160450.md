---
key: 最强汉字文生图Qwen-image Q8+万相wan2.2洗图+CN控制+多重预设自动扩词_1953317233869160450.json
name: 最强汉字文生图Qwen-image Q8+万相wan2.2洗图+CN控制+多重预设自动扩词_1953317233869160450
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/最强汉字文生图Qwen-image Q8+万相wan2.2洗图+CN控制+多重预设自动扩词_1953317233869160450.json
hash: 33111395e4c1e3cf
coverage: 0.693548
learned_at: 2026-10-10 20:59:50
nodes: [LayerUtility: PurgeVRAM, CLIPLoader, CLIPTextEncode, ModelSamplingSD3, LayerUtility: PurgeVRAM, INPAINT_ExpandMask, BBoxesToSAM2, VAELoader, InpaintModelConditioning, VAEDecode, PathchSageAttentionKJ, MaskPreview+, InvertMask, CLIPTextEncode, QwenVLDetection, LayerUtility: PurgeVRAM V2, SaveImage, CLIPTextEncode, CLIPLoader, VAELoader, EmptySD3LatentImage, LayerMask: LoadSAM2Model, easy showAnything, LayerMask: SAM2UltraV2, LayerUtility: PurgeVRAM, SaveImage, Image Comparer (rgthree), UNETLoader, KSampler, LoraLoaderModelOnly, DownloadAndLoadQwenModel, ImageResizeKJv2, ModelSamplingAuraFlow, CLIPTextEncode, ReferenceLatent, easy anythingIndexSwitch, easy anythingIndexSwitch, LayerUtility: PurgeVRAM V2, VAEEncode, CR Prompt Text, LoraLoaderModelOnly, LoadImage, PreviewImage, GetControlImage, PrimitiveStringMultiline, JWInteger, JWInteger, ShowText|pysssss, SaveImage, KSampler, VAEDecode, PathchSageAttentionKJ, easy promptConcat, LoraLoaderModelOnly, LoraLoaderModelOnly, SeedVR2, SeedVR2BlockSwap, PrimitiveFloat, Fast Groups Muter (rgthree), PresetTextSelector, RHHiddenNodes, UnetLoaderGGUF]
patterns: [image_to_image]
missing: [LayerMask: LoadSAM2Model, LayerMask: SAM2UltraV2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, easy anythingIndexSwitch, easy anythingIndexSwitch, CR Prompt Text, MaskPreview+, easy promptConcat]
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "res_3m", "scheduler": "beta57", "seed": 963613917353141, "steps": 40}
discoveries: [次要节点 `LayerMask: LoadSAM2Model` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: SAM2UltraV2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `MaskPreview+` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 最强汉字文生图Qwen-image Q8+万相wan2.2洗图+CN控制+多重预设自动扩词_1953317233869160450.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/最强汉字文生图Qwen-image Q8+万相wan2.2洗图+CN控制+多重预设自动扩词_1953317233869160450.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `LayerUtility: PurgeVRAM`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM`
- `INPAINT_ExpandMask`
- `BBoxesToSAM2`
- `VAELoader`
- `InpaintModelConditioning`
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `MaskPreview+`
- `InvertMask`
- `CLIPTextEncode` ★核心
- `QwenVLDetection`
- `LayerUtility: PurgeVRAM V2`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptySD3LatentImage`
- `LayerMask: LoadSAM2Model`
- `easy showAnything`
- `LayerMask: SAM2UltraV2`
- `LayerUtility: PurgeVRAM`
- `SaveImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `DownloadAndLoadQwenModel`
- `ImageResizeKJv2`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `LayerUtility: PurgeVRAM V2`
- `VAEEncode` ★核心
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `PreviewImage`
- `GetControlImage`
- `PrimitiveStringMultiline`
- `JWInteger`
- `JWInteger`
- `ShowText|pysssss`
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `easy promptConcat`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SeedVR2`
- `SeedVR2BlockSwap`
- `PrimitiveFloat`
- `Fast Groups Muter (rgthree)`
- `PresetTextSelector`
- `RHHiddenNodes`
- `UnetLoaderGGUF` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `963613917353141`
- `steps` = `40`
- `cfg` = `5`
- `sampler_name` = `res_3m`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **69%**（43/62）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`INPAINT_ExpandMask`、`BBoxesToSAM2`、`VAELoader`、`InpaintModelConditioning`、`VAEDecode`、`PathchSageAttentionKJ`、`InvertMask`、`QwenVLDetection`、`SaveImage`、`EmptySD3LatentImage`、`UNETLoader`、`KSampler`、`LoraLoaderModelOnly`、`DownloadAndLoadQwenModel`、`ImageResizeKJv2`、`ModelSamplingAuraFlow`、`ReferenceLatent`、`VAEEncode`、`LoadImage`、`GetControlImage`、`JWInteger`、`SeedVR2`、`SeedVR2BlockSwap`、`PresetTextSelector`、`RHHiddenNodes`、`UnetLoaderGGUF`

**缺卡**（12）：`LayerMask: LoadSAM2Model`、`LayerMask: SAM2UltraV2`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`easy anythingIndexSwitch`、`easy anythingIndexSwitch`、`CR Prompt Text`、`MaskPreview+`、`easy promptConcat`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 学习发现

- 次要节点 `LayerMask: LoadSAM2Model` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: SAM2UltraV2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `MaskPreview+` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
