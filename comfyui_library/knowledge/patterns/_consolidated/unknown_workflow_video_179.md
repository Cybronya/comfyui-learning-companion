---
name: unknown_workflow_video_179
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.84
common_nodes: [GetImageSize+, Image Transpose, ImageResizeKJ, ImpactImageBatchToImageList, InspyrenetRembg, LoadImage, MaskToImage, PreviewImage, SaveImage, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/【AI小王子】22.视频去背景 批量抠图换背景教学工作流_2046852026700668929.json, 平台全量/视频去背景 批量抠图换背景教学工作流可以本地批量抠图_1971408264837709825.json]
source: knowledge_consolidation
---

# unknown_workflow_video_179

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【AI小王子】22.视频去背景 批量抠图换背景教学工作流_2046852026700668929.json、平台全量/视频去背景 批量抠图换背景教学工作流可以本地批量抠图_1971408264837709825.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `GetImageSize+`
- `Image Transpose`
- `ImageResizeKJ`
- `ImpactImageBatchToImageList`
- `InspyrenetRembg`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BiRefNet_Hugo` —— 1/2 个有
- `LoadImageFromPath` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `RHBatchImages:` —— 1/2 个有
- `RHUploadZip` —— 1/2 个有
- `VHS_LoadImagesPath` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
