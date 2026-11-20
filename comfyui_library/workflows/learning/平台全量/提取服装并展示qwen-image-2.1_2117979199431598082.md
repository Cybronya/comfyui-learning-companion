---
key: 平台全量/提取服装并展示qwen-image-2.1_2117979199431598082.json
name: 提取服装并展示qwen-image-2.1_2117979199431598082
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/提取服装并展示qwen-image-2.1_2117979199431598082.json
hash: 4058cbcc6ce5aa1a
coverage: 1
learned_at: 2026-11-14 02:09:56
nodes: [UNETLoader, CLIPLoader, VAEDecode, LoadImage, VAELoader, QwenImage21Cache, SaveImage, KSampler, CR Text, CR Text, TextEncodeQwenImage21, CR Text, VOSR2ModelLoader, VOSR2Upscale, DF_Integer, ImageRGBA2RGB, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 543679665216295, "steps": 20}
---

# 平台全量/提取服装并展示qwen-image-2.1_2117979199431598082.json

> 来源文件 `comfyui_library/workflows/平台全量/提取服装并展示qwen-image-2.1_2117979199431598082.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `LoadImage`
- `VAELoader`
- `QwenImage21Cache`
- `SaveImage`
- `KSampler` ★核心
- `CR Text`
- `CR Text`
- `TextEncodeQwenImage21`
- `CR Text`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `DF_Integer`
- `ImageRGBA2RGB`
- `SaveImage`

## 关键参数

- `seed` = `543679665216295`
- `steps` = `20`
- `cfg` = `3`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAEDecode`、`LoadImage`、`VAELoader`、`QwenImage21Cache`、`SaveImage`、`KSampler`、`CR Text`、`TextEncodeQwenImage21`、`VOSR2ModelLoader`、`VOSR2Upscale`、`DF_Integer`、`ImageRGBA2RGB`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
