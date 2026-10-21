---
key: 图片生成/文生图/qwen2.1 文生图_2102025901952299009.json
name: qwen2.1 文生图_2102025901952299009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen2.1 文生图_2102025901952299009.json
hash: 055ffefe5e9bbf53
coverage: 0.875
learned_at: 2026-10-20 01:51:58
nodes: [UNETLoader, VAELoader, CLIPLoader, VAEDecode, EmptyLatentImage, TextGenerateLTX2Prompt, KSampler, easy showAnything, SaveImage, ComfySwitchNode, TextEncodeQwenImage21, CLIPLoader, RH_LLMAPI_Pro_Node, Text Multiline, Text Multiline, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 345895800121548, "steps": 50, "width": 768}
---

# 图片生成/文生图/qwen2.1 文生图_2102025901952299009.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen2.1 文生图_2102025901952299009.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `TextGenerateLTX2Prompt`
- `KSampler` ★核心
- `easy showAnything`
- `SaveImage`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `RH_LLMAPI_Pro_Node`
- `Text Multiline`
- `Text Multiline`
- `ResolutionSelector`

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `345895800121548`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`UNETLoader`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`EmptyLatentImage`、`TextGenerateLTX2Prompt`、`KSampler`、`SaveImage`、`TextEncodeQwenImage21`、`RH_LLMAPI_Pro_Node`、`Text Multiline`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
