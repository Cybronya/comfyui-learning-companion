---
name: unknown_workflow_video_sampler_vae_218
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5005
common_nodes: [BlockifyMask, CR Text, DWPreprocessor, DrawMaskOnImage, FaceMaskFromPoseKeypoints, Fast Groups Bypasser (rgthree), GetNode, GrowMask, ImageCropByMaskAndResize, ImageCropper, ImageResizeKJv2, Int, JWInteger, LayerMask: SegformerB2ClothesUltra, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, LoadImage, PixelPerfectResolution, PrimitiveInt, RHHiddenNodes, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoDecode, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, workflow>WanVideo, 孤海注释]
problems: []
missing: []
members: [平台全量/高清视频换脸_换发型_自定时长_真实自然_人物动作迁移_数字人_2080189346115842050.json, 数字人/数字人/视频换脸 高清 换发型 自定时长 真实自然 人物动作迁移 数字人_2094590534886187009.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_218

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/高清视频换脸_换发型_自定时长_真实自然_人物动作迁移_数字人_2080189346115842050.json、数字人/数字人/视频换脸 高清 换发型 自定时长 真实自然 人物动作迁移 数字人_2094590534886187009.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：50%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockifyMask`
- `CR Text`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GrowMask`
- `ImageCropByMaskAndResize`
- `ImageCropper`
- `ImageResizeKJv2`
- `Int`
- `JWInteger`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `PixelPerfectResolution`
- `PrimitiveInt`
- `RHHiddenNodes`
- `SetNode`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoDecode`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `workflow>WanVideo`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
