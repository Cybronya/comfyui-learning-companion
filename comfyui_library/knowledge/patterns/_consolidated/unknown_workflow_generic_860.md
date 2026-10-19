---
name: unknown_workflow_generic_860
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.693
common_nodes: [CR Text, RH_LLMAPI_NODE, RH_Suno_Single, SaveAudio, ShellAgentPluginOutputText, ShowText|pysssss]
problems: []
missing: []
members: [音频生成/音频生成/suno音乐V5（自动歌词版）_1973000499152687105.json, 音频生成/音频生成/suno音乐V5（自动歌词）-自用留存版本_1985230387066585090.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_860

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/suno音乐V5（自动歌词版）_1973000499152687105.json、音频生成/音频生成/suno音乐V5（自动歌词）-自用留存版本_1985230387066585090.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `RH_LLMAPI_NODE`
- `RH_Suno_Single`
- `SaveAudio`
- `ShellAgentPluginOutputText`
- `ShowText|pysssss`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
