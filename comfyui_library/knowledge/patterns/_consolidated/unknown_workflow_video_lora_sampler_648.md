---
name: unknown_workflow_video_lora_sampler_648
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.877333
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/Infinitetalk_视频对口型-保持原视频动作一致_1979962837202276353.json, 数字人/数字人/数字人-视频对口型-完美复刻动作，保持原视频动作一致_1988076238738796546.json, 视频生成/图生视频/InfiniteTalk数字人 _ 视频生视频-自动对口型（支持唱歌_说话）高动态_1992841755221618690.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_648

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/Infinitetalk_视频对口型-保持原视频动作一致_1979962837202276353.json、数字人/数字人/数字人-视频对口型-完美复刻动作，保持原视频动作一致_1988076238738796546.json、视频生成/图生视频/InfiniteTalk数字人 _ 视频生视频-自动对口型（支持唱歌_说话）高动态_1992841755221618690.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `VHS_LoadVideo`
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
- `Float to Int` —— 2/3 个有
- `GetImageRangeFromBatch` —— 2/3 个有
- `GetImageSizeAndCount` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `easy int` —— 2/3 个有
- `CM_FloatToInt` —— 1/3 个有
- `ImageFromBatch` —— 1/3 个有
- `Int` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `RH_GetAudioDuration` —— 1/3 个有
- `SaveAudio` —— 1/3 个有
- `SoundFlow_GetLength` —— 1/3 个有
- `Switch any [Crystools]` —— 1/3 个有
- `VHS_VideoInfo` —— 1/3 个有
- `VHS_VideoInfoSource` —— 1/3 个有
- `easy seed` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
