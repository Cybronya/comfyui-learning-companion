---
name: unknown_workflow_video_lora_sampler_294
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.809286
common_nodes: [CLIPVisionLoader, CR Prompt Text, GetImageSizeAndCount, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2006714011445895170.json, 视频生成/图生视频/1967041274844995586.json, 视频生成/图生视频/1968534429834588161.json, 视频生成/图生视频/1967057695654207489.json, 视频生成/图生视频/2065824497244135425.json, 视频生成/图生视频/1980902275004678145.json, 音频生成/音频生成/Infinite Talk-对口型说话+唱歌无限时长+高动态_2021031552670507010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_294

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2006714011445895170.json、视频生成/图生视频/1967041274844995586.json、视频生成/图生视频/1968534429834588161.json、视频生成/图生视频/1967057695654207489.json、视频生成/图生视频/2065824497244135425.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `JWInteger` —— 5/7 个有
- `AudioSeparation` —— 4/7 个有
- `DownloadAndLoadWav2VecModel` —— 4/7 个有
- `LoadAudio` —— 4/7 个有
- `MultiTalkSilentEmbeds` —— 4/7 个有
- `MultiTalkWav2VecEmbeds` —— 4/7 个有
- `GetNode` —— 3/7 个有
- `PreviewAny` —— 3/7 个有
- `SetNode` —— 3/7 个有
- `SimpleMath+` —— 3/7 个有
- `AudioCrop` —— 2/7 个有
- `Display Int (rgthree)` —— 2/7 个有
- `SoundFlow_GetLength` —— 2/7 个有
- `ToInt` —— 2/7 个有
- `AddLabel` —— 1/7 个有
- `Any Switch (rgthree)` —— 1/7 个有
- `Fast Groups Muter (rgthree)` —— 1/7 个有
- `Float` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `Int` —— 1/7 个有
- `JWFloat` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `Primitive integer [Crystools]` —— 1/7 个有
- `easy int` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
