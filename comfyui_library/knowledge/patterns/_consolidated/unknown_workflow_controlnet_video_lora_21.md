---
name: unknown_workflow_controlnet_video_lora_21
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.43
common_nodes: [Any Switch (rgthree), Audio Cut (mtb), AudioSeparation, DownloadAndLoadWav2VecModel, Fast Groups Bypasser (rgthree), GetNode, ImageFromBatch+, ImageResizeKJ, Int, LoadImage, MultiTalkModelLoader, MultiTalkSilentEmbeds, MultiTalkWav2VecEmbeds, PreviewAny, SetNode, SimpleMath+, VHS_LoadAudioUpload, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy seed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1_2.2 low VACE姿势+u3c运镜+对口型multi_infinitetalk_1977065847162314754.json, 视频生成/图生视频/🈚️对口型+动作迁移+表情+运镜_翻唱 Multitalk_InfiniteTalk-wan2.1_1971491546132594689.json, 视频生成/图生视频/🈚️数字人_唱歌_音频驱动图片_对口型 MultiTalk_InfiniteTalk-wan2.1_1937131515212107778.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_21

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.1_2.2 low VACE姿势+u3c运镜+对口型multi_infinitetalk_1977065847162314754.json、视频生成/图生视频/🈚️对口型+动作迁移+表情+运镜_翻唱 Multitalk_InfiniteTalk-wan2.1_1971491546132594689.json、视频生成/图生视频/🈚️数字人_唱歌_音频驱动图片_对口型 MultiTalk_InfiniteTalk-wan2.1_1937131515212107778.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：43%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Audio Cut (mtb)`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `ImageFromBatch+`
- `ImageResizeKJ`
- `Int`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkSilentEmbeds`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `SetNode`
- `SimpleMath+`
- `VHS_LoadAudioUpload`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `FantasyPortraitFaceDetector` —— 2/3 个有
- `FantasyPortraitModelLoader` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `ImageSmartSharpen+` —— 2/3 个有
- `ImpactControlBridge` —— 2/3 个有
- `LoadLynxResampler` —— 2/3 个有
- `LoadWanVideoClipTextEncoder` —— 2/3 个有
- `LoadWanVideoT5TextEncoder` —— 2/3 个有
- `LynxEncodeFaceIP` —— 2/3 个有
- `LynxInsightFaceCrop` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Text` —— 2/3 个有
- `WanVideoAddFantasyPortrait` —— 2/3 个有
- `WanVideoAddLynxEmbeds` —— 2/3 个有
- `WanVideoClipVisionEncode` —— 2/3 个有
- `WanVideoExtraModelSelect` —— 2/3 个有
- `WanVideoImageToVideoEncode` —— 2/3 个有
- `WanVideoTextEncodeCached` —— 2/3 个有
- `WanVideoTextEncodeSingle` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `easy imageRemBg` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `ApplyFaceProcessor` —— 1/3 个有
- `BboxVisualize` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `DWPreprocessor` —— 1/3 个有
- `FaceProcessorLoader` —— 1/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `InpaintCropImproved` —— 1/3 个有
- `LandmarksToImage` —— 1/3 个有
- `LayerMask: PersonMaskUltra V2` —— 1/3 个有
- `OnnxDetectionModelLoader` —— 1/3 个有
- `PoseDetectionOneToAllAnimation` —— 1/3 个有
- `WanVideoAddStandInLatent` —— 1/3 个有
- `WanVideoUniAnimatePoseInput` —— 1/3 个有
- `WanVideoVACEEncode` —— 1/3 个有
- `WanVideoVACEModelSelect` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
