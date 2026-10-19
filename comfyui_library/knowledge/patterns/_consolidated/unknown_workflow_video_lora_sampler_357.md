---
name: unknown_workflow_video_lora_sampler_357
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.766667
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, ToInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2007804749827022850.json, 视频生成/图生视频/1968672721771143169.json, 视频生成/图生视频/2069716627356217345.json, 视频生成/图生视频/2054541988237717506.json, 视频生成/图生视频/2050200100416311298.json, 音频生成/音频生成/Infinite Talk-对口型说话+唱歌无限时长+高动态_2021031552670507010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_357

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2007804749827022850.json、视频生成/图生视频/1968672721771143169.json、视频生成/图生视频/2069716627356217345.json、视频生成/图生视频/2054541988237717506.json、视频生成/图生视频/2050200100416311298.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `ToInt`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 5/6 个有
- `ImageResizeKJv2` —— 5/6 个有
- `Int` —— 5/6 个有
- `CR Prompt Text` —— 4/6 个有
- `GetNode` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `Display Int (rgthree)` —— 3/6 个有
- `Float` —— 3/6 个有
- `GetImageSizeAndCount` —— 3/6 个有
- `PreviewAny` —— 3/6 个有
- `RH_GetAudioDuration` —— 3/6 个有
- `SoundFlow_GetLength` —— 3/6 个有
- `WanVideoTorchCompileSettings` —— 3/6 个有
- `easy showAnything` —— 3/6 个有
- `AddLabel` —— 2/6 个有
- `GetImageRangeFromBatch` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `SeedVR2` —— 1/6 个有
- `SeedVR2BlockSwap` —— 1/6 个有
- `TTResolutionSelector` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
