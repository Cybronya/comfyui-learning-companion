---
key: qwen2.1文生图_2104275580962304002.json
name: qwen2.1文生图_2104275580962304002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen2.1文生图_2104275580962304002.json
hash: 03e2c7ce7617bebc
coverage: 0.909091
learned_at: 2026-10-10 20:59:25
nodes: [ResolutionSelector, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, SaveImage, VAELoader, CLIPLoader, UNETLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 331652005049054, "steps": 25, "width": 1024}
---

# qwen2.1文生图_2104275580962304002.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen2.1文生图_2104275580962304002.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `SaveImage`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `331652005049054`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`ResolutionSelector`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`SaveImage`、`VAELoader`、`CLIPLoader`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
