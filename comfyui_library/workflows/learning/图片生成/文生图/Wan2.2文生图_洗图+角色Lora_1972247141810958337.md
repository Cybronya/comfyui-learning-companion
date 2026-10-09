---
key: 图片生成/文生图/Wan2.2文生图_洗图+角色Lora_1972247141810958337.json
name: Wan2.2文生图_洗图+角色Lora_1972247141810958337.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2文生图_洗图+角色Lora_1972247141810958337.json
hash: a62a4bb920a502dc
coverage: 0.657895
learned_at: 2026-10-09 19:50:52
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, KSamplerAdvanced, UNETLoader, VAEDecode, EmptyHunyuanLatentVideo, ImageResizeKJv2, GetNode, GetNode, GetNode, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, StringConcatenate, Int, SetNode, TextInput_, GetNode, SetNode, SetNode, AILab_QwenVL, TextInput_, Int, SetNode, SetNode, Fast Groups Bypasser (rgthree), Note, LoadImage, KSamplerAdvanced, SaveImage, GetNode, GetNode]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/文生图/Wan2.2文生图_洗图+角色Lora_1972247141810958337.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1972247141810958337.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `EmptyHunyuanLatentVideo`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `StringConcatenate`
- `Int`
- `SetNode`
- `TextInput_`
- `GetNode`
- `SetNode`
- `SetNode`
- `AILab_QwenVL`
- `TextInput_`
- `Int`
- `SetNode`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `LoadImage`
- `KSamplerAdvanced` ★核心
- `SaveImage`
- `GetNode`
- `GetNode`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **66%**（25/38）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`UNETLoader`、`VAEDecode`、`EmptyHunyuanLatentVideo`、`ImageResizeKJv2`、`ModelSamplingSD3`、`StringConcatenate`、`Int`、`TextInput_`、`AILab_QwenVL`、`LoadImage`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
