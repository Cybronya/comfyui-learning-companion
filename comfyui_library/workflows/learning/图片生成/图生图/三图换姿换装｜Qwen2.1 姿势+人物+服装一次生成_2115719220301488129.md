---
key: 图片生成/图生图/三图换姿换装｜Qwen2.1 姿势+人物+服装一次生成_2115719220301488129.json
name: 三图换姿换装｜Qwen2.1 姿势+人物+服装一次生成_2115719220301488129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/三图换姿换装｜Qwen2.1 姿势+人物+服装一次生成_2115719220301488129.json
hash: 2b166933ba1dc48a
coverage: 1
learned_at: 2026-10-30 17:52:10
nodes: [LoadImage, PoseGallery, UNETLoader, QwenImage21Cache, CLIPLoader, VAELoader, TextEncodeQwenImage21, KSampler, VAEDecode, SaveImage, LoraLoaderModelOnly, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 20261029, "steps": 25}
---

# 图片生成/图生图/三图换姿换装｜Qwen2.1 姿势+人物+服装一次生成_2115719220301488129.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/三图换姿换装｜Qwen2.1 姿势+人物+服装一次生成_2115719220301488129.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `LoadImage`
- `PoseGallery`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `20261029`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`LoadImage`、`PoseGallery`、`UNETLoader`、`QwenImage21Cache`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`SaveImage`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
