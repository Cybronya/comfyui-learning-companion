---
key: 图片生成/图生图/Put On Any Clothes V5 Qwen Image Edit 2509图像编辑工作流_2039933364802691073.json
name: Put On Any Clothes V5 Qwen Image Edit 2509图像编辑工作流_2039933364802691073
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Put On Any Clothes V5 Qwen Image Edit 2509图像编辑工作流_2039933364802691073.json
hash: 3a901cb19b4bc9f4
coverage: 0.772727
learned_at: 2026-10-23 11:10:59
nodes: [Note, VAEDecode, ModelSamplingAuraFlow, CFGNorm, MaskBlur+, PreviewMask_, Image Comparer (rgthree), SaveImage, MarkdownNote, UnetLoaderGGUF, VAELoader, Note, KSampler, LoadImage, Note, UNETLoader, CLIPLoader, InpaintModelConditioning, TextEncodeQwenImageEditPlus, LoadImage, TextEncodeQwenImageEditPlus, LoraLoaderVanilla]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.97, "lora_name": "Qwen-Image-Edit-2509-Lightning-8steps-V1.0-bf16.safe.safetensors", "sampler_name": "euler_ancestral", "scheduler": "normal", "seed": 334843534886133, "steps": 8, "strength_clip": 1, "strength_model": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Put On Any Clothes V5 Qwen Image Edit 2509图像编辑工作流_2039933364802691073.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Put On Any Clothes V5 Qwen Image Edit 2509图像编辑工作流_2039933364802691073.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（22 个）：
- `Note`
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `MaskBlur+`
- `PreviewMask_`
- `Image Comparer (rgthree)`
- `SaveImage`
- `MarkdownNote`
- `UnetLoaderGGUF` ★核心
- `VAELoader`
- `Note`
- `KSampler` ★核心
- `LoadImage`
- `Note`
- `UNETLoader` ★核心
- `CLIPLoader`
- `InpaintModelConditioning`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `LoraLoaderVanilla` ★核心

## 关键参数

- `seed` = `334843534886133`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `normal`
- `denoise` = `0.97`
- `lora_name` = `Qwen-Image-Edit-2509-Lightning-8steps-V1.0-bf16.safe.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **77%**（17/22）

**有卡**：`VAEDecode`、`ModelSamplingAuraFlow`、`CFGNorm`、`MaskBlur+`、`PreviewMask_`、`SaveImage`、`UnetLoaderGGUF`、`VAELoader`、`KSampler`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`InpaintModelConditioning`、`TextEncodeQwenImageEditPlus`、`LoraLoaderVanilla`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、CFGNorm、TextEncodeQwenImageEditPlus

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
