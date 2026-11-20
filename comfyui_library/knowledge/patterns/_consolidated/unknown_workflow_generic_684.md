---
name: unknown_workflow_generic_684
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.764
common_nodes: [LoadAudio, LoadImage, PreviewAny, RH_FireRedAudioLoader, SaveImage, ShellAgentPluginOutputText]
problems: []
missing: []
members: [图片生成/反推提示词/FireRed Audio ASR语音转译文字_2093559905507700737.json, 图片生成/反推提示词/Firered Audio Unstand语音理解_2093560835770769410.json, 音频生成/音频生成/FireRed Audio ASR语音转文字2608_2094001942090575874.json, 音频生成/音频生成/FireRed Audio语音理解2608_2094002011908956162.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_684

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/FireRed Audio ASR语音转译文字_2093559905507700737.json、图片生成/反推提示词/Firered Audio Unstand语音理解_2093560835770769410.json、音频生成/音频生成/FireRed Audio ASR语音转文字2608_2094001942090575874.json、音频生成/音频生成/FireRed Audio语音理解2608_2094002011908956162.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadAudio`
- `LoadImage`
- `PreviewAny`
- `RH_FireRedAudioLoader`
- `SaveImage`
- `ShellAgentPluginOutputText`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/4 个有
- `RH_FireRedAudioASR` —— 2/4 个有
- `RH_FireRedAudioUnderstand` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
