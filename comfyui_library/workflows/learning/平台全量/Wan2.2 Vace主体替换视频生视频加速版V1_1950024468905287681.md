---
key: 平台全量/Wan2.2 Vace主体替换视频生视频加速版V1_1950024468905287681.json
name: Wan2.2 Vace主体替换视频生视频加速版V1_1950024468905287681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Vace主体替换视频生视频加速版V1_1950024468905287681.json
hash: 57307a03eccbbf91
coverage: 0.851852
learned_at: 2026-11-14 01:05:35
nodes: [CLIPTextEncode, MarkdownNote, PathchSageAttentionKJ, UnetLoaderGGUF, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, UnetLoaderGGUF, ModelSamplingSD3, ModelSamplingSD3, PrimitiveNode, VHS_VideoCombine, KSamplerAdvanced, KSamplerAdvanced, InvertMask, LayerMask: SAM2VideoUltra, LayerUtility: ImageScaleByAspectRatio V2, LayerMask: SAM2VideoUltra, GrowMaskWithBlur, MaskToImage, VAELoader, ImageFromBatch+, RebatchImages, ImageCompositeMasked, JWInteger, GetImageSize, PreviewImage, JWInteger, TrimVideoLatent, VAEDecode, VHS_LoadVideo, ImageFromBatch+, ImageConcanate, PDIMAGE_LongerSize, WanVaceToVideo, RebatchImages, JWInteger, CLIPTextEncode, LoadImage, ImageMirror, ImpactSwitch, JWInteger, JWInteger, LayerMask: ObjectDetectorFL2, CR Prompt Text, Note, LayerMask: LoadFlorence2Model, Note, Note, Note, PDIMAGE_LongerSize, VHS_VideoCombine, ImageConcanate, CLIPLoader]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "randomize"}
---

# 平台全量/Wan2.2 Vace主体替换视频生视频加速版V1_1950024468905287681.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Vace主体替换视频生视频加速版V1_1950024468905287681.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `PathchSageAttentionKJ`
- `UnetLoaderGGUF` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PrimitiveNode`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `InvertMask`
- `LayerMask: SAM2VideoUltra`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerMask: SAM2VideoUltra`
- `GrowMaskWithBlur`
- `MaskToImage`
- `VAELoader`
- `ImageFromBatch+`
- `RebatchImages`
- `ImageCompositeMasked`
- `JWInteger`
- `GetImageSize`
- `PreviewImage`
- `JWInteger`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `VHS_LoadVideo`
- `ImageFromBatch+`
- `ImageConcanate`
- `PDIMAGE_LongerSize`
- `WanVaceToVideo`
- `RebatchImages`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ImageMirror`
- `ImpactSwitch`
- `JWInteger`
- `JWInteger`
- `LayerMask: ObjectDetectorFL2`
- `CR Prompt Text`
- `Note`
- `LayerMask: LoadFlorence2Model`
- `Note`
- `Note`
- `Note`
- `PDIMAGE_LongerSize`
- `VHS_VideoCombine`
- `ImageConcanate`
- `CLIPLoader`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **85%**（46/54）

**有卡**：`CLIPTextEncode`、`PathchSageAttentionKJ`、`UnetLoaderGGUF`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VHS_VideoCombine`、`KSamplerAdvanced`、`InvertMask`、`LayerMask: SAM2VideoUltra`、`LayerUtility: ImageScaleByAspectRatio V2`、`GrowMaskWithBlur`、`MaskToImage`、`VAELoader`、`ImageFromBatch+`、`RebatchImages`、`ImageCompositeMasked`、`JWInteger`、`GetImageSize`、`TrimVideoLatent`、`VAEDecode`、`VHS_LoadVideo`、`ImageConcanate`、`PDIMAGE_LongerSize`、`WanVaceToVideo`、`LoadImage`、`ImageMirror`、`LayerMask: ObjectDetectorFL2`、`CR Prompt Text`、`LayerMask: LoadFlorence2Model`、`CLIPLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、KSamplerAdvanced、TrimVideoLatent
