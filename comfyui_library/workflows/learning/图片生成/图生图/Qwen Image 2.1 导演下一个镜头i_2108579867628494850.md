---
key: 图片生成/图生图/Qwen Image 2.1 导演下一个镜头i_2108579867628494850.json
name: Qwen Image 2.1 导演下一个镜头i_2108579867628494850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 导演下一个镜头i_2108579867628494850.json
hash: b6460bdd4f8355de
coverage: 1
learned_at: 2026-10-23 11:12:44
nodes: [CLIPLoader, VAELoader, UNETLoader, SeedNode, TextEncodeQwenImage21, QwenImage21Cache, KSampler, VAEDecode, SplitImageWithAlpha, LoadImage, CR Text, LoraLoaderModelOnly, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25}
---

# 图片生成/图生图/Qwen Image 2.1 导演下一个镜头i_2108579867628494850.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 导演下一个镜头i_2108579867628494850.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `SeedNode`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SplitImageWithAlpha`
- `LoadImage`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`

## 关键参数

- `seed` = `0`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`SeedNode`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`SplitImageWithAlpha`、`LoadImage`、`CR Text`、`LoraLoaderModelOnly`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
