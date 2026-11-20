---
key: 平台全量/WanVideo MiniMax Remover视频全自动去水印_1961258734213382145.json
name: WanVideo MiniMax Remover视频全自动去水印_1961258734213382145
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/WanVideo MiniMax Remover视频全自动去水印_1961258734213382145.json
hash: c2751c3ec2358609
coverage: 0.96
learned_at: 2026-11-14 01:07:10
nodes: [WanVideoDecode, ImageToMask, MaskToImage, ImageListToBatch+, GrowMaskWithBlur, VHS_VideoInfo, WanVideoEncode, WanVideoVAELoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoSampler, WanVideoMiniMaxRemoverEmbeds, ImageCompositeMasked, MaskToImage, SolidMask, BboxDetectorCombined_v2, easy imageBatchToImageList, UltralyticsDetectorProvider, VHS_LoadVideo, Fast Groups Bypasser (rgthree), MaskToImage, WanVideoEncode, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/WanVideo MiniMax Remover视频全自动去水印_1961258734213382145.json

> 来源文件 `comfyui_library/workflows/平台全量/WanVideo MiniMax Remover视频全自动去水印_1961258734213382145.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（25 个）：
- `WanVideoDecode`
- `ImageToMask`
- `MaskToImage`
- `ImageListToBatch+`
- `GrowMaskWithBlur`
- `VHS_VideoInfo`
- `WanVideoEncode`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoMiniMaxRemoverEmbeds`
- `ImageCompositeMasked`
- `MaskToImage`
- `SolidMask`
- `BboxDetectorCombined_v2`
- `easy imageBatchToImageList`
- `UltralyticsDetectorProvider`
- `VHS_LoadVideo`
- `Fast Groups Bypasser (rgthree)`
- `MaskToImage`
- `WanVideoEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`WanVideoDecode`、`ImageToMask`、`MaskToImage`、`ImageListToBatch+`、`GrowMaskWithBlur`、`VHS_VideoInfo`、`WanVideoEncode`、`WanVideoVAELoader`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoMiniMaxRemoverEmbeds`、`ImageCompositeMasked`、`SolidMask`、`BboxDetectorCombined_v2`、`easy imageBatchToImageList`、`UltralyticsDetectorProvider`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、BboxDetectorCombined_v2、easy imageBatchToImageList
