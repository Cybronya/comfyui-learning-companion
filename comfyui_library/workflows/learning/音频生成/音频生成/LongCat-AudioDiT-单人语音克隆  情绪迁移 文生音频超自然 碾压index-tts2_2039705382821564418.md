---
key: 音频生成/音频生成/LongCat-AudioDiT-单人语音克隆  情绪迁移 文生音频超自然 碾压index-tts2_2039705382821564418.json
name: LongCat-AudioDiT-单人语音克隆  情绪迁移 文生音频超自然 碾压index-tts2_2039705382821564418
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/LongCat-AudioDiT-单人语音克隆  情绪迁移 文生音频超自然 碾压index-tts2_2039705382821564418.json
hash: 12420e93bf596a72
coverage: 0.9
learned_at: 2026-10-18 02:28:41
nodes: [LongCatVoiceCloneTTS, LoadAudio, TrimAudioDuration, NormalizeAudioLoudness, Qwen3ASRLoader, Qwen3ASRTranscribe, ShowText|pysssss, easy cleanGpuUsed, SaveAudioMP3, CR Text]
patterns: []
missing: []
---

# 音频生成/音频生成/LongCat-AudioDiT-单人语音克隆  情绪迁移 文生音频超自然 碾压index-tts2_2039705382821564418.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/LongCat-AudioDiT-单人语音克隆  情绪迁移 文生音频超自然 碾压index-tts2_2039705382821564418.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（10 个）：
- `LongCatVoiceCloneTTS`
- `LoadAudio`
- `TrimAudioDuration`
- `NormalizeAudioLoudness`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `ShowText|pysssss`
- `easy cleanGpuUsed`
- `SaveAudioMP3`
- `CR Text`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`LongCatVoiceCloneTTS`、`LoadAudio`、`TrimAudioDuration`、`NormalizeAudioLoudness`、`Qwen3ASRLoader`、`Qwen3ASRTranscribe`、`easy cleanGpuUsed`、`SaveAudioMP3`、`CR Text`

**用到的条目**：SaveAudioMP3、LoadAudio、TrimAudioDuration、Qwen3ASRLoader、Qwen3ASRTranscribe、NormalizeAudioLoudness、LongCatVoiceCloneTTS、CR Text
