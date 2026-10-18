---
key: 音频生成/音频生成/TTS2.5双人对话工作流，音频生成语音合成处理工具_2107566962367885313.json
name: TTS2.5双人对话工作流，音频生成语音合成处理工具_2107566962367885313
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/TTS2.5双人对话工作流，音频生成语音合成处理工具_2107566962367885313.json
hash: 569985364b51ee3e
coverage: 0.897436
learned_at: 2026-10-18 18:02:28
nodes: [T8_IndexTTS25_VoiceProfile, T8_IndexTTS25_ModelLoader, T8_IndexTTS25_VoiceProfile, T8_IndexTTS25_DialogueScript, T8_IndexTTS25_DialogueGenerate, SaveAudio, T8_IndexTTS25_RoleLibrary, LoadAudio, LoadAudio, T8_IndexTTS25_SamplingConfig, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 音频生成/音频生成/TTS2.5双人对话工作流，音频生成语音合成处理工具_2107566962367885313.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/TTS2.5双人对话工作流，音频生成语音合成处理工具_2107566962367885313.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（39 个）：
- `T8_IndexTTS25_VoiceProfile`
- `T8_IndexTTS25_ModelLoader`
- `T8_IndexTTS25_VoiceProfile`
- `T8_IndexTTS25_DialogueScript`
- `T8_IndexTTS25_DialogueGenerate`
- `SaveAudio`
- `T8_IndexTTS25_RoleLibrary`
- `LoadAudio`
- `LoadAudio`
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
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
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

**有卡**：`T8_IndexTTS25_VoiceProfile`、`T8_IndexTTS25_ModelLoader`、`T8_IndexTTS25_DialogueScript`、`T8_IndexTTS25_DialogueGenerate`、`SaveAudio`、`T8_IndexTTS25_RoleLibrary`、`LoadAudio`、`T8_IndexTTS25_SamplingConfig`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`CLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
