---
name: unknown_workflow_generic_1105
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.883333
common_nodes: [Apply Whisper, LoadAudio, Qwen3TTSCustomVoice, Qwen3TTSModelLoader, Qwen3TTSVoiceClone, Qwen3TTSVoiceDesign, SaveAudio, ShowText|pysssss]
problems: []
missing: []
members: [音频生成/音频生成/Qwen3 TTS 声音设计_克隆_2014901954920583169.json, 音频生成/音频生成/Qwen3 TTS 最强声音开源工作流整合包_2015600681440256001.json, 音频生成/音频生成/Qwen3-TTS 音色设计+音色克隆+自定义情绪_2014604292602208258.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1105

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/Qwen3 TTS 声音设计_克隆_2014901954920583169.json、音频生成/音频生成/Qwen3 TTS 最强声音开源工作流整合包_2015600681440256001.json、音频生成/音频生成/Qwen3-TTS 音色设计+音色克隆+自定义情绪_2014604292602208258.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `Apply Whisper`
- `LoadAudio`
- `Qwen3TTSCustomVoice`
- `Qwen3TTSModelLoader`
- `Qwen3TTSVoiceClone`
- `Qwen3TTSVoiceDesign`
- `SaveAudio`
- `ShowText|pysssss`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 2/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `ImageLoader` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `TextInputNode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
