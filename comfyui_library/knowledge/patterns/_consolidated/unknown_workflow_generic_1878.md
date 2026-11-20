---
name: unknown_workflow_generic_1878
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4675
common_nodes: [LayerUtility: ColorPicker, LayerUtility: GradientImage V2, LayerUtility: ImageBlend V2, LoadImage, PreviewImage, SaveImage]
problems: []
missing: []
members: [平台全量/30种混合模式示例 blend_mode_v2_example_1899374484913307650.json, 平台全量/█ █ █  调色大师自定义渐变映射（30种预设）_workflow  █ █ █_1895719220334755841.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1878

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/30种混合模式示例 blend_mode_v2_example_1899374484913307650.json、平台全量/█ █ █  调色大师自定义渐变映射（30种预设）_workflow  █ █ █_1895719220334755841.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：47%

## 共有节点

全部 2 个 workflow 都包含：
- `LayerUtility: ColorPicker`
- `LayerUtility: GradientImage V2`
- `LayerUtility: ImageBlend V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 1/2 个有
- `SetNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
