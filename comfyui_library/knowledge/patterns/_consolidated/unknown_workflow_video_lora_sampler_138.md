---
name: unknown_workflow_video_lora_sampler_138
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.94325
common_nodes: [CLIPVisionLoader, CR Text, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1952655521791819778.json, 视频生成/图生视频/1954868813227593730.json, 视频生成/图生视频/1952724785534070786.json, 视频生成/图生视频/1979755261789376514.json, 视频生成/图生视频/2026920860375851010.json, 视频生成/图生视频/1941429442441015297.json, 视频生成/图生视频/1954737241992118273.json, 视频生成/文生视频/视频数字人对口 IndexTTS V2 带情绪的声音克隆 能生成一段音频，根据不同类型音调克隆声音_1994301248816037890.json, 音频生成/音频生成/IndexTTS语音克隆+Multitalk数字人对口型_1954811221523390466.json, 音频生成/音频生成/Multitalk单人唱歌数字人_1952348321673359361.json, 音频生成/音频生成/【数字人说话】 语音克隆音频驱动对口型_1957341883464871937.json, 音频生成/音频生成/【文字转音频】IndexTTS V2 带情绪的声音克隆 能生成一段音频，根据不同类型音调克隆声音_1986588000891109378.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_138

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/1952655521791819778.json、视频生成/图生视频/1954868813227593730.json、视频生成/图生视频/1952724785534070786.json、视频生成/图生视频/1979755261789376514.json、视频生成/图生视频/2026920860375851010.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPVisionLoader`
- `CR Text`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 11/12 个有
- `WanVideoImageToVideoMultiTalk` —— 11/12 个有
- `WanVideoTorchCompileSettings` —— 11/12 个有
- `Audio Duration (mtb)` —— 9/12 个有
- `ImpactInt` —— 9/12 个有
- `IndexTTSRun` —— 8/12 个有
- `MultiLinePromptIndex` —— 8/12 个有
- `SaveAudioMP3` —— 8/12 个有
- `AudioSeparation` —— 4/12 个有
- `SaveAudio` —— 4/12 个有
- `easy showAnything` —— 4/12 个有
- `AudioCrop` —— 3/12 个有
- `Int` —— 3/12 个有
- `LayerUtility: PurgeVRAM V2` —— 3/12 个有
- `MaskPreview+` —— 3/12 个有
- `SeparateMasks` —— 3/12 个有
- `WanVideoContextOptions` —— 3/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `WanVideoImageToVideoEncode` —— 1/12 个有
- `easy convertAnything` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
