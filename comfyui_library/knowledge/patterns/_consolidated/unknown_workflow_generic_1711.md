---
name: unknown_workflow_generic_1711
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7455
common_nodes: [AudioSeparation, ComfyMathExpression, GemmaxRun, GetNode, GetVideoComponents, GoogleTranslateTextNode, LoadAudio, LoadVideo, OmniVoiceVoiceCloneTTS, PreviewAudio, PrimitiveBoolean, Qwen3ASRLoader, Qwen3ASRTranscribe, RH_GetAudioDuration, RH_LLMAPI_Pro_Node, SaveAudioMP3, SetNode, SoundFlow_TrimAudio, Text, easy ifElse, easy showAnything]
problems: []
missing: []
members: [音频生成/音频生成/【定制专用，LLM大模型翻译可选】音色+音调同步克隆，支持自定义朗读文本_2072901391768702977.json, 音频生成/音频生成/【定制专用，日语版】音色+音调同步克隆，支持自定义朗读文本_2072712122575966209.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1711

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/【定制专用，LLM大模型翻译可选】音色+音调同步克隆，支持自定义朗读文本_2072901391768702977.json、音频生成/音频生成/【定制专用，日语版】音色+音调同步克隆，支持自定义朗读文本_2072712122575966209.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioSeparation`
- `ComfyMathExpression`
- `GemmaxRun`
- `GetNode`
- `GetVideoComponents`
- `GoogleTranslateTextNode`
- `LoadAudio`
- `LoadVideo`
- `OmniVoiceVoiceCloneTTS`
- `PreviewAudio`
- `PrimitiveBoolean`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `RH_GetAudioDuration`
- `RH_LLMAPI_Pro_Node`
- `SaveAudioMP3`
- `SetNode`
- `SoundFlow_TrimAudio`
- `Text`
- `easy ifElse`
- `easy showAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
