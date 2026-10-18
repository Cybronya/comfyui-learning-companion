---
key: 视频生成/图生视频/换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2102960653840510977.json
name: 换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2102960653840510977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2102960653840510977.json
hash: 66f8b42b9b81a41a
coverage: 0.842105
learned_at: 2026-10-17 02:29:58
nodes: [ComfySwitchNode, VAEDecode, KSampler, QwenImage21Cache, TextGenerateLTX2Prompt, TextEncodeQwenImage21, UNETLoader, BatchImagesNode, CLIPLoader, CLIPLoader, VAELoader, EmptyLatentImage, ResolutionSelector, JjkText, SaveImage, LoadImage, LoadImage, EmptyImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 596250188102056, "steps": 50, "width": 1024}
---

# 视频生成/图生视频/换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2102960653840510977.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2102960653840510977.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `QwenImage21Cache`
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `JjkText`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `EmptyImage`
- `PreviewImage`

## 关键参数

- `seed` = `596250188102056`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`UNETLoader`、`BatchImagesNode`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`ResolutionSelector`、`SaveImage`、`LoadImage`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
