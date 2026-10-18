---
key: 音频生成/音频生成/001-brezze-tts2-智能创作助手v3.4_2097607239157768193.json
name: 001-brezze-tts2-智能创作助手v3.4_2097607239157768193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/001-brezze-tts2-智能创作助手v3.4_2097607239157768193.json
hash: 1b19eb8adf701c97
coverage: 0.735294
learned_at: 2026-10-18 17:45:25
nodes: [llama_cpp_parameters, SetNode, BreezeTTS2VoiceClone, GetNode, BreezeTTS2VoiceDirection, GetNode, GetNode, GetNode, BreezeTTS2MultiSpeaker, BreezeTTS2VoiceDesign, ShowText|pysssss, llama_cpp_instruct_adv, PreviewAudio, BreezeTTS2LoadModel, llama_cpp_model_loader, Any Switch (rgthree), PreviewAudio, PreviewAudio, LoadAudio, WhisperSTT, BreezeTTS2Speaker, BreezeTTS2Speaker, PreviewAudio, SaveAudioAdvanced, SaveAudioAdvanced, SaveAudioAdvanced, SaveAudioAdvanced, Fast Groups Bypasser (rgthree), Note, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline]
patterns: []
missing: []
---

# 音频生成/音频生成/001-brezze-tts2-智能创作助手v3.4_2097607239157768193.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/001-brezze-tts2-智能创作助手v3.4_2097607239157768193.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（34 个）：
- `llama_cpp_parameters`
- `SetNode`
- `BreezeTTS2VoiceClone`
- `GetNode`
- `BreezeTTS2VoiceDirection`
- `GetNode`
- `GetNode`
- `GetNode`
- `BreezeTTS2MultiSpeaker`
- `BreezeTTS2VoiceDesign`
- `ShowText|pysssss`
- `llama_cpp_instruct_adv`
- `PreviewAudio`
- `BreezeTTS2LoadModel`
- `llama_cpp_model_loader`
- `Any Switch (rgthree)`
- `PreviewAudio`
- `PreviewAudio`
- `LoadAudio`
- `WhisperSTT`
- `BreezeTTS2Speaker`
- `BreezeTTS2Speaker`
- `PreviewAudio`
- `SaveAudioAdvanced`
- `SaveAudioAdvanced`
- `SaveAudioAdvanced`
- `SaveAudioAdvanced`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`

## 知识

覆盖率 **74%**（25/34）

**有卡**：`llama_cpp_parameters`、`BreezeTTS2VoiceClone`、`BreezeTTS2VoiceDirection`、`BreezeTTS2MultiSpeaker`、`BreezeTTS2VoiceDesign`、`llama_cpp_instruct_adv`、`PreviewAudio`、`BreezeTTS2LoadModel`、`llama_cpp_model_loader`、`LoadAudio`、`WhisperSTT`、`BreezeTTS2Speaker`、`SaveAudioAdvanced`、`Text Multiline`

**用到的条目**：PreviewAudio、SaveAudioAdvanced、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、LoadAudio、WhisperSTT、Text Multiline
