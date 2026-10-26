---
name: unknown_workflow_video_lora_sampler_815
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8455
common_nodes: [AudioSeparation, CLIPVisionLoader, CM_FloatBinaryOperation, CM_FloatToInt, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetImageSizeAndCount, ImageConcanate, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, SoundFlow_GetLength, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/视频-视频对音频口型(时长对齐)-wan2.1-InfiniteTalk-KJ_2009923766071070722.json, 视频生成/图生视频/视频-图片对音频口型-wan2.1-InfiniteTalk-KJ_1973987778281213954.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_815

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/视频-视频对音频口型(时长对齐)-wan2.1-InfiniteTalk-KJ_2009923766071070722.json、视频生成/图生视频/视频-图片对音频口型-wan2.1-InfiniteTalk-KJ_1973987778281213954.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `CM_FloatBinaryOperation`
- `CM_FloatToInt`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `ImageConcanate`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `SoundFlow_GetLength`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 1/2 个有
- `CM_BoolToInt` —— 1/2 个有
- `CM_IntBinaryCondition JK` —— 1/2 个有
- `CM_IntBinaryOperation` —— 1/2 个有
- `CM_IntToFloat` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageBatchMulti` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有
- `WanVideoVACEStartToEndFrame` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
