---
key: 图片生成/文生图/Qwen-iamge2.1-文生图（自动提示词版）_2102004749242552322.json
name: Qwen-iamge2.1-文生图（自动提示词版）_2102004749242552322
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-iamge2.1-文生图（自动提示词版）_2102004749242552322.json
hash: c118fda9e0012f81
coverage: 0.842105
learned_at: 2026-10-20 01:51:18
nodes: [UNETLoader, SaveImage, QwenImage21Cache, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, ConditioningZeroOut, KSampler, CLIPTextEncode, llama_cpp_instruct_adv, ResolutionSelector, llama_cpp_model_loader, ShowText|pysssss, CR Prompt Text, CLIPLoader, ShowText|pysssss, TextGenerateLTX2Prompt, PreviewImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 94880928332866, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen-iamge2.1-文生图（自动提示词版）_2102004749242552322.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-iamge2.1-文生图（自动提示词版）_2102004749242552322.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `UNETLoader` ★核心
- `SaveImage`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `llama_cpp_instruct_adv`
- `ResolutionSelector`
- `llama_cpp_model_loader`
- `ShowText|pysssss`
- `CR Prompt Text`
- `CLIPLoader`
- `ShowText|pysssss`
- `TextGenerateLTX2Prompt`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `94880928332866`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`UNETLoader`、`SaveImage`、`QwenImage21Cache`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`EmptyLatentImage`、`ConditioningZeroOut`、`KSampler`、`CLIPTextEncode`、`llama_cpp_instruct_adv`、`ResolutionSelector`、`llama_cpp_model_loader`、`CR Prompt Text`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、ResolutionSelector
