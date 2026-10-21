---
key: 图片生成/文生图/Qwen反推+ZImage+controlnet生图-支持无限制。_2032331030291554306.json
name: Qwen反推+ZImage+controlnet生图-支持无限制。_2032331030291554306
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen反推+ZImage+controlnet生图-支持无限制。_2032331030291554306.json
hash: fad42b2a00b6d683
coverage: 0.814815
learned_at: 2026-10-21 02:54:55
nodes: [llama_cpp_parameters, QwenImageDiffsynthControlnet, CLIPLoader, VAELoader, VAEDecode, ConditioningZeroOut, KSamplerAdvanced, KSamplerAdvanced, CompressImages, VAEDecode, CompressImages, KSampler, ModelSamplingAuraFlow, UNETLoader, PreviewImage, llama_cpp_instruct_adv, CLIPTextEncode, CR Combine Prompt, PrimitiveNode, PrimitiveNode, PrimitiveNode, ShowText|pysssss, llama_cpp_model_loader, ModelPatchLoader, AIO_Preprocessor, LoadImage, EmptyLatentImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2048, "sampler_name": "euler", "scheduler": "simple", "seed": 206808321981369, "steps": 8, "width": 1200}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen反推+ZImage+controlnet生图-支持无限制。_2032331030291554306.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen反推+ZImage+controlnet生图-支持无限制。_2032331030291554306.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `llama_cpp_parameters`
- `QwenImageDiffsynthControlnet`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CompressImages`
- `VAEDecode` ★核心
- `CompressImages`
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `PreviewImage`
- `llama_cpp_instruct_adv`
- `CLIPTextEncode` ★核心
- `CR Combine Prompt`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `ShowText|pysssss`
- `llama_cpp_model_loader`
- `ModelPatchLoader`
- `AIO_Preprocessor`
- `LoadImage`
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `206808321981369`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1200`
- `height` = `2048`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（22/27）

**有卡**：`llama_cpp_parameters`、`QwenImageDiffsynthControlnet`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`ConditioningZeroOut`、`KSamplerAdvanced`、`CompressImages`、`KSampler`、`ModelSamplingAuraFlow`、`UNETLoader`、`llama_cpp_instruct_adv`、`CLIPTextEncode`、`CR Combine Prompt`、`llama_cpp_model_loader`、`ModelPatchLoader`、`AIO_Preprocessor`、`LoadImage`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
