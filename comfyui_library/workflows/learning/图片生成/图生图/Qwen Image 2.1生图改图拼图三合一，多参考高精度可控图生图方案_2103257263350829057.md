---
key: 图片生成/图生图/Qwen Image 2.1生图改图拼图三合一，多参考高精度可控图生图方案_2103257263350829057.json
name: Qwen Image 2.1生图改图拼图三合一，多参考高精度可控图生图方案_2103257263350829057
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1生图改图拼图三合一，多参考高精度可控图生图方案_2103257263350829057.json
hash: 509b250971cede2f
coverage: 0.45098
learned_at: 2026-10-21 00:42:42
nodes: [SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, PrimitiveStringMultiline, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, LoadImage, SetNode, LoadImage, SetNode, GetNode, LoadImage, SetNode, SetNode, GetNode, SetNode, GetNode, LoadImage, SetNode, LoadImage, GetNode, LoadImage, SetNode, SetNode, LoadImage, SetNode, LoadImage, GetNode, GetNode, GetNode, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, PrimitiveStringMultiline, ResolutionSelector, EmptyLatentImage, SetNode, UNETLoader, SetNode, QwenImage21Cache, CLIPLoader, TextEncodeQwenImage21, ComfySwitchNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, VAEDecode, KSampler, SetNode, VAELoader, SaveImage, SetNode, GetNode, SaveImageAdvanced, SetNode, LoadImage, Fast Groups Bypasser (rgthree), 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1生图改图拼图三合一，多参考高精度可控图生图方案_2103257263350829057.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1生图改图拼图三合一，多参考高精度可控图生图方案_2103257263350829057.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（102 个）：
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PrimitiveStringMultiline`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `GetNode`
- `LoadImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `GetNode`
- `LoadImage`
- `SetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `SetNode`
- `UNETLoader` ★核心
- `SetNode`
- `QwenImage21Cache`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SetNode`
- `VAELoader`
- `SaveImage`
- `SetNode`
- `GetNode`
- `SaveImageAdvanced`
- `SetNode`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
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

覆盖率 **45%**（46/102）

**有卡**：`LoadImage`、`ResolutionSelector`、`EmptyLatentImage`、`UNETLoader`、`QwenImage21Cache`、`CLIPLoader`、`TextEncodeQwenImage21`、`VAEDecode`、`KSampler`、`VAELoader`、`SaveImage`、`SaveImageAdvanced`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
