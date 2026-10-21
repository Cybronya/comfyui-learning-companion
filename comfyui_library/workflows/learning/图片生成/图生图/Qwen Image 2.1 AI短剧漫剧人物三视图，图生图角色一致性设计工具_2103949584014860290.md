---
key: 图片生成/图生图/Qwen Image 2.1 AI短剧漫剧人物三视图，图生图角色一致性设计工具_2103949584014860290.json
name: Qwen Image 2.1 AI短剧漫剧人物三视图，图生图角色一致性设计工具_2103949584014860290
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 AI短剧漫剧人物三视图，图生图角色一致性设计工具_2103949584014860290.json
hash: 2396567952735f71
coverage: 0.785714
learned_at: 2026-10-21 00:42:04
nodes: [VAELoader, CLIPLoader, TextGenerateLTX2Prompt, TextEncodeQwenImage21, KSampler, easy setNode, VAEDecode, ShowText|pysssss, EmptyLatentImage, ComfySwitchNode, LoadImage, CLIPLoader, CLIPLoader, SetNode, SetNode, GetNode, ResolutionSelector, LayerUtility: ImageReelComposit, LayerUtility: ImageReel, UNETLoader, PreviewImage, Image Comparer (rgthree), QwenImage21Cache, Anything Everywhere3, LoraLoaderModelOnly, CR Prompt Text, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1 AI短剧漫剧人物三视图，图生图角色一致性设计工具_2103949584014860290.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 AI短剧漫剧人物三视图，图生图角色一致性设计工具_2103949584014860290.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `VAELoader`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `easy setNode`
- `VAEDecode` ★核心
- `ShowText|pysssss`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `CLIPLoader`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `ResolutionSelector`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReel`
- `UNETLoader` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `QwenImage21Cache`
- `Anything Everywhere3`
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `SaveImage`
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

覆盖率 **79%**（44/56）

**有卡**：`VAELoader`、`CLIPLoader`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`KSampler`、`easy setNode`、`VAEDecode`、`EmptyLatentImage`、`LoadImage`、`ResolutionSelector`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`UNETLoader`、`QwenImage21Cache`、`LoraLoaderModelOnly`、`CR Prompt Text`、`SaveImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
