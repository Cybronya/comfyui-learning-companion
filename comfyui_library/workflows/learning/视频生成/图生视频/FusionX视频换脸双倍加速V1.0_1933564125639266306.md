---
key: 视频生成/图生视频/FusionX视频换脸双倍加速V1.0_1933564125639266306.json
name: FusionX视频换脸双倍加速V1.0_1933564125639266306.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/FusionX视频换脸双倍加速V1.0_1933564125639266306.json
hash: f90e40146688c67f
coverage: 0.818182
learned_at: 2026-10-15 22:30:14
nodes: [LoadWanVideoT5TextEncoder, Note Plus (mtb), Note, Note, Note, Note, ImageConcatMulti, PDIMAGE_LongerSize, ImageConcatMulti, PDIMAGE_LongerSize, WanVideoDecode, Note, WanVideoTextEncode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoVAELoader, LayerUtility: PurgeVRAM V2, Text Concatenate, InpaintPreprocessor, APersonMaskGenerator, easy showAnything, LoadImage, WanVideoSampler, WanVideoModelLoader, WanVideoVACEEncode, GrowMaskWithBlur, WanVideoBlockSwap, VHS_LoadVideo, JWInteger, RH_Captioner, ImageResizeKJ, ImageResizeKJ, PreviewImage, ACE_ImageFaceCrop, PreviewImage, PDIMAGE_LongerSize, VHS_VideoCombine, WanVideoTeaCache, JWInteger, JWInteger, CR Prompt Text, VHS_VideoCombine, PDIMAGE_LongerSize, ImageFromBatch+, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/FusionX视频换脸双倍加速V1.0_1933564125639266306.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1933564125639266306.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（44 个）：
- `LoadWanVideoT5TextEncoder`
- `Note Plus (mtb)`
- `Note`
- `Note`
- `Note`
- `Note`
- `ImageConcatMulti`
- `PDIMAGE_LongerSize`
- `ImageConcatMulti`
- `PDIMAGE_LongerSize`
- `WanVideoDecode`
- `Note`
- `WanVideoTextEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoVAELoader`
- `LayerUtility: PurgeVRAM V2`
- `Text Concatenate`
- `InpaintPreprocessor`
- `APersonMaskGenerator`
- `easy showAnything`
- `LoadImage`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoVACEEncode`
- `GrowMaskWithBlur`
- `WanVideoBlockSwap`
- `VHS_LoadVideo`
- `JWInteger`
- `RH_Captioner`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `PreviewImage`
- `ACE_ImageFaceCrop`
- `PreviewImage`
- `PDIMAGE_LongerSize`
- `VHS_VideoCombine`
- `WanVideoTeaCache`
- `JWInteger`
- `JWInteger`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `PDIMAGE_LongerSize`
- `ImageFromBatch+`
- `VHS_VideoCombine`

## 知识

覆盖率 **82%**（36/44）

**有卡**：`LoadWanVideoT5TextEncoder`、`Note Plus (mtb)`、`ImageConcatMulti`、`PDIMAGE_LongerSize`、`WanVideoDecode`、`WanVideoTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVAELoader`、`LayerUtility: PurgeVRAM V2`、`Text Concatenate`、`InpaintPreprocessor`、`APersonMaskGenerator`、`LoadImage`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoVACEEncode`、`GrowMaskWithBlur`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`JWInteger`、`RH_Captioner`、`ImageResizeKJ`、`ACE_ImageFaceCrop`、`VHS_VideoCombine`、`WanVideoTeaCache`、`CR Prompt Text`、`ImageFromBatch+`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode
