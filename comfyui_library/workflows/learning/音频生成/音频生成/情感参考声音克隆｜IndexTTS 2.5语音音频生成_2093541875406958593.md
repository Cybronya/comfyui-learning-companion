---
key: 音频生成/音频生成/情感参考声音克隆｜IndexTTS 2.5语音音频生成_2093541875406958593.json
name: 情感参考声音克隆｜IndexTTS 2.5语音音频生成_2093541875406958593
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/情感参考声音克隆｜IndexTTS 2.5语音音频生成_2093541875406958593.json
hash: 8092e14a71834876
coverage: 0.897436
learned_at: 2026-10-18 17:45:54
nodes: [T8_IndexTTS25_EmotionControl, NormalizeAudioLoudness, NormalizeAudioLoudness, CR Prompt Text, LoadAudio, LoadAudio, SaveAudioMP3, T8_IndexTTS25_ModelLoader, T8_IndexTTS25_Generate, Float, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 音频生成/音频生成/情感参考声音克隆｜IndexTTS 2.5语音音频生成_2093541875406958593.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/情感参考声音克隆｜IndexTTS 2.5语音音频生成_2093541875406958593.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（39 个）：
- `T8_IndexTTS25_EmotionControl`
- `NormalizeAudioLoudness`
- `NormalizeAudioLoudness`
- `CR Prompt Text`
- `LoadAudio`
- `LoadAudio`
- `SaveAudioMP3`
- `T8_IndexTTS25_ModelLoader`
- `T8_IndexTTS25_Generate`
- `Float`
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

覆盖率 **90%**（35/39）

**有卡**：`T8_IndexTTS25_EmotionControl`、`NormalizeAudioLoudness`、`CR Prompt Text`、`LoadAudio`、`SaveAudioMP3`、`T8_IndexTTS25_ModelLoader`、`T8_IndexTTS25_Generate`、`Float`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`CLIPLoader`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`VAEDecode`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
