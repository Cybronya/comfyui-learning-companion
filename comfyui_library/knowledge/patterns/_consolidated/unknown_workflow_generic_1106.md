---
name: unknown_workflow_generic_1106
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.715333
common_nodes: [FB_Qwen3TTSCustomVoice, FB_Qwen3TTSVoiceClone, FB_Qwen3TTSVoiceDesign, LoadAudio, PreviewAny, RH_LLMAPI_Pro_Node, SaveAudio, WhisperSTT]
problems: []
missing: []
members: [音频生成/音频生成/Qwen3 TTS-四合一 语音克隆_2015976240687095809.json, "音频生成/音频生成/Qwen3-TTS语音克隆,设计,自定义三合一_2014962110224142337.json", 音频生成/音频生成/【语音三合一】语音克隆+自定义语音+语音音色设计_2018169808604368898.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1106

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/Qwen3 TTS-四合一 语音克隆_2015976240687095809.json、音频生成/音频生成/Qwen3-TTS语音克隆,设计,自定义三合一_2014962110224142337.json、音频生成/音频生成/【语音三合一】语音克隆+自定义语音+语音音色设计_2018169808604368898.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 3 个 workflow 都包含：
- `FB_Qwen3TTSCustomVoice`
- `FB_Qwen3TTSVoiceClone`
- `FB_Qwen3TTSVoiceDesign`
- `LoadAudio`
- `PreviewAny`
- `RH_LLMAPI_Pro_Node`
- `SaveAudio`
- `WhisperSTT`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `PreviewAudio` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LoadImage` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
