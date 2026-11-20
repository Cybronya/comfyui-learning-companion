---
key: 平台全量/🈚️人物置入视频场景_人物迁移_换人物-wan 2.2-vace 2.2 fun+stand in_1967004177702457346.json
name: 🈚️人物置入视频场景_人物迁移_换人物-wan 2.2-vace 2.2 fun+stand in_1967004177702457346
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/🈚️人物置入视频场景_人物迁移_换人物-wan 2.2-vace 2.2 fun+stand in_1967004177702457346.json
hash: a421d053b34e6c53
coverage: 0.507692
learned_at: 2026-11-14 02:54:32
nodes: [SetNode, GetNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, GetNode, SetNode, GetImageSizeAndCount, GetNode, SetNode, WanVideoTextEncode, GetNode, GetNode, SetNode, GetImageSizeAndCount, GetNode, GetNode, ApplyFaceProcessor, GetNode, WanVideoVACEEncode, CreateCFGScheduleFloatList, GetNode, ImageResizeKJ, GetNode, WanVideoSampler, ImageResizeKJ, VHS_VideoCombine, GetNode, MaskToImage, ImageListToBatch+, MaskFromBatch+, ToBinaryMask, GrowMaskWithBlur, ImageListToBatch+, easy imageBatchToImageList, Reroute, SAM3Segmentation, Reroute, SAM3PointCollector, VHS_VideoCombine, GetImageRangeFromBatch, SeCModelLoader_Ultra-Fast, Florence2Run, SeCVideoSegmentation, Reroute, DownloadAndLoadFlorence2Model, GetImageSizeAndCount, Florence2toCoordinates, Reroute, GetNode, GetNode, DrawMaskOnImage, SetNode, SetNode, WanVideoBlockSwap, SetNode, WanVideoLoraSelect, GetNode, GetNode, easy imageConcat, GetNode, SetNode, LoadImage, VHS_LoadVideo, SetNode, SetNode, SetNode, SetNode, SetNode, ImageResizeKJ, GetNode, WanVideoLoraSelect, WanVideoModelLoader, SetNode, WanVideoSampler, WanVideoDecode, GetNode, SetNode, GetNode, LoadSAM3Model, ImageListToBatch+, GetNode, BlockifyMask, SetNode, SetNode, GetNode, GetNode, Manual XY Entry Info, GetNode, GetNode, GetNode, GetNode, GetNode, DWPreprocessor, GetNode, LayerMask: MaskGrow, WanVideoContextOptions, FaceProcessorLoader, GetNode, WanVideoEncode, WanVideoAddStandInLatent, GetNode, PreviewImage, SetNode, WanVideoVACEEncode, SetNode, LayerUtility: PurgeVRAM V2, ImageCompositeMasked, easy imageRemBg, easy cleanGpuUsed, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, PreviewImage, GetNode, GetNode, GetNode, VHS_VideoCombine, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, GetNode, ImpactSwitch, GetNode, ImpactSwitch, ImpactSwitch, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect]
patterns: []
missing: []
---

# 平台全量/🈚️人物置入视频场景_人物迁移_换人物-wan 2.2-vace 2.2 fun+stand in_1967004177702457346.json

> 来源文件 `comfyui_library/workflows/平台全量/🈚️人物置入视频场景_人物迁移_换人物-wan 2.2-vace 2.2 fun+stand in_1967004177702457346.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（130 个）：
- `SetNode`
- `GetNode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `SetNode`
- `WanVideoTextEncode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `ApplyFaceProcessor`
- `GetNode`
- `WanVideoVACEEncode`
- `CreateCFGScheduleFloatList`
- `GetNode`
- `ImageResizeKJ`
- `GetNode`
- `WanVideoSampler` ★核心
- `ImageResizeKJ`
- `VHS_VideoCombine`
- `GetNode`
- `MaskToImage`
- `ImageListToBatch+`
- `MaskFromBatch+`
- `ToBinaryMask`
- `GrowMaskWithBlur`
- `ImageListToBatch+`
- `easy imageBatchToImageList`
- `Reroute`
- `SAM3Segmentation`
- `Reroute`
- `SAM3PointCollector`
- `VHS_VideoCombine`
- `GetImageRangeFromBatch`
- `SeCModelLoader_Ultra-Fast`
- `Florence2Run`
- `SeCVideoSegmentation`
- `Reroute`
- `DownloadAndLoadFlorence2Model`
- `GetImageSizeAndCount`
- `Florence2toCoordinates`
- `Reroute`
- `GetNode`
- `GetNode`
- `DrawMaskOnImage`
- `SetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `SetNode`
- `WanVideoLoraSelect`
- `GetNode`
- `GetNode`
- `easy imageConcat`
- `GetNode`
- `SetNode`
- `LoadImage`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJ`
- `GetNode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `SetNode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LoadSAM3Model`
- `ImageListToBatch+`
- `GetNode`
- `BlockifyMask`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Manual XY Entry Info`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `DWPreprocessor`
- `GetNode`
- `LayerMask: MaskGrow`
- `WanVideoContextOptions`
- `FaceProcessorLoader`
- `GetNode`
- `WanVideoEncode`
- `WanVideoAddStandInLatent`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `WanVideoVACEEncode`
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `ImageCompositeMasked`
- `easy imageRemBg`
- `easy cleanGpuUsed`
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `GetNode`
- `ImpactSwitch`
- `GetNode`
- `ImpactSwitch`
- `ImpactSwitch`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`

## 知识

覆盖率 **51%**（66/130）

**有卡**：`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`GetImageSizeAndCount`、`WanVideoTextEncode`、`ApplyFaceProcessor`、`WanVideoVACEEncode`、`CreateCFGScheduleFloatList`、`ImageResizeKJ`、`WanVideoSampler`、`VHS_VideoCombine`、`MaskToImage`、`ImageListToBatch+`、`MaskFromBatch+`、`ToBinaryMask`、`GrowMaskWithBlur`、`easy imageBatchToImageList`、`SAM3Segmentation`、`SAM3PointCollector`、`GetImageRangeFromBatch`、`SeCModelLoader_Ultra-Fast`、`Florence2Run`、`SeCVideoSegmentation`、`DownloadAndLoadFlorence2Model`、`Florence2toCoordinates`、`DrawMaskOnImage`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`easy imageConcat`、`LoadImage`、`VHS_LoadVideo`、`WanVideoModelLoader`、`WanVideoDecode`、`LoadSAM3Model`、`BlockifyMask`、`Manual XY Entry Info`、`DWPreprocessor`、`LayerMask: MaskGrow`、`WanVideoContextOptions`、`FaceProcessorLoader`、`WanVideoEncode`、`WanVideoAddStandInLatent`、`LayerUtility: PurgeVRAM V2`、`ImageCompositeMasked`、`easy imageRemBg`、`easy cleanGpuUsed`

**用到的条目**：LoadImage、CreateCFGScheduleFloatList、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoAddStandInLatent、WanVideoDecode、WanVideoEncode、WanVideoTextEncode
