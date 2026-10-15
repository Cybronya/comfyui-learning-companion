---
key: 图片生成/图生图/（贞贞lora-图像编辑）Qwen Image 2.1 PE 姿势编辑_2105844300620853250.json
name: （贞贞lora-图像编辑）Qwen Image 2.1 PE 姿势编辑_2105844300620853250
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（贞贞lora-图像编辑）Qwen Image 2.1 PE 姿势编辑_2105844300620853250.json
hash: fe703fb0d0e8bd84
coverage: 0.868421
learned_at: 2026-10-15 22:26:03
nodes: [Note, CLIPLoader, VAELoader, Note, ResolutionSelector, ComfySwitchNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Note, VAEDecode, CR Prompt Text, QwenImage21SageAttentionT8, ConcatTextOfUtils, TextEncodeQwenImage21, LoadImage, CR Prompt Text, UNETLoader, EmptyLatentImage, SaveImage, LoraLoaderModelOnly, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, SaveImage, easy cleanGpuUsed, LoadImage, KSampler, LoadImage, SaveImage, SaveImage, SaveImage, QwenPERewriteT8, easy showAnything, CR Prompt Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
---

# 图片生成/图生图/（贞贞lora-图像编辑）Qwen Image 2.1 PE 姿势编辑_2105844300620853250.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（贞贞lora-图像编辑）Qwen Image 2.1 PE 姿势编辑_2105844300620853250.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `Note`
- `CLIPLoader`
- `VAELoader`
- `Note`
- `ResolutionSelector`
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Note`
- `VAEDecode` ★核心
- `CR Prompt Text`
- `QwenImage21SageAttentionT8`
- `ConcatTextOfUtils`
- `TextEncodeQwenImage21`
- `LoadImage`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `SaveImage`
- `easy cleanGpuUsed`
- `LoadImage`
- `KSampler` ★核心
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `QwenPERewriteT8`
- `easy showAnything`
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

覆盖率 **87%**（33/38）

**有卡**：`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`LoadImage`、`VAEDecode`、`CR Prompt Text`、`QwenImage21SageAttentionT8`、`ConcatTextOfUtils`、`TextEncodeQwenImage21`、`UNETLoader`、`EmptyLatentImage`、`SaveImage`、`LoraLoaderModelOnly`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`easy cleanGpuUsed`、`KSampler`、`QwenPERewriteT8`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
