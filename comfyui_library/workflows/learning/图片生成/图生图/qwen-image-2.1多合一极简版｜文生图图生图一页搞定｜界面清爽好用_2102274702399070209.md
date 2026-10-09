---
key: 图片生成/图生图/qwen-image-2.1多合一极简版｜文生图图生图一页搞定｜界面清爽好用_2102274702399070209.json
name: qwen-image-2.1多合一极简版｜文生图图生图一页搞定｜界面清爽好用_2102274702399070209.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-2.1多合一极简版｜文生图图生图一页搞定｜界面清爽好用_2102274702399070209.json
hash: 67e28f90277d6a0e
coverage: 0.835821
learned_at: 2026-10-09 22:27:10
nodes: [Seed (rgthree), UNETLoader, SetNode, CLIPLoader, CLIPLoader, EmptyLatentImage, SetNode, QwenImage21Cache, CLIPLoader, KSampler, VAELoader, ResolutionSelector, VAEDecode, SaveImage, Fast Groups Bypasser (rgthree), TextEncodeQwenImage21, TextGenerateLTX2Prompt, ImageBatchMultiV2, MiniMaxH3EasyMediaSplitter, MiniMaxH3EasyMediaLoader, GetNode, PreviewAny, MiniMaxH3EasyMediaSplitter, CR Prompt Text, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [CR Prompt Text, Seed (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen-image-2.1多合一极简版｜文生图图生图一页搞定｜界面清爽好用_2102274702399070209.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102274702399070209.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（67 个）：
- `Seed (rgthree)`
- `UNETLoader` ★核心
- `SetNode`
- `CLIPLoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `SetNode`
- `QwenImage21Cache`
- `CLIPLoader`
- `KSampler` ★核心
- `VAELoader`
- `ResolutionSelector`
- `VAEDecode` ★核心
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `ImageBatchMultiV2`
- `MiniMaxH3EasyMediaSplitter`
- `MiniMaxH3EasyMediaLoader`
- `GetNode`
- `PreviewAny`
- `MiniMaxH3EasyMediaSplitter`
- `CR Prompt Text`
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

覆盖率 **84%**（56/67）

**有卡**：`UNETLoader`、`CLIPLoader`、`EmptyLatentImage`、`QwenImage21Cache`、`KSampler`、`VAELoader`、`ResolutionSelector`、`VAEDecode`、`SaveImage`、`TextEncodeQwenImage21`、`TextGenerateLTX2Prompt`、`ImageBatchMultiV2`、`MiniMaxH3EasyMediaSplitter`、`MiniMaxH3EasyMediaLoader`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**缺卡**（2）：`CR Prompt Text`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
