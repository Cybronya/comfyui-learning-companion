---
name: unknown_workflow_video_inpaint_lora_9
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.81
common_nodes: [AIO_Preprocessor, AddLabel, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CM_BoolToInt, DepthAnything_V2, DifferentialDiffusion, DownloadAndLoadDepthAnythingV2Model, DownloadAndLoadFlorence2Model, DownloadAndLoadSAM2Model, DualCLIPLoader, EmptyImage, Florence2Run, Florence2toCoordinates, FluxGuidance, GetImageSizeAndCount, GetNode, GrowMask, GrowMaskWithBlur, Image To Mask, ImageBlend, ImageConcanate, ImageConcatMulti, ImageFromBatch, ImageResize+, ImageResizeKJ, ImageScale, ImpactSwitch, InpaintCrop, InpaintModelConditioning, InpaintPreprocessor, InpaintStitch, KSampler, LayerMask: SegmentAnythingUltra V2, LayerUtility: ColorImage V2, LayerUtility: CropByMask, LayerUtility: ImageBlend, LayerUtility: ImageRemoveAlpha, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, MaskPreview+, MaskToImage, PreviewImage, Primitive float [Crystools], Primitive integer [Crystools], PrimitiveString, RHHiddenNodes, RH_Captioner, RH_Translator, Sam2Segmentation, SaveImage, SetNode, ShowText|pysssss, SimpleMath+, StyleModelApply, StyleModelLoader, Text Concatenate, Text Multiline, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader, easy cleanGpuUsed, easy imageInsetCrop, easy imageRemBg, easy imageSize, easy isMaskEmpty, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/视频换装+人物替换-娱乐版本-180帧_1968193256179773442.json, 视频生成/图生视频/视频换装+人物替换-娱乐版本-_1985391896409292801.json, 视频生成/图生视频/视频换装+人物替换-娱乐版本_1972521006562734081.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_9

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/视频换装+人物替换-娱乐版本-180帧_1968193256179773442.json、视频生成/图生视频/视频换装+人物替换-娱乐版本-_1985391896409292801.json、视频生成/图生视频/视频换装+人物替换-娱乐版本_1972521006562734081.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `AddLabel`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CM_BoolToInt`
- `DepthAnything_V2`
- `DifferentialDiffusion`
- `DownloadAndLoadDepthAnythingV2Model`
- `DownloadAndLoadFlorence2Model`
- `DownloadAndLoadSAM2Model`
- `DualCLIPLoader`
- `EmptyImage`
- `Florence2Run`
- `Florence2toCoordinates`
- `FluxGuidance`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `GrowMaskWithBlur`
- `Image To Mask`
- `ImageBlend`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageResize+`
- `ImageResizeKJ`
- `ImageScale`
- `ImpactSwitch`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintPreprocessor`
- `InpaintStitch`
- `KSampler`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ColorImage V2`
- `LayerUtility: CropByMask`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `MaskToImage`
- `PreviewImage`
- `Primitive float [Crystools]`
- `Primitive integer [Crystools]`
- `PrimitiveString`
- `RHHiddenNodes`
- `RH_Captioner`
- `RH_Translator`
- `Sam2Segmentation`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `SimpleMath+`
- `StyleModelApply`
- `StyleModelLoader`
- `Text Concatenate`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy imageInsetCrop`
- `easy imageRemBg`
- `easy imageSize`
- `easy isMaskEmpty`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
