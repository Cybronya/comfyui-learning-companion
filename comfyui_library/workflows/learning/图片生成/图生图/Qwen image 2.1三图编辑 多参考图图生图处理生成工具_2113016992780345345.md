---
key: 图片生成/图生图/Qwen image 2.1三图编辑 多参考图图生图处理生成工具_2113016992780345345.json
name: Qwen image 2.1三图编辑 多参考图图生图处理生成工具_2113016992780345345
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1三图编辑 多参考图图生图处理生成工具_2113016992780345345.json
hash: 42f7553992c26bd3
coverage: 0.785714
learned_at: 2026-10-26 22:03:11
nodes: [VAEDecode, ComfySwitchNode, QwenImage21Cache, CLIPLoader, CLIPLoader, KSampler, SaveImage, EmptyLatentImage, TextEncodeQwenImage21, SaveImageAdvanced, VAELoader, Int, Int, UNETLoader, SDVN Load Image Url, SDVN Load Image Url, PrimitiveStringMultiline, SDVN Load Image Url, PrimitiveStringMultiline, SDVN Load Image Url, PrimitiveStringMultiline, SDVN Load Image Url, PrimitiveStringMultiline, SDVN Load Image Url, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image 2.1三图编辑 多参考图图生图处理生成工具_2113016992780345345.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1三图编辑 多参考图图生图处理生成工具_2113016992780345345.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（56 个）：
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `CLIPLoader`
- `CLIPLoader`
- `KSampler` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `SaveImageAdvanced`
- `VAELoader`
- `Int`
- `Int`
- `UNETLoader` ★核心
- `SDVN Load Image Url`
- `SDVN Load Image Url`
- `PrimitiveStringMultiline`
- `SDVN Load Image Url`
- `PrimitiveStringMultiline`
- `SDVN Load Image Url`
- `PrimitiveStringMultiline`
- `SDVN Load Image Url`
- `PrimitiveStringMultiline`
- `SDVN Load Image Url`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
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

覆盖率 **79%**（44/56）

**有卡**：`VAEDecode`、`QwenImage21Cache`、`CLIPLoader`、`KSampler`、`SaveImage`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`SaveImageAdvanced`、`VAELoader`、`Int`、`UNETLoader`、`SDVN Load Image Url`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
