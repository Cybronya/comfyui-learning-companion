---
name: unknown_workflow_video_lora_sampler_879
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.565
common_nodes: [AudioSeparation, CLIPVisionLoader, Display Int (rgthree), DownloadAndLoadWav2VecModel, FantasyPortraitFaceDetector, FantasyPortraitModelLoader, Float, GetNode, ImageConcatMulti, ImageFromBatch, ImageResizeKJv2, ImpactInt, ImpactSwitch, LandmarksToImage, LoadAudio, LoadImage, MultiTalkWav2VecEmbeds, PreviewImage, Primitive integer [Crystools], RHHiddenNodes, RH_GetAudioDuration, SaveAudio, SetNode, SimpleMath+, TextInput_, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddFantasyPortrait, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1958495349935652865.json, 视频生成/图生视频/一键生成口播数字人  表情+口型+声音克隆_1958115573953679362.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_879

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1958495349935652865.json、视频生成/图生视频/一键生成口播数字人  表情+口型+声音克隆_1958115573953679362.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `Display Int (rgthree)`
- `DownloadAndLoadWav2VecModel`
- `FantasyPortraitFaceDetector`
- `FantasyPortraitModelLoader`
- `Float`
- `GetNode`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImpactInt`
- `ImpactSwitch`
- `LandmarksToImage`
- `LoadAudio`
- `LoadImage`
- `MultiTalkWav2VecEmbeds`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `RHHiddenNodes`
- `RH_GetAudioDuration`
- `SaveAudio`
- `SetNode`
- `SimpleMath+`
- `TextInput_`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddFantasyPortrait`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 1/2 个有
- `IndexTTSRun` —— 1/2 个有
- `MegaTTS3Run` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
