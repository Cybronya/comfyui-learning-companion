---
name: unknown_workflow_video_lora_sampler_1001
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.527
common_nodes: [ApplyFaceProcessor, BlockifyMask, DWPreprocessor, DownloadAndLoadFlorence2Model, DrawMaskOnImage, FaceProcessorLoader, Florence2Run, Florence2toCoordinates, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, GrowMaskWithBlur, ImageCompositeMasked, ImageListToBatch+, ImageResizeKJ, ImpactSwitch, LayerMask: MaskGrow, LayerUtility: PurgeVRAM V2, LoadImage, LoadSAM3Model, LoadWanVideoT5TextEncoder, MaskFromBatch+, MaskToImage, PreviewImage, SAM3PointCollector, SAM3Segmentation, SeCModelLoader_Ultra-Fast, SeCVideoSegmentation, SetNode, ToBinaryMask, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader, easy cleanGpuUsed, easy imageBatchToImageList, easy imageConcat, easy imageRemBg]
problems: []
missing: []
members: [平台全量/🈚️人物置入视频场景_人物迁移_换人物-wan 2.1_2.2 low vace+stand in_1937951058335567873.json, 平台全量/🈚️人物置入视频场景_人物迁移_换人物-wan 2.2-vace 2.2 fun+stand in_1967004177702457346.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1001

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/🈚️人物置入视频场景_人物迁移_换人物-wan 2.1_2.2 low vace+stand in_1937951058335567873.json、平台全量/🈚️人物置入视频场景_人物迁移_换人物-wan 2.2-vace 2.2 fun+stand in_1967004177702457346.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：53%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyFaceProcessor`
- `BlockifyMask`
- `DWPreprocessor`
- `DownloadAndLoadFlorence2Model`
- `DrawMaskOnImage`
- `FaceProcessorLoader`
- `Florence2Run`
- `Florence2toCoordinates`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `ImageListToBatch+`
- `ImageResizeKJ`
- `ImpactSwitch`
- `LayerMask: MaskGrow`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadSAM3Model`
- `LoadWanVideoT5TextEncoder`
- `MaskFromBatch+`
- `MaskToImage`
- `PreviewImage`
- `SAM3PointCollector`
- `SAM3Segmentation`
- `SeCModelLoader_Ultra-Fast`
- `SeCVideoSegmentation`
- `SetNode`
- `ToBinaryMask`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddStandInLatent`
- `WanVideoBlockSwap`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`
- `easy imageConcat`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `CreateCFGScheduleFloatList` —— 1/2 个有
- `Manual XY Entry Info` —— 1/2 个有
- `WanVideoVACEModelSelect` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
