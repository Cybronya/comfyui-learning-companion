---
name: unknown_workflow_upscale_37
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 1
common_nodes: [ImageUpscaleWithModel, LoadImage, SaveImage, UpscaleModelLoader]
problems: []
missing: []
members: [平台全量/图片4倍放大+九宫格4X放大切片（9张）_2033118961411301378.json, 平台全量/图片放大像素增强_2044590969957388290.json, 平台全量/尺寸放大器_1826534435230543873.json, 平台全量/空间效果图快速放大｜默认4K_2118595861491048450.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_37

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/图片4倍放大+九宫格4X放大切片（9张）_2033118961411301378.json、平台全量/图片放大像素增强_2044590969957388290.json、平台全量/尺寸放大器_1826534435230543873.json、平台全量/空间效果图快速放大｜默认4K_2118595861491048450.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `ImageUpscaleWithModel`
- `LoadImage`
- `SaveImage`
- `UpscaleModelLoader`

**可变部分**（部分 workflow 才有）：
- `1hew_ImageGridSplit` —— 1/4 个有
- `ImageScaleToMaxDimension` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
