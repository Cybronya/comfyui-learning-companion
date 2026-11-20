---
key: 图片生成/图生图/qwen2.1漫剧角色三视图生成｜漫剧人设资料卡一键出图_2114765300842450946.json
name: qwen2.1漫剧角色三视图生成｜漫剧人设资料卡一键出图_2114765300842450946
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen2.1漫剧角色三视图生成｜漫剧人设资料卡一键出图_2114765300842450946.json
hash: cc214716899b7eb3
coverage: 0.866667
learned_at: 2026-10-30 17:51:48
nodes: [EmptyLatentImage, ResolutionSelector, UNETLoader, VAEDecode, CLIPLoader, CLIPLoader, KSampler, TextEncodeQwenImage21, VAELoader, ComfySwitchNode, SaveImage, CR Prompt Text, LoadImage, LoadImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 280648360900381, "steps": 25, "width": 1024}
---

# 图片生成/图生图/qwen2.1漫剧角色三视图生成｜漫剧人设资料卡一键出图_2114765300842450946.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen2.1漫剧角色三视图生成｜漫剧人设资料卡一键出图_2114765300842450946.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `VAELoader`
- `ComfySwitchNode`
- `SaveImage`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `PreviewImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `280648360900381`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`EmptyLatentImage`、`ResolutionSelector`、`UNETLoader`、`VAEDecode`、`CLIPLoader`、`KSampler`、`TextEncodeQwenImage21`、`VAELoader`、`SaveImage`、`CR Prompt Text`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
