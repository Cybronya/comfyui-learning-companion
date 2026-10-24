---
name: unknown_workflow_video_inpaint_lora_2
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.83575
common_nodes: [AIO_Preprocessor, ApplyFaceProcessor, ColorMatch, FaceProcessorLoader, GetImageSizeAndCount, GetNode, GrowMaskWithBlur, ImageConcatMulti, ImageFromBatch, ImageResizeKJ, ImageResizeKJv2, InpaintPreprocessor, InspyrenetRembg, LayerUtility: ImageBlend, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, PreviewImage, SetNode, SimpleMath+, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoDecode, WanVideoEncode, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/视频人物替换2.1产品一致性_2089735759791214593.json, 视频生成/图生视频/Wan2.1+Stand-In一致性人物主体替换工作流-v1_1957443614760693762.json, 视频生成/图生视频/Wan2.1视频换主体工作流-V.1_1957007357193457666.json, 视频生成/图生视频/Wan2.1视频换主体工作流-V.1_1959057918983352321.json, 视频生成/图生视频/Wan2.1视频换主体工作流_1960183828935553025.json, 视频生成/图生视频/视频人物替换2.1_1957743367306276865.json, 视频生成/图生视频/视频人物替换2.1产品一致性_2037228582350622721.json, 视频生成/文生视频/美女跳舞转绘视频人物替换视频主体替换V1.0_1958502748553637889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_2

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/视频人物替换2.1产品一致性_2089735759791214593.json、视频生成/图生视频/Wan2.1+Stand-In一致性人物主体替换工作流-v1_1957443614760693762.json、视频生成/图生视频/Wan2.1视频换主体工作流-V.1_1957007357193457666.json、视频生成/图生视频/Wan2.1视频换主体工作流-V.1_1959057918983352321.json、视频生成/图生视频/Wan2.1视频换主体工作流_1960183828935553025.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `AIO_Preprocessor`
- `ApplyFaceProcessor`
- `ColorMatch`
- `FaceProcessorLoader`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageResizeKJ`
- `ImageResizeKJv2`
- `InpaintPreprocessor`
- `InspyrenetRembg`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `PreviewImage`
- `SetNode`
- `SimpleMath+`
- `Text Multiline`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddStandInLatent`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 7/8 个有
- `AudioSeparation` —— 7/8 个有
- `DownloadAndLoadWav2VecModel` —— 7/8 个有
- `Fast Groups Bypasser (rgthree)` —— 7/8 个有
- `ImageFromBatch+` —— 7/8 个有
- `ImageUpscaleWithModel` —— 7/8 个有
- `JWInteger` —— 7/8 个有
- `JWIntegerToString` —— 7/8 个有
- `LoadWanVideoT5TextEncoder` —— 7/8 个有
- `MultiTalkModelLoader` —— 7/8 个有
- `MultiTalkWav2VecEmbeds` —— 7/8 个有
- `PreviewAudio` —— 7/8 个有
- `RHHiddenNodes` —— 7/8 个有
- `UpscaleModelLoader` —— 7/8 个有
- `VHS_VideoInfo` —— 7/8 个有
- `WanVideoBlockSwap` —— 7/8 个有
- `WanVideoModelLoader` —— 7/8 个有
- `WanVideoSLG` —— 7/8 个有
- `WanVideoTorchCompileSettings` —— 7/8 个有
- `WanVideoVACEModelSelect` —— 7/8 个有
- `WanVideoEasyCache` —— 6/8 个有
- `WanVideoLoraSelect` —— 6/8 个有
- `MaskPreview+` —— 4/8 个有
- `DownloadAndLoadFlorence2Model` —— 3/8 个有
- `Florence2Run` —— 3/8 个有
- `Florence2toCoordinates` —— 3/8 个有
- `ImpactSwitch` —— 3/8 个有
- `LayerUtility: PurgeVRAM` —— 3/8 个有
- `PrimitiveString` —— 3/8 个有
- `RH_Captioner` —— 3/8 个有
- `RH_Translator` —— 3/8 个有
- `ShowText|pysssss` —— 3/8 个有
- `Text Concatenate` —— 3/8 个有
- `DownloadAndLoadSAM2Model` —— 2/8 个有
- `Sam2Segmentation` —— 2/8 个有
- `AddLabel` —— 1/8 个有
- `DepthAnything_V2` —— 1/8 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/8 个有
- `EmptyImage` —— 1/8 个有
- `ImageBlend` —— 1/8 个有
- `Primitive integer [Crystools]` —— 1/8 个有
- `WanVideoExperimentalArgs` —— 1/8 个有
- `easy imageRemBg` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
