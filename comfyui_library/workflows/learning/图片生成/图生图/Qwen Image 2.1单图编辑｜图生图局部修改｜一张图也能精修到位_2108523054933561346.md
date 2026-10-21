---
key: 图片生成/图生图/Qwen Image 2.1单图编辑｜图生图局部修改｜一张图也能精修到位_2108523054933561346.json
name: Qwen Image 2.1单图编辑｜图生图局部修改｜一张图也能精修到位_2108523054933561346
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1单图编辑｜图生图局部修改｜一张图也能精修到位_2108523054933561346.json
hash: 8136e13052ef7343
coverage: 0.904762
learned_at: 2026-10-21 00:42:24
nodes: [UNETLoader, QwenImage21Cache, Anything Everywhere3, VAEDecode, TextEncodeQwenImage21, EmptyLatentImage, ResolutionSelector, KSampler, CLIPLoader, CLIPLoader, VAELoader, ComfySwitchNode, Seed (rgthree), ResizeLongestToNode, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note, LoadImage, CR Text Concatenate, JjkText, TextGenerate, SaveImage, CompressImages, CR Prompt Text, ShowText|pysssss]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1单图编辑｜图生图局部修改｜一张图也能精修到位_2108523054933561346.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1单图编辑｜图生图局部修改｜一张图也能精修到位_2108523054933561346.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `Anything Everywhere3`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `KSampler` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `ComfySwitchNode`
- `Seed (rgthree)`
- `ResizeLongestToNode`
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
- `LoadImage`
- `CR Text Concatenate`
- `JjkText`
- `TextGenerate`
- `SaveImage`
- `CompressImages`
- `CR Prompt Text`
- `ShowText|pysssss`

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

覆盖率 **90%**（57/63）

**有卡**：`UNETLoader`、`QwenImage21Cache`、`VAEDecode`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`ResolutionSelector`、`KSampler`、`CLIPLoader`、`VAELoader`、`Seed (rgthree)`、`ResizeLongestToNode`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`、`LoadImage`、`CR Text Concatenate`、`TextGenerate`、`SaveImage`、`CompressImages`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
