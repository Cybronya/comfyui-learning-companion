---
key: 图片生成/文生图/Qwen image2.1 文生图_2099195780748890113.json
name: Qwen image2.1 文生图_2099195780748890113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image2.1 文生图_2099195780748890113.json
hash: 43921810464fd547
coverage: 0.8
learned_at: 2026-10-15 22:27:07
nodes: [VAEDecode, ShowText|pysssss, UNETLoader, CLIPLoader, VAELoader, QwenImage21Cache, Anything Everywhere3, Seed (rgthree), EmptyLatentImage, SaveImage, TextEncodeQwenImage21, KSampler, RHLLMChatNode, ResolutionSelector, JjkText]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "beta", "seed": 272655035358961, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen image2.1 文生图_2099195780748890113.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image2.1 文生图_2099195780748890113.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `VAEDecode` ★核心
- `ShowText|pysssss`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `Anything Everywhere3`
- `Seed (rgthree)`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `RHLLMChatNode`
- `ResolutionSelector`
- `JjkText`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `272655035358961`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`Seed (rgthree)`、`EmptyLatentImage`、`SaveImage`、`TextEncodeQwenImage21`、`KSampler`、`RHLLMChatNode`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
