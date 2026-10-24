---
key: 图片生成/图生图/自动抠图 Qwen-image2.1_2112044955593166850.json
name: 自动抠图 Qwen-image2.1_2112044955593166850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/自动抠图 Qwen-image2.1_2112044955593166850.json
hash: 42f50e6530c6665d
coverage: 0.933333
learned_at: 2026-10-23 13:24:02
nodes: [UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, VAEDecode, SaveImage, CR Text, CR Text, CR Text, LoadImage, LayerUtility: TextJoin]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 226811893419253, "steps": 25, "width": 1024}
---

# 图片生成/图生图/自动抠图 Qwen-image2.1_2112044955593166850.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/自动抠图 Qwen-image2.1_2112044955593166850.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `SaveImage`
- `CR Text`
- `CR Text`
- `CR Text`
- `LoadImage`
- `LayerUtility: TextJoin`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `226811893419253`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImage`、`CR Text`、`LoadImage`、`LayerUtility: TextJoin`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
