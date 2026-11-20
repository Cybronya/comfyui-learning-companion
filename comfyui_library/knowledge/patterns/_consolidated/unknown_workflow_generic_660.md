---
name: unknown_workflow_generic_660
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8984
common_nodes: [FB_Qwen3TTSVoiceClone, FB_Qwen3TTSVoiceDesign, LoadAudio, SaveAudio]
problems: []
missing: []
members: [音频生成/音频生成/Qwen3-TTS 语音合成 全能工作流 声音克隆+语音设计+自定义语音_2015126708516556801.json, 音频生成/音频生成/Qwen3-TTS_2017648745889927170.json, "音频生成/音频生成/Qwen3-TTS音色克隆,设计音色_2038656384841031682.json", 音频生成/音频生成/Qwen3-TTS音色推理生成，音色克隆_2018651821329354753.json, 音频生成/音频生成/Qwen3-TTS音色推理设计，预设，克隆多合一_2017567768417148929.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_660

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（音频生成/音频生成/Qwen3-TTS 语音合成 全能工作流 声音克隆+语音设计+自定义语音_2015126708516556801.json、音频生成/音频生成/Qwen3-TTS_2017648745889927170.json、音频生成/音频生成/Qwen3-TTS音色克隆,设计音色_2038656384841031682.json、音频生成/音频生成/Qwen3-TTS音色推理生成，音色克隆_2018651821329354753.json、音频生成/音频生成/Qwen3-TTS音色推理设计，预设，克隆多合一_2017567768417148929.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `FB_Qwen3TTSVoiceClone`
- `FB_Qwen3TTSVoiceDesign`
- `LoadAudio`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `FB_Qwen3TTSCustomVoice` —— 4/5 个有
- `PreviewAudio` —— 4/5 个有
- `WhisperSTT` —— 3/5 个有
- `RH_LLMAPI_Pro_Node` —— 2/5 个有
- `SaveImage` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
