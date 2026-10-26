---
key: 图片生成/图生图/【API】Qwen-Image2.1角色四视图_2111987076626468865.json
name: 【API】Qwen-Image2.1角色四视图_2111987076626468865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【API】Qwen-Image2.1角色四视图_2111987076626468865.json
hash: bcb9017d8b8bd209
coverage: 0.952381
learned_at: 2026-10-26 22:04:27
nodes: [VAEDecode, QwenImage21Cache, KSampler, llama_cpp_unload_model, llama_cpp_clean_states, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_parameters, easy showAnything, CR Text, ResolutionSelector, EmptyLatentImage, TextEncodeQwenImage21, llama_cpp_model_loader, UNETLoader, PlaySound|pysssss, CLIPLoader, VAELoader, LoadImage, easy cleanGpuUsed, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 856159367113910, "steps": 40, "width": 1024}
---

# 图片生成/图生图/【API】Qwen-Image2.1角色四视图_2111987076626468865.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【API】Qwen-Image2.1角色四视图_2111987076626468865.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `KSampler` ★核心
- `llama_cpp_unload_model`
- `llama_cpp_clean_states`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `llama_cpp_parameters`
- `easy showAnything`
- `CR Text`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `llama_cpp_model_loader`
- `UNETLoader` ★核心
- `PlaySound|pysssss`
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `easy cleanGpuUsed`
- `SaveImage`

## 关键参数

- `seed` = `856159367113910`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`VAEDecode`、`QwenImage21Cache`、`KSampler`、`llama_cpp_unload_model`、`llama_cpp_clean_states`、`easy cleanGpuUsed`、`llama_cpp_instruct_adv`、`llama_cpp_parameters`、`CR Text`、`ResolutionSelector`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`llama_cpp_model_loader`、`UNETLoader`、`PlaySound|pysssss`、`CLIPLoader`、`VAELoader`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
