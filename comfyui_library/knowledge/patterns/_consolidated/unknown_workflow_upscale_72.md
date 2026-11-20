---
name: unknown_workflow_upscale_72
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7685
common_nodes: [Image Comparer (rgthree), ImageUpscaleWithModel, LoadImage, PreviewImage, SaveImage, UpscaleModelLoader]
problems: []
missing: []
members: [图片生成/图生图/图像分块放大_1903718815060889601.json, 平台全量/图像通过模型高清放大_1968577459551653889.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_72

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/图像分块放大_1903718815060889601.json、平台全量/图像通过模型高清放大_1968577459551653889.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UpscaleModelLoader`

**可变部分**（部分 workflow 才有）：
- `Image Tiled` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
