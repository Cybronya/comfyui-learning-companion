---
name: unknown_workflow_video_lora_sampler_535
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.786667
common_nodes: [AudioSeparation, CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/【推荐，图片声音对口型（说话唱歌）】（单人版）Infinite Talk超自然无限长度图生视频数字人V3_2008048511492825090.json, 视频生成/图生视频/一键生成最长3500帧万相2.1图生视频（可对口型）_1967057695654207489.json, 视频生成/图生视频/不限时长生成 【Infinite Talk 支持多角度数字人完美口型 】_1978136142623203329.json, 视频生成/图生视频/乔帮主-对口型数字人 最强音色克隆带语气情感 音频生成 数字人 声音克隆  情绪参考   Infinite+_2086424507589423105.json, 视频生成/图生视频/人声分离精准识别-生成mv-高质量数字人Infinite Talk极速版_1986427607413620737.json, 视频生成/图生视频/数字人-音频驱动_2008032708106133505.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_535

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/【推荐，图片声音对口型（说话唱歌）】（单人版）Infinite Talk超自然无限长度图生视频数字人V3_2008048511492825090.json、视频生成/图生视频/一键生成最长3500帧万相2.1图生视频（可对口型）_1967057695654207489.json、视频生成/图生视频/不限时长生成 【Infinite Talk 支持多角度数字人完美口型 】_1978136142623203329.json、视频生成/图生视频/乔帮主-对口型数字人 最强音色克隆带语气情感 音频生成 数字人 声音克隆  情绪参考   Infinite+_2086424507589423105.json、视频生成/图生视频/人声分离精准识别-生成mv-高质量数字人Infinite Talk极速版_1986427607413620737.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 6 个 workflow 都包含：
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
- `AudioCrop` —— 5/6 个有
- `GetImageSizeAndCount` —— 5/6 个有
- `LoadWanVideoT5TextEncoder` —— 5/6 个有
- `WanVideoBlockSwap` —— 5/6 个有
- `WanVideoTextEncode` —— 5/6 个有
- `PreviewAny` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `SimpleMath+` —— 3/6 个有
- `GetAudioDurationFromAudio` —— 2/6 个有
- `GetNode` —— 2/6 个有
- `LayerUtility: PurgeVRAM V2` —— 2/6 个有
- `MelBandRoFormerModelLoader` —— 2/6 个有
- `MelBandRoFormerSampler` —— 2/6 个有
- `PreviewAudio` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `SoundFlow_TrimAudio` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `easy clearCacheAll` —— 2/6 个有
- `Any Switch (rgthree)` —— 1/6 个有
- `AudioToFPS` —— 1/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有
- `Int` —— 1/6 个有
- `JWFloat` —— 1/6 个有
- `MultiTalkSilentEmbeds` —— 1/6 个有
- `RIFE VFI` —— 1/6 个有
- `WanVideoTextEncodeCached` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
