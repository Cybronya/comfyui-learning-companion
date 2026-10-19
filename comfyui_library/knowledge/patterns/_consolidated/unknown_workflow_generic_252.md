---
name: unknown_workflow_generic_252
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6954
common_nodes: [CR Text, LoadAudio, Qwen3TTSModelLoader, Qwen3TTSVoiceClone, SaveAudioMP3, ShowText|pysssss]
problems: []
missing: []
members: [视频生成/文生视频/Qwen3-TTS 声音克隆，适用解说漫，配音色，文本转音频_2094370946944692226.json, 音频生成/音频生成/Qwen3-TTS 声音克隆_2015963024938504194.json, 音频生成/音频生成/Qwen3-TTS 音色克隆_2014663509912588289.json, 音频生成/音频生成/Qwen3-TTS--声音克隆（方言可克隆）_2059954156898705410.json, 音频生成/音频生成/声音克隆Qwen3+TTS（支持多国语言）_2014615319716827138.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_252

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/Qwen3-TTS 声音克隆，适用解说漫，配音色，文本转音频_2094370946944692226.json、音频生成/音频生成/Qwen3-TTS 声音克隆_2015963024938504194.json、音频生成/音频生成/Qwen3-TTS 音色克隆_2014663509912588289.json、音频生成/音频生成/Qwen3-TTS--声音克隆（方言可克隆）_2059954156898705410.json、音频生成/音频生成/声音克隆Qwen3+TTS（支持多国语言）_2014615319716827138.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 5 个 workflow 都包含：
- `CR Text`
- `LoadAudio`
- `Qwen3TTSModelLoader`
- `Qwen3TTSVoiceClone`
- `SaveAudioMP3`
- `ShowText|pysssss`

**可变部分**（部分 workflow 才有）：
- `Qwen3ASRLoader` —— 3/5 个有
- `Qwen3ASRTranscribe` —— 3/5 个有
- `Apply Whisper` —— 2/5 个有
- `PreviewAny` —— 1/5 个有
- `SaveAudio` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
