---
key: 图片生成/图生图/多角度转换-Qwen_image2.1图像编辑_2114522210210766849.json
name: 多角度转换-Qwen_image2.1图像编辑_2114522210210766849
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/多角度转换-Qwen_image2.1图像编辑_2114522210210766849.json
hash: b86be81e83984c3f
coverage: 0.759259
learned_at: 2026-10-26 22:05:55
nodes: [GetNode, VAELoader, GetNode, TextEncodeQwenImage21, QwenImage21Cache, EmptyLatentImage, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, VAEDecode, SaveImageAdvanced, CR Text, CR Text, LoadImage, ResolutionSelector, ImageResizeKJv2, SetNode, SetNode, SetNode, CR Text, CR Text, CR Text, CR Text, ImpactSwitch, CR Text, CR Text, CR Text, CR Text, ImpactSwitch, CR Text, CR Text Concatenate, ShowText|pysssss, ttN concat, CR Text, GetNode, UNETLoader, CLIPLoader, MarkdownNote, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), ImpactSwitch, GetNode, LayerUtility: ImageRemoveAlpha, SaveImage, Image Comparer (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "deis_2m", "scheduler": "simple", "seed": 889866864724872, "steps": 40, "width": 1024}
---

# 图片生成/图生图/多角度转换-Qwen_image2.1图像编辑_2114522210210766849.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/多角度转换-Qwen_image2.1图像编辑_2114522210210766849.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `GetNode`
- `VAELoader`
- `GetNode`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `CR Text`
- `CR Text`
- `LoadImage`
- `ResolutionSelector`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `SetNode`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `ImpactSwitch`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `ImpactSwitch`
- `CR Text`
- `CR Text Concatenate`
- `ShowText|pysssss`
- `ttN concat`
- `CR Text`
- `GetNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `MarkdownNote`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `ImpactSwitch`
- `GetNode`
- `LayerUtility: ImageRemoveAlpha`
- `SaveImage`
- `Image Comparer (rgthree)`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `889866864724872`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `deis_2m`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（41/54）

**有卡**：`VAELoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`KSampler`、`VAEDecode`、`SaveImageAdvanced`、`CR Text`、`LoadImage`、`ResolutionSelector`、`ImageResizeKJv2`、`CR Text Concatenate`、`ttN concat`、`UNETLoader`、`CLIPLoader`、`Label (rgthree)`、`LayerUtility: ImageRemoveAlpha`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
