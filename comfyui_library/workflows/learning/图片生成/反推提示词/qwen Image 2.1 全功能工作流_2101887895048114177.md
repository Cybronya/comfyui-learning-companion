---
key: 图片生成/反推提示词/qwen Image 2.1 全功能工作流_2101887895048114177.json
name: qwen Image 2.1 全功能工作流_2101887895048114177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/qwen Image 2.1 全功能工作流_2101887895048114177.json
hash: a463d17d0c3e709d
coverage: 0.897436
learned_at: 2026-10-26 22:01:07
nodes: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, easy setNode, VAEDecode, LoadImage, SaveImage, Anything Everywhere3, LoadImage, PreviewImage, Image Comparer (rgthree), UNETLoader, QwenImage21Cache, CLIPLoader, VAELoader, EmptyLatentImage, ResolutionSelector, llama_cpp_model_loader, llama_cpp_instruct_adv, llama_cpp_parameters, easy showAnything, VAEDecode, KSampler, SaveImage, LoadImage, TextEncodeQwenImage21, RepeatLatentBatch, KSampler, SaveImage, KSampler, TextEncodeQwenImage21, CR Prompt Text, LoadImage, CR Prompt Text, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, LoadImage, VAEDecode]
patterns: []
missing: []
parameters: {"batch_size": 2, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 585680792055306, "steps": 25, "width": 1024}
---

# 图片生成/反推提示词/qwen Image 2.1 全功能工作流_2101887895048114177.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/qwen Image 2.1 全功能工作流_2101887895048114177.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `easy setNode`
- `VAEDecode` ★核心
- `LoadImage`
- `SaveImage`
- `Anything Everywhere3`
- `LoadImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `llama_cpp_parameters`
- `easy showAnything`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `RepeatLatentBatch`
- `KSampler` ★核心
- `SaveImage`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `CR Prompt Text`
- `LoadImage`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `VAEDecode` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `2`
- `seed` = `585680792055306`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（35/39）

**有卡**：`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`easy setNode`、`VAEDecode`、`LoadImage`、`SaveImage`、`UNETLoader`、`QwenImage21Cache`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`ResolutionSelector`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`llama_cpp_parameters`、`KSampler`、`TextEncodeQwenImage21`、`RepeatLatentBatch`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
