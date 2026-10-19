---
name: unknown_workflow_video_lora_sampler_298
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.700143
common_nodes: [CLIPVisionLoader, CR Prompt Text, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2006714011445895170.json, 视频生成/图生视频/1967041274844995586.json, 视频生成/图生视频/1968534429834588161.json, 视频生成/图生视频/1967057695654207489.json, 视频生成/图生视频/1986427607413620737.json, 视频生成/图生视频/2008032708106133505.json, 视频生成/图生视频/1979836579130806274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_298

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2006714011445895170.json、视频生成/图生视频/1967041274844995586.json、视频生成/图生视频/1968534429834588161.json、视频生成/图生视频/1967057695654207489.json、视频生成/图生视频/1986427607413620737.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `CR Prompt Text`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `JWInteger` —— 6/7 个有
- `AudioSeparation` —— 4/7 个有
- `DownloadAndLoadWav2VecModel` —— 4/7 个有
- `GetNode` —— 4/7 个有
- `LoadAudio` —— 4/7 个有
- `MultiTalkSilentEmbeds` —— 4/7 个有
- `MultiTalkWav2VecEmbeds` —— 4/7 个有
- `SetNode` —— 4/7 个有
- `SimpleMath+` —— 4/7 个有
- `AudioCrop` —— 3/7 个有
- `GetAudioDurationFromAudio` —— 3/7 个有
- `PreviewAny` —— 3/7 个有
- `easy cleanGpuUsed` —— 3/7 个有
- `easy showAnything` —— 3/7 个有
- `MelBandRoFormerModelLoader` —— 2/7 个有
- `MelBandRoFormerSampler` —— 2/7 个有
- `PreviewAudio` —— 2/7 个有
- `SoundFlow_TrimAudio` —— 2/7 个有
- `easy clearCacheAll` —— 2/7 个有
- `Any Switch (rgthree)` —— 1/7 个有
- `Fast Groups Muter (rgthree)` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `Primitive integer [Crystools]` —— 1/7 个有
- `RIFE VFI` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
