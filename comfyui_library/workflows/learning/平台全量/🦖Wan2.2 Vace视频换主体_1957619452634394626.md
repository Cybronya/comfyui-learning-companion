---
key: 平台全量/🦖Wan2.2 Vace视频换主体_1957619452634394626.json
name: 🦖Wan2.2 Vace视频换主体_1957619452634394626
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/🦖Wan2.2 Vace视频换主体_1957619452634394626.json
hash: 8aaa6a8f4efb55d8
coverage: 0.857143
learned_at: 2026-11-14 02:55:48
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, ModelSamplingSD3, PrimitiveNode, UnetLoaderGGUF, LoraLoaderModelOnly, Note, CR Prompt Text, Note, Note, JWInteger, JWInteger, Note, JWInteger, VHS_LoadVideo, LoadImage, CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2, ImageFromBatch+, UnetLoaderGGUF, LayerMask: LoadFlorence2Model, ImageMirror, MarkdownNote, RebatchImages, RebatchImages, PreviewImage, MaskToImage, InvertMask, ImageCompositeMasked, VAELoader, CLIPLoader, CLIPTextEncode, WanVaceToVideo, PreviewImage, RH_Captioner, ShowText, easy promptConcat, ShowText, KSamplerAdvanced, KSamplerAdvanced, TrimVideoLatent, VAEDecode, ModelSamplingSD3, VHS_VideoInfo, LayerMask: ObjectDetectorFL2, LayerMask: SAM2VideoUltra, LayerMask: SAM2VideoUltra, GrowMaskWithBlur, JWInteger, ImpactSwitch, JWInteger, GetImageSize, InspyrenetRembg, LayerUtility: ImageRemoveAlpha, CLIPTextEncode, ImageConcanate, ImageFromBatch+, PDIMAGE_LongerSize, ImageConcanate, PDIMAGE_LongerSize, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "randomize"}
---

# 平台全量/🦖Wan2.2 Vace视频换主体_1957619452634394626.json

> 来源文件 `comfyui_library/workflows/平台全量/🦖Wan2.2 Vace视频换主体_1957619452634394626.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `PrimitiveNode`
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `CR Prompt Text`
- `Note`
- `Note`
- `JWInteger`
- `JWInteger`
- `Note`
- `JWInteger`
- `VHS_LoadVideo`
- `LoadImage`
- `CR Prompt Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageFromBatch+`
- `UnetLoaderGGUF` ★核心
- `LayerMask: LoadFlorence2Model`
- `ImageMirror`
- `MarkdownNote`
- `RebatchImages`
- `RebatchImages`
- `PreviewImage`
- `MaskToImage`
- `InvertMask`
- `ImageCompositeMasked`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `PreviewImage`
- `RH_Captioner`
- `ShowText`
- `easy promptConcat`
- `ShowText`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `VHS_VideoInfo`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: SAM2VideoUltra`
- `LayerMask: SAM2VideoUltra`
- `GrowMaskWithBlur`
- `JWInteger`
- `ImpactSwitch`
- `JWInteger`
- `GetImageSize`
- `InspyrenetRembg`
- `LayerUtility: ImageRemoveAlpha`
- `CLIPTextEncode` ★核心
- `ImageConcanate`
- `ImageFromBatch+`
- `PDIMAGE_LongerSize`
- `ImageConcanate`
- `PDIMAGE_LongerSize`
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

覆盖率 **86%**（54/63）

**有卡**：`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`UnetLoaderGGUF`、`CR Prompt Text`、`JWInteger`、`VHS_LoadVideo`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageFromBatch+`、`LayerMask: LoadFlorence2Model`、`ImageMirror`、`RebatchImages`、`MaskToImage`、`InvertMask`、`ImageCompositeMasked`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`WanVaceToVideo`、`RH_Captioner`、`ShowText`、`easy promptConcat`、`KSamplerAdvanced`、`TrimVideoLatent`、`VAEDecode`、`VHS_VideoInfo`、`LayerMask: ObjectDetectorFL2`、`LayerMask: SAM2VideoUltra`、`GrowMaskWithBlur`、`GetImageSize`、`InspyrenetRembg`、`LayerUtility: ImageRemoveAlpha`、`ImageConcanate`、`PDIMAGE_LongerSize`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、KSamplerAdvanced、TrimVideoLatent
