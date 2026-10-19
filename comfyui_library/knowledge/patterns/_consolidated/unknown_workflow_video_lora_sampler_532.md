---
name: unknown_workflow_video_lora_sampler_532
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.97175
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, LoadImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2069313439394254850.json, 视频生成/图生视频/2062116414055608321.json, 视频生成/图生视频/2061019045620699138.json, 视频生成/图生视频/2062101371284975617.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_532

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2069313439394254850.json、视频生成/图生视频/2062116414055608321.json、视频生成/图生视频/2061019045620699138.json、视频生成/图生视频/2062101371284975617.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
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
- `WanVideoExperimentalArgs` —— 3/4 个有
- `WanVideoVRAMManagement` —— 2/4 个有
- `CreateCFGScheduleFloatList` —— 1/4 个有
- `DownloadAndLoadWav2VecModel` —— 1/4 个有
- `FantasyTalkingModelLoader` —— 1/4 个有
- `FantasyTalkingWav2VecEmbeds` —— 1/4 个有
- `LoadAudio` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
