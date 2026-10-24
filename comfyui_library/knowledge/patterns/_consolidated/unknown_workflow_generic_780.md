---
name: unknown_workflow_generic_780
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.80875
common_nodes: [Bjornulf_IfElse, CR Text, ImpactSwitch, LazySwitch1way, LoadAudio, PreviewAny, RH_LLMAPI_NODE, RunningHub_VoxCPM_LoadModel, SaveAudio, easy boolean, easy int, ttN concat]
problems: []
missing: []
members: [音频生成/音频生成/-声音克隆_语音设计-多人-VoxCPM2【small-JJ小健健】_2043960563025321986.json, 音频生成/音频生成/VoxCPM2-声音克隆_语音设计-单人_多人整合版【small-JJ小健健】_2043612797136801793.json, 音频生成/音频生成/VoxCPM2-声音克隆_语音设计-单人【small-JJ小健健】_2042886943972794370.json, 音频生成/音频生成/VoxCPM2-声音克隆_语音设计-单人【老崔】_2062234010562154497.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_780

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（音频生成/音频生成/-声音克隆_语音设计-多人-VoxCPM2【small-JJ小健健】_2043960563025321986.json、音频生成/音频生成/VoxCPM2-声音克隆_语音设计-单人_多人整合版【small-JJ小健健】_2043612797136801793.json、音频生成/音频生成/VoxCPM2-声音克隆_语音设计-单人【small-JJ小健健】_2042886943972794370.json、音频生成/音频生成/VoxCPM2-声音克隆_语音设计-单人【老崔】_2062234010562154497.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `Bjornulf_IfElse`
- `CR Text`
- `ImpactSwitch`
- `LazySwitch1way`
- `LoadAudio`
- `PreviewAny`
- `RH_LLMAPI_NODE`
- `RunningHub_VoxCPM_LoadModel`
- `SaveAudio`
- `easy boolean`
- `easy int`
- `ttN concat`

**可变部分**（部分 workflow 才有）：
- `RunningHub_VoxCPM_Generate` —— 3/4 个有
- `CharacterCount` —— 2/4 个有
- `RunningHub_VoxCPM_MultiSpeaker` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `easy compare` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
