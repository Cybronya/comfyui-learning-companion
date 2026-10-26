---
key: 图片生成/图生图/Qwen image 2.1单图编辑 一张参考图图生图处理工具_2113031173294350337.json
name: Qwen image 2.1单图编辑 一张参考图图生图处理工具_2113031173294350337
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1单图编辑 一张参考图图生图处理工具_2113031173294350337.json
hash: 4d03573262d7a4c2
coverage: 0.860465
learned_at: 2026-10-26 22:03:12
nodes: [VAEDecode, ComfySwitchNode, QwenImage21Cache, KSampler, EmptyLatentImage, VAELoader, TextEncodeQwenImage21, CLIPLoader, SaveImage, PrimitiveStringMultiline, LoadImage, UNETLoader, easy int, easy int, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image 2.1单图编辑 一张参考图图生图处理工具_2113031173294350337.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1单图编辑 一张参考图图生图处理工具_2113031173294350337.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（43 个）：
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `SaveImage`
- `PrimitiveStringMultiline`
- `LoadImage`
- `UNETLoader` ★核心
- `easy int`
- `easy int`
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
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
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

覆盖率 **86%**（37/43）

**有卡**：`VAEDecode`、`QwenImage21Cache`、`KSampler`、`EmptyLatentImage`、`VAELoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`SaveImage`、`LoadImage`、`UNETLoader`、`easy int`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
