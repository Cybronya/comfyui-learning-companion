---
key: 图片生成/文生图/Qwen 3.5 反推图片提示词_2063823684560834561.json
name: Qwen 3.5 反推图片提示词_2063823684560834561
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen 3.5 反推图片提示词_2063823684560834561.json
hash: 92245a78e9e57ca6
coverage: 0.857143
learned_at: 2026-10-19 23:21:39
nodes: [VAELoader, CLIPTextEncode, VAEDecode, SaveImage, LoraLoaderModelOnly, llama_cpp_model_loader, llama_cpp_parameters, LoadImage, CLIPLoader, UNETLoader, EmptyLatentImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, Fast Groups Bypasser (rgthree), SaveImage, Note, PreviewAny, llama_cpp_instruct_adv]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "res_2s", "scheduler": "kl_optimal", "seed": 525884827147573, "steps": 8, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen 3.5 反推图片提示词_2063823684560834561.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen 3.5 反推图片提示词_2063823684560834561.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `LoadImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `Note`
- `PreviewAny`
- `llama_cpp_instruct_adv`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `525884827147573`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `kl_optimal`
- `denoise` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`SaveImage`、`LoraLoaderModelOnly`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`LoadImage`、`CLIPLoader`、`UNETLoader`、`EmptyLatentImage`、`KSampler`、`llama_cpp_instruct_adv`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
