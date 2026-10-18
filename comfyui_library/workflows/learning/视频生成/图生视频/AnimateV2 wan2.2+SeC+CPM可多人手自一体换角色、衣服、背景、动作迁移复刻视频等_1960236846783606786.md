---
key: 视频生成/图生视频/AnimateV2 wan2.2+SeC+CPM可多人手自一体换角色、衣服、背景、动作迁移复刻视频等_1960236846783606786.json
name: AnimateV2 wan2.2+SeC+CPM可多人手自一体换角色、衣服、背景、动作迁移复刻视频等_1960236846783606786.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AnimateV2 wan2.2+SeC+CPM可多人手自一体换角色、衣服、背景、动作迁移复刻视频等_1960236846783606786.json
hash: a7bbb9c8b9bc6aaf
coverage: 0.888889
learned_at: 2026-10-15 22:31:26
nodes: [WanVideoTorchCompileSettings, WanVideoDecode, VHS_VideoCombine, CLIPVisionLoader, Int, easy int, easy int, DownloadAndLoadWav2VecModel, AudioSeparation, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, LayerUtility: PurgeVRAM V2, GetImageSizeAndCount, ImageConcatMulti, KEEP_ModelLoader, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoVAELoader, RHHiddenNodes, GetImageRangeFromBatch, WanVideoClipVisionEncode, RHHiddenNodes, WanVideoTextEncode, WanVideoAnimateEmbeds, KEEP_ProcessImageSequence, KEEP_ModelLoader, ImageResizeKJv2, FaceProcessorLoader, KEEP_ProcessImageSequence, KEEP_ModelLoader, KEEP_ProcessImageSequence, WanVideoSampler, Any Switch (rgthree), VHS_LoadVideo, PoseAndFaceDetection, OnnxDetectionModelLoader, DrawMaskOnImage, BlockifyMask, easy clearCacheAll, easy cleanGpuUsed, ResizeMask, APersonMaskGenerator, APersonMaskGenerator, GrowMask, WanVideoModelLoader, FaceProcessorLoader, VHS_VideoCombine, APersonMaskGenerator, ApplyFaceProcessor, SeCModelLoader, ApplyFaceProcessor, Any Switch (rgthree), LayerMask: LoadSegformerModel, RHHiddenNodes, VHS_VideoInfo, PrimitiveInt, LayerMask: SegformerUltraV3, ImageFromBatch, ImageResizeKJ, SeCVideoSegmentation, PointsEditor, Any Switch (rgthree), DrawViTPose, LayerMask: SegformerClothesSetting, Fast Groups Muter (rgthree), Note, Fast Groups Muter (rgthree), VHS_LoadVideo, LoadImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/AnimateV2 wan2.2+SeC+CPM可多人手自一体换角色、衣服、背景、动作迁移复刻视频等_1960236846783606786.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1960236846783606786.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（72 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `Int`
- `easy int`
- `easy int`
- `DownloadAndLoadWav2VecModel`
- `AudioSeparation`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `LayerUtility: PurgeVRAM V2`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `KEEP_ModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `RHHiddenNodes`
- `GetImageRangeFromBatch`
- `WanVideoClipVisionEncode`
- `RHHiddenNodes`
- `WanVideoTextEncode`
- `WanVideoAnimateEmbeds`
- `KEEP_ProcessImageSequence`
- `KEEP_ModelLoader`
- `ImageResizeKJv2`
- `FaceProcessorLoader`
- `KEEP_ProcessImageSequence`
- `KEEP_ModelLoader`
- `KEEP_ProcessImageSequence`
- `WanVideoSampler` ★核心
- `Any Switch (rgthree)`
- `VHS_LoadVideo`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `DrawMaskOnImage`
- `BlockifyMask`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `ResizeMask`
- `APersonMaskGenerator`
- `APersonMaskGenerator`
- `GrowMask`
- `WanVideoModelLoader`
- `FaceProcessorLoader`
- `VHS_VideoCombine`
- `APersonMaskGenerator`
- `ApplyFaceProcessor`
- `SeCModelLoader`
- `ApplyFaceProcessor`
- `Any Switch (rgthree)`
- `LayerMask: LoadSegformerModel`
- `RHHiddenNodes`
- `VHS_VideoInfo`
- `PrimitiveInt`
- `LayerMask: SegformerUltraV3`
- `ImageFromBatch`
- `ImageResizeKJ`
- `SeCVideoSegmentation`
- `PointsEditor`
- `Any Switch (rgthree)`
- `DrawViTPose`
- `LayerMask: SegformerClothesSetting`
- `Fast Groups Muter (rgthree)`
- `Note`
- `Fast Groups Muter (rgthree)`
- `VHS_LoadVideo`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **89%**（64/72）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoDecode`、`VHS_VideoCombine`、`CLIPVisionLoader`、`Int`、`easy int`、`DownloadAndLoadWav2VecModel`、`AudioSeparation`、`MultiTalkModelLoader`、`MultiTalkWav2VecEmbeds`、`LayerUtility: PurgeVRAM V2`、`GetImageSizeAndCount`、`ImageConcatMulti`、`KEEP_ModelLoader`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`RHHiddenNodes`、`GetImageRangeFromBatch`、`WanVideoClipVisionEncode`、`WanVideoTextEncode`、`WanVideoAnimateEmbeds`、`KEEP_ProcessImageSequence`、`ImageResizeKJv2`、`FaceProcessorLoader`、`WanVideoSampler`、`VHS_LoadVideo`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`DrawMaskOnImage`、`BlockifyMask`、`easy clearCacheAll`、`easy cleanGpuUsed`、`ResizeMask`、`APersonMaskGenerator`、`GrowMask`、`WanVideoModelLoader`、`ApplyFaceProcessor`、`SeCModelLoader`、`LayerMask: LoadSegformerModel`、`VHS_VideoInfo`、`LayerMask: SegformerUltraV3`、`ImageFromBatch`、`ImageResizeKJ`、`SeCVideoSegmentation`、`PointsEditor`、`DrawViTPose`、`LayerMask: SegformerClothesSetting`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoSetLoRAs
