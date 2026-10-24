---
name: unknown_workflow_upscale_vae_52
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8
common_nodes: [HAIGC_SaveImagesToZip, ImageScaleToTotalPixels, JoinImageWithAlpha, RHUploadZip_V2, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, easy cleanGpuUsed, easy clearCacheAll, easy imageSize, easy int]
problems: []
missing: []
members: [图片生成/图生图/批量放大4K—ZIP格式上传批量出图，稳定版_2016504245368918018.json, 图片生成/文生图/批量放大4K—ZIP格式下载_2015323229090488321.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_52

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/批量放大4K—ZIP格式上传批量出图，稳定版_2016504245368918018.json、图片生成/文生图/批量放大4K—ZIP格式下载_2015323229090488321.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `HAIGC_SaveImagesToZip`
- `ImageScaleToTotalPixels`
- `JoinImageWithAlpha`
- `RHUploadZip_V2`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy imageSize`
- `easy int`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
