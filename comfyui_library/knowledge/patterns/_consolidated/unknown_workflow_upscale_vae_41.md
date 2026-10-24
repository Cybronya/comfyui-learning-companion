---
name: unknown_workflow_upscale_vae_41
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.886
common_nodes: [PrimitiveInt, RHBatchImages:, RHExtractImage, RHUploadZip, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, easy batchAnything, easy clearCacheAll, easy forLoopEnd, easy forLoopStart, easy imageCount]
problems: []
missing: []
members: [图片生成/图生图/批量SeedVR2图像放大_2070317807069392897.json, 图片生成/图生图/批量放大高清重绘_2013299056503693314.json, 图片生成/图生图/批量高清图像放大_2080825158469775362.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_41

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/批量SeedVR2图像放大_2070317807069392897.json、图片生成/图生图/批量放大高清重绘_2013299056503693314.json、图片生成/图生图/批量高清图像放大_2080825158469775362.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
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
- `HAIGC_SaveImagesToZip` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `AspectRatio` —— 1/3 个有
- `CompressImages` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SaveImagePlus` —— 1/3 个有
- `easy imageListToImageBatch` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
