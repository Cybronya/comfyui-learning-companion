---
name: unknown_workflow_generic_1242
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.85
common_nodes: [LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/文生图/CN预处理图像生成_2012106453284298753.json, 平台全量/一键出人物骨骼图_1919015748952592386.json, 平台全量/人物姿态骨骼图生成_2046890293072498689.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1242

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/CN预处理图像生成_2012106453284298753.json、平台全量/一键出人物骨骼图_1919015748952592386.json、平台全量/人物姿态骨骼图生成_2046890293072498689.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `DWPreprocessor` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
