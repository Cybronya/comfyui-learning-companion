---
key: 图片生成/图生图/BFS换脸6步加速版Qwen_Image_2.1图像编辑_2110554314409332737.json
name: BFS换脸6步加速版Qwen_Image_2.1图像编辑_2110554314409332737
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/BFS换脸6步加速版Qwen_Image_2.1图像编辑_2110554314409332737.json
hash: 2e5c3a9b7474e9c8
coverage: 0.84375
learned_at: 2026-10-23 10:51:27
nodes: [CLIPLoader, VAELoader, Note, easy showAnything, EmptyLatentImage, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, QwenImage21SageAttentionT8, Note, QwenPERewriteT8, UNETLoader, LoraLoaderModelOnly, VAEDecode, ResolutionSelector, easy cleanGpuUsed, CR Prompt Text, ComfySwitchNode, CR Prompt Text, LoadImage, SaveImage, KSampler, LoraLoaderBypassModelOnly, QwenImage21Cache, LoadImage, ConcatTextOfUtils, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 796238619326657, "steps": 6, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/BFS换脸6步加速版Qwen_Image_2.1图像编辑_2110554314409332737.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/BFS换脸6步加速版Qwen_Image_2.1图像编辑_2110554314409332737.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `CLIPLoader`
- `VAELoader`
- `Note`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `QwenImage21SageAttentionT8`
- `Note`
- `QwenPERewriteT8`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `ResolutionSelector`
- `easy cleanGpuUsed`
- `CR Prompt Text`
- `ComfySwitchNode`
- `CR Prompt Text`
- `LoadImage`
- `SaveImage`
- `KSampler` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `QwenImage21Cache`
- `LoadImage`
- `ConcatTextOfUtils`
- `Note`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `796238619326657`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（27/32）

**有卡**：`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`LoadImage`、`QwenImage21SageAttentionT8`、`QwenPERewriteT8`、`UNETLoader`、`LoraLoaderModelOnly`、`VAEDecode`、`ResolutionSelector`、`easy cleanGpuUsed`、`CR Prompt Text`、`SaveImage`、`KSampler`、`LoraLoaderBypassModelOnly`、`QwenImage21Cache`、`ConcatTextOfUtils`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
