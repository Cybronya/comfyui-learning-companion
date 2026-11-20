---
name: unknown_workflow_controlnet_video_lora_43
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4925
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetNode, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, SimpleMath+, VHS_DuplicateImages, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2 multitalk 数字人工作流_1950489721401167873.json, 视频生成/图生视频/wanvideo_multitalk 声音驱动视频生成_1937349573826527233.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_43

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/wan2.2 multitalk 数字人工作流_1950489721401167873.json、视频生成/图生视频/wanvideo_multitalk 声音驱动视频生成_1937349573826527233.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：49%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `SimpleMath+`
- `VHS_DuplicateImages`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 1/2 个有
- `CreateCFGScheduleFloatList` —— 1/2 个有
- `Display Int (rgthree)` —— 1/2 个有
- `DownloadAndLoadFlorence2Model` —— 1/2 个有
- `FloatConstant` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `Int` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_GetAudioDuration` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `WanVideoExperimentalArgs` —— 1/2 个有
- `WanVideoTeaCache` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
