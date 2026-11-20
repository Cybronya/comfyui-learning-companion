---
name: unknown_workflow_video_inpaint_upscale_5
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8925
common_nodes: [AIO_Preprocessor, ApplyFaceProcessor, CR Text Concatenate, ColorMatch, DownloadAndLoadWav2VecModel, FaceProcessorLoader, GetImageSizeAndCount, GrowMaskWithBlur, ImageConcatMulti, ImageFromBatch, ImageFromBatch+, ImageResizeKJ, ImageResizeKJv2, ImageUpscaleWithModel, InpaintPreprocessor, JWInteger, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerMask: LoadSegmentAnythingModels, LayerMask: ObjectDetectorMask, LayerMask: SAM2VideoUltra, LayerMask: SegmentAnythingUltra V3, LayerUtility: ImageBlend, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewImage, PrimitiveStringMultiline, RH_Captioner, ShowText|pysssss, SimpleMath+, UpscaleModelLoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoEasyCache, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVAELoader, easy int, easy showAnything]
problems: []
missing: []
members: [平台全量/[🛫书墨]视频换主体_1958480217083953153.json, 视频生成/文生视频/美女跳舞转绘视频人物替换视频主体替换V1.1_1958674460129837058.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_upscale_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/[🛫书墨]视频换主体_1958480217083953153.json、视频生成/文生视频/美女跳舞转绘视频人物替换视频主体替换V1.1_1958674460129837058.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `ApplyFaceProcessor`
- `CR Text Concatenate`
- `ColorMatch`
- `DownloadAndLoadWav2VecModel`
- `FaceProcessorLoader`
- `GetImageSizeAndCount`
- `GrowMaskWithBlur`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageFromBatch+`
- `ImageResizeKJ`
- `ImageResizeKJv2`
- `ImageUpscaleWithModel`
- `InpaintPreprocessor`
- `JWInteger`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: ObjectDetectorMask`
- `LayerMask: SAM2VideoUltra`
- `LayerMask: SegmentAnythingUltra V3`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RH_Captioner`
- `ShowText|pysssss`
- `SimpleMath+`
- `UpscaleModelLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoAddStandInLatent`
- `WanVideoBlockSwap`
- `WanVideoEasyCache`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RHHiddenNodes` —— 1/2 个有
- `WanVideoDecode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
