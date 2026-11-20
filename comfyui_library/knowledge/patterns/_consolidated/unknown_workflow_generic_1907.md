---
name: unknown_workflow_generic_1907
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.845
common_nodes: [CreateVideo, GetVideoComponents, LoadVideo, RTXVideoSuperResolution, SaveVideo]
problems: []
missing: []
members: [平台全量/RTX视频放大_2068896753327370241.json, 平台全量/视频放大_2032023974367993857.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1907

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/RTX视频放大_2068896753327370241.json、平台全量/视频放大_2032023974367993857.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CreateVideo`
- `GetVideoComponents`
- `LoadVideo`
- `RTXVideoSuperResolution`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `easy indexAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
