---
key: 图片生成/图生图/稳定加速版Qwen Image 2.1 PE姿势编辑 人物姿态精准控制_2109389400659554306.json
name: 稳定加速版Qwen Image 2.1 PE姿势编辑 人物姿态精准控制_2109389400659554306
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/稳定加速版Qwen Image 2.1 PE姿势编辑 人物姿态精准控制_2109389400659554306.json
hash: 1b1e451bd1072d0d
coverage: 0.892857
learned_at: 2026-10-23 13:20:09
nodes: [CLIPLoader, VAELoader, easy showAnything, EmptyLatentImage, ResolutionSelector, ComfySwitchNode, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, QwenImage21Cache, UNETLoader, QwenImage21SpectrumT8, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, KSampler, VAEDecode, easy cleanGpuUsed, QwenPERewriteT8, CR Prompt Text, SaveImage, LoadImage, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/稳定加速版Qwen Image 2.1 PE姿势编辑 人物姿态精准控制_2109389400659554306.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/稳定加速版Qwen Image 2.1 PE姿势编辑 人物姿态精准控制_2109389400659554306.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `CLIPLoader`
- `VAELoader`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `QwenImage21SpectrumT8`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `QwenPERewriteT8`
- `CR Prompt Text`
- `SaveImage`
- `LoadImage`
- `LoadImage`
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

覆盖率 **89%**（50/56）

**有卡**：`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`ResolutionSelector`、`TextEncodeQwenImage21`、`LoadImage`、`QwenImage21Cache`、`UNETLoader`、`QwenImage21SpectrumT8`、`QwenImage21BlockCacheT8`、`QwenImage21SageAttentionT8`、`KSampler`、`VAEDecode`、`easy cleanGpuUsed`、`QwenPERewriteT8`、`CR Prompt Text`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
