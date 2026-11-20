---
name: unknown_workflow_video_lora_sampler_397
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.942667
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, RH_GetAudioDuration, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/数字人-口播_2088243121611173889.json, 数字人/数字人/数字人_新闻_带货_口播_2059369980210270210.json, 数字人/数字人/数字人infinitetalk_1985970612617322498.json, 数字人/数字人/数字人infinitetalk_2017517708992057345.json, 数字人/数字人/数字人对口型-infinitetalk_1969380544364617729.json, 数字人/数字人/数字人项目_1986113856391053314.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_397

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/数字人-口播_2088243121611173889.json、数字人/数字人/数字人_新闻_带货_口播_2059369980210270210.json、数字人/数字人/数字人infinitetalk_1985970612617322498.json、数字人/数字人/数字人infinitetalk_2017517708992057345.json、数字人/数字人/数字人对口型-infinitetalk_1969380544364617729.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `RH_GetAudioDuration`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 5/6 个有
- `ToInt` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `Int` —— 3/6 个有
- `Float to Int` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `easy anythingIndexSwitch` —— 2/6 个有
- `Apply Whisper` —— 1/6 个有
- `ImageScale` —— 1/6 个有
- `IndexTTS2Run` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `OmniVoiceVoiceCloneTTS` —— 1/6 个有
- `OmniVoiceWhisperLoader` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `SaveAudio` —— 1/6 个有
- `SaveAudioMP3` —— 1/6 个有
- `SeedVR2` —— 1/6 个有
- `SeedVR2BlockSwap` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
