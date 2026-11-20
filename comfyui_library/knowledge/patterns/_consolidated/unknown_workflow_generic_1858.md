---
name: unknown_workflow_generic_1858
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5875
common_nodes: [CR Text, Float, Int, PrimitiveBoolean, RH_Suno_Lyrics, RunningHub ACE-Step Creator, RunningHub ACE-Step GenerationParams, RunningHub ACE-Step Loader, SaveAudioMP3, ShowText|pysssss, String, Text Multiline, easy ifElse]
problems: []
missing: []
members: [音频生成/音频生成/【短剧主题曲制作】ACE-Step1.5文生音乐（RH破音修复版）_2019467965212663810.json, 音频生成/音频生成/歌曲生成 _ ACE-Step1.5_2021444202046955521.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1858

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/【短剧主题曲制作】ACE-Step1.5文生音乐（RH破音修复版）_2019467965212663810.json、音频生成/音频生成/歌曲生成 _ ACE-Step1.5_2021444202046955521.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：59%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `Float`
- `Int`
- `PrimitiveBoolean`
- `RH_Suno_Lyrics`
- `RunningHub ACE-Step Creator`
- `RunningHub ACE-Step GenerationParams`
- `RunningHub ACE-Step Loader`
- `SaveAudioMP3`
- `ShowText|pysssss`
- `String`
- `Text Multiline`
- `easy ifElse`

**可变部分**（部分 workflow 才有）：
- `ACE_TextSelector` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `IO_input_any` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `ShellAgentPluginOutputText` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `TextListSelelct` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
