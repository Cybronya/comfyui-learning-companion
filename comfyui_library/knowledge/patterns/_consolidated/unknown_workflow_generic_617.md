---
name: unknown_workflow_generic_617
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8172
common_nodes: [CR Text, SaveAudio, Text Multiline]
problems: []
missing: []
members: [音频生成/音频生成/音频-单人文本克隆配音-FishAudio S2 TTS_2037058223412355073.json, 音频生成/音频生成/音频-单人文本克隆配音-Qwen3 TTS_2014568722706472961.json, 音频生成/音频生成/音频-单人文本克隆配音-Qwen3 TTS_2014584875277361154.json, 音频生成/音频生成/音频-声音设计配音-Qwen3 TTS_2014572376549236737.json, 音频生成/音频生成/音频设计+文本声音克隆配音-Qwen3-TTS_2014684290608537601.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_617

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（音频生成/音频生成/音频-单人文本克隆配音-FishAudio S2 TTS_2037058223412355073.json、音频生成/音频生成/音频-单人文本克隆配音-Qwen3 TTS_2014568722706472961.json、音频生成/音频生成/音频-单人文本克隆配音-Qwen3 TTS_2014584875277361154.json、音频生成/音频生成/音频-声音设计配音-Qwen3 TTS_2014572376549236737.json、音频生成/音频生成/音频设计+文本声音克隆配音-Qwen3-TTS_2014684290608537601.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `CR Text`
- `SaveAudio`
- `Text Multiline`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 4/5 个有
- `Qwen3TTSModelLoader` —— 4/5 个有
- `Qwen3TTSVoiceClone` —— 3/5 个有
- `Qwen3TTSVoiceDesign` —— 3/5 个有
- `easy seed` —— 3/5 个有
- `SaveAudioMP3` —— 2/5 个有
- `FishS2VoiceCloneTTS` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
