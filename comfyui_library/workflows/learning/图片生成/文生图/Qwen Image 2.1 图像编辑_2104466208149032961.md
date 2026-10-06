---
key: 图片生成/文生图/Qwen Image 2.1 图像编辑_2104466208149032961.json
name: Qwen Image 2.1 图像编辑_2104466208149032961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 图像编辑_2104466208149032961.json
hash: ec2551a60b934668
coverage: 0.714286
learned_at: 2026-10-07 02:15:03
nodes: [CLIPLoader, VAELoader, UNETLoader, EmptyLatentImage, QwenImage21Cache, ComfySwitchNode, Anything Everywhere3, TextEncodeQwenImage21, PreviewAny, KSampler, VAEDecode, Image Comparer (rgthree), LayerUtility: ImageReel, LayerUtility: ImageReelComposit, TextGenerateLTX2Prompt, BatchImagesNode, CLIPLoader, LoadImage, LoadImage, CLIPLoader, CR Prompt Text, LoadImage, LoadImage, LoadImage, ResolutionSelector, PreviewImage, SaveImage, LoadImage]
patterns: []
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 600888457809348, "steps": 40, "width": 1024}
discoveries: [次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen Image 2.1 图像编辑_2104466208149032961.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 图像编辑_2104466208149032961.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `ComfySwitchNode`
- `Anything Everywhere3`
- `TextEncodeQwenImage21`
- `PreviewAny`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `TextGenerateLTX2Prompt`
- `BatchImagesNode`
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `PreviewImage`
- `SaveImage`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `600888457809348`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（20/28）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`EmptyLatentImage`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`TextGenerateLTX2Prompt`、`BatchImagesNode`、`LoadImage`、`ResolutionSelector`、`SaveImage`

**缺卡**（3）：`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
