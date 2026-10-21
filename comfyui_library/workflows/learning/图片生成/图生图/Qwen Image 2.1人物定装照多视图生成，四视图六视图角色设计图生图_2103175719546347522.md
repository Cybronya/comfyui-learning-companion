---
key: 图片生成/图生图/Qwen Image 2.1人物定装照多视图生成，四视图六视图角色设计图生图_2103175719546347522.json
name: Qwen Image 2.1人物定装照多视图生成，四视图六视图角色设计图生图_2103175719546347522
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1人物定装照多视图生成，四视图六视图角色设计图生图_2103175719546347522.json
hash: 450daffc76438b9b
coverage: 0.666667
learned_at: 2026-10-21 00:42:18
nodes: [LayerUtility: ImageScaleByAspectRatio V2, PrimitiveStringMultiline, PrimitiveStringMultiline, ComfySwitchNode, PreviewAny, TextEncodeQwenImage21, PrimitiveInt, PrimitiveInt, easy seed, VAEDecode, GetNode, GetNode, UNETLoader, QwenImage21Cache, CLIPLoader, SetNode, SetNode, SetNode, SaveImage, PrimitiveBoolean, KSampler, GetNode, VAELoader, ComfySwitchNode, EmptyLatentImage, PrimitiveInt, ComfySwitchNode, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1人物定装照多视图生成，四视图六视图角色设计图生图_2103175719546347522.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1人物定装照多视图生成，四视图六视图角色设计图生图_2103175719546347522.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `PreviewAny`
- `TextEncodeQwenImage21`
- `PrimitiveInt`
- `PrimitiveInt`
- `easy seed`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SaveImage`
- `PrimitiveBoolean`
- `KSampler` ★核心
- `GetNode`
- `VAELoader`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `PrimitiveInt`
- `ComfySwitchNode`
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

覆盖率 **67%**（38/57）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImage21`、`easy seed`、`VAEDecode`、`UNETLoader`、`QwenImage21Cache`、`CLIPLoader`、`SaveImage`、`PrimitiveBoolean`、`KSampler`、`VAELoader`、`EmptyLatentImage`、`LoadImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
