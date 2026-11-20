---
name: unknown_workflow_generic_1117
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.936333
common_nodes: [BRIA_RMBG_ModelLoader_Zho, BRIA_RMBG_Zho, ImageGenResolutionFromImage, LayerUtility: ColorImage, LayerUtility: ColorPicker, LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/BRIA RMBG一键抠图_抠像_去背景-透明背景_2020007942497509377.json, 图片生成/图生图/BRIA抠像_2052677009523912705.json, 平台全量/移除背景任意填充颜色_1900032331359334401.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1117

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/BRIA RMBG一键抠图_抠像_去背景-透明背景_2020007942497509377.json、图片生成/图生图/BRIA抠像_2052677009523912705.json、平台全量/移除背景任意填充颜色_1900032331359334401.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `BRIA_RMBG_ModelLoader_Zho`
- `BRIA_RMBG_Zho`
- `ImageGenResolutionFromImage`
- `LayerUtility: ColorImage`
- `LayerUtility: ColorPicker`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `Image Overlay` —— 2/3 个有
- `InvertMask` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Label (rgthree)` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
