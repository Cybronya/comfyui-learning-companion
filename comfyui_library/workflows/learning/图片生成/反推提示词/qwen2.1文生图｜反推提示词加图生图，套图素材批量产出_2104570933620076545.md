---
key: 图片生成/反推提示词/qwen2.1文生图｜反推提示词加图生图，套图素材批量产出_2104570933620076545.json
name: qwen2.1文生图｜反推提示词加图生图，套图素材批量产出_2104570933620076545
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/qwen2.1文生图｜反推提示词加图生图，套图素材批量产出_2104570933620076545.json
hash: e95045ae99a7fbff
coverage: 0.868852
learned_at: 2026-10-07 02:41:05
nodes: [UNETLoader, CLIPLoader, VAELoader, VAEDecode, ResolutionSelector, PreviewAny, StringReplace, EmptyLatentImage, TextEncodeQwenImage21, KSampler, SaveImage, StringConstantMultiline, StringConstantMultiline, CLIPLoader, TextGenerate, easy showAnything, easy showAnything, StringFunction|pysssss, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [StringFunction|pysssss]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/反推提示词/qwen2.1文生图｜反推提示词加图生图，套图素材批量产出_2104570933620076545.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/qwen2.1文生图｜反推提示词加图生图，套图素材批量产出_2104570933620076545.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（61 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `ResolutionSelector`
- `PreviewAny`
- `StringReplace`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `SaveImage`
- `StringConstantMultiline`
- `StringConstantMultiline`
- `CLIPLoader`
- `TextGenerate`
- `easy showAnything`
- `easy showAnything`
- `StringFunction|pysssss`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
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

覆盖率 **87%**（53/61）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`ResolutionSelector`、`StringReplace`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`KSampler`、`SaveImage`、`StringConstantMultiline`、`TextGenerate`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**缺卡**（1）：`StringFunction|pysssss`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
