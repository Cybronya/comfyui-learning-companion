---
key: 图片生成/图生图/（Remove模型）Qwen Image 2.1 PE 姿势编辑_2106290030498111489.json
name: （Remove模型）Qwen Image 2.1 PE 姿势编辑_2106290030498111489
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（Remove模型）Qwen Image 2.1 PE 姿势编辑_2106290030498111489.json
hash: 7bdd37f125d06b62
coverage: 0.896552
learned_at: 2026-10-21 00:57:12
nodes: [Note, VAELoader, easy showAnything, EmptyLatentImage, ResolutionSelector, ComfySwitchNode, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, QwenImage21Cache, QwenImage21SpectrumT8, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, KSampler, VAEDecode, easy cleanGpuUsed, CLIPLoader, UNETLoader, LoraLoaderModelOnly, LoadImage, SaveImage, QwenPERewriteT8, LoadImage, CR Prompt Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
---

# 图片生成/图生图/（Remove模型）Qwen Image 2.1 PE 姿势编辑_2106290030498111489.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（Remove模型）Qwen Image 2.1 PE 姿势编辑_2106290030498111489.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `Note`
- `VAELoader`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `QwenImage21Cache`
- `QwenImage21SpectrumT8`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `SaveImage`
- `QwenPERewriteT8`
- `LoadImage`
- `CR Prompt Text`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `19960422`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`VAELoader`、`EmptyLatentImage`、`ResolutionSelector`、`TextEncodeQwenImage21`、`LoadImage`、`QwenImage21Cache`、`QwenImage21SpectrumT8`、`QwenImage21BlockCacheT8`、`QwenImage21SageAttentionT8`、`KSampler`、`VAEDecode`、`easy cleanGpuUsed`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`SaveImage`、`QwenPERewriteT8`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
