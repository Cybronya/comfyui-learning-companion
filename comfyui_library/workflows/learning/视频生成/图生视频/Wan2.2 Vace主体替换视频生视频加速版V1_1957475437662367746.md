---
key: 视频生成/图生视频/Wan2.2 Vace主体替换视频生视频加速版V1_1957475437662367746.json
name: Wan2.2 Vace主体替换视频生视频加速版V1_1957475437662367746.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1957475437662367746.json
hash: 1c3110999d0f9242
coverage: 0.854839
learned_at: 2026-10-15 22:31:17
nodes: [CLIPTextEncode, MarkdownNote, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, PrimitiveNode, KSamplerAdvanced, InvertMask, LayerMask: SAM2VideoUltra, LayerUtility: ImageScaleByAspectRatio V2, LayerMask: SAM2VideoUltra, MaskToImage, VAELoader, ImageFromBatch+, RebatchImages, ImageCompositeMasked, JWInteger, ImageConcanate, JWInteger, JWInteger, LayerMask: ObjectDetectorFL2, Note, LayerMask: LoadFlorence2Model, Note, Note, Note, PDIMAGE_LongerSize, ImageConcanate, CLIPLoader, ImageMirror, CR Prompt Text, CLIPTextEncode, UnetLoaderGGUF, UnetLoaderGGUF, LoraLoaderModelOnly, JWInteger, ImpactSwitch, InspyrenetRembg, TrimVideoLatent, VAEDecode, ImageFromBatch+, VHS_LoadVideo, JWInteger, KSamplerAdvanced, PDIMAGE_LongerSize, VHS_VideoCombine, VHS_VideoCombine, GetImageSize, WanVaceToVideo, PreviewImage, RebatchImages, GrowMaskWithBlur, PreviewImage, LoadImage, CR Prompt Text, easy promptConcat, ShowText, ShowText, RH_Captioner, LayerUtility: ImageRemoveAlpha]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 Vace主体替换视频生视频加速版V1_1957475437662367746.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1957475437662367746.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PrimitiveNode`
- `KSamplerAdvanced` ★核心
- `InvertMask`
- `LayerMask: SAM2VideoUltra`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerMask: SAM2VideoUltra`
- `MaskToImage`
- `VAELoader`
- `ImageFromBatch+`
- `RebatchImages`
- `ImageCompositeMasked`
- `JWInteger`
- `ImageConcanate`
- `JWInteger`
- `JWInteger`
- `LayerMask: ObjectDetectorFL2`
- `Note`
- `LayerMask: LoadFlorence2Model`
- `Note`
- `Note`
- `Note`
- `PDIMAGE_LongerSize`
- `ImageConcanate`
- `CLIPLoader`
- `ImageMirror`
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `JWInteger`
- `ImpactSwitch`
- `InspyrenetRembg`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ImageFromBatch+`
- `VHS_LoadVideo`
- `JWInteger`
- `KSamplerAdvanced` ★核心
- `PDIMAGE_LongerSize`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetImageSize`
- `WanVaceToVideo`
- `PreviewImage`
- `RebatchImages`
- `GrowMaskWithBlur`
- `PreviewImage`
- `LoadImage`
- `CR Prompt Text`
- `easy promptConcat`
- `ShowText`
- `ShowText`
- `RH_Captioner`
- `LayerUtility: ImageRemoveAlpha`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **85%**（53/62）

**有卡**：`CLIPTextEncode`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`KSamplerAdvanced`、`InvertMask`、`LayerMask: SAM2VideoUltra`、`LayerUtility: ImageScaleByAspectRatio V2`、`MaskToImage`、`VAELoader`、`ImageFromBatch+`、`RebatchImages`、`ImageCompositeMasked`、`JWInteger`、`ImageConcanate`、`LayerMask: ObjectDetectorFL2`、`LayerMask: LoadFlorence2Model`、`PDIMAGE_LongerSize`、`CLIPLoader`、`ImageMirror`、`CR Prompt Text`、`UnetLoaderGGUF`、`InspyrenetRembg`、`TrimVideoLatent`、`VAEDecode`、`VHS_LoadVideo`、`VHS_VideoCombine`、`GetImageSize`、`WanVaceToVideo`、`GrowMaskWithBlur`、`LoadImage`、`easy promptConcat`、`ShowText`、`RH_Captioner`、`LayerUtility: ImageRemoveAlpha`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、TrimVideoLatent
