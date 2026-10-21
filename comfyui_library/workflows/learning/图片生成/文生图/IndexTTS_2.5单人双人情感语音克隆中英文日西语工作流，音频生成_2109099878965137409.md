---
key: 图片生成/文生图/IndexTTS_2.5单人双人情感语音克隆中英文日西语工作流，音频生成_2109099878965137409.json
name: IndexTTS_2.5单人双人情感语音克隆中英文日西语工作流，音频生成_2109099878965137409
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/IndexTTS_2.5单人双人情感语音克隆中英文日西语工作流，音频生成_2109099878965137409.json
hash: f20768b5a9e198e3
coverage: 0.892857
learned_at: 2026-10-21 02:52:48
nodes: [SaveAudioAdvanced, PrimitiveNode, PrimitiveNode, PrimitiveNode, T8_IndexTTS25_EmotionControl, CR Prompt Text, PreviewAudio, Float, T8_IndexTTS25_VoiceProfile, CR Prompt Text, T8_IndexTTS25_VoiceProfile, T8_IndexTTS25_ModelLoader, SaveAudioAdvanced, LoadAudio, T8_IndexTTS25_SamplingConfig, T8_IndexTTS25_Generate, LoadAudio, LoadAudio, T8_IndexTTS25_RoleLibrary, T8_IndexTTS25_DialogueScript, T8_IndexTTS25_SamplingConfig, PreviewAudio, T8_IndexTTS25_EmotionControl, T8_IndexTTS25_ModelLoader, PixaromaGroupSwitch, T8_IndexTTS25_DialogueGenerate, T8_IndexTTS25_EmotionControl, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/IndexTTS_2.5单人双人情感语音克隆中英文日西语工作流，音频生成_2109099878965137409.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/IndexTTS_2.5单人双人情感语音克隆中英文日西语工作流，音频生成_2109099878965137409.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `SaveAudioAdvanced`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `T8_IndexTTS25_EmotionControl`
- `CR Prompt Text`
- `PreviewAudio`
- `Float`
- `T8_IndexTTS25_VoiceProfile`
- `CR Prompt Text`
- `T8_IndexTTS25_VoiceProfile`
- `T8_IndexTTS25_ModelLoader`
- `SaveAudioAdvanced`
- `LoadAudio`
- `T8_IndexTTS25_SamplingConfig`
- `T8_IndexTTS25_Generate`
- `LoadAudio`
- `LoadAudio`
- `T8_IndexTTS25_RoleLibrary`
- `T8_IndexTTS25_DialogueScript`
- `T8_IndexTTS25_SamplingConfig`
- `PreviewAudio`
- `T8_IndexTTS25_EmotionControl`
- `T8_IndexTTS25_ModelLoader`
- `PixaromaGroupSwitch`
- `T8_IndexTTS25_DialogueGenerate`
- `T8_IndexTTS25_EmotionControl`
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
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `EmptyImage`
- `PreviewImage`

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

覆盖率 **89%**（50/56）

**有卡**：`SaveAudioAdvanced`、`T8_IndexTTS25_EmotionControl`、`CR Prompt Text`、`PreviewAudio`、`Float`、`T8_IndexTTS25_VoiceProfile`、`T8_IndexTTS25_ModelLoader`、`LoadAudio`、`T8_IndexTTS25_SamplingConfig`、`T8_IndexTTS25_Generate`、`T8_IndexTTS25_RoleLibrary`、`T8_IndexTTS25_DialogueScript`、`PixaromaGroupSwitch`、`T8_IndexTTS25_DialogueGenerate`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
