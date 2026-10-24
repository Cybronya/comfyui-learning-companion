---
name: unknown_workflow_generic_1695
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.875
common_nodes: [LoadAudio, RunningHub_VoxCPM_Generate, RunningHub_VoxCPM_LoadModel, SaveAudioAdvanced, SaveImage]
problems: []
missing: []
members: [音频生成/音频生成/VoxCPM 语音克隆_2080098857383448577.json, 音频生成/音频生成/danotebook-voxcpm2_2066880930291212290.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1695

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/VoxCPM 语音克隆_2080098857383448577.json、音频生成/音频生成/danotebook-voxcpm2_2066880930291212290.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadAudio`
- `RunningHub_VoxCPM_Generate`
- `RunningHub_VoxCPM_LoadModel`
- `SaveAudioAdvanced`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
