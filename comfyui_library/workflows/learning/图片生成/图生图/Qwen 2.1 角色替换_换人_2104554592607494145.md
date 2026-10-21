---
key: 图片生成/图生图/Qwen 2.1 角色替换_换人_2104554592607494145.json
name: Qwen 2.1 角色替换_换人_2104554592607494145
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen 2.1 角色替换_换人_2104554592607494145.json
hash: 39e04fd69cfe6b7d
coverage: 1
learned_at: 2026-10-21 00:41:58
nodes: [VAELoader, VAEDecode, KSampler, QwenImage21Cache, LoadImage, LoadImage, SaveImage, TextEncodeQwenImage21, LoraLoaderModelOnly, UNETLoader, CLIPLoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 631895203758443, "steps": 40}
---

# 图片生成/图生图/Qwen 2.1 角色替换_换人_2104554592607494145.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen 2.1 角色替换_换人_2104554592607494145.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
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

## 关键参数

- `seed` = `631895203758443`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`VAELoader`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`LoadImage`、`SaveImage`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
