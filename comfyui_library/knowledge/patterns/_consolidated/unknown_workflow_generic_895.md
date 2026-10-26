---
name: unknown_workflow_generic_895
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.91475
common_nodes: [DF_Text, FB_Qwen3TTSDialogueInference, FB_Qwen3TTSRoleBank, FB_Qwen3TTSVoiceClonePrompt, JjkText, LayerUtility: PurgeVRAM V2, SaveAudio]
problems: []
missing: []
members: [音频生成/音频生成/多人物声音克隆 Qwen3 TTS_2015264650748760065.json, 音频生成/音频生成/多人物配音 可编辑角色声音 Qwen3TTS_2015257162548776961.json, 音频生成/音频生成/多角色声音克隆配音 Qwen3 TTS_2015260825090527234.json, 音频生成/音频生成/多角色编辑配音 Qwen3TTS_2015252252562300930.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_895

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（音频生成/音频生成/多人物声音克隆 Qwen3 TTS_2015264650748760065.json、音频生成/音频生成/多人物配音 可编辑角色声音 Qwen3TTS_2015257162548776961.json、音频生成/音频生成/多角色声音克隆配音 Qwen3 TTS_2015260825090527234.json、音频生成/音频生成/多角色编辑配音 Qwen3TTS_2015252252562300930.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `DF_Text`
- `FB_Qwen3TTSDialogueInference`
- `FB_Qwen3TTSRoleBank`
- `FB_Qwen3TTSVoiceClonePrompt`
- `JjkText`
- `LayerUtility: PurgeVRAM V2`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 3/4 个有
- `WhisperSTT` —— 3/4 个有
- `FB_Qwen3TTSVoiceDesign` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
