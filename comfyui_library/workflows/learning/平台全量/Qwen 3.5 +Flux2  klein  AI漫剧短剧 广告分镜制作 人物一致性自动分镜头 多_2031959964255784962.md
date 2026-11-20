---
key: 平台全量/Qwen 3.5 +Flux2  klein  AI漫剧短剧 广告分镜制作 人物一致性自动分镜头 多_2031959964255784962.json
name: Qwen 3.5 +Flux2  klein  AI漫剧短剧 广告分镜制作 人物一致性自动分镜头 多_2031959964255784962
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen 3.5 +Flux2  klein  AI漫剧短剧 广告分镜制作 人物一致性自动分镜头 多_2031959964255784962.json
hash: feaf5d74c49347d9
coverage: 0.826923
learned_at: 2026-11-14 00:49:17
nodes: [Int, CLIPTextEncode, VAELoader, ReferenceLatent, ReferenceLatent, VAEEncode, ConditioningZeroOut, EmptyFlux2LatentImage, VAEDecode, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), LayerUtility: ImageScaleByAspectRatio V2, ProcessString, easy promptLine, llama_cpp_model_loader, PreviewAny, KSampler, easy cleanGpuUsed, easy showAnything, llama_cpp_parameters, llama_cpp_instruct_adv, UNETLoader, CLIPLoader, JjkText, ShellAgentPluginOutputText, ProcessString, easy promptLine, Int, easy showAnything, UNETLoader, KSampler, CLIPTextEncode, CLIPLoader, VAELoader, ReferenceLatent, ReferenceLatent, VAEEncode, ConditioningZeroOut, EmptyFlux2LatentImage, easy cleanGpuUsed, VAEDecode, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), JjkText, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, RH_LLMAPI_Pro_Node, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 508943691248227, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Qwen 3.5 +Flux2  klein  AI漫剧短剧 广告分镜制作 人物一致性自动分镜头 多_2031959964255784962.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen 3.5 +Flux2  klein  AI漫剧短剧 广告分镜制作 人物一致性自动分镜头 多_2031959964255784962.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `Int`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ProcessString`
- `easy promptLine`
- `llama_cpp_model_loader`
- `PreviewAny`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `easy showAnything`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `UNETLoader` ★核心
- `CLIPLoader`
- `JjkText`
- `ShellAgentPluginOutputText`
- `ProcessString`
- `easy promptLine`
- `Int`
- `easy showAnything`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `JjkText`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `RH_LLMAPI_Pro_Node`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `508943691248227`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（43/52）

**有卡**：`Int`、`CLIPTextEncode`、`VAELoader`、`ReferenceLatent`、`VAEEncode`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`VAEDecode`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`ProcessString`、`easy promptLine`、`llama_cpp_model_loader`、`KSampler`、`easy cleanGpuUsed`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`UNETLoader`、`CLIPLoader`、`ShellAgentPluginOutputText`、`SaveImage`、`RH_LLMAPI_Pro_Node`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
