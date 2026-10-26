---
name: unknown_workflow_video_lora_sampler_211
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8342
common_nodes: [ApplyFaceProcessor, FaceProcessorLoader, GetNode, ImageConcatMulti, ImageResizeKJv2, InspyrenetRembg, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoDecode, WanVideoEncode, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/人脸一致性数字人_1957753380335878145.json, 数字人/数字人/视频人物替换2.1产品一致性_2089735759791214593.json, 视频生成/图生视频/Wan2.1+Stand-In一致性人物主体替换工作流-v1_1957443614760693762.json, 视频生成/图生视频/Wan2.1+姿势参考+Stand-In+MultiTalk 人脸一致性文生数字人_1956357600432541698.json, 视频生成/图生视频/Wan2.1视频换主体工作流-V.1_1957007357193457666.json, 视频生成/图生视频/Wan2.1视频换主体工作流-V.1_1959057918983352321.json, 视频生成/图生视频/Wan2.1视频换主体工作流_1960183828935553025.json, 视频生成/图生视频/视频人物替换2.1_1957743367306276865.json, 视频生成/图生视频/视频人物替换2.1产品一致性_2037228582350622721.json, 视频生成/文生视频/美女跳舞转绘视频人物替换视频主体替换V1.0_1958502748553637889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_211

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（数字人/数字人/人脸一致性数字人_1957753380335878145.json、数字人/数字人/视频人物替换2.1产品一致性_2089735759791214593.json、视频生成/图生视频/Wan2.1+Stand-In一致性人物主体替换工作流-v1_1957443614760693762.json、视频生成/图生视频/Wan2.1+姿势参考+Stand-In+MultiTalk 人脸一致性文生数字人_1956357600432541698.json、视频生成/图生视频/Wan2.1视频换主体工作流-V.1_1957007357193457666.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 10 个 workflow 都包含：
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `InspyrenetRembg`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SetNode`
- `SimpleMath+`
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
- `AudioCrop` —— 9/10 个有
- `AudioSeparation` —— 9/10 个有
- `DownloadAndLoadWav2VecModel` —— 9/10 个有
- `ImageFromBatch+` —— 9/10 个有
- `JWInteger` —— 9/10 个有
- `JWIntegerToString` —— 9/10 个有
- `LoadWanVideoT5TextEncoder` —— 9/10 个有
- `MultiTalkModelLoader` —— 9/10 个有
- `MultiTalkWav2VecEmbeds` —— 9/10 个有
- `PreviewAudio` —— 9/10 个有
- `VHS_VideoInfo` —— 9/10 个有
- `WanVideoBlockSwap` —— 9/10 个有
- `WanVideoModelLoader` —— 9/10 个有
- `WanVideoTorchCompileSettings` —— 9/10 个有
- `WanVideoVACEModelSelect` —— 9/10 个有
- `AIO_Preprocessor` —— 8/10 个有
- `ColorMatch` —— 8/10 个有
- `GetImageSizeAndCount` —— 8/10 个有
- `GrowMaskWithBlur` —— 8/10 个有
- `ImageFromBatch` —— 8/10 个有
- `ImageResizeKJ` —— 8/10 个有
- `InpaintPreprocessor` —— 8/10 个有
- `LayerUtility: ImageBlend` —— 8/10 个有
- `LayerUtility: PurgeVRAM V2` —— 8/10 个有
- `Text Multiline` —— 8/10 个有
- `WanVideoLoraSelect` —— 8/10 个有
- `Fast Groups Bypasser (rgthree)` —— 7/10 个有
- `ImageUpscaleWithModel` —— 7/10 个有
- `RHHiddenNodes` —— 7/10 个有
- `UpscaleModelLoader` —— 7/10 个有
- `WanVideoSLG` —— 7/10 个有
- `WanVideoEasyCache` —— 6/10 个有
- `ImpactSwitch` —— 5/10 个有
- `Text Concatenate` —— 5/10 个有
- `MaskPreview+` —— 4/10 个有
- `DownloadAndLoadFlorence2Model` —— 3/10 个有
- `Florence2Run` —— 3/10 个有
- `Florence2toCoordinates` —— 3/10 个有
- `LayerUtility: PurgeVRAM` —— 3/10 个有
- `PrimitiveString` —— 3/10 个有
- `RH_Captioner` —— 3/10 个有
- `RH_Translator` —— 3/10 个有
- `ShowText|pysssss` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `DownloadAndLoadSAM2Model` —— 2/10 个有
- `OpenposePreprocessor` —— 2/10 个有
- `RH_LLMAPI_NODE` —— 2/10 个有
- `Sam2Segmentation` —— 2/10 个有
- `Wan22PromptSelector` —— 2/10 个有
- `WanVideoVACEStartToEndFrame` —— 2/10 个有
- `easy imageScaleDownToSize` —— 2/10 个有
- `AddLabel` —— 1/10 个有
- `DepthAnything_V2` —— 1/10 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/10 个有
- `EmptyImage` —— 1/10 个有
- `ImageBlend` —— 1/10 个有
- `Primitive integer [Crystools]` —— 1/10 个有
- `WanVideoExperimentalArgs` —— 1/10 个有
- `easy imageRemBg` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
