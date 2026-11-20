---
key: 平台全量/AnimateV2+wan2.2单人OR多人极速角色背景替换、动作迁移极速生成复刻视频_1976130068323938305.json
name: AnimateV2+wan2.2单人OR多人极速角色背景替换、动作迁移极速生成复刻视频_1976130068323938305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/AnimateV2+wan2.2单人OR多人极速角色背景替换、动作迁移极速生成复刻视频_1976130068323938305.json
hash: b5328eda176f2b62
coverage: 0.904762
learned_at: 2026-11-14 00:18:22
nodes: [WanVideoTorchCompileSettings, WanVideoDecode, VHS_VideoCombine, CLIPVisionLoader, Int, easy int, easy int, DownloadAndLoadWav2VecModel, AudioSeparation, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, LayerUtility: PurgeVRAM V2, GetImageSizeAndCount, ImageConcatMulti, KEEP_ModelLoader, VHS_VideoCombine, GrowMask, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoVAELoader, RHHiddenNodes, ResizeMask, GetImageRangeFromBatch, WanVideoClipVisionEncode, easy cleanGpuUsed, easy clearCacheAll, BlockifyMask, VHS_LoadVideo, RHHiddenNodes, WanVideoTextEncode, WanVideoAnimateEmbeds, PoseAndFaceDetection, APersonMaskGenerator, KEEP_ProcessImageSequence, KEEP_ModelLoader, ImageResizeKJ, ImageResizeKJv2, LoadImage, RHHiddenNodes, Any Switch (rgthree), APersonMaskGenerator, ApplyFaceProcessor, FaceProcessorLoader, ApplyFaceProcessor, FaceProcessorLoader, KEEP_ProcessImageSequence, KEEP_ModelLoader, KEEP_ProcessImageSequence, APersonMaskGenerator, DrawViTPose, WanVideoSampler, Any Switch (rgthree), DrawMaskOnImage, Any Switch (rgthree), VHS_VideoInfo, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Note, WanVideoModelLoader, OnnxDetectionModelLoader, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/AnimateV2+wan2.2单人OR多人极速角色背景替换、动作迁移极速生成复刻视频_1976130068323938305.json

> 来源文件 `comfyui_library/workflows/平台全量/AnimateV2+wan2.2单人OR多人极速角色背景替换、动作迁移极速生成复刻视频_1976130068323938305.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（63 个）：
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
- `VHS_VideoCombine`
- `GrowMask`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `RHHiddenNodes`
- `ResizeMask`
- `GetImageRangeFromBatch`
- `WanVideoClipVisionEncode`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `BlockifyMask`
- `VHS_LoadVideo`
- `RHHiddenNodes`
- `WanVideoTextEncode`
- `WanVideoAnimateEmbeds`
- `PoseAndFaceDetection`
- `APersonMaskGenerator`
- `KEEP_ProcessImageSequence`
- `KEEP_ModelLoader`
- `ImageResizeKJ`
- `ImageResizeKJv2`
- `LoadImage`
- `RHHiddenNodes`
- `Any Switch (rgthree)`
- `APersonMaskGenerator`
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
- `KEEP_ProcessImageSequence`
- `KEEP_ModelLoader`
- `KEEP_ProcessImageSequence`
- `APersonMaskGenerator`
- `DrawViTPose`
- `WanVideoSampler` ★核心
- `Any Switch (rgthree)`
- `DrawMaskOnImage`
- `Any Switch (rgthree)`
- `VHS_VideoInfo`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `Note`
- `WanVideoModelLoader`
- `OnnxDetectionModelLoader`
- `VHS_LoadVideo`

## 知识

覆盖率 **90%**（57/63）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoDecode`、`VHS_VideoCombine`、`CLIPVisionLoader`、`Int`、`easy int`、`DownloadAndLoadWav2VecModel`、`AudioSeparation`、`MultiTalkModelLoader`、`MultiTalkWav2VecEmbeds`、`LayerUtility: PurgeVRAM V2`、`GetImageSizeAndCount`、`ImageConcatMulti`、`KEEP_ModelLoader`、`GrowMask`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`RHHiddenNodes`、`ResizeMask`、`GetImageRangeFromBatch`、`WanVideoClipVisionEncode`、`easy cleanGpuUsed`、`easy clearCacheAll`、`BlockifyMask`、`VHS_LoadVideo`、`WanVideoTextEncode`、`WanVideoAnimateEmbeds`、`PoseAndFaceDetection`、`APersonMaskGenerator`、`KEEP_ProcessImageSequence`、`ImageResizeKJ`、`ImageResizeKJv2`、`LoadImage`、`ApplyFaceProcessor`、`FaceProcessorLoader`、`DrawViTPose`、`WanVideoSampler`、`DrawMaskOnImage`、`VHS_VideoInfo`、`WanVideoModelLoader`、`OnnxDetectionModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoSetLoRAs
