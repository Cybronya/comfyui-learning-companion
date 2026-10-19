---
name: unknown_workflow_video_lora_sampler_61
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.834
common_nodes: [CLIPVisionLoader, CR Prompt Text, GetImageSizeAndCount, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1970454402555408386.json, 视频生成/图生视频/2004160279342686209.json, 视频生成/图生视频/2029081632229036033.json, 视频生成/图生视频/2065824497244135425.json, 视频生成/图生视频/2044411398406545409.json, 视频生成/图生视频/1988898686707044353.json, 视频生成/图生视频/2026900959795879938.json, 视频生成/图生视频/2028672160373415937.json, 视频生成/图生视频/1960048260402589698.json, 视频生成/图生视频/2029971317079937026.json, 视频生成/图生视频/1984094280551694338.json, 视频生成/图生视频/1960792886629601281.json, 视频生成/图生视频/2025798781039546370.json, 视频生成/图生视频/2041353094105141250.json, 视频生成/图生视频/2026920632201515010.json, 视频生成/图生视频/1971615313714475009.json, 视频生成/图生视频/1961304716842045442.json, 视频生成/图生视频/1963526777896521730.json, 音频生成/音频生成/(歌曲数字人)全流程精准口型高强动作V4_1989287142675369986.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_61

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/1970454402555408386.json、视频生成/图生视频/2004160279342686209.json、视频生成/图生视频/2029081632229036033.json、视频生成/图生视频/2065824497244135425.json、视频生成/图生视频/2044411398406545409.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPVisionLoader`
- `CR Prompt Text`
- `GetImageSizeAndCount`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
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
- `AudioSeparation` —— 18/19 个有
- `DownloadAndLoadWav2VecModel` —— 18/19 个有
- `JWInteger` —— 18/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 18/19 个有
- `LoadAudio` —— 18/19 个有
- `MultiTalkWav2VecEmbeds` —— 18/19 个有
- `PreviewAny` —— 17/19 个有
- `AudioCrop` —— 16/19 个有
- `Int` —— 5/19 个有
- `JWFloat` —— 5/19 个有
- `SimpleMath+` —— 4/19 个有
- `Label (rgthree)` —— 3/19 个有
- `RH_GetAudioDuration` —— 3/19 个有
- `ToInt` —— 3/19 个有
- `easy showAnything` —— 3/19 个有
- `AddLabel` —— 1/19 个有
- `Comfly_api_set` —— 1/19 个有
- `Comfly_suno_custom` —— 1/19 个有
- `ConcatTextOfUtils` —— 1/19 个有
- `Fast Groups Bypasser (rgthree)` —— 1/19 个有
- `MathExpression|pysssss` —— 1/19 个有
- `MultiTalkSilentEmbeds` —— 1/19 个有
- `RHHiddenNodes` —— 1/19 个有
- `SaveAudio` —— 1/19 个有
- `TextToUppercase` —— 1/19 个有
- `VRGDG_AudioCropTime` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
