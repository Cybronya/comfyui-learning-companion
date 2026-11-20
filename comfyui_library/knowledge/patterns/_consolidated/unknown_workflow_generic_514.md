---
name: unknown_workflow_generic_514
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.896
common_nodes: [CR Prompt Text, FB_Qwen3TTSVoiceDesign, PreviewAny, PreviewAudio, RH_LLMAPI_Pro_Node, SaveAudio]
problems: []
missing: []
members: [音频生成/音频生成/(Smile版)Qwen3 TTS声音设计_2015076900074426370.json, 音频生成/音频生成/(Smile版)Qwen3 TTS声音设计_2015998086245519362.json, 音频生成/音频生成/(Smile版)Qwen3 TTS声音设计_2033382385605156865.json, 音频生成/音频生成/Qwen3 TTS声音设计+VoxCPM2语音克隆组合版_2046465787099095041.json, 音频生成/音频生成/Qwen3 TTS声音设计+VoxCPM2语音克隆组合版工作流_2046803129345249282.json, 音频生成/音频生成/Qwen3-TTS 音色设计_2034082246776332290.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_514

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（音频生成/音频生成/(Smile版)Qwen3 TTS声音设计_2015076900074426370.json、音频生成/音频生成/(Smile版)Qwen3 TTS声音设计_2015998086245519362.json、音频生成/音频生成/(Smile版)Qwen3 TTS声音设计_2033382385605156865.json、音频生成/音频生成/Qwen3 TTS声音设计+VoxCPM2语音克隆组合版_2046465787099095041.json、音频生成/音频生成/Qwen3 TTS声音设计+VoxCPM2语音克隆组合版工作流_2046803129345249282.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CR Prompt Text`
- `FB_Qwen3TTSVoiceDesign`
- `PreviewAny`
- `PreviewAudio`
- `RH_LLMAPI_Pro_Node`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `ConcatTextOfUtils` —— 2/6 个有
- `RunningHub_VoxCPM_LoadModel` —— 2/6 个有
- `RunningHub_VoxCPM_MultiSpeaker_ListReference` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
