---
name: unknown_workflow_video_lora_sampler_817
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5715
common_nodes: [AudioBeforeAfterSilence, AudioCrop, AudioSeparation, Bjornulf_ShowInt, CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageSize, GetNode, ImageConcanate, ImageResizeKJv2, ImpactSwitch, IndexTTS2Run, LoadAudio, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkSilentEmbeds, MultiTalkWav2VecEmbeds, PreviewAudio, SaveAudio, SetNode, SimpleMath+, SoundFlow_GetLength, ToInt, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/🈚️wan2.1 Infinite Talk 视频改口型_对口型_数字人_口播 视频重绘_1969616527890804738.json, 视频生成/图生视频/✅wan2.1 Infinite Talk-图片对口型_固定机位-图生视频，口播数字人_1964014354544869377.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_817

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/🈚️wan2.1 Infinite Talk 视频改口型_对口型_数字人_口播 视频重绘_1969616527890804738.json、视频生成/图生视频/✅wan2.1 Infinite Talk-图片对口型_固定机位-图生视频，口播数字人_1964014354544869377.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：57%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioBeforeAfterSilence`
- `AudioCrop`
- `AudioSeparation`
- `Bjornulf_ShowInt`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `GetImageSize`
- `GetNode`
- `ImageConcanate`
- `ImageResizeKJv2`
- `ImpactSwitch`
- `IndexTTS2Run`
- `LoadAudio`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkSilentEmbeds`
- `MultiTalkWav2VecEmbeds`
- `PreviewAudio`
- `SaveAudio`
- `SetNode`
- `SimpleMath+`
- `SoundFlow_GetLength`
- `ToInt`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Audio To Text (mtb)` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `ImageBatchMulti` —— 1/2 个有
- `ImagePass` —— 1/2 个有
- `Int` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `Load Whisper (mtb)` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RepeatImageBatch` —— 1/2 个有
- `ReverseImageBatch` —— 1/2 个有
- `VHS_GetImageCount` —— 1/2 个有
- `WanVideoEncode` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
