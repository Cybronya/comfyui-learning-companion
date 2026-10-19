---
name: unknown_workflow_video_lora_sampler_899
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.921
common_nodes: [CLIPVisionLoader, DWPreprocessor, Image Crop Face, ImageResizeKJv2, Int, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PixelPerfectResolution, PreviewImage, SimpleMath+, Text, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2014597791112237058.json, 视频生成/图生视频/2014700203747581954.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_899

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2014597791112237058.json、视频生成/图生视频/2014700203747581954.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `Image Crop Face`
- `ImageResizeKJv2`
- `Int`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PixelPerfectResolution`
- `PreviewImage`
- `SimpleMath+`
- `Text`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BatchThief` —— 1/2 个有
- `BlockifyMask` —— 1/2 个有
- `DrawMaskOnImage` —— 1/2 个有
- `LayerMask: MaskPreview` —— 1/2 个有
- `PointsEditor` —— 1/2 个有
- `RH_Nano_Banana2_Image2Image` —— 1/2 个有
- `RMBG` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `easy sam3ModelLoader` —— 1/2 个有
- `easy sam3VideoSegmentation` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
