---
name: unknown_workflow_video_sampler_vae_185
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.696
common_nodes: [BlockifyMask, CLIPVisionLoader, DWPreprocessor, DrawMaskOnImage, FaceMaskFromPoseKeypoints, GetImageSizeAndCount, GetNode, GrowMaskWithBlur, ImageConcatMulti, ImageCropByMaskAndResize, ImageResizeKJv2, LayerUtility: PurgeVRAM V2, LoadImage, PixelPerfectResolution, PointsEditor, PreviewImage, Primitive integer [Crystools], RHHiddenNodes, RH_Captioner, RMBG, SetNode, ShowText|pysssss, SimpleMath+, Text Concatenate, Text Multiline, UnloadModel, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2064955834492342273.json, 视频生成/图生视频/2043943018939551745.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_185

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2064955834492342273.json、视频生成/图生视频/2043943018939551745.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageConcatMulti`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `PixelPerfectResolution`
- `PointsEditor`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `RHHiddenNodes`
- `RH_Captioner`
- `RMBG`
- `SetNode`
- `ShowText|pysssss`
- `SimpleMath+`
- `Text Concatenate`
- `Text Multiline`
- `UnloadModel`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `SeCModelLoader` —— 1/2 个有
- `SeCVideoSegmentation` —— 1/2 个有
- `WanVideoEnhanceAVideo` —— 1/2 个有
- `WanVideoSLG` —— 1/2 个有
- `WanVideoSetLoRAs` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
