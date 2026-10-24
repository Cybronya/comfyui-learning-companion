---
key: 图片生成/图生图/Qwen image 2.1姿势参考编辑 人物姿态精准控制_2109070115789692929.json
name: Qwen image 2.1姿势参考编辑 人物姿态精准控制_2109070115789692929
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1姿势参考编辑 人物姿态精准控制_2109070115789692929.json
hash: 2f1ab8299b89a378
coverage: 0.784314
learned_at: 2026-10-23 11:14:08
nodes: [UNETLoader, QwenImage21SageAttentionT8, QwenImage21BlockCacheT8, CLIPLoader, SetNode, VAELoader, SetNode, QwenImage21SpectrumT8, SetNode, QwenPERewriteT8, GetNode, GetNode, GetNode, KSampler, TextEncodeQwenImage21, EmptyLatentImage, VAEDecode, JjkText, ResolutionSelector, SaveImage, LoadImage, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image 2.1姿势参考编辑 人物姿态精准控制_2109070115789692929.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1姿势参考编辑 人物姿态精准控制_2109070115789692929.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `UNETLoader` ★核心
- `QwenImage21SageAttentionT8`
- `QwenImage21BlockCacheT8`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `QwenImage21SpectrumT8`
- `SetNode`
- `QwenPERewriteT8`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `ResolutionSelector`
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

覆盖率 **78%**（40/51）

**有卡**：`UNETLoader`、`QwenImage21SageAttentionT8`、`QwenImage21BlockCacheT8`、`CLIPLoader`、`VAELoader`、`QwenImage21SpectrumT8`、`QwenPERewriteT8`、`KSampler`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`ResolutionSelector`、`SaveImage`、`LoadImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
