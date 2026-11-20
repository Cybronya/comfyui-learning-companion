---
name: unknown_workflow_generic_1882
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.732
common_nodes: [CreateVideo, GetVideoComponents, LoadVideo, PrimitiveInt, SaveVideo]
problems: []
missing: []
members: [平台全量/AI视频4K超分放大工作流_2099312879957794817.json, 平台全量/AI视频星光增强工作流_2099311826780643329.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1882

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/AI视频4K超分放大工作流_2099312879957794817.json、平台全量/AI视频星光增强工作流_2099311826780643329.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `CreateVideo`
- `GetVideoComponents`
- `LoadVideo`
- `PrimitiveInt`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `FlashVSRInitPipe` —— 1/2 个有
- `FlashVSRNode` —— 1/2 个有
- `FlashVSRNodeAdv` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
