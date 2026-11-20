---
name: unknown_workflow_generic_1843
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.667
common_nodes: [LoadAudio, PrimitiveStringMultiline, RunningHub_VoxCPM_LoadModel, SaveAudio]
problems: []
missing: []
members: [音频生成/音频生成/VoxCPM2 语音克隆_2056949209022164994.json, 音频生成/音频生成/VoxCPM2语音克隆_2065345286356164609.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1843

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/VoxCPM2 语音克隆_2056949209022164994.json、音频生成/音频生成/VoxCPM2语音克隆_2065345286356164609.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadAudio`
- `PrimitiveStringMultiline`
- `RunningHub_VoxCPM_LoadModel`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `RunningHub_VoxCPM_Generate` —— 1/2 个有
- `RunningHub_VoxCPM_MultiSpeaker_ListReference` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
