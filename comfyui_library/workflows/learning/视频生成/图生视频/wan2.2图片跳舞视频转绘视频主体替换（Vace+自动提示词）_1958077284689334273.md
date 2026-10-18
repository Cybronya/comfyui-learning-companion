---
key: 视频生成/图生视频/wan2.2图片跳舞视频转绘视频主体替换（Vace+自动提示词）_1958077284689334273.json
name: wan2.2图片跳舞视频转绘视频主体替换（Vace+自动提示词）_1958077284689334273.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2图片跳舞视频转绘视频主体替换（Vace+自动提示词）_1958077284689334273.json
hash: faa00117124751c9
coverage: 0.859375
learned_at: 2026-10-15 22:31:20
nodes: [CLIPTextEncode, MarkdownNote, PathchSageAttentionKJ, LoraLoaderModelOnly, ModelSamplingSD3, InvertMask, MaskToImage, ImageFromBatch+, RebatchImages, ImageCompositeMasked, LayerMask: LoadFlorence2Model, Note, Note, Note, CLIPTextEncode, LoraLoaderModelOnly, GetImageSize, WanVaceToVideo, RebatchImages, PreviewImage, PreviewImage, ImageMirror, ImpactSwitch, InspyrenetRembg, CLIPLoader, VAELoader, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, CR Prompt Text, Note, LayerMask: ObjectDetectorFL2, LayerMask: SAM2VideoUltra, LayerMask: SAM2VideoUltra, GrowMaskWithBlur, UnetLoaderGGUF, UnetLoaderGGUF, PathchSageAttentionKJ, ModelSamplingSD3, PrimitiveNode, KSamplerAdvanced, KSamplerAdvanced, ImageConcanate, TrimVideoLatent, ImageFromBatch+, VAEDecode, PDIMAGE_LongerSize, ImageConcanate, PDIMAGE_LongerSize, VHS_LoadVideo, JWInteger, JWInteger, JWInteger, LayerUtility: ImageRemoveAlpha, RH_Captioner, ShowText, easy promptConcat, ShowText, SimpleMath+, JWInteger, LoadImage, CR Prompt Text, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2图片跳舞视频转绘视频主体替换（Vace+自动提示词）_1958077284689334273.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1958077284689334273.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `InvertMask`
- `MaskToImage`
- `ImageFromBatch+`
- `RebatchImages`
- `ImageCompositeMasked`
- `LayerMask: LoadFlorence2Model`
- `Note`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetImageSize`
- `WanVaceToVideo`
- `RebatchImages`
- `PreviewImage`
- `PreviewImage`
- `ImageMirror`
- `ImpactSwitch`
- `InspyrenetRembg`
- `CLIPLoader`
- `VAELoader`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `CR Prompt Text`
- `Note`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: SAM2VideoUltra`
- `LayerMask: SAM2VideoUltra`
- `GrowMaskWithBlur`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PrimitiveNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ImageConcanate`
- `TrimVideoLatent`
- `ImageFromBatch+`
- `VAEDecode` ★核心
- `PDIMAGE_LongerSize`
- `ImageConcanate`
- `PDIMAGE_LongerSize`
- `VHS_LoadVideo`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `LayerUtility: ImageRemoveAlpha`
- `RH_Captioner`
- `ShowText`
- `easy promptConcat`
- `ShowText`
- `SimpleMath+`
- `JWInteger`
- `LoadImage`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **86%**（55/64）

**有卡**：`CLIPTextEncode`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`InvertMask`、`MaskToImage`、`ImageFromBatch+`、`RebatchImages`、`ImageCompositeMasked`、`LayerMask: LoadFlorence2Model`、`GetImageSize`、`WanVaceToVideo`、`ImageMirror`、`InspyrenetRembg`、`CLIPLoader`、`VAELoader`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Prompt Text`、`LayerMask: ObjectDetectorFL2`、`LayerMask: SAM2VideoUltra`、`GrowMaskWithBlur`、`UnetLoaderGGUF`、`KSamplerAdvanced`、`ImageConcanate`、`TrimVideoLatent`、`VAEDecode`、`PDIMAGE_LongerSize`、`VHS_LoadVideo`、`LayerUtility: ImageRemoveAlpha`、`RH_Captioner`、`ShowText`、`easy promptConcat`、`SimpleMath+`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、TrimVideoLatent
