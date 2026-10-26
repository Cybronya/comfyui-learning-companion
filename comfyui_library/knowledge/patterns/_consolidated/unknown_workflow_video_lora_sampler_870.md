---
name: unknown_workflow_video_lora_sampler_870
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.706
common_nodes: [BlockifyMask, CLIPVisionLoader, DWPreprocessor, DrawMaskOnImage, FaceMaskFromPoseKeypoints, GetNode, GrowMask, ImageConcatMulti, ImageCropByMaskAndResize, ImageResizeKJv2, Int, LoadImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, easy sam3ModelLoader, easy sam3VideoSegmentation, easy sam3Visualization]
problems: []
missing: []
members: [视频生成/图生视频/SAM3游戏人物替换二创_2034955430325129218.json, 视频生成/图生视频/人物替换，SAM3自动分割_2046159964988776450.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_870

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/SAM3游戏人物替换二创_2034955430325129218.json、视频生成/图生视频/人物替换，SAM3自动分割_2046159964988776450.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `GrowMask`
- `ImageConcatMulti`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `SetNode`
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
- `easy cleanGpuUsed`
- `easy sam3ModelLoader`
- `easy sam3VideoSegmentation`
- `easy sam3Visualization`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `PixelPerfectResolution` —— 1/2 个有
- `PointsEditor` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `TT_img_enc_v2` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有
- `VHS_VideoInfoLoaded` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有
- `easy framesEditor` —— 1/2 个有
- `easy sam3GetObjectMask` —— 1/2 个有
- `easy sam3VideoModelExtraConfig` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
