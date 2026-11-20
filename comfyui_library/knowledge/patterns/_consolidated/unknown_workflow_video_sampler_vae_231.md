---
name: unknown_workflow_video_sampler_vae_231
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8095
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: TextBox, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoApplyNAG, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/多图参考视频 MAGREF_1935321450800939010.json, 视频生成/图生视频/大融合图生视频 FusionX I2V_1934261735870390274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_231

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/多图参考视频 MAGREF_1935321450800939010.json、视频生成/图生视频/大融合图生视频 FusionX I2V_1934261735870390274.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: TextBox`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 1/2 个有
- `GIMMVFI_interpolate` —— 1/2 个有
- `GetImageSize+` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `LayerUtility: CropByMask V3` —— 1/2 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `WanVideoBlockSwap` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `WanVideoVRAMManagement` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
