---
name: unknown_workflow_upscale_vae_48
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.875
common_nodes: [PrimitiveInt, RHBatchImages:, RHExtractImage, RHUploadZip, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, easy batchAnything, easy clearCacheAll, easy forLoopEnd, easy forLoopStart, easy imageCount]
problems: []
missing: []
members: [图片生成/图生图/批量SeedVR2图像放大_2070317807069392897.json, 图片生成/图生图/批量放大高清重绘_2013299056503693314.json, 图片生成/图生图/批量高清图像放大_2080825158469775362.json, 平台全量/批量放大高清重绘！_2006336339943366658.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_48

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/批量SeedVR2图像放大_2070317807069392897.json、图片生成/图生图/批量放大高清重绘_2013299056503693314.json、图片生成/图生图/批量高清图像放大_2080825158469775362.json、平台全量/批量放大高清重绘！_2006336339943366658.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `PrimitiveInt`
- `RHBatchImages:`
- `RHExtractImage`
- `RHUploadZip`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `easy batchAnything`
- `easy clearCacheAll`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`

**可变部分**（部分 workflow 才有）：
- `AspectRatio` —— 2/4 个有
- `CompressImages` —— 2/4 个有
- `HAIGC_SaveImagesToZip` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `SaveImagePlus` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `easy imageListToImageBatch` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
