---
key: 图片生成/文生图/Qwen3.5反推提示词+ernie_image_turbo_2046120898310180865.json
name: Qwen3.5反推提示词+ernie_image_turbo_2046120898310180865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen3.5反推提示词+ernie_image_turbo_2046120898310180865.json
hash: 2b999ddfbb14f73f
coverage: 0.75
learned_at: 2026-10-21 02:54:46
nodes: [VAEDecode, TextGenerate, StringReplace, StringReplace, PreviewAny, PreviewAny, PreviewAny, CLIPLoader, EmptyFlux2LatentImage, INTConstant, CLIPTextEncode, ComfySwitchNode, PrimitiveBoolean, VAELoader, CLIPTextEncode, KSampler, CLIPLoader, UNETLoader, llama_cpp_model_loader, INTConstant, llama_cpp_parameters, PrimitiveStringMultiline, LoadImage, SaveImage, PreviewAny, StringReplace, PreviewAny, llama_cpp_instruct_adv]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 148224456047262, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen3.5反推提示词+ernie_image_turbo_2046120898310180865.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen3.5反推提示词+ernie_image_turbo_2046120898310180865.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `VAEDecode` ★核心
- `TextGenerate`
- `StringReplace`
- `StringReplace`
- `PreviewAny`
- `PreviewAny`
- `PreviewAny`
- `CLIPLoader`
- `EmptyFlux2LatentImage`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `llama_cpp_model_loader`
- `INTConstant`
- `llama_cpp_parameters`
- `PrimitiveStringMultiline`
- `LoadImage`
- `SaveImage`
- `PreviewAny`
- `StringReplace`
- `PreviewAny`
- `llama_cpp_instruct_adv`

## 关键参数

- `seed` = `148224456047262`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **75%**（21/28）

**有卡**：`VAEDecode`、`TextGenerate`、`StringReplace`、`CLIPLoader`、`EmptyFlux2LatentImage`、`INTConstant`、`CLIPTextEncode`、`PrimitiveBoolean`、`VAELoader`、`KSampler`、`UNETLoader`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`LoadImage`、`SaveImage`、`llama_cpp_instruct_adv`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、EmptyFlux2LatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
