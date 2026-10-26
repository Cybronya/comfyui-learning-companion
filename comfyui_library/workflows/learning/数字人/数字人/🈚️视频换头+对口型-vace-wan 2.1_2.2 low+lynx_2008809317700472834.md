---
key: 数字人/数字人/🈚️视频换头+对口型-vace-wan 2.1_2.2 low+lynx_2008809317700472834.json
name: 🈚️视频换头+对口型-vace-wan 2.1_2.2 low+lynx_2008809317700472834
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/🈚️视频换头+对口型-vace-wan 2.1_2.2 low+lynx_2008809317700472834.json
hash: 4b8e97ff24084469
coverage: 0.51875
learned_at: 2026-10-26 02:06:16
nodes: [GetNode, SetNode, GetNode, GetImageSizeAndCount, GetNode, SetNode, FaceProcessorLoader, GetNode, GetNode, GetNode, ApplyFaceProcessor, WanVideoEncode, WanVideoDecode, SetNode, SetNode, GetNode, ImageResizeKJ, GetNode, GetNode, GetNode, GetNode, WanVideoContextOptions, LayerUtility: PurgeVRAM V2, GetNode, GetNode, GetNode, LayerUtility: ImageBlend, SetNode, InpaintPreprocessor, LayerUtility: PurgeVRAM V2, SetNode, SetNode, LayerMask: ObjectDetectorYOLO8, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerMask: DrawBBoxMaskV2, LayerUtility: PurgeVRAM V2, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, PrimitiveNode, PrimitiveNode, LayerMask: DrawBBoxMaskV2, LayerMask: ObjectDetectorYOLO8, LayerMask: ObjectDetectorYOLO8, LayerMask: DrawBBoxMaskV2, Masks Combine Regions, Reroute, ImageFromBatch+, Reroute, LayerMask: MaskGrow, ResizeMask, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, GetNode, WanVideoBlockSwap, GetNode, GetNode, GetNode, DWPreprocessor, ImageResizeKJ, OnnxDetectionModelLoader, GetNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, GetNode, InpaintCropImproved, PreviewAny, GetNode, MultiTalkSilentEmbeds, DownloadAndLoadWav2VecModel, SetNode, AudioSeparation, SimpleMath+, LayerMask: PersonMaskUltra V2, Note, GetNode, PreviewImage, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, WanVideoTextEncode, GetNode, Text, GetNode, Int, Int, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, Audio Cut (mtb), ImageFromBatch+, VHS_VideoCombine, SimpleMath+, GetNode, GetNode, ImageConcatMulti, GetNode, GetNode, SaveAudio, GetNode, SetNode, PreviewImage, PreviewImage, LynxEncodeFaceIP, LynxInsightFaceCrop, WanVideoExtraModelSelect, LoadLynxResampler, GetNode, WanVideoTextEncodeCached, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoModelLoader, SetNode, VHS_VideoCombine, PoseDetectionOneToAllAnimation, WanVideoExtraModelSelect, GetNode, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoAddStandInLatent, GetNode, MultiTalkModelLoader, easy seed, ImpactSwitch, VHS_LoadVideo, WanVideoVACEEncode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, ImpactSwitch, GetNode, MultiTalkModelLoader, PrimitiveNode, WanVideoSampler, WanVideoSampler, PreviewImage, WanVideoAddLynxEmbeds, SetNode, WanVideoLoraSelect, MultiTalkWav2VecEmbeds, VHS_VideoCombine, LoadImage, VHS_LoadAudioUpload]
patterns: []
missing: []
---

# 数字人/数字人/🈚️视频换头+对口型-vace-wan 2.1_2.2 low+lynx_2008809317700472834.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/🈚️视频换头+对口型-vace-wan 2.1_2.2 low+lynx_2008809317700472834.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（160 个）：
- `GetNode`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `SetNode`
- `FaceProcessorLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `ApplyFaceProcessor`
- `WanVideoEncode`
- `WanVideoDecode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageResizeKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoContextOptions`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageBlend`
- `SetNode`
- `InpaintPreprocessor`
- `LayerUtility: PurgeVRAM V2`
- `SetNode`
- `SetNode`
- `LayerMask: ObjectDetectorYOLO8`
- `LayerMask: MaskGrow`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: DrawBBoxMaskV2`
- `LayerUtility: PurgeVRAM V2`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: SegmentAnythingUltra V3`
- `PrimitiveNode`
- `PrimitiveNode`
- `LayerMask: DrawBBoxMaskV2`
- `LayerMask: ObjectDetectorYOLO8`
- `LayerMask: ObjectDetectorYOLO8`
- `LayerMask: DrawBBoxMaskV2`
- `Masks Combine Regions`
- `Reroute`
- `ImageFromBatch+`
- `Reroute`
- `LayerMask: MaskGrow`
- `ResizeMask`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `GetNode`
- `WanVideoBlockSwap`
- `GetNode`
- `GetNode`
- `GetNode`
- `DWPreprocessor`
- `ImageResizeKJ`
- `OnnxDetectionModelLoader`
- `GetNode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `InpaintCropImproved`
- `PreviewAny`
- `GetNode`
- `MultiTalkSilentEmbeds`
- `DownloadAndLoadWav2VecModel`
- `SetNode`
- `AudioSeparation`
- `SimpleMath+`
- `LayerMask: PersonMaskUltra V2`
- `Note`
- `GetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoTextEncode`
- `GetNode`
- `Text`
- `GetNode`
- `Int`
- `Int`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Audio Cut (mtb)`
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `SaveAudio`
- `GetNode`
- `SetNode`
- `PreviewImage`
- `PreviewImage`
- `LynxEncodeFaceIP`
- `LynxInsightFaceCrop`
- `WanVideoExtraModelSelect`
- `LoadLynxResampler` ★核心
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoModelLoader`
- `SetNode`
- `VHS_VideoCombine`
- `PoseDetectionOneToAllAnimation`
- `WanVideoExtraModelSelect`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoVACEModelSelect`
- `WanVideoAddStandInLatent`
- `GetNode`
- `MultiTalkModelLoader`
- `easy seed`
- `ImpactSwitch`
- `VHS_LoadVideo`
- `WanVideoVACEEncode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `ImpactSwitch`
- `GetNode`
- `MultiTalkModelLoader`
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `PreviewImage`
- `WanVideoAddLynxEmbeds`
- `SetNode`
- `WanVideoLoraSelect`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_LoadAudioUpload`

## 知识

覆盖率 **52%**（83/160）

**有卡**：`GetImageSizeAndCount`、`FaceProcessorLoader`、`ApplyFaceProcessor`、`WanVideoEncode`、`WanVideoDecode`、`ImageResizeKJ`、`WanVideoContextOptions`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: ImageBlend`、`InpaintPreprocessor`、`LayerMask: ObjectDetectorYOLO8`、`LayerMask: MaskGrow`、`LayerMask: PersonMaskUltra V2`、`LayerMask: DrawBBoxMaskV2`、`LayerMask: LoadSegmentAnythingModels`、`LayerMask: SegmentAnythingUltra V3`、`Masks Combine Regions`、`ImageFromBatch+`、`ResizeMask`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`DWPreprocessor`、`OnnxDetectionModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`InpaintCropImproved`、`MultiTalkSilentEmbeds`、`DownloadAndLoadWav2VecModel`、`AudioSeparation`、`SimpleMath+`、`WanVideoTextEncode`、`Text`、`Int`、`Audio Cut (mtb)`、`VHS_VideoCombine`、`ImageConcatMulti`、`SaveAudio`、`LynxEncodeFaceIP`、`LynxInsightFaceCrop`、`WanVideoExtraModelSelect`、`LoadLynxResampler`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`PoseDetectionOneToAllAnimation`、`WanVideoVACEModelSelect`、`WanVideoAddStandInLatent`、`MultiTalkModelLoader`、`easy seed`、`VHS_LoadVideo`、`WanVideoVACEEncode`、`WanVideoSampler`、`WanVideoAddLynxEmbeds`、`MultiTalkWav2VecEmbeds`、`LoadImage`、`VHS_LoadAudioUpload`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
