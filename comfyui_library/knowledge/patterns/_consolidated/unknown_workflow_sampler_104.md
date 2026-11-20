---
name: unknown_workflow_sampler_104
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.949
common_nodes: [ImageConcanate, ImageResize+, LoadImage, RunningHub_UNO_Loadmodel, RunningHub_UNO_Sampler, SaveImage]
problems: []
missing: []
members: [图片生成/文生图/UNO多图结合_1912493797195087874.json, 平台全量/【大炮精选】4o平替 UNO多图参考一致性方案_1910951991957487618.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_104

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/UNO多图结合_1912493797195087874.json、平台全量/【大炮精选】4o平替 UNO多图参考一致性方案_1910951991957487618.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageConcanate`
- `ImageResize+`
- `LoadImage`
- `RunningHub_UNO_Loadmodel`
- `RunningHub_UNO_Sampler`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `Note Plus (mtb)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
