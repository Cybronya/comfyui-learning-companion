---
name: unknown_workflow_sampler_17
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.963
common_nodes: [GetImageSizeAndCount, ImageConcanate, ImageResizeKJv2, ImageScaleDownToSize, LoadImage, RunningHubUniWorldSampler, RunningUniworldModelLoader, SaveImage]
problems: []
missing: [Text Multiline, CR SDXL Aspect Ratio]
members: [图片生成/文生图/1931570428488429570.json, 图片生成/文生图/1931579845157781506.json, 图片生成/文生图/1935641351222657025.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_17

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1931570428488429570.json、图片生成/文生图/1931579845157781506.json、图片生成/文生图/1935641351222657025.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `GetImageSizeAndCount`
- `ImageConcanate`
- `ImageResizeKJv2`
- `ImageScaleDownToSize`
- `LoadImage`
- `RunningHubUniWorldSampler`
- `RunningUniworldModelLoader`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `RH_Translator` —— 2/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `DDColor_Colorize` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Text Multiline` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline、CR SDXL Aspect Ratio
