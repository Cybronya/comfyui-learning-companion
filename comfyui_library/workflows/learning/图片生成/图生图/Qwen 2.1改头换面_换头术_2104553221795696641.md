---
key: 图片生成/图生图/Qwen 2.1改头换面_换头术_2104553221795696641.json
name: Qwen 2.1改头换面_换头术_2104553221795696641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen 2.1改头换面_换头术_2104553221795696641.json
hash: 8546044f213b9024
coverage: 1
learned_at: 2026-10-21 00:42:01
nodes: [VAELoader, VAEDecode, LoadImage, LoadImage, CLIPLoader, TextEncodeQwenImage21, KSampler, UNETLoader, QwenImage21Cache, LoraLoaderModelOnly, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 309962691144888, "steps": 40}
---

# 图片生成/图生图/Qwen 2.1改头换面_换头术_2104553221795696641.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen 2.1改头换面_换头术_2104553221795696641.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
- `VAELoader`
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`

## 关键参数

- `seed` = `309962691144888`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`VAELoader`、`VAEDecode`、`LoadImage`、`CLIPLoader`、`TextEncodeQwenImage21`、`KSampler`、`UNETLoader`、`QwenImage21Cache`、`LoraLoaderModelOnly`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
