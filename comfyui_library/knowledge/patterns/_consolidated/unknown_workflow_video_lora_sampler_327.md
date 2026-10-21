---
name: unknown_workflow_video_lora_sampler_327
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.717
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2008048511492825090.json, 视频生成/图生视频/1978136142623203329.json, 视频生成/图生视频/乔帮主-对口型数字人 最强音色克隆带语气情感 音频生成 数字人 声音克隆  情绪参考   Infinite+_2086424507589423105.json, 视频生成/图生视频/1986427607413620737.json, 视频生成/图生视频/2002936132511907841.json, 视频生成/图生视频/2008032708106133505.json, 视频生成/图生视频/1979836579130806274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_327

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2008048511492825090.json、视频生成/图生视频/1978136142623203329.json、视频生成/图生视频/乔帮主-对口型数字人 最强音色克隆带语气情感 音频生成 数字人 声音克隆  情绪参考   Infinite+_2086424507589423105.json、视频生成/图生视频/1986427607413620737.json、视频生成/图生视频/2002936132511907841.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 6/7 个有
- `LoadWanVideoT5TextEncoder` —— 6/7 个有
- `PreviewAny` —— 6/7 个有
- `WanVideoBlockSwap` —— 6/7 个有
- `WanVideoTextEncode` —— 6/7 个有
- `easy showAnything` —— 6/7 个有
- `GetNode` —— 4/7 个有
- `SetNode` —— 4/7 个有
- `SimpleMath+` —— 4/7 个有
- `GetAudioDurationFromAudio` —— 3/7 个有
- `easy cleanGpuUsed` —— 3/7 个有
- `AudioToFPS` —— 2/7 个有
- `JWFloat` —— 2/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `MelBandRoFormerModelLoader` —— 2/7 个有
- `MelBandRoFormerSampler` —— 2/7 个有
- `PreviewAudio` —— 2/7 个有
- `SoundFlow_TrimAudio` —— 2/7 个有
- `easy clearCacheAll` —— 2/7 个有
- `Int` —— 1/7 个有
- `RIFE VFI` —— 1/7 个有
- `WanVideoTextEncodeCached` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
