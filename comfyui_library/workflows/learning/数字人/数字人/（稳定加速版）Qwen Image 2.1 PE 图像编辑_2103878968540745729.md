---
key: 数字人/数字人/（稳定加速版）Qwen Image 2.1 PE 图像编辑_2103878968540745729.json
name: （稳定加速版）Qwen Image 2.1 PE 图像编辑_2103878968540745729
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/（稳定加速版）Qwen Image 2.1 PE 图像编辑_2103878968540745729.json
hash: 9bfe169d1ca348a4
coverage: 0.875
learned_at: 2026-10-19 00:41:14
nodes: [VAELoader, ResolutionSelector, QwenPERewriteT8, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, Note, VAEDecode, CLIPLoader, UNETLoader, QwenImage21Cache, Note, easy showAnything, QwenImage21SpectrumT8, Lora Loader Stack (rgthree), LoadImage, CR Prompt Text, ComfySwitchNode, EmptyLatentImage, KSampler, SaveImage, easy cleanGpuUsed, UNETLoader, CLIPLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 414462163208523, "steps": 40, "width": 1024}
---

# 数字人/数字人/（稳定加速版）Qwen Image 2.1 PE 图像编辑_2103878968540745729.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/（稳定加速版）Qwen Image 2.1 PE 图像编辑_2103878968540745729.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `VAELoader`
- `ResolutionSelector`
- `QwenPERewriteT8`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`
- `Note`
- `VAEDecode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `Note`
- `easy showAnything`
- `QwenImage21SpectrumT8`
- `Lora Loader Stack (rgthree)`
- `LoadImage`
- `CR Prompt Text`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `SaveImage`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `CLIPLoader`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `414462163208523`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（28/32）

**有卡**：`VAELoader`、`ResolutionSelector`、`QwenPERewriteT8`、`TextEncodeQwenImage21`、`LoadImage`、`QwenImage21BlockCacheT8`、`QwenImage21SageAttentionT8`、`VAEDecode`、`CLIPLoader`、`UNETLoader`、`QwenImage21Cache`、`QwenImage21SpectrumT8`、`Lora Loader Stack (rgthree)`、`CR Prompt Text`、`EmptyLatentImage`、`KSampler`、`SaveImage`、`easy cleanGpuUsed`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
