---
name: unknown_workflow_video_lora_sampler_630
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.963333
common_nodes: [CLIPVisionLoader, LoadImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/【遇见AI】wan2.1 skyreels V3 A2V数字人模型_2067528819833135106.json, 视频生成/图生视频/【遇见AI】wan2.1 Skyreels V2 图生视频，支持超过81帧_2067521044533039105.json, 视频生成/图生视频/【遇见AI】wan2.1 fantasytalking 数字人对口型_2069313439394254850.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_630

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/【遇见AI】wan2.1 skyreels V3 A2V数字人模型_2067528819833135106.json、视频生成/图生视频/【遇见AI】wan2.1 Skyreels V2 图生视频，支持超过81帧_2067521044533039105.json、视频生成/图生视频/【遇见AI】wan2.1 fantasytalking 数字人对口型_2069313439394254850.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTeaCache`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadWav2VecModel` —— 2/3 个有
- `LoadAudio` —— 2/3 个有
- `WanVideoExperimentalArgs` —— 2/3 个有
- `CreateCFGScheduleFloatList` —— 1/3 个有
- `FantasyTalkingModelLoader` —— 1/3 个有
- `FantasyTalkingWav2VecEmbeds` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `MelBandRoFormerModelLoader` —— 1/3 个有
- `MelBandRoFormerSampler` —— 1/3 个有
- `MultiTalkWav2VecEmbeds` —— 1/3 个有
- `TrimAudioDuration` —— 1/3 个有
- `WanVideoImageToVideoSkyreelsv3_audio` —— 1/3 个有
- `WanVideoPassImagesFromSamples` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
