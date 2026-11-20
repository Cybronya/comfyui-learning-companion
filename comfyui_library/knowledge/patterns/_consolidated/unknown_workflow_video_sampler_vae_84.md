---
name: unknown_workflow_video_sampler_vae_84
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.887143
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/InfiniteTalk单人版数字人【超过1分钟的】_2003019304549380098.json, 数字人/数字人/InfiniteTalk对口型工作流 V1.0_2052269912881676289.json, 数字人/数字人/Infinitetalk单人数字人无限时长自循环_2088948708812611585.json, 数字人/数字人/Infinitetalk单人数字人无限时长自循环_2108715715753766913.json, 数字人/数字人/LLM+InfiniteTalk+IndexTTS_1962434815804968962.json, 数字人/数字人/LLM+MultiTalk+IndexTTS数字人_1942407637285679105.json, 视频生成/图生视频/InfiniteTalk & LatentSync 对口型工作流 V1.0_2028880263652052993.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_84

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/InfiniteTalk单人版数字人【超过1分钟的】_2003019304549380098.json、数字人/数字人/InfiniteTalk对口型工作流 V1.0_2052269912881676289.json、数字人/数字人/Infinitetalk单人数字人无限时长自循环_2088948708812611585.json、数字人/数字人/Infinitetalk单人数字人无限时长自循环_2108715715753766913.json、数字人/数字人/LLM+InfiniteTalk+IndexTTS_1962434815804968962.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `MultiTalkModelLoader` —— 6/7 个有
- `SimpleMath+` —— 6/7 个有
- `ToInt` —— 6/7 个有
- `WanVideoImageToVideoMultiTalk` —— 6/7 个有
- `WanVideoModelLoader` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `easy showAnything` —— 6/7 个有
- `RH_GetAudioDuration` —— 5/7 个有
- `Int` —— 4/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/7 个有
- `PreviewAudio` —— 4/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `WanVideoLoraSelect` —— 4/7 个有
- `ImageResizeKJv2` —— 3/7 个有
- `IndexTTSRun` —— 2/7 个有
- `LLMLoader` —— 2/7 个有
- `LLMSampler` —— 2/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `PrimitiveFloat` —— 2/7 个有
- `ShowText` —— 2/7 个有
- `WanVideoLoraSelectMulti` —— 2/7 个有
- `Audio Duration (mtb)` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `LatentSyncNode` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `String Literal` —— 1/7 个有
- `ToFloat` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有
- `VideoLengthAdjuster` —— 1/7 个有
- `WanVideoImageToVideoEncode` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
