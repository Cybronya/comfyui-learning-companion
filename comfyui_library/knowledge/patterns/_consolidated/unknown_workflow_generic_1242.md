---
name: unknown_workflow_generic_1242
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.909
common_nodes: [InstantCharacterGenerate, InstantCharacterLoadModel, LoadImage, RH_LLMAPI_NODE, RunningHub_Omini_Subject, SaveImage, TextBox, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/InstantCharacter VS OminiControl_1914521770274058242.json, 图片生成/图生图/角色一致性InstantCharacter+VS+OminiControl_1914668086782324737.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1242

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/InstantCharacter VS OminiControl_1914521770274058242.json、图片生成/图生图/角色一致性InstantCharacter+VS+OminiControl_1914668086782324737.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `InstantCharacterGenerate`
- `InstantCharacterLoadModel`
- `LoadImage`
- `RH_LLMAPI_NODE`
- `RunningHub_Omini_Subject`
- `SaveImage`
- `TextBox`
- `easy cleanGpuUsed`
- `easy showAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
