---
name: unknown_workflow_video_lora_sampler_829
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.838667
common_nodes: [AudioSeparation, CLIPVisionLoader, CM_FloatBinaryOperation, CM_FloatToInt, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetImageSizeAndCount, ImageConcanate, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, SoundFlow_GetLength, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/视频-视频对音频口型-wan2.1-InfiniteTalk-KJ_1973968886301331458.json, 数字人/数字人/视频-视频对音频口型(时长对齐)-wan2.1-InfiniteTalk-KJ_2009923766071070722.json, 视频生成/图生视频/视频-图片对音频口型-wan2.1-InfiniteTalk-KJ_1973987778281213954.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_829

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/视频-视频对音频口型-wan2.1-InfiniteTalk-KJ_1973968886301331458.json、数字人/数字人/视频-视频对音频口型(时长对齐)-wan2.1-InfiniteTalk-KJ_2009923766071070722.json、视频生成/图生视频/视频-图片对音频口型-wan2.1-InfiniteTalk-KJ_1973987778281213954.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
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
- `AudioCrop` —— 2/3 个有
- `CM_BoolToInt` —— 2/3 个有
- `CM_IntBinaryCondition JK` —— 2/3 个有
- `CM_IntBinaryOperation` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `ImageBatchMulti` —— 2/3 个有
- `MaskPreview+` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `VHS_VideoInfo` —— 2/3 个有
- `WanVideoVACEStartToEndFrame` —— 2/3 个有
- `easy anythingIndexSwitch` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `CM_IntToFloat` —— 1/3 个有
- `CM_IntUnaryOperation` —— 1/3 个有
- `ImageBatchRepeatInterleaving` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `PreviewAny` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
