---
key: 图片生成/图生图/Qwen Image 2.1单图编辑产品展示图生图处理工具_2102489354336821249.json
name: Qwen Image 2.1单图编辑产品展示图生图处理工具_2102489354336821249.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1单图编辑产品展示图生图处理工具_2102489354336821249.json
hash: 0aacdbd7c9d0584c
coverage: 0.844444
learned_at: 2026-10-09 22:19:28
nodes: [LoadImage, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, VAEDecode, SaveImage, ResizeLongestToNode, UNETLoader, VAELoader, CLIPLoader, QwenImage21Cache, TextEncodeQwenImage21, RHLLMChatNode, ShowText|pysssss, CR Prompt Text, KSampler, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1单图编辑产品展示图生图处理工具_2102489354336821249.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102489354336821249.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（45 个）：
- `LoadImage`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `SaveImage`
- `ResizeLongestToNode`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `RHLLMChatNode`
- `ShowText|pysssss`
- `CR Prompt Text`
- `KSampler` ★核心
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

覆盖率 **84%**（38/45）

**有卡**：`LoadImage`、`ResolutionSelector`、`EmptyLatentImage`、`VAEDecode`、`SaveImage`、`ResizeLongestToNode`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`RHLLMChatNode`、`KSampler`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
