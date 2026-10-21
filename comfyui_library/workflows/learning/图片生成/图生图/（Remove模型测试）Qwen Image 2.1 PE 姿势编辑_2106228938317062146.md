---
key: 图片生成/图生图/（Remove模型测试）Qwen Image 2.1 PE 姿势编辑_2106228938317062146.json
name: （Remove模型测试）Qwen Image 2.1 PE 姿势编辑_2106228938317062146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（Remove模型测试）Qwen Image 2.1 PE 姿势编辑_2106228938317062146.json
hash: d5d86e874d255618
coverage: 0.83871
learned_at: 2026-10-21 00:57:12
nodes: [Note, VAELoader, Note, easy showAnything, EmptyLatentImage, ResolutionSelector, ComfySwitchNode, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, QwenImage21Cache, QwenImage21SpectrumT8, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, Note, KSampler, VAEDecode, easy cleanGpuUsed, LoadImage, CR Prompt Text, CLIPLoader, UNETLoader, LoraLoaderModelOnly, QwenPERewriteT8, LoadImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
---

# 图片生成/图生图/（Remove模型测试）Qwen Image 2.1 PE 姿势编辑_2106228938317062146.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（Remove模型测试）Qwen Image 2.1 PE 姿势编辑_2106228938317062146.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `Note`
- `VAELoader`
- `Note`
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
- `Note`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `LoadImage`
- `CR Prompt Text`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `QwenPERewriteT8`
- `LoadImage`
- `SaveImage`

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

覆盖率 **84%**（26/31）

**有卡**：`VAELoader`、`EmptyLatentImage`、`ResolutionSelector`、`TextEncodeQwenImage21`、`LoadImage`、`QwenImage21Cache`、`QwenImage21SpectrumT8`、`QwenImage21BlockCacheT8`、`QwenImage21SageAttentionT8`、`KSampler`、`VAEDecode`、`easy cleanGpuUsed`、`CR Prompt Text`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`QwenPERewriteT8`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
