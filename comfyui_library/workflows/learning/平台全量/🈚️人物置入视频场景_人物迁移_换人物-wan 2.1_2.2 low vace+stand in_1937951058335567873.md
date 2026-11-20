---
key: 平台全量/🈚️人物置入视频场景_人物迁移_换人物-wan 2.1_2.2 low vace+stand in_1937951058335567873.json
name: 🈚️人物置入视频场景_人物迁移_换人物-wan 2.1_2.2 low vace+stand in_1937951058335567873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/🈚️人物置入视频场景_人物迁移_换人物-wan 2.1_2.2 low vace+stand in_1937951058335567873.json
hash: 7a76c525fa0afaad
coverage: 0.546218
learned_at: 2026-11-14 02:54:30
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, GetImageSizeAndCount, GetNode, FaceProcessorLoader, GetNode, GetNode, ApplyFaceProcessor, PreviewImage, GetNode, WanVideoEncode, GetNode, WanVideoAddStandInLatent, LoadImage, WanVideoVACEEncode, GetImageSizeAndCount, GetNode, GetNode, GetNode, WanVideoVACEEncode, WanVideoTextEncode, SetNode, WanVideoDecode, GetNode, SetNode, WanVideoSampler, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine, GetNode, GetNode, easy imageConcat, GetNode, ImageResizeKJ, GetNode, ImageResizeKJ, GetNode, MaskToImage, ImageListToBatch+, MaskFromBatch+, ToBinaryMask, GrowMaskWithBlur, ImageListToBatch+, easy imageBatchToImageList, Reroute, SAM3Segmentation, Reroute, SAM3PointCollector, VHS_VideoCombine, GetImageRangeFromBatch, SeCModelLoader_Ultra-Fast, Florence2Run, SeCVideoSegmentation, Reroute, DownloadAndLoadFlorence2Model, GetImageSizeAndCount, Florence2toCoordinates, Reroute, GetNode, GetNode, DrawMaskOnImage, SetNode, SetNode, SetNode, ImageResizeKJ, GetNode, GetNode, LoadSAM3Model, ImageListToBatch+, GetNode, BlockifyMask, SetNode, SetNode, DWPreprocessor, GetNode, LayerMask: MaskGrow, LayerUtility: PurgeVRAM V2, ImageCompositeMasked, easy cleanGpuUsed, PreviewImage, GetNode, GetNode, GetNode, WanVideoContextOptions, WanVideoSampler, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, PreviewImage, easy imageRemBg, WanVideoVAELoader, LoadWanVideoT5TextEncoder, SetNode, SetNode, WanVideoBlockSwap, SetNode, WanVideoVACEModelSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, GetNode, GetNode, ImpactSwitch, WanVideoVACEModelSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect]
patterns: []
missing: []
---

# 平台全量/🈚️人物置入视频场景_人物迁移_换人物-wan 2.1_2.2 low vace+stand in_1937951058335567873.json

> 来源文件 `comfyui_library/workflows/平台全量/🈚️人物置入视频场景_人物迁移_换人物-wan 2.1_2.2 low vace+stand in_1937951058335567873.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（119 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `FaceProcessorLoader`
- `GetNode`
- `GetNode`
- `ApplyFaceProcessor`
- `PreviewImage`
- `GetNode`
- `WanVideoEncode`
- `GetNode`
- `WanVideoAddStandInLatent`
- `LoadImage`
- `WanVideoVACEEncode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoVACEEncode`
- `WanVideoTextEncode`
- `SetNode`
- `WanVideoDecode`
- `GetNode`
- `SetNode`
- `WanVideoSampler` ★核心
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `easy imageConcat`
- `GetNode`
- `ImageResizeKJ`
- `GetNode`
- `ImageResizeKJ`
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
- `SetNode`
- `ImageResizeKJ`
- `GetNode`
- `GetNode`
- `LoadSAM3Model`
- `ImageListToBatch+`
- `GetNode`
- `BlockifyMask`
- `SetNode`
- `SetNode`
- `DWPreprocessor`
- `GetNode`
- `LayerMask: MaskGrow`
- `LayerUtility: PurgeVRAM V2`
- `ImageCompositeMasked`
- `easy cleanGpuUsed`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoContextOptions`
- `WanVideoSampler` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PreviewImage`
- `easy imageRemBg`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `SetNode`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `GetNode`
- `GetNode`
- `ImpactSwitch`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`

## 知识

覆盖率 **55%**（65/119）

**有卡**：`GetImageSizeAndCount`、`FaceProcessorLoader`、`ApplyFaceProcessor`、`WanVideoEncode`、`WanVideoAddStandInLatent`、`LoadImage`、`WanVideoVACEEncode`、`WanVideoTextEncode`、`WanVideoDecode`、`WanVideoSampler`、`VHS_LoadVideo`、`VHS_VideoCombine`、`easy imageConcat`、`ImageResizeKJ`、`MaskToImage`、`ImageListToBatch+`、`MaskFromBatch+`、`ToBinaryMask`、`GrowMaskWithBlur`、`easy imageBatchToImageList`、`SAM3Segmentation`、`SAM3PointCollector`、`GetImageRangeFromBatch`、`SeCModelLoader_Ultra-Fast`、`Florence2Run`、`SeCVideoSegmentation`、`DownloadAndLoadFlorence2Model`、`Florence2toCoordinates`、`DrawMaskOnImage`、`LoadSAM3Model`、`BlockifyMask`、`DWPreprocessor`、`LayerMask: MaskGrow`、`LayerUtility: PurgeVRAM V2`、`ImageCompositeMasked`、`easy cleanGpuUsed`、`WanVideoContextOptions`、`easy imageRemBg`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoVACEModelSelect`、`WanVideoLoraSelect`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoAddStandInLatent、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVACEEncode
