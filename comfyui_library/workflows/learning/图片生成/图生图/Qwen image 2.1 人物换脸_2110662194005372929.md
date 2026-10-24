---
key: 图片生成/图生图/Qwen image 2.1 人物换脸_2110662194005372929.json
name: Qwen image 2.1 人物换脸_2110662194005372929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 人物换脸_2110662194005372929.json
hash: 565c2425c6de74f6
coverage: 0.909091
learned_at: 2026-10-23 11:13:56
nodes: [CLIPLoader, VAELoader, ImageConcanate, Image Comparer (rgthree), SaveImage, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, QwenImage21Cache, EmptyLatentImage, Latent Switch (JPS), ImageConcanate, LoadImage, UNETLoader, LoadImage, TextEncodeQwenImage21, CR Text, LoraLoaderModelOnly, KSampler, VAEDecode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image 2.1 人物换脸_2110662194005372929.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 人物换脸_2110662194005372929.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `CLIPLoader`
- `VAELoader`
- `ImageConcanate`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `Latent Switch (JPS)`
- `ImageConcanate`
- `LoadImage`
- `UNETLoader` ★核心
- `LoadImage`
- `TextEncodeQwenImage21`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `999`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`CLIPLoader`、`VAELoader`、`ImageConcanate`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ResolutionSelector`、`EmptyLatentImage`、`QwenImage21Cache`、`Latent Switch (JPS)`、`LoadImage`、`UNETLoader`、`TextEncodeQwenImage21`、`CR Text`、`LoraLoaderModelOnly`、`KSampler`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
