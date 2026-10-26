---
key: 图片生成/图生图/Qwen_2.1_角色替换_换人_2114261197271953410.json
name: Qwen_2.1_角色替换_换人_2114261197271953410
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_2.1_角色替换_换人_2114261197271953410.json
hash: d32a9e72a7157149
coverage: 0.923077
learned_at: 2026-10-26 22:03:34
nodes: [VAELoader, VAEDecode, KSampler, QwenImage21Cache, LoadImage, LoadImage, SaveImage, TextEncodeQwenImage21, LoraLoaderModelOnly, UNETLoader, CLIPLoader, LoadImage, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1063767470927732, "steps": 40}
---

# 图片生成/图生图/Qwen_2.1_角色替换_换人_2114261197271953410.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_2.1_角色替换_换人_2114261197271953410.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `VAELoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `QwenImage21Cache`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoadImage`
- `PreviewImage`

## 关键参数

- `seed` = `1063767470927732`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`VAELoader`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`LoadImage`、`SaveImage`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
