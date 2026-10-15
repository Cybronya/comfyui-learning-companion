---
key: 视频生成/文生视频/Qwen_Image_2.1_文生图-PE版_2106926003867185154.json
name: Qwen_Image_2.1_文生图-PE版_2106926003867185154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Qwen_Image_2.1_文生图-PE版_2106926003867185154.json
hash: 1be51d6dd6fed1ce
coverage: 0.823529
learned_at: 2026-10-15 22:46:52
nodes: [QwenImage21Cache, CLIPLoader, UNETLoader, TextEncodeQwenImage21, EmptyLatentImage, ComfySwitchNode, VAELoader, easy showAnything, QwenPERewriteT8, KSampler, easy cleanGpuUsed, VAEDecode, SaveImage, ResolutionSelector, CR Prompt Text, EmptyImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 263451641996201, "steps": 40, "width": 1024}
---

# 视频生成/文生视频/Qwen_Image_2.1_文生图-PE版_2106926003867185154.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Qwen_Image_2.1_文生图-PE版_2106926003867185154.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `QwenImage21Cache`
- `CLIPLoader`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAELoader`
- `easy showAnything`
- `QwenPERewriteT8`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `SaveImage`
- `ResolutionSelector`
- `CR Prompt Text`
- `EmptyImage`
- `PreviewImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `263451641996201`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`UNETLoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAELoader`、`QwenPERewriteT8`、`KSampler`、`easy cleanGpuUsed`、`VAEDecode`、`SaveImage`、`ResolutionSelector`、`CR Prompt Text`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
