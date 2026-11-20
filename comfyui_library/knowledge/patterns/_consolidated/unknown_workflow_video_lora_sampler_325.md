---
name: unknown_workflow_video_lora_sampler_325
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.842222
common_nodes: [ApplyFaceProcessor, AudioCrop, AudioSeparation, DownloadAndLoadWav2VecModel, FaceProcessorLoader, GetNode, ImageConcatMulti, ImageFromBatch+, ImageResizeKJv2, InspyrenetRembg, JWInteger, JWIntegerToString, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAudio, PreviewImage, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAddStandInLatent, WanVideoDecode, WanVideoEncode, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/人脸一致性数字人_1957753380335878145.json, 数字人/数字人/视频人物替换2.1产品一致性_2089735759791214593.json, 视频生成/图生视频/Wan2.1+Stand-In一致性人物主体替换工作流-v1_1957443614760693762.json, 视频生成/图生视频/Wan2.1+姿势参考+Stand-In+MultiTalk 人脸一致性文生数字人_1956357600432541698.json, 视频生成/图生视频/Wan2.1视频换主体工作流-V.1_1957007357193457666.json, 视频生成/图生视频/Wan2.1视频换主体工作流-V.1_1959057918983352321.json, 视频生成/图生视频/Wan2.1视频换主体工作流_1960183828935553025.json, 视频生成/图生视频/视频人物替换2.1_1957743367306276865.json, 视频生成/图生视频/视频人物替换2.1产品一致性_2037228582350622721.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_325

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（数字人/数字人/人脸一致性数字人_1957753380335878145.json、数字人/数字人/视频人物替换2.1产品一致性_2089735759791214593.json、视频生成/图生视频/Wan2.1+Stand-In一致性人物主体替换工作流-v1_1957443614760693762.json、视频生成/图生视频/Wan2.1+姿势参考+Stand-In+MultiTalk 人脸一致性文生数字人_1956357600432541698.json、视频生成/图生视频/Wan2.1视频换主体工作流-V.1_1957007357193457666.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 9 个 workflow 都包含：
- `ApplyFaceProcessor`
- `AudioCrop`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `FaceProcessorLoader`
- `GetNode`
- `ImageConcatMulti`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `InspyrenetRembg`
- `JWInteger`
- `JWIntegerToString`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAudio`
- `PreviewImage`
- `SetNode`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
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
- `LoadWanVideoT5TextEncoder` —— 8/9 个有
- `WanVideoBlockSwap` —— 8/9 个有
- `WanVideoModelLoader` —— 8/9 个有
- `WanVideoTorchCompileSettings` —— 8/9 个有
- `WanVideoVACEModelSelect` —— 8/9 个有
- `AIO_Preprocessor` —— 7/9 个有
- `ColorMatch` —— 7/9 个有
- `Fast Groups Bypasser (rgthree)` —— 7/9 个有
- `GetImageSizeAndCount` —— 7/9 个有
- `GrowMaskWithBlur` —— 7/9 个有
- `ImageFromBatch` —— 7/9 个有
- `ImageResizeKJ` —— 7/9 个有
- `InpaintPreprocessor` —— 7/9 个有
- `LayerUtility: ImageBlend` —— 7/9 个有
- `LayerUtility: PurgeVRAM V2` —— 7/9 个有
- `Text Multiline` —— 7/9 个有
- `WanVideoLoraSelect` —— 7/9 个有
- `ImageUpscaleWithModel` —— 6/9 个有
- `RHHiddenNodes` —— 6/9 个有
- `UpscaleModelLoader` —— 6/9 个有
- `WanVideoEasyCache` —— 6/9 个有
- `WanVideoSLG` —— 6/9 个有
- `ImpactSwitch` —— 4/9 个有
- `MaskPreview+` —— 4/9 个有
- `Text Concatenate` —— 4/9 个有
- `LayerUtility: PurgeVRAM` —— 3/9 个有
- `CR Text` —— 2/9 个有
- `DownloadAndLoadFlorence2Model` —— 2/9 个有
- `DownloadAndLoadSAM2Model` —— 2/9 个有
- `Florence2Run` —— 2/9 个有
- `Florence2toCoordinates` —— 2/9 个有
- `OpenposePreprocessor` —— 2/9 个有
- `PrimitiveString` —— 2/9 个有
- `RH_Captioner` —— 2/9 个有
- `RH_LLMAPI_NODE` —— 2/9 个有
- `RH_Translator` —— 2/9 个有
- `Sam2Segmentation` —— 2/9 个有
- `ShowText|pysssss` —— 2/9 个有
- `Wan22PromptSelector` —— 2/9 个有
- `WanVideoVACEStartToEndFrame` —— 2/9 个有
- `easy imageScaleDownToSize` —— 2/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
