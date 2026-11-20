---
name: unknown_workflow_video_inpaint_lora_16
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.50975
common_nodes: [DWPreprocessor, GetImageSizeAndCount, GetNode, ImageFromBatch+, ImageResizeKJ, InpaintPreprocessor, LayerMask: DrawBBoxMaskV2, LayerMask: LoadSegmentAnythingModels, LayerMask: MaskGrow, LayerMask: ObjectDetectorYOLO8, LayerMask: PersonMaskUltra V2, LayerMask: SegmentAnythingUltra V3, LayerUtility: ImageBlend, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, ResizeMask, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/最新视频换头_换脸_1980197977019027458.json, 平台全量/🈚️视频换头_换脸_面部重绘-vace-wan 2.1_2.2 low+stand in_1940657492189753345.json, 平台全量/🈚️视频换头_换脸_面部重绘-wan2.2 vace 2.2 fun+stand in_1966970471642226689.json, 数字人/数字人/🈚️视频换头+对口型-vace-wan 2.1_2.2 low+lynx_2008809317700472834.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_16

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/最新视频换头_换脸_1980197977019027458.json、平台全量/🈚️视频换头_换脸_面部重绘-vace-wan 2.1_2.2 low+stand in_1940657492189753345.json、平台全量/🈚️视频换头_换脸_面部重绘-wan2.2 vace 2.2 fun+stand in_1966970471642226689.json、数字人/数字人/🈚️视频换头+对口型-vace-wan 2.1_2.2 low+lynx_2008809317700472834.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 4 个 workflow 都包含：
- `DWPreprocessor`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageFromBatch+`
- `ImageResizeKJ`
- `InpaintPreprocessor`
- `LayerMask: DrawBBoxMaskV2`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: MaskGrow`
- `LayerMask: ObjectDetectorYOLO8`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: SegmentAnythingUltra V3`
- `LayerUtility: ImageBlend`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `ResizeMask`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ApplyFaceProcessor` —— 3/4 个有
- `FaceProcessorLoader` —— 3/4 个有
- `ImpactSwitch` —— 3/4 个有
- `InpaintCropImproved` —— 3/4 个有
- `Masks Combine Regions` —— 3/4 个有
- `OnnxDetectionModelLoader` —— 3/4 个有
- `PoseDetectionOneToAllAnimation` —— 3/4 个有
- `WanVideoAddStandInLatent` —— 3/4 个有
- `WanVideoContextOptions` —— 3/4 个有
- `WanVideoEncode` —— 3/4 个有
- `CreateCFGScheduleFloatList` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `LayerMask: MaskPreview` —— 2/4 个有
- `LayerMask: ObjectDetectorFL2` —— 2/4 个有
- `LoadFlorence2Model` —— 2/4 个有
- `WanVideoVACEModelSelect` —— 2/4 个有
- `Audio Cut (mtb)` —— 1/4 个有
- `AudioSeparation` —— 1/4 个有
- `DownloadAndLoadWav2VecModel` —— 1/4 个有
- `InpaintCrop` —— 1/4 个有
- `Int` —— 1/4 个有
- `LoadLynxResampler` —— 1/4 个有
- `LynxEncodeFaceIP` —— 1/4 个有
- `LynxInsightFaceCrop` —— 1/4 个有
- `MultiTalkModelLoader` —— 1/4 个有
- `MultiTalkSilentEmbeds` —— 1/4 个有
- `MultiTalkWav2VecEmbeds` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `SaveAudio` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有
- `Text` —— 1/4 个有
- `VHS_LoadAudioUpload` —— 1/4 个有
- `WanVideoAddLynxEmbeds` —— 1/4 个有
- `WanVideoExtraModelSelect` —— 1/4 个有
- `WanVideoTextEncodeCached` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
