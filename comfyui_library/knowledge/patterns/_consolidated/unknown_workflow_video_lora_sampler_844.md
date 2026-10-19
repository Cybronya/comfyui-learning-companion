---
name: unknown_workflow_video_lora_sampler_844
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.52
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, CreateCFGScheduleFloatList, DF_Int_to_Float, DownloadAndLoadWav2VecModel, GetNode, INTConstant, JWImageResize, LayerUtility: ImageScaleByAspectRatio, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, PreviewAudio, PreviewImage, RH_GetAudioDuration, SetNode, ShowAnything|Mie, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoExtraModelSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2044768518683500546.json, 视频生成/图生视频/2045415712142925826.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_844

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2044768518683500546.json、视频生成/图生视频/2045415712142925826.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：52%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `CreateCFGScheduleFloatList`
- `DF_Int_to_Float`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `INTConstant`
- `JWImageResize`
- `LayerUtility: ImageScaleByAspectRatio`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewAudio`
- `PreviewImage`
- `RH_GetAudioDuration`
- `SetNode`
- `ShowAnything|Mie`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `FantasyTalkingModelLoader` —— 1/2 个有
- `FantasyTalkingWav2VecEmbeds` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `MultiTalkModelLoader` —— 1/2 个有
- `MultiTalkWav2VecEmbeds` —— 1/2 个有
- `VHS_DuplicateImages` —— 1/2 个有
- `WanVideoEncode` —— 1/2 个有
- `WanVideoExperimentalArgs` —— 1/2 个有
- `WanVideoImageToVideoEncode` —— 1/2 个有
- `WanVideoImageToVideoMultiTalk` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/2 个有
- `WanVideoUni3C_embeds` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
