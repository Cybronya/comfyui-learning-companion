---
key: 图片生成/图生图/Qwen3.5+Klein AI 短剧漫剧｜自动写剧情一键出九宫格分镜_2046582075771326466.json
name: Qwen3.5+Klein AI 短剧漫剧｜自动写剧情一键出九宫格分镜_2046582075771326466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen3.5+Klein AI 短剧漫剧｜自动写剧情一键出九宫格分镜_2046582075771326466.json
hash: 1df9c7ab8596dac4
coverage: 0.961538
learned_at: 2026-10-23 11:19:47
nodes: [SamplerCustomAdvanced, CFGGuider, Flux2Scheduler, ConditioningZeroOut, KSamplerSelect, RandomNoise, ReferenceLatent, ReferenceLatent, VAEEncode, EmptyFlux2LatentImage, PathchSageAttentionKJ, ModelPatchTorchSettings, GetImageSize, VAEDecode, CLIPTextEncode, easy promptLine, ShowText|pysssss, UnetLoaderGGUF, VAELoader, llama_cpp_parameters, llama_cpp_model_loader, LoadImage, llama_cpp_instruct_adv, Text, CLIPLoader, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/Qwen3.5+Klein AI 短剧漫剧｜自动写剧情一键出九宫格分镜_2046582075771326466.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen3.5+Klein AI 短剧漫剧｜自动写剧情一键出九宫格分镜_2046582075771326466.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `Flux2Scheduler`
- `ConditioningZeroOut`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `EmptyFlux2LatentImage`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `GetImageSize`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `easy promptLine`
- `ShowText|pysssss`
- `UnetLoaderGGUF` ★核心
- `VAELoader`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `LoadImage`
- `llama_cpp_instruct_adv`
- `Text`
- `CLIPLoader`
- `SaveImage`

## 知识

覆盖率 **96%**（25/26）

**有卡**：`SamplerCustomAdvanced`、`CFGGuider`、`Flux2Scheduler`、`ConditioningZeroOut`、`KSamplerSelect`、`RandomNoise`、`ReferenceLatent`、`VAEEncode`、`EmptyFlux2LatentImage`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`GetImageSize`、`VAEDecode`、`CLIPTextEncode`、`easy promptLine`、`UnetLoaderGGUF`、`VAELoader`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`LoadImage`、`llama_cpp_instruct_adv`、`Text`、`CLIPLoader`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider、KSamplerSelect
