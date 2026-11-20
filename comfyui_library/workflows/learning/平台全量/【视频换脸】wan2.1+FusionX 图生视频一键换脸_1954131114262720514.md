---
key: 平台全量/【视频换脸】wan2.1+FusionX 图生视频一键换脸_1954131114262720514.json
name: 【视频换脸】wan2.1+FusionX 图生视频一键换脸_1954131114262720514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【视频换脸】wan2.1+FusionX 图生视频一键换脸_1954131114262720514.json
hash: e1fa8da56ce95235
coverage: 0.813953
learned_at: 2026-11-14 01:25:10
nodes: [Note, LayerUtility: ImageScaleByAspectRatio V2, WanVideoDecode, WanVideoBlockSwap, WanVideoTextEncode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoTeaCache, ImageResizeKJ, PreviewImage, ImageFromBatch+, RH_Captioner, Text Concatenate, LayerUtility: PurgeVRAM V2, JWInteger, Note, Note, Note, Note, JWInteger, JWInteger, easy showAnything, GrowMaskWithBlur, VHS_VideoCombine, ImageResizeKJ, WanVideoModelLoader, ImageConcatMulti, ImageConcatMulti, PDIMAGE_LongerSize, PDIMAGE_LongerSize, PDIMAGE_LongerSize, PDIMAGE_LongerSize, VHS_VideoCombine, InpaintPreprocessor, LoadImage, ACE_ImageFaceCrop, APersonMaskGenerator, PreviewImage, WanVideoSampler, VHS_VideoCombine, WanVideoVACEEncode, VHS_LoadVideo, CR Prompt Text]
patterns: []
missing: []
---

# 平台全量/【视频换脸】wan2.1+FusionX 图生视频一键换脸_1954131114262720514.json

> 来源文件 `comfyui_library/workflows/平台全量/【视频换脸】wan2.1+FusionX 图生视频一键换脸_1954131114262720514.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（43 个）：
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTeaCache`
- `ImageResizeKJ`
- `PreviewImage`
- `ImageFromBatch+`
- `RH_Captioner`
- `Text Concatenate`
- `LayerUtility: PurgeVRAM V2`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `Note`
- `JWInteger`
- `JWInteger`
- `easy showAnything`
- `GrowMaskWithBlur`
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `WanVideoModelLoader`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `PDIMAGE_LongerSize`
- `PDIMAGE_LongerSize`
- `PDIMAGE_LongerSize`
- `PDIMAGE_LongerSize`
- `VHS_VideoCombine`
- `InpaintPreprocessor`
- `LoadImage`
- `ACE_ImageFaceCrop`
- `APersonMaskGenerator`
- `PreviewImage`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoVACEEncode`
- `VHS_LoadVideo`
- `CR Prompt Text`

## 知识

覆盖率 **81%**（35/43）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoDecode`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTeaCache`、`ImageResizeKJ`、`ImageFromBatch+`、`RH_Captioner`、`Text Concatenate`、`LayerUtility: PurgeVRAM V2`、`JWInteger`、`GrowMaskWithBlur`、`VHS_VideoCombine`、`WanVideoModelLoader`、`ImageConcatMulti`、`PDIMAGE_LongerSize`、`InpaintPreprocessor`、`LoadImage`、`ACE_ImageFaceCrop`、`APersonMaskGenerator`、`WanVideoSampler`、`WanVideoVACEEncode`、`VHS_LoadVideo`、`CR Prompt Text`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader
