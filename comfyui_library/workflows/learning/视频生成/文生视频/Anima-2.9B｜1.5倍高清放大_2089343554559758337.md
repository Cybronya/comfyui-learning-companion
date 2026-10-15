---
key: 视频生成/文生视频/Anima-2.9B｜1.5倍高清放大_2089343554559758337.json
name: Anima-2.9B｜1.5倍高清放大_2089343554559758337
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Anima-2.9B｜1.5倍高清放大_2089343554559758337.json
hash: 3a61887323759ece
coverage: 1
learned_at: 2026-10-15 22:44:02
nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, PathchSageAttentionKJ, UNETLoader, FluxResolutionNode, VAELoaderKJ, CLIPLoader, KSampler, CLIPTextEncode, LatentUpscaleBy, VAEDecode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 5, "denoise": 1, "height": 1024, "sampler_name": "res_multistep", "scheduler": "linear_quadratic", "seed": 440806743335793, "steps": 28, "width": 1024}
---

# 视频生成/文生视频/Anima-2.9B｜1.5倍高清放大_2089343554559758337.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Anima-2.9B｜1.5倍高清放大_2089343554559758337.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `SaveImage`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `FluxResolutionNode`
- `VAELoaderKJ`
- `CLIPLoader`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `LatentUpscaleBy`
- `VAEDecode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `440806743335793`
- `steps` = `28`
- `cfg` = `5`
- `sampler_name` = `res_multistep`
- `scheduler` = `linear_quadratic`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`SaveImage`、`PathchSageAttentionKJ`、`UNETLoader`、`FluxResolutionNode`、`VAELoaderKJ`、`CLIPLoader`、`LatentUpscaleBy`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LatentUpscaleBy、VAELoaderKJ
