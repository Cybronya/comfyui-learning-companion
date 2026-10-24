---
name: unknown_workflow_generic_473
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.887667
common_nodes: [Apply Whisper, LoadAudio, Qwen3TTSModelLoader, Qwen3TTSVoiceClone, SaveAudio, ShowText|pysssss]
problems: []
missing: []
members: [音频生成/音频生成/Qwen3 一键声音克隆_2067135176295145473.json, 音频生成/音频生成/Qwen3+TTS+声音克隆 KTN_2017793326098948097.json, 音频生成/音频生成/Qwen3+TTS+声音克隆 优化版本_2086006617899884546.json, 音频生成/音频生成/Qwen3+TTS+声音克隆_2016062956731113474.json, 音频生成/音频生成/Qwen3TTS（文本分为3段）_2033793004783276034.json, 音频生成/音频生成/千问语音合成（文本分段）_2032834024103743490.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_473

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（音频生成/音频生成/Qwen3 一键声音克隆_2067135176295145473.json、音频生成/音频生成/Qwen3+TTS+声音克隆 KTN_2017793326098948097.json、音频生成/音频生成/Qwen3+TTS+声音克隆 优化版本_2086006617899884546.json、音频生成/音频生成/Qwen3+TTS+声音克隆_2016062956731113474.json、音频生成/音频生成/Qwen3TTS（文本分为3段）_2033793004783276034.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `Apply Whisper`
- `LoadAudio`
- `Qwen3TTSModelLoader`
- `Qwen3TTSVoiceClone`
- `SaveAudio`
- `ShowText|pysssss`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 5/6 个有
- `CR Text` —— 3/6 个有
- `PreviewAudio` —— 2/6 个有
- `SoundFlow_Concatenator` —— 2/6 个有
- `SynVowTextSplitter` —— 2/6 个有
- `TextPreview` —— 2/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
