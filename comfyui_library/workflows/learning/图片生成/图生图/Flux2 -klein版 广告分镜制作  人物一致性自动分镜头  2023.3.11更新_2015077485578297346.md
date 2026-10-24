---
key: 图片生成/图生图/Flux2 -klein版 广告分镜制作  人物一致性自动分镜头  2023.3.11更新_2015077485578297346.json
name: Flux2 -klein版 广告分镜制作  人物一致性自动分镜头  2023.3.11更新_2015077485578297346
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux2 -klein版 广告分镜制作  人物一致性自动分镜头  2023.3.11更新_2015077485578297346.json
hash: 2835cc3218c6d76b
coverage: 0.766667
learned_at: 2026-10-23 10:59:02
nodes: [Int, CLIPTextEncode, VAELoader, ReferenceLatent, ReferenceLatent, VAEEncode, ConditioningZeroOut, EmptyFlux2LatentImage, VAEDecode, LoadImage, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), LoadImage, MarkdownNote, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, ProcessString, easy promptLine, llama_cpp_model_loader, PreviewAny, KSampler, easy cleanGpuUsed, MarkdownNote, MarkdownNote, easy showAnything, llama_cpp_parameters, llama_cpp_instruct_adv, UNETLoader, CLIPLoader, JjkText, ShellAgentPluginOutputText, ProcessString, easy promptLine, Int, easy showAnything, UNETLoader, KSampler, CLIPTextEncode, CLIPLoader, VAELoader, ReferenceLatent, ReferenceLatent, VAEEncode, ConditioningZeroOut, EmptyFlux2LatentImage, easy cleanGpuUsed, VAEDecode, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), LoadImage, JjkText, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, Fast Groups Bypasser (rgthree), MarkdownNote, Fast Groups Bypasser (rgthree), LoadImage, RH_LLMAPI_Pro_Node, MarkdownNote]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 270399300851672, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Flux2 -klein版 广告分镜制作  人物一致性自动分镜头  2023.3.11更新_2015077485578297346.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux2 -klein版 广告分镜制作  人物一致性自动分镜头  2023.3.11更新_2015077485578297346.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `Int`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `VAEDecode` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `MarkdownNote`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ProcessString`
- `easy promptLine`
- `llama_cpp_model_loader`
- `PreviewAny`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `MarkdownNote`
- `MarkdownNote`
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
- `LoadImage`
- `JjkText`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `RH_LLMAPI_Pro_Node`
- `MarkdownNote`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `270399300851672`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（46/60）

**有卡**：`Int`、`CLIPTextEncode`、`VAELoader`、`ReferenceLatent`、`VAEEncode`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`VAEDecode`、`LoadImage`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`ProcessString`、`easy promptLine`、`llama_cpp_model_loader`、`KSampler`、`easy cleanGpuUsed`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`UNETLoader`、`CLIPLoader`、`ShellAgentPluginOutputText`、`SaveImage`、`RH_LLMAPI_Pro_Node`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
