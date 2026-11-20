---
name: unknown_workflow_upscale_vae_49
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.88075
common_nodes: [ImageScaleToTotalPixels, JoinImageWithAlpha, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, easy cleanGpuUsed, easy clearCacheAll, easy imageSize, easy int]
problems: []
missing: []
members: [图片生成/图生图/批量放大4K—ZIP格式上传批量出图，稳定版_2016504245368918018.json, 图片生成/文生图/批量放大4K—ZIP格式下载_2015323229090488321.json, 平台全量/图像超清8张图画布_2015044793159655425.json, 视频生成/文生视频/5.1 工具：拆图+放大_2031785449819217921.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_49

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/批量放大4K—ZIP格式上传批量出图，稳定版_2016504245368918018.json、图片生成/文生图/批量放大4K—ZIP格式下载_2015323229090488321.json、平台全量/图像超清8张图画布_2015044793159655425.json、视频生成/文生视频/5.1 工具：拆图+放大_2031785449819217921.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `ImageScaleToTotalPixels`
- `JoinImageWithAlpha`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy imageSize`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `HAIGC_SaveImagesToZip` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `RHUploadZip_V2` —— 2/4 个有
- `ImageFromBatch+` —— 1/4 个有
- `ImageTile+` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
