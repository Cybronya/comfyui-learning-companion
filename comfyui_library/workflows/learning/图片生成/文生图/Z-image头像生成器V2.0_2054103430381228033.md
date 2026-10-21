---
key: 图片生成/文生图/Z-image头像生成器V2.0_2054103430381228033.json
name: Z-image头像生成器V2.0_2054103430381228033
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image头像生成器V2.0_2054103430381228033.json
hash: c4d6fdf40e82a6c9
coverage: 0.95
learned_at: 2026-10-21 02:56:20
nodes: [UNETLoader, KSampler, ConditioningZeroOut, VAEDecode, LoraLoaderModelOnly, CLIPLoader, VAELoader, EmptyLatentImage, CLIPTextEncode, CLIPTextEncode, UNETLoader, SaveImage, KSampler, VAEDecode, Latent Noise Injection, CLIPTextEncode, PreviewImage, llama_cpp_parameters, llama_cpp_instruct_adv, llama_cpp_model_loader]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.30000000000000004, "height": 1536, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 249854872316145, "steps": 10, "width": 1024}
---

# 图片生成/文生图/Z-image头像生成器V2.0_2054103430381228033.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image头像生成器V2.0_2054103430381228033.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（20 个）：
- `UNETLoader` ★核心
- `KSampler` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Latent Noise Injection`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `249854872316145`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.30000000000000004`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`UNETLoader`、`KSampler`、`ConditioningZeroOut`、`VAEDecode`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`CLIPTextEncode`、`SaveImage`、`Latent Noise Injection`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
