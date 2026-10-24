---
name: unknown_workflow_video_sampler_vae_18
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.869133
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, Float to Int, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, RH_GetAudioDuration, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEasyCache, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/【数字人口播】静态图一键生成带货数字人视频_2072520035003879425.json, 视频生成/图生视频/【数字人口播】静态图一键生成带货数字人视频_2075913669199884290.json, 视频生成/图生视频/对口型 MV 唱歌音频音频驱动_2045503009345507330.json, 视频生成/图生视频/数字人口播 一键生成带货数字人视频 图生视频_2073671180170645506.json, 视频生成/图生视频/数字人口播 美妆模特 主播 静态图一键生成带货数字人视频_2074322783164788738.json, 视频生成/图生视频/数字人对口型RCM+Infinite Talk+VoxCPM TTS1.5_2020512883326586881.json, 视频生成/图生视频/数字人直播带货对口型RCM+Infinite Talk+VoxCPM TTS1.5_2027651848353615874.json, 视频生成/图生视频/无限时长（电商带货，音乐，数字人）_2054887667418050562.json, 视频生成/图生视频/电商专属--图生视频--AI数字人对口型RCM+Infinite Talk_2056187222017224706.json, 视频生成/图生视频/电商专属--图生视频--AI数字人对口型RCM+Infinite Talk_2056198886519263233.json, 视频生成/图生视频/直播带货数字人对口型RCM+Infinite Talk+VoxCPM TTS1.5_1993682109309059073.json, 视频生成/图生视频/超自然Infinite Talk+VoxCPM TTS1.5 方言克隆 直播带货数字人主播对口型_2005895609095782402.json, 视频生成/图生视频/高动态Infinite Talk+VoxCPM TTS1.5 方言克隆 直播带货数字人主播对口型_2004571944911601665.json, 视频生成/文生视频/AI演唱数字人对口型RCM+Infinite+Talk+VoxCPM+TTS1.5 (1)_2034196163921977346.json, 视频生成/文生视频/Wan2_1+infinite+数字人唱歌对口型_2064331203859279874.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_18

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/【数字人口播】静态图一键生成带货数字人视频_2072520035003879425.json、视频生成/图生视频/【数字人口播】静态图一键生成带货数字人视频_2075913669199884290.json、视频生成/图生视频/对口型 MV 唱歌音频音频驱动_2045503009345507330.json、视频生成/图生视频/数字人口播 一键生成带货数字人视频 图生视频_2073671180170645506.json、视频生成/图生视频/数字人口播 美妆模特 主播 静态图一键生成带货数字人视频_2074322783164788738.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `Float to Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `RH_GetAudioDuration`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEasyCache`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 13/15 个有
- `AudioSeparation` —— 11/15 个有
- `SoundFlow_TrimAudio` —— 11/15 个有
- `easy anythingIndexSwitch` —— 11/15 个有
- `Int` —— 10/15 个有
- `PrimitiveStringMultiline` —— 10/15 个有
- `Apply Whisper` —— 7/15 个有
- `FlashVSRNode` —— 7/15 个有
- `String Literal` —— 7/15 个有
- `VoxCPM_TTS` —— 7/15 个有
- `Fast Groups Muter (rgthree)` —— 6/15 个有
- `GetNode` —— 3/15 个有
- `SetNode` —— 3/15 个有
- `AudioCrop` —— 2/15 个有
- `PreviewAudio` —— 2/15 个有
- `RHHiddenNodes` —— 2/15 个有
- `WanVideoTorchCompileSettings` —— 2/15 个有
- `Fast Groups Bypasser (rgthree)` —— 1/15 个有
- `PrimitiveFloat` —— 1/15 个有
- `intToFloat _O` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
