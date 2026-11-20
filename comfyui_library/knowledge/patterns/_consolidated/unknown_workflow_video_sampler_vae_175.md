---
name: unknown_workflow_video_sampler_vae_175
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.908
common_nodes: [Any Switch (rgthree), BboxDetectorCombined_v2, Fast Groups Bypasser (rgthree), GrowMaskWithBlur, ImageCompositeMasked, ImageListToBatch+, ImageToMask, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, MaskToImage, SolidMask, UltralyticsDetectorProvider, VHS_LoadVideo, VHS_VideoInfo, WanVideoDecode, WanVideoEncode, WanVideoMiniMaxRemoverEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/反推提示词/57shipinqushuiyin_2051294749801361410.json, 数字人/数字人/视频水印去除即梦 、可灵、豆包、全能视频V3 通用版（楚门的ai世界）11111111111_1990403314384867330.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_175

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/57shipinqushuiyin_2051294749801361410.json、数字人/数字人/视频水印去除即梦 、可灵、豆包、全能视频V3 通用版（楚门的ai世界）11111111111_1990403314384867330.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BboxDetectorCombined_v2`
- `Fast Groups Bypasser (rgthree)`
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `ImageListToBatch+`
- `ImageToMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `MaskToImage`
- `SolidMask`
- `UltralyticsDetectorProvider`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoMiniMaxRemoverEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 1/2 个有
- `DiffuEraserLoader` —— 1/2 个有
- `DiffuEraserSampler` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `PreviewBridge` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `VHS_DuplicateMasks` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
