---
key: 图片生成/图生图/Qwen-image2.1文生_图片编辑多合一_2104057908613967874.json
name: Qwen-image2.1文生_图片编辑多合一_2104057908613967874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1文生_图片编辑多合一_2104057908613967874.json
hash: 493c671a0224272a
coverage: 0.818182
learned_at: 2026-10-21 00:43:30
nodes: [VAELoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, llama_cpp_model_loader, ImpactConditionalBranch, llama_cpp_instruct_adv, XB_BatchImages, CR Text, CR Text, ResolutionSelector, QwenImage21Cache, ComfySwitchNode, ImpactConditionalBranch, easy boolean, llama_cpp_instruct_adv, ShowText|pysssss, easy cleanGpuUsed, TextEncodeQwenImage21, easy boolean, UNETLoader, CLIPLoader, ComfySwitchNode, INTConstant, EmptyLatentImage, VAEDecode, LoadImage, INTConstant, Image Comparer (rgthree), KSampler, Fast Groups Bypasser (rgthree), Note, Fast Groups Muter (rgthree), CR Text, SaveImage, LoadImage, LoadImage, LoadImage, EmptyImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 105165641583100, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen-image2.1文生_图片编辑多合一_2104057908613967874.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1文生_图片编辑多合一_2104057908613967874.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `llama_cpp_model_loader`
- `ImpactConditionalBranch`
- `llama_cpp_instruct_adv`
- `XB_BatchImages`
- `CR Text`
- `CR Text`
- `ResolutionSelector`
- `QwenImage21Cache`
- `ComfySwitchNode`
- `ImpactConditionalBranch`
- `easy boolean`
- `llama_cpp_instruct_adv`
- `ShowText|pysssss`
- `easy cleanGpuUsed`
- `TextEncodeQwenImage21`
- `easy boolean`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ComfySwitchNode`
- `INTConstant`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `INTConstant`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Fast Groups Muter (rgthree)`
- `CR Text`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `EmptyImage`
- `PreviewImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `105165641583100`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（36/44）

**有卡**：`VAELoader`、`LoadImage`、`llama_cpp_model_loader`、`ImpactConditionalBranch`、`llama_cpp_instruct_adv`、`XB_BatchImages`、`CR Text`、`ResolutionSelector`、`QwenImage21Cache`、`easy boolean`、`easy cleanGpuUsed`、`TextEncodeQwenImage21`、`UNETLoader`、`CLIPLoader`、`INTConstant`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`SaveImage`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
