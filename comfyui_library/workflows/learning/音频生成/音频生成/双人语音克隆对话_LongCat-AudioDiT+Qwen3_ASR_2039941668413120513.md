---
key: 音频生成/音频生成/双人语音克隆对话_LongCat-AudioDiT+Qwen3_ASR_2039941668413120513.json
name: 双人语音克隆对话_LongCat-AudioDiT+Qwen3_ASR_2039941668413120513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/双人语音克隆对话_LongCat-AudioDiT+Qwen3_ASR_2039941668413120513.json
hash: 373fc959a7ec7acf
coverage: 0.764706
learned_at: 2026-10-18 02:28:47
nodes: [LongCatMultiSpeakerTTS, PreviewAny, PreviewAny, PreviewAny, Qwen3ASRLoader, Qwen3ASRTranscribe, easy positive, PreviewAudio, SaveImage, LoadImage, PreviewAny, LoadAudio, LoadAudio, Qwen3ASRTranscribe, NormalizeAudioLoudness, NormalizeAudioLoudness, SaveAudioMP3]
patterns: []
missing: []
---

# 音频生成/音频生成/双人语音克隆对话_LongCat-AudioDiT+Qwen3_ASR_2039941668413120513.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/双人语音克隆对话_LongCat-AudioDiT+Qwen3_ASR_2039941668413120513.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（17 个）：
- `LongCatMultiSpeakerTTS`
- `PreviewAny`
- `PreviewAny`
- `PreviewAny`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `easy positive`
- `PreviewAudio`
- `SaveImage`
- `LoadImage`
- `PreviewAny`
- `LoadAudio`
- `LoadAudio`
- `Qwen3ASRTranscribe`
- `NormalizeAudioLoudness`
- `NormalizeAudioLoudness`
- `SaveAudioMP3`

## 知识

覆盖率 **76%**（13/17）

**有卡**：`LongCatMultiSpeakerTTS`、`Qwen3ASRLoader`、`Qwen3ASRTranscribe`、`easy positive`、`PreviewAudio`、`SaveImage`、`LoadImage`、`LoadAudio`、`NormalizeAudioLoudness`、`SaveAudioMP3`

**用到的条目**：LoadImage、SaveImage、PreviewAudio、SaveAudioMP3、LoadAudio、Qwen3ASRLoader、Qwen3ASRTranscribe、NormalizeAudioLoudness
