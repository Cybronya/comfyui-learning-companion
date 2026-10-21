---
name: unknown_workflow_video_lora_sampler_217
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.924
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEasyCache, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1948391193374797826.json, 视频生成/图生视频/2072520035003879425.json, 视频生成/图生视频/2075913669199884290.json, 视频生成/图生视频/2073671180170645506.json, 视频生成/图生视频/2074322783164788738.json, 视频生成/图生视频/2054887667418050562.json, 视频生成/图生视频/2056187222017224706.json, 视频生成/图生视频/2056198886519263233.json, 视频生成/文生视频/AI演唱数字人对口型RCM+Infinite+Talk+VoxCPM+TTS1.5 (1)_2034196163921977346.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_217

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1948391193374797826.json、视频生成/图生视频/2072520035003879425.json、视频生成/图生视频/2075913669199884290.json、视频生成/图生视频/2073671180170645506.json、视频生成/图生视频/2074322783164788738.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEasyCache`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Float to Int` —— 8/9 个有
- `RH_GetAudioDuration` —— 8/9 个有
- `WanVideoImageToVideoMultiTalk` —— 8/9 个有
- `WanVideoTextEncodeCached` —— 8/9 个有
- `AudioSeparation` —— 5/9 个有
- `Int` —— 5/9 个有
- `easy anythingIndexSwitch` —— 5/9 个有
- `PrimitiveStringMultiline` —— 4/9 个有
- `SoundFlow_TrimAudio` —— 4/9 个有
- `Fast Groups Muter (rgthree)` —— 3/9 个有
- `FlashVSRNode` —— 3/9 个有
- `String Literal` —— 2/9 个有
- `Apply Whisper` —— 1/9 个有
- `GetNode` —— 1/9 个有
- `IndexTTSRun` —— 1/9 个有
- `LoadWanVideoT5TextEncoder` —— 1/9 个有
- `SetNode` —— 1/9 个有
- `VoxCPM_TTS` —— 1/9 个有
- `WanVideoFreeInitArgs` —— 1/9 个有
- `WanVideoImageToVideoEncode` —— 1/9 个有
- `WanVideoSetRadialAttention` —— 1/9 个有
- `WanVideoTextEncode` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
