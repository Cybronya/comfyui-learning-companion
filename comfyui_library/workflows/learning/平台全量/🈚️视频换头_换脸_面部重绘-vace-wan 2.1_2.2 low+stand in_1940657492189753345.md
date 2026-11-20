---
key: 平台全量/🈚️视频换头_换脸_面部重绘-vace-wan 2.1_2.2 low+stand in_1940657492189753345.json
name: 🈚️视频换头_换脸_面部重绘-vace-wan 2.1_2.2 low+stand in_1940657492189753345
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/🈚️视频换头_换脸_面部重绘-vace-wan 2.1_2.2 low+stand in_1940657492189753345.json
hash: e02380b54c4b0daf
coverage: 0.523364
learned_at: 2026-11-14 02:54:33
nodes: [GetNode, SetNode, SetNode, GetNode, GetImageSizeAndCount, GetNode, SetNode, SetNode, GetNode, SetNode, FaceProcessorLoader, GetNode, GetNode, GetNode, ApplyFaceProcessor, PreviewImage, WanVideoEncode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, GetNode, GetNode, GetImageSizeAndCount, GetNode, GetNode, GetNode, WanVideoDecode, WanVideoAddStandInLatent, SetNode, WanVideoTextEncode, SetNode, GetNode, WanVideoVACEEncode, ImageResizeKJ, SetNode, GetNode, GetNode, GetNode, GetNode, WanVideoVACEEncode, WanVideoSampler, PrimitiveNode, SetNode, VHS_LoadVideo, WanVideoSampler, WanVideoContextOptions, SetNode, LayerMask: PersonMaskUltra V2, GetNode, LayerUtility: PurgeVRAM V2, InpaintCropImproved, GetNode, GetNode, GetNode, LayerUtility: ImageBlend, SetNode, InpaintPreprocessor, LayerUtility: PurgeVRAM V2, SetNode, SetNode, LayerMask: ObjectDetectorYOLO8, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerMask: DrawBBoxMaskV2, LayerUtility: PurgeVRAM V2, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, PrimitiveNode, PrimitiveNode, LayerMask: DrawBBoxMaskV2, LayerMask: ObjectDetectorYOLO8, LayerMask: ObjectDetectorYOLO8, LayerMask: DrawBBoxMaskV2, Masks Combine Regions, Reroute, ImageFromBatch+, Reroute, ImageConcatMulti, LayerMask: MaskGrow, PreviewImage, ResizeMask, PreviewImage, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, SetNode, WanVideoModelLoader, WanVideoModelLoader, GetNode, GetNode, GetNode, ImpactSwitch, WanVideoBlockSwap, GetNode, GetNode, GetNode, PoseDetectionOneToAllAnimation, DWPreprocessor, ImageResizeKJ, OnnxDetectionModelLoader, VHS_VideoCombine, VHS_VideoCombine, LoadImage, GetNode, WanVideoLoraSelect]
patterns: []
missing: []
---

# 平台全量/🈚️视频换头_换脸_面部重绘-vace-wan 2.1_2.2 low+stand in_1940657492189753345.json

> 来源文件 `comfyui_library/workflows/平台全量/🈚️视频换头_换脸_面部重绘-vace-wan 2.1_2.2 low+stand in_1940657492189753345.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（107 个）：
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `FaceProcessorLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `ApplyFaceProcessor`
- `PreviewImage`
- `WanVideoEncode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `WanVideoAddStandInLatent`
- `SetNode`
- `WanVideoTextEncode`
- `SetNode`
- `GetNode`
- `WanVideoVACEEncode`
- `ImageResizeKJ`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoVACEEncode`
- `WanVideoSampler` ★核心
- `PrimitiveNode`
- `SetNode`
- `VHS_LoadVideo`
- `WanVideoSampler` ★核心
- `WanVideoContextOptions`
- `SetNode`
- `LayerMask: PersonMaskUltra V2`
- `GetNode`
- `LayerUtility: PurgeVRAM V2`
- `InpaintCropImproved`
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
- `ImageConcatMulti`
- `LayerMask: MaskGrow`
- `PreviewImage`
- `ResizeMask`
- `PreviewImage`
- `WanVideoVACEModelSelect`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImpactSwitch`
- `WanVideoBlockSwap`
- `GetNode`
- `GetNode`
- `GetNode`
- `PoseDetectionOneToAllAnimation`
- `DWPreprocessor`
- `ImageResizeKJ`
- `OnnxDetectionModelLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `GetNode`
- `WanVideoLoraSelect`

## 知识

覆盖率 **52%**（56/107）

**有卡**：`GetImageSizeAndCount`、`FaceProcessorLoader`、`ApplyFaceProcessor`、`WanVideoEncode`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`WanVideoAddStandInLatent`、`WanVideoTextEncode`、`WanVideoVACEEncode`、`ImageResizeKJ`、`WanVideoSampler`、`VHS_LoadVideo`、`WanVideoContextOptions`、`LayerMask: PersonMaskUltra V2`、`LayerUtility: PurgeVRAM V2`、`InpaintCropImproved`、`LayerUtility: ImageBlend`、`InpaintPreprocessor`、`LayerMask: ObjectDetectorYOLO8`、`LayerMask: MaskGrow`、`LayerMask: DrawBBoxMaskV2`、`LayerMask: LoadSegmentAnythingModels`、`LayerMask: SegmentAnythingUltra V3`、`Masks Combine Regions`、`ImageFromBatch+`、`ImageConcatMulti`、`ResizeMask`、`WanVideoVACEModelSelect`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`PoseDetectionOneToAllAnimation`、`DWPreprocessor`、`OnnxDetectionModelLoader`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoAddStandInLatent、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVACEEncode
