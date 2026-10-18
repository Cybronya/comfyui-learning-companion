---
key: 音频生成/音频生成/IndexTTS 2.5多音字语音克隆｜中文版多发音支持音频生成_2090445429296160769.json
name: IndexTTS 2.5多音字语音克隆｜中文版多发音支持音频生成_2090445429296160769
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/IndexTTS 2.5多音字语音克隆｜中文版多发音支持音频生成_2090445429296160769.json
hash: 28227115a35dda52
coverage: 0.882353
learned_at: 2026-10-18 17:45:33
nodes: [T8_IndexTTS25_ModelLoader, CR Prompt Text, T8_IndexTTS25_Pronunciation, CR Prompt Text, SaveAudio, T8_IndexTTS25_Generate, LoadAudio, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 音频生成/音频生成/IndexTTS 2.5多音字语音克隆｜中文版多发音支持音频生成_2090445429296160769.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/IndexTTS 2.5多音字语音克隆｜中文版多发音支持音频生成_2090445429296160769.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（34 个）：
- `T8_IndexTTS25_ModelLoader`
- `CR Prompt Text`
- `T8_IndexTTS25_Pronunciation`
- `CR Prompt Text`
- `SaveAudio`
- `T8_IndexTTS25_Generate`
- `LoadAudio`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
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
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **88%**（30/34）

**有卡**：`T8_IndexTTS25_ModelLoader`、`CR Prompt Text`、`T8_IndexTTS25_Pronunciation`、`SaveAudio`、`T8_IndexTTS25_Generate`、`LoadAudio`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
