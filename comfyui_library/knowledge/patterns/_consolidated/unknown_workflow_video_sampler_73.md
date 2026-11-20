---
name: unknown_workflow_video_sampler_73
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7415
common_nodes: [DiffuEraserLoader, DiffuEraserSampler, FlashVSRInitPipe, FlashVSRNodeAdv, Image Flip, ImageConcanate, ImageResizeKJv2, ImageToMask, JWInteger, LayerColor: Brightness & Contrast, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskFlip+, MaskToImage, PreviewImage, RepeatImageBatch, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoExtraModelSelect, easy showAnything]
problems: []
missing: []
members: [平台全量/去水印_2025145341003177986.json, 视频生成/图生视频/小云雀去水印横屏_2107266964589735937.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_73

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/去水印_2025145341003177986.json、视频生成/图生视频/小云雀去水印横屏_2107266964589735937.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `DiffuEraserLoader`
- `DiffuEraserSampler`
- `FlashVSRInitPipe`
- `FlashVSRNodeAdv`
- `Image Flip`
- `ImageConcanate`
- `ImageResizeKJv2`
- `ImageToMask`
- `JWInteger`
- `LayerColor: Brightness & Contrast`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskFlip+`
- `MaskToImage`
- `PreviewImage`
- `RepeatImageBatch`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoExtraModelSelect`
- `easy showAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
