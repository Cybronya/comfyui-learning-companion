---
key: 图片生成/文生图/Qwen Image 2.1全能文生图处理生成工具_2102476988983365633.json
name: Qwen Image 2.1全能文生图处理生成工具_2102476988983365633
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1全能文生图处理生成工具_2102476988983365633.json
hash: 4be94b234f32e76d
coverage: 0.728571
learned_at: 2026-10-20 01:50:54
nodes: [PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, StringConcatenate, StringConcatenate, StringConcatenate, PrimitiveBoolean, PrimitiveBoolean, PrimitiveStringMultiline, PrimitiveStringMultiline, ComfySwitchNode, StringConcatenate, StringConcatenate, CLIPLoader, TextGenerate, RegexExtract, JsonExtractString, RegexMatch, ComfySwitchNode, RegexMatch, ComfySwitchNode, PrimitiveStringMultiline, StringCompare, ComfySwitchNode, ComfySwitchNode, VAELoader, TextEncodeQwenImage21, ResolutionSelector, EmptyLatentImage, KSampler, VAEDecode, PreviewImage, SaveImageAdvanced, SaveImage, JsonExtractString, StringCompare, ComfySwitchNode, UNETLoader, CLIPLoader, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1全能文生图处理生成工具_2102476988983365633.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1全能文生图处理生成工具_2102476988983365633.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（70 个）：
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `StringConcatenate`
- `StringConcatenate`
- `StringConcatenate`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `StringConcatenate`
- `StringConcatenate`
- `CLIPLoader`
- `TextGenerate`
- `RegexExtract`
- `JsonExtractString`
- `RegexMatch`
- `ComfySwitchNode`
- `RegexMatch`
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `StringCompare`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `VAELoader`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImageAdvanced`
- `SaveImage`
- `JsonExtractString`
- `StringCompare`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `CLIPLoader`
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

覆盖率 **73%**（51/70）

**有卡**：`StringConcatenate`、`PrimitiveBoolean`、`CLIPLoader`、`TextGenerate`、`RegexExtract`、`JsonExtractString`、`RegexMatch`、`StringCompare`、`VAELoader`、`TextEncodeQwenImage21`、`ResolutionSelector`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImageAdvanced`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
