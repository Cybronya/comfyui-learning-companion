---
name: unknown_workflow_video_lora_sampler_467
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.5696
common_nodes: [AudioSeparation, CLIPVisionLoader, Display Int (rgthree), DownloadAndLoadWav2VecModel, FantasyPortraitModelLoader, Float, GetNode, ImageFromBatch, ImageResizeKJv2, ImpactInt, LoadAudio, LoadImage, MultiTalkWav2VecEmbeds, RHHiddenNodes, RH_GetAudioDuration, SetNode, SimpleMath+, TextInput_, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/一键生成口播数字人  表情+口型+声音克隆_1990236506012962817.json, 数字人/数字人/一键生成口播数字人  表情+口型+声音克隆_1999134312589127682.json, 数字人/数字人/数字人_1966800389586759681.json, 视频生成/图生视频/一键生成 带货数字人_1958495349935652865.json, 视频生成/图生视频/一键生成口播数字人  表情+口型+声音克隆_1958115573953679362.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_467

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/一键生成口播数字人  表情+口型+声音克隆_1990236506012962817.json、数字人/数字人/一键生成口播数字人  表情+口型+声音克隆_1999134312589127682.json、数字人/数字人/数字人_1966800389586759681.json、视频生成/图生视频/一键生成 带货数字人_1958495349935652865.json、视频生成/图生视频/一键生成口播数字人  表情+口型+声音克隆_1958115573953679362.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `Display Int (rgthree)`
- `DownloadAndLoadWav2VecModel`
- `FantasyPortraitModelLoader`
- `Float`
- `GetNode`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImpactInt`
- `LoadAudio`
- `LoadImage`
- `MultiTalkWav2VecEmbeds`
- `RHHiddenNodes`
- `RH_GetAudioDuration`
- `SetNode`
- `SimpleMath+`
- `TextInput_`
- `VHS_VideoCombine`
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
- `AudioCrop` —— 4/5 个有
- `FantasyPortraitFaceDetector` —— 4/5 个有
- `ImageConcatMulti` —— 4/5 个有
- `ImpactSwitch` —— 4/5 个有
- `LandmarksToImage` —— 4/5 个有
- `MegaTTS3Run` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `Primitive integer [Crystools]` —— 4/5 个有
- `SaveAudio` —— 4/5 个有
- `VHS_LoadVideo` —— 4/5 个有
- `WanVideoAddFantasyPortrait` —— 4/5 个有
- `IndexTTSRun` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
