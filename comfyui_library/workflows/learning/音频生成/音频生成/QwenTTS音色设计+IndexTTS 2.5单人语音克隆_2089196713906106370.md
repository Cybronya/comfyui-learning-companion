---
key: 音频生成/音频生成/QwenTTS音色设计+IndexTTS 2.5单人语音克隆_2089196713906106370.json
name: QwenTTS音色设计+IndexTTS 2.5单人语音克隆_2089196713906106370
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/QwenTTS音色设计+IndexTTS 2.5单人语音克隆_2089196713906106370.json
hash: 52c4e7abb58a10cf
coverage: 0.560976
learned_at: 2026-10-18 17:45:43
nodes: [Qwen3ASRLoader, T8_IndexTTS25_SamplingConfig, SetNode, Qwen3ASRTranscribe, SetNode, PreviewAny, GetNode, GetNode, SetNode, SetNode, TDQwen3TTSModelLoader, GetNode, GetNode, ImpactConditionalBranch, ZML_BooleanSwitch, easy positive, SetNode, CR Prompt Text, AudioCrop, PreviewAudio, GetNode, 忽略多组孤海, GetNode, NormalizeAudioLoudness, GetNode, TDQwen3TTSVoiceDesign, GetNode, NormalizeAudioLoudness, ImpactConditionalBranch, T8_IndexTTS25_ModelLoader, GetNode, SaveAudioMP3, SetNode, T8_IndexTTS25_Generate, SaveAudioAdvanced, LoadAudio, SetNode, T8_IndexTTS25_EmotionControl, ZML_BooleanSwitch, 孤海注释, PreviewAudio]
patterns: []
missing: []
---

# 音频生成/音频生成/QwenTTS音色设计+IndexTTS 2.5单人语音克隆_2089196713906106370.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/QwenTTS音色设计+IndexTTS 2.5单人语音克隆_2089196713906106370.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（41 个）：
- `Qwen3ASRLoader`
- `T8_IndexTTS25_SamplingConfig`
- `SetNode`
- `Qwen3ASRTranscribe`
- `SetNode`
- `PreviewAny`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `TDQwen3TTSModelLoader`
- `GetNode`
- `GetNode`
- `ImpactConditionalBranch`
- `ZML_BooleanSwitch`
- `easy positive`
- `SetNode`
- `CR Prompt Text`
- `AudioCrop`
- `PreviewAudio`
- `GetNode`
- `忽略多组孤海`
- `GetNode`
- `NormalizeAudioLoudness`
- `GetNode`
- `TDQwen3TTSVoiceDesign`
- `GetNode`
- `NormalizeAudioLoudness`
- `ImpactConditionalBranch`
- `T8_IndexTTS25_ModelLoader`
- `GetNode`
- `SaveAudioMP3`
- `SetNode`
- `T8_IndexTTS25_Generate`
- `SaveAudioAdvanced`
- `LoadAudio`
- `SetNode`
- `T8_IndexTTS25_EmotionControl`
- `ZML_BooleanSwitch`
- `孤海注释`
- `PreviewAudio`

## 知识

覆盖率 **56%**（23/41）

**有卡**：`Qwen3ASRLoader`、`T8_IndexTTS25_SamplingConfig`、`Qwen3ASRTranscribe`、`TDQwen3TTSModelLoader`、`ImpactConditionalBranch`、`ZML_BooleanSwitch`、`easy positive`、`CR Prompt Text`、`AudioCrop`、`PreviewAudio`、`忽略多组孤海`、`NormalizeAudioLoudness`、`TDQwen3TTSVoiceDesign`、`T8_IndexTTS25_ModelLoader`、`SaveAudioMP3`、`T8_IndexTTS25_Generate`、`SaveAudioAdvanced`、`LoadAudio`、`T8_IndexTTS25_EmotionControl`

**用到的条目**：CR Prompt Text、PreviewAudio、SaveAudioAdvanced、SaveAudioMP3、LoadAudio、ZML_BooleanSwitch、AudioCrop、ImpactConditionalBranch
