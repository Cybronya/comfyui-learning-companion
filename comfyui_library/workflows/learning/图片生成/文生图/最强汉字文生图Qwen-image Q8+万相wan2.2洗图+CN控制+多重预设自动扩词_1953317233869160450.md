---
key: 图片生成/文生图/最强汉字文生图Qwen-image Q8+万相wan2.2洗图+CN控制+多重预设自动扩词_1953317233869160450.json
name: 最强汉字文生图Qwen-image Q8+万相wan2.2洗图+CN控制+多重预设自动扩词_1953317233869160450
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/最强汉字文生图Qwen-image Q8+万相wan2.2洗图+CN控制+多重预设自动扩词_1953317233869160450.json
hash: 33111395e4c1e3cf
coverage: 0.887097
learned_at: 2026-10-15 22:28:53
nodes: [LayerUtility: PurgeVRAM, CLIPLoader, CLIPTextEncode, ModelSamplingSD3, LayerUtility: PurgeVRAM, INPAINT_ExpandMask, BBoxesToSAM2, VAELoader, InpaintModelConditioning, VAEDecode, PathchSageAttentionKJ, MaskPreview+, InvertMask, CLIPTextEncode, QwenVLDetection, LayerUtility: PurgeVRAM V2, SaveImage, CLIPTextEncode, CLIPLoader, VAELoader, EmptySD3LatentImage, LayerMask: LoadSAM2Model, easy showAnything, LayerMask: SAM2UltraV2, LayerUtility: PurgeVRAM, SaveImage, Image Comparer (rgthree), UNETLoader, KSampler, LoraLoaderModelOnly, DownloadAndLoadQwenModel, ImageResizeKJv2, ModelSamplingAuraFlow, CLIPTextEncode, ReferenceLatent, easy anythingIndexSwitch, easy anythingIndexSwitch, LayerUtility: PurgeVRAM V2, VAEEncode, CR Prompt Text, LoraLoaderModelOnly, LoadImage, PreviewImage, GetControlImage, PrimitiveStringMultiline, JWInteger, JWInteger, ShowText|pysssss, SaveImage, KSampler, VAEDecode, PathchSageAttentionKJ, easy promptConcat, LoraLoaderModelOnly, LoraLoaderModelOnly, SeedVR2, SeedVR2BlockSwap, PrimitiveFloat, Fast Groups Muter (rgthree), PresetTextSelector, RHHiddenNodes, UnetLoaderGGUF]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "res_3m", "scheduler": "beta57", "seed": 963613917353141, "steps": 40}
---

# 图片生成/文生图/最强汉字文生图Qwen-image Q8+万相wan2.2洗图+CN控制+多重预设自动扩词_1953317233869160450.json

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

覆盖率 **89%**（55/62）

**有卡**：`LayerUtility: PurgeVRAM`、`CLIPLoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`INPAINT_ExpandMask`、`BBoxesToSAM2`、`VAELoader`、`InpaintModelConditioning`、`VAEDecode`、`PathchSageAttentionKJ`、`MaskPreview+`、`InvertMask`、`QwenVLDetection`、`LayerUtility: PurgeVRAM V2`、`SaveImage`、`EmptySD3LatentImage`、`LayerMask: LoadSAM2Model`、`LayerMask: SAM2UltraV2`、`UNETLoader`、`KSampler`、`LoraLoaderModelOnly`、`DownloadAndLoadQwenModel`、`ImageResizeKJv2`、`ModelSamplingAuraFlow`、`ReferenceLatent`、`easy anythingIndexSwitch`、`VAEEncode`、`CR Prompt Text`、`LoadImage`、`GetControlImage`、`JWInteger`、`easy promptConcat`、`SeedVR2`、`SeedVR2BlockSwap`、`PresetTextSelector`、`RHHiddenNodes`、`UnetLoaderGGUF`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
