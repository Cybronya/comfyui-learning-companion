---
name: unknown_workflow_generic_1984
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6835
common_nodes: [PrimitiveString, PrimitiveStringMultiline, R2T2GGUFLoader, R2T2Transcribe, RB_Code, SaveText]
problems: []
missing: []
members: [平台全量/视频语音转文字（R2T2）_2108534284754702338.json, 平台全量/音频语音转文字（R2T2）_2108519125520838657.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1984

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频语音转文字（R2T2）_2108534284754702338.json、平台全量/音频语音转文字（R2T2）_2108519125520838657.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `PrimitiveString`
- `PrimitiveStringMultiline`
- `R2T2GGUFLoader`
- `R2T2Transcribe`
- `RB_Code`
- `SaveText`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 1/2 个有
- `LoadVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
