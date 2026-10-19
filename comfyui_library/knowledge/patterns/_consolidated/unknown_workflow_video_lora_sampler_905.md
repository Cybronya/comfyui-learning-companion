---
name: unknown_workflow_video_lora_sampler_905
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPVisionLoader, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, JWInteger, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoMagCache, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1914138516001910786.json, 视频生成/图生视频/1935149925716172801.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_905

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1914138516001910786.json、视频生成/图生视频/1935149925716172801.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `JWInteger`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoMagCache`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `RH_OneShot_Prompter` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `VHS_VideoInfoLoaded` —— 1/2 个有
- `WanVideoApplyNAG` —— 1/2 个有
- `WanVideoTextEncode` —— 1/2 个有
- `WanVideoTextEncodeSingle` —— 1/2 个有
- `WanVideoUniAnimateDWPoseDetector` —— 1/2 个有
- `WanVideoUniAnimatePoseInput` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
