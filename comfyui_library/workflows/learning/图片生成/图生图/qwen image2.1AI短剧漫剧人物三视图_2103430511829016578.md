---
key: 图片生成/图生图/qwen image2.1AI短剧漫剧人物三视图_2103430511829016578.json
name: qwen image2.1AI短剧漫剧人物三视图_2103430511829016578
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen image2.1AI短剧漫剧人物三视图_2103430511829016578.json
hash: ce9ceb36f0525e91
coverage: 0.655172
learned_at: 2026-10-21 00:46:03
nodes: [VAELoader, CLIPLoader, TextGenerateLTX2Prompt, TextEncodeQwenImage21, KSampler, easy setNode, VAEDecode, ShowText|pysssss, EmptyLatentImage, ComfySwitchNode, LoadImage, CLIPLoader, CLIPLoader, SetNode, SetNode, GetNode, ResolutionSelector, LayerUtility: ImageReelComposit, LayerUtility: ImageReel, UNETLoader, PreviewImage, Image Comparer (rgthree), QwenImage21Cache, Anything Everywhere3, LoraLoaderModelOnly, CR Prompt Text, Note, Note, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 778512812007155, "steps": 40, "width": 1024}
---

# 图片生成/图生图/qwen image2.1AI短剧漫剧人物三视图_2103430511829016578.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen image2.1AI短剧漫剧人物三视图_2103430511829016578.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
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
- `Note`
- `Note`
- `SaveImage`

## 关键参数

- `seed` = `778512812007155`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **66%**（19/29）

**有卡**：`VAELoader`、`CLIPLoader`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`KSampler`、`easy setNode`、`VAEDecode`、`EmptyLatentImage`、`LoadImage`、`ResolutionSelector`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`UNETLoader`、`QwenImage21Cache`、`LoraLoaderModelOnly`、`CR Prompt Text`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
