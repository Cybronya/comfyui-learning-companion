---
name: unknown_workflow_generic_1055
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.805
common_nodes: [FB_Qwen3TTSDialogueInference, FB_Qwen3TTSRoleBank, FB_Qwen3TTSVoiceClonePrompt, SaveAudio]
problems: []
missing: []
members: [音频生成/音频生成/余温克隆音色多人对话配音工作流_2107641636846133249.json, 音频生成/音频生成/余温出品｜克隆音色驱动多人对话配音的音频生成方案_2114745080312590337.json, 音频生成/音频生成/多人对话（声音克隆）Qwen3-TTS_2109166934381121537.json, 音频生成/音频生成/多人对话（声音设计）Qwen3-TTS_2109223062850859010.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1055

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（音频生成/音频生成/余温克隆音色多人对话配音工作流_2107641636846133249.json、音频生成/音频生成/余温出品｜克隆音色驱动多人对话配音的音频生成方案_2114745080312590337.json、音频生成/音频生成/多人对话（声音克隆）Qwen3-TTS_2109166934381121537.json、音频生成/音频生成/多人对话（声音设计）Qwen3-TTS_2109223062850859010.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `FB_Qwen3TTSDialogueInference`
- `FB_Qwen3TTSRoleBank`
- `FB_Qwen3TTSVoiceClonePrompt`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 3/4 个有
- `HeartMuLa_Transcribe` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `忽略多组孤海` —— 2/4 个有
- `FB_Qwen3TTSVoiceDesign` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
