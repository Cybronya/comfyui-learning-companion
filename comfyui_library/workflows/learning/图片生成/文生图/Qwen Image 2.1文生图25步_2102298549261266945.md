---
key: 图片生成/文生图/Qwen Image 2.1文生图25步_2102298549261266945.json
name: Qwen Image 2.1文生图25步_2102298549261266945
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图25步_2102298549261266945.json
hash: 97e1ec4da0d6aece
coverage: 0.894737
learned_at: 2026-10-10 20:58:53
nodes: [VAELoader, TextEncodeQwenImage21, KSampler, VAEDecode, EmptyLatentImage, CLIPLoader, UNETLoader, ResolutionSelector, easy seed, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage, Text Multiline]
patterns: [text_to_image]
missing: [Text Multiline, easy seed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1文生图25步_2102298549261266945.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图25步_2102298549261266945.json`

## 结构

**节点**（38 个）：
- `VAELoader`
- `TextEncodeQwenImage21`
- `KSampler`
- `VAEDecode`
- `EmptyLatentImage`
- `CLIPLoader`
- `UNETLoader`
- `ResolutionSelector`
- `easy seed`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `KSampler`
- `EmptyLatentImage`
- `JjkText`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `solarL_SaveImagesToZip`
- `VAEDecode`
- `CLIPLoader`
- `VAELoader`
- `Note`
- `SaveImage`
- `Text Multiline`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4.5`
- `denoise` = `1`
- `height` = `80`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `seed` = `598626327129635`
- `steps` = `4`
- `width` = `80`

## 知识

覆盖率 **89%**（34/38）

**有卡**：`VAELoader`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`CLIPLoader`、`UNETLoader`、`ResolutionSelector`、`easy seed`、`LoraLoaderModelOnly`、`JjkText`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（2）：`Text Multiline`、`easy seed`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
