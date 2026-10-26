---
key: 图片生成/反推提示词/Qwen 3.5反推图片提示词（llama反推高速版）_2071872448303292417.json
name: Qwen 3.5反推图片提示词（llama反推高速版）_2071872448303292417
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen 3.5反推图片提示词（llama反推高速版）_2071872448303292417.json
hash: cb409fe3350427a9
coverage: 0.857143
learned_at: 2026-10-26 01:45:49
nodes: [VAELoader, CLIPTextEncode, VAEDecode, SaveImage, LoraLoaderModelOnly, llama_cpp_model_loader, llama_cpp_parameters, CLIPLoader, UNETLoader, EmptyLatentImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, SaveImage, Note, llama_cpp_instruct_adv, LoadImage, PreviewAny, Fast Groups Bypasser (rgthree)]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "res_2s", "scheduler": "kl_optimal", "seed": 641405167500165, "steps": 8, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/反推提示词/Qwen 3.5反推图片提示词（llama反推高速版）_2071872448303292417.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen 3.5反推图片提示词（llama反推高速版）_2071872448303292417.json`

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
- `CLIPLoader`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `Note`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `PreviewAny`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `641405167500165`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `kl_optimal`
- `denoise` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`SaveImage`、`LoraLoaderModelOnly`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`CLIPLoader`、`UNETLoader`、`EmptyLatentImage`、`KSampler`、`llama_cpp_instruct_adv`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
