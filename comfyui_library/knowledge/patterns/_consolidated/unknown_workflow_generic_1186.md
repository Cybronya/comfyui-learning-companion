---
name: unknown_workflow_generic_1186
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.861
common_nodes: [LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RH_Nano_Banana_Image2Image, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/全能图片V1-单图编辑_1976916044315070466.json, 图片生成/图生图/全能图片V1单图编辑1.0_1980977373631954946.json, 平台全量/全能图片V1 双图编辑_1976655617182126081.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1186

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/全能图片V1-单图编辑_1976916044315070466.json、图片生成/图生图/全能图片V1单图编辑1.0_1980977373631954946.json、平台全量/全能图片V1 双图编辑_1976655617182126081.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RH_Nano_Banana_Image2Image`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 2/3 个有
- `easy seed` —— 2/3 个有
- `LayerUtility: ImageAutoCrop V2` —— 1/3 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `easy imageRemBg` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
