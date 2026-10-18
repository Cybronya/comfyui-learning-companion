---
key: 视频生成/图生视频/双人同框fusionx_Phantom一致性视频万相wan2.1+补帧_1927650135201988609.json
name: 双人同框fusionx_Phantom一致性视频万相wan2.1+补帧_1927650135201988609.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/双人同框fusionx_Phantom一致性视频万相wan2.1+补帧_1927650135201988609.json
hash: c3f2b66a79e45b18
coverage: 0.957447
learned_at: 2026-10-15 22:29:55
nodes: [DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, VHS_VideoCombine, WanVideoEnhanceAVideo, WanVideoDecode, LayerUtility: PurgeVRAM V2, LayerMask: ObjectDetectorFL2, GetImageSize, LayerMask: LoadFlorence2Model, LayerMask: SAM2Ultra, ImageCompositeMasked, LayerMask: LoadFlorence2Model, LayerMask: ObjectDetectorFL2, GetImageSize, Image Blank, LayerMask: SAM2Ultra, ImageCompositeMasked, ImageResizeKJ, ImagePadKJ, ImageResizeKJ, ImagePadKJ, PreviewImage, PreviewImage, WanVideoEncode, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, WanVideoEncode, WanVideoExperimentalArgs, Image Blank, Int, Int, Int, VHS_VideoCombine, LoadImage, LoadImage, WanVideoMagCache, WanVideoSLG, WanVideoSampler, WanVideoApplyNAG, WanVideoTextEncodeSingle, WanVideoPhantomEmbeds, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoBlockSwap, WanVideoTextEncodeSingle, CR Text]
patterns: []
missing: []
---

# 视频生成/图生视频/双人同框fusionx_Phantom一致性视频万相wan2.1+补帧_1927650135201988609.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1927650135201988609.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（47 个）：
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `VHS_VideoCombine`
- `WanVideoEnhanceAVideo`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `LayerMask: ObjectDetectorFL2`
- `GetImageSize`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: SAM2Ultra`
- `ImageCompositeMasked`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: ObjectDetectorFL2`
- `GetImageSize`
- `Image Blank`
- `LayerMask: SAM2Ultra`
- `ImageCompositeMasked`
- `ImageResizeKJ`
- `ImagePadKJ`
- `ImageResizeKJ`
- `ImagePadKJ`
- `PreviewImage`
- `PreviewImage`
- `WanVideoEncode`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoEncode`
- `WanVideoExperimentalArgs`
- `Image Blank`
- `Int`
- `Int`
- `Int`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `WanVideoMagCache`
- `WanVideoSLG`
- `WanVideoSampler` ★核心
- `WanVideoApplyNAG`
- `WanVideoTextEncodeSingle`
- `WanVideoPhantomEmbeds`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeSingle`
- `CR Text`

## 知识

覆盖率 **96%**（45/47）

**有卡**：`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`VHS_VideoCombine`、`WanVideoEnhanceAVideo`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`LayerMask: ObjectDetectorFL2`、`GetImageSize`、`LayerMask: LoadFlorence2Model`、`LayerMask: SAM2Ultra`、`ImageCompositeMasked`、`Image Blank`、`ImageResizeKJ`、`ImagePadKJ`、`WanVideoEncode`、`WanVideoExperimentalArgs`、`Int`、`LoadImage`、`WanVideoMagCache`、`WanVideoSLG`、`WanVideoSampler`、`WanVideoApplyNAG`、`WanVideoTextEncodeSingle`、`WanVideoPhantomEmbeds`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`CR Text`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、WanVideoEncode、GetImageSize
