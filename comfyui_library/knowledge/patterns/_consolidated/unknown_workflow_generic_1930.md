---
name: unknown_workflow_generic_1930
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8665
common_nodes: [EG_ZZ_TMTX, GrowMaskWithBlur, Int, LoadImage, PreviewImage, RMBG, SaveImage, SimpleMath+]
problems: []
missing: []
members: [平台全量/一键抠图（去白边）_1946992560956551169.json, 平台全量/指定元素抠图_1989689089844760577.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1930

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/一键抠图（去白边）_1946992560956551169.json、平台全量/指定元素抠图_1989689089844760577.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `EG_ZZ_TMTX`
- `GrowMaskWithBlur`
- `Int`
- `LoadImage`
- `PreviewImage`
- `RMBG`
- `SaveImage`
- `SimpleMath+`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `Sa2VANodeTpl` —— 1/2 个有
- `easy imageCropFromMask` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
