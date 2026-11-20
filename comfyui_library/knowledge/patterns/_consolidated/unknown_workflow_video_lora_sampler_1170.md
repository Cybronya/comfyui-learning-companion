---
name: unknown_workflow_video_lora_sampler_1170
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7825
common_nodes: [AudioCrop, CLIPVisionLoader, DownloadAndLoadWav2VecModel, FantasyTalkingModelLoader, FantasyTalkingWav2VecEmbeds, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/电商数字人 fantasy talking_1929716245694943233.json, 视频生成/图生视频/终极数字人 FantasyTalking_1933459219561500673.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1170

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/电商数字人 fantasy talking_1929716245694943233.json、视频生成/图生视频/终极数字人 FantasyTalking_1933459219561500673.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `FantasyTalkingModelLoader`
- `FantasyTalkingWav2VecEmbeds`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 1/2 个有
- `CreateCFGScheduleFloatList` —— 1/2 个有
- `Float` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LayerUtility: TextBox` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `WanVideoExperimentalArgs` —— 1/2 个有
- `WanVideoTeaCache` —— 1/2 个有
- `WanVideoVRAMManagement` —— 1/2 个有
- `easy showAnything` —— 1/2 个有
- `easy textSwitch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
