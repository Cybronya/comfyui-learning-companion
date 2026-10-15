---
key: 图片生成/图生图/Qwen Image 2.1 参考人物姿势_2102935036923310081.json
name: Qwen Image 2.1 参考人物姿势_2102935036923310081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 参考人物姿势_2102935036923310081.json
hash: 8839c6f33fdd711e
coverage: 0.863636
learned_at: 2026-10-15 22:25:11
nodes: [CLIPLoader, CR Prompt Text, easy cleanGpuUsed, SaveImage, Note, QwenPERewriteT8, easy showAnything, TextEncodeQwenImage21, LoadImage, ResolutionSelector, LoadImage, VAELoader, AIO_Preprocessor, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, UNETLoader, QwenImage21SpectrumT8, KSampler, VAEDecode, QwenImage21Cache, EmptyLatentImage, ComfySwitchNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1 参考人物姿势_2102935036923310081.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 参考人物姿势_2102935036923310081.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `CLIPLoader`
- `CR Prompt Text`
- `easy cleanGpuUsed`
- `SaveImage`
- `Note`
- `QwenPERewriteT8`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `LoadImage`
- `ResolutionSelector`
- `LoadImage`
- `VAELoader`
- `AIO_Preprocessor`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`
- `UNETLoader` ★核心
- `QwenImage21SpectrumT8`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`

## 关键参数

- `seed` = `19960422`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`CLIPLoader`、`CR Prompt Text`、`easy cleanGpuUsed`、`SaveImage`、`QwenPERewriteT8`、`TextEncodeQwenImage21`、`LoadImage`、`ResolutionSelector`、`VAELoader`、`AIO_Preprocessor`、`QwenImage21BlockCacheT8`、`QwenImage21SageAttentionT8`、`UNETLoader`、`QwenImage21SpectrumT8`、`KSampler`、`VAEDecode`、`QwenImage21Cache`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
