---
key: 平台全量/🈚️视频换头_换脸_面部重绘-wan2.2 vace 2.2 fun+stand in_1966970471642226689.json
name: 🈚️视频换头_换脸_面部重绘-wan2.2 vace 2.2 fun+stand in_1966970471642226689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/🈚️视频换头_换脸_面部重绘-wan2.2 vace 2.2 fun+stand in_1966970471642226689.json
hash: 651bbf9192383c9e
coverage: 0.508772
learned_at: 2026-11-14 02:54:33
nodes: [GetNode, LoadWanVideoT5TextEncoder, GetNode, SetNode, SetNode, GetNode, GetImageSizeAndCount, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, SetNode, LayerUtility: PurgeVRAM V2, LayerMask: LoadSegmentAnythingModels, LoadFlorence2Model, LayerMask: MaskPreview, LayerMask: ObjectDetectorFL2, LayerUtility: PurgeVRAM V2, GetNode, LayerMask: DrawBBoxMaskV2, LayerMask: MaskPreview, LayerMask: SegmentAnythingUltra V3, LayerMask: ObjectDetectorYOLO8, LayerMask: MaskGrow, LayerMask: DrawBBoxMaskV2, LoadImage, SetNode, SetNode, SetNode, WanVideoTextEncode, WanVideoModelLoader, GetNode, GetNode, ResizeMask, SetNode, LayerUtility: ImageBlend, ImageResizeKJ, SetNode, LayerUtility: PurgeVRAM V2, InpaintPreprocessor, SetNode, SetNode, GetNode, GetNode, WanVideoDecode, SetNode, GetNode, SetNode, GetNode, WanVideoSampler, CreateCFGScheduleFloatList, VHS_LoadVideo, GetNode, GetImageSizeAndCount, GetNode, GetNode, GetNode, GetNode, WanVideoVACEEncode, GetNode, VHS_VideoCombine, SetNode, LayerMask: PersonMaskUltra V2, GetNode, LayerUtility: PurgeVRAM V2, PreviewImage, PrimitiveNode, PrimitiveNode, LayerMask: DrawBBoxMaskV2, LayerMask: ObjectDetectorYOLO8, LayerMask: ObjectDetectorYOLO8, LayerMask: DrawBBoxMaskV2, Masks Combine Regions, ImageFromBatch+, Reroute, FaceProcessorLoader, GetNode, ApplyFaceProcessor, PreviewImage, WanVideoEncode, GetNode, WanVideoVACEEncode, WanVideoAddStandInLatent, InpaintCropImproved, WanVideoModelLoader, PreviewImage, WanVideoSampler, WanVideoContextOptions, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoVAELoader, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, SetNode, GetNode, GetNode, ImpactSwitch, ImpactSwitch, GetNode, GetNode, ImageResizeKJ, DWPreprocessor, WanVideoLoraSelect, WanVideoLoraSelect, ImpactSwitch, GetNode, PreviewImage, OnnxDetectionModelLoader, GetNode, GetNode, PoseDetectionOneToAllAnimation]
patterns: []
missing: []
---

# 平台全量/🈚️视频换头_换脸_面部重绘-wan2.2 vace 2.2 fun+stand in_1966970471642226689.json

> 来源文件 `comfyui_library/workflows/平台全量/🈚️视频换头_换脸_面部重绘-wan2.2 vace 2.2 fun+stand in_1966970471642226689.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（114 个）：
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `LayerMask: LoadSegmentAnythingModels`
- `LoadFlorence2Model`
- `LayerMask: MaskPreview`
- `LayerMask: ObjectDetectorFL2`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `LayerMask: DrawBBoxMaskV2`
- `LayerMask: MaskPreview`
- `LayerMask: SegmentAnythingUltra V3`
- `LayerMask: ObjectDetectorYOLO8`
- `LayerMask: MaskGrow`
- `LayerMask: DrawBBoxMaskV2`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `GetNode`
- `GetNode`
- `ResizeMask`
- `SetNode`
- `LayerUtility: ImageBlend`
- `ImageResizeKJ`
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `InpaintPreprocessor`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `VHS_LoadVideo`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoVACEEncode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `LayerMask: PersonMaskUltra V2`
- `GetNode`
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `PrimitiveNode`
- `PrimitiveNode`
- `LayerMask: DrawBBoxMaskV2`
- `LayerMask: ObjectDetectorYOLO8`
- `LayerMask: ObjectDetectorYOLO8`
- `LayerMask: DrawBBoxMaskV2`
- `Masks Combine Regions`
- `ImageFromBatch+`
- `Reroute`
- `FaceProcessorLoader`
- `GetNode`
- `ApplyFaceProcessor`
- `PreviewImage`
- `WanVideoEncode`
- `GetNode`
- `WanVideoVACEEncode`
- `WanVideoAddStandInLatent`
- `InpaintCropImproved`
- `WanVideoModelLoader`
- `PreviewImage`
- `WanVideoSampler` ★核心
- `WanVideoContextOptions`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImpactSwitch`
- `ImpactSwitch`
- `GetNode`
- `GetNode`
- `ImageResizeKJ`
- `DWPreprocessor`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `ImpactSwitch`
- `GetNode`
- `PreviewImage`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `PoseDetectionOneToAllAnimation`

## 知识

覆盖率 **51%**（58/114）

**有卡**：`LoadWanVideoT5TextEncoder`、`GetImageSizeAndCount`、`LayerUtility: PurgeVRAM V2`、`LayerMask: LoadSegmentAnythingModels`、`LoadFlorence2Model`、`LayerMask: MaskPreview`、`LayerMask: ObjectDetectorFL2`、`LayerMask: DrawBBoxMaskV2`、`LayerMask: SegmentAnythingUltra V3`、`LayerMask: ObjectDetectorYOLO8`、`LayerMask: MaskGrow`、`LoadImage`、`WanVideoTextEncode`、`WanVideoModelLoader`、`ResizeMask`、`LayerUtility: ImageBlend`、`ImageResizeKJ`、`InpaintPreprocessor`、`WanVideoDecode`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`VHS_LoadVideo`、`WanVideoVACEEncode`、`VHS_VideoCombine`、`LayerMask: PersonMaskUltra V2`、`Masks Combine Regions`、`ImageFromBatch+`、`FaceProcessorLoader`、`ApplyFaceProcessor`、`WanVideoEncode`、`WanVideoAddStandInLatent`、`InpaintCropImproved`、`WanVideoContextOptions`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`DWPreprocessor`、`OnnxDetectionModelLoader`、`PoseDetectionOneToAllAnimation`

**用到的条目**：LoadImage、CreateCFGScheduleFloatList、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoAddStandInLatent、WanVideoDecode、WanVideoEncode、WanVideoTextEncode
