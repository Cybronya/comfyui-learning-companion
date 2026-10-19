---
name: unknown_workflow_controlnet_video_upscale_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.548
common_nodes: [AIO_Preprocessor, CR Upscale Image, DWPreprocessor, DownloadAndLoadWav2VecModel, GetNode, ImageResizeKJ, ImageSmartSharpen+, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, MultiTalkWav2VecEmbeds, MyOpenPoseNode, OpenposePreprocessor, PreviewImage, ReActorFaceSwap, ReActorRestoreFace, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEasyCache, WanVideoEncode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoFreeInitArgs, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoRealisDanceLatents, WanVideoSLG, WanVideoSampler, WanVideoSetRadialAttention, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoUniAnimatePoseInput, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1947729409547583489.json, 视频生成/图生视频/1933449210870308865.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_upscale_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1947729409547583489.json、视频生成/图生视频/1933449210870308865.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：55%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CR Upscale Image`
- `DWPreprocessor`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `ImageResizeKJ`
- `ImageSmartSharpen+`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkWav2VecEmbeds`
- `MyOpenPoseNode`
- `OpenposePreprocessor`
- `PreviewImage`
- `ReActorFaceSwap`
- `ReActorRestoreFace`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEasyCache`
- `WanVideoEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoFreeInitArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoRealisDanceLatents`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetRadialAttention`
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoUniAnimatePoseInput`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Manual XY Entry Info` —— 1/2 个有
- `RIFE VFI` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy imageListToImageBatch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
