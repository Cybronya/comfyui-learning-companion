---
key: 音频生成/音频生成/长文本语音克隆｜IndexTTS 2.5音色复刻音频生成_2093406742762835970.json
name: 长文本语音克隆｜IndexTTS 2.5音色复刻音频生成_2093406742762835970
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/长文本语音克隆｜IndexTTS 2.5音色复刻音频生成_2093406742762835970.json
hash: 4ab9989df826f266
coverage: 0.888889
learned_at: 2026-10-18 17:45:58
nodes: [NormalizeAudioLoudness, LoadAudio, SaveAudioMP3, CR Prompt Text, T8_IndexTTS25_ModelLoader, T8_IndexTTS25_Generate, T8_IndexTTS25_SamplingConfig, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 音频生成/音频生成/长文本语音克隆｜IndexTTS 2.5音色复刻音频生成_2093406742762835970.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/长文本语音克隆｜IndexTTS 2.5音色复刻音频生成_2093406742762835970.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（36 个）：
- `NormalizeAudioLoudness`
- `LoadAudio`
- `SaveAudioMP3`
- `CR Prompt Text`
- `T8_IndexTTS25_ModelLoader`
- `T8_IndexTTS25_Generate`
- `T8_IndexTTS25_SamplingConfig`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`NormalizeAudioLoudness`、`LoadAudio`、`SaveAudioMP3`、`CR Prompt Text`、`T8_IndexTTS25_ModelLoader`、`T8_IndexTTS25_Generate`、`T8_IndexTTS25_SamplingConfig`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`CLIPLoader`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`VAEDecode`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
