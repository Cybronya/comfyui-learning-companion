---
key: 图片生成/文生图/Qwen-image2.1文生图_图片编辑多合一_2101867200528347138.json
name: Qwen-image2.1文生图_图片编辑多合一_2101867200528347138
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-image2.1文生图_图片编辑多合一_2101867200528347138.json
hash: dbc9edcea8e8b670
coverage: 0.409639
learned_at: 2026-10-20 01:51:20
nodes: [VAELoader, 孤海注释, MarkdownNote, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, LoadImage, LoadImage, UNETLoader, CLIPLoader, SetNode, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, GetNode, GetNode, GetNode, EmptyLatentImage, GetNode, easy boolean, SetNode, easy boolean, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, GetNode, Any To String (mtb), llama_cpp_model_loader, ImpactConditionalBranch, ImpactConditionalBranch, GetNode, llama_cpp_instruct_adv, XB_BatchImages, ShowText|pysssss, SetNode, CR Text, CR Text, Fast Groups Muter (rgthree), ResolutionSelector, SetNode, SetNode, QwenImage21Cache, KSampler, GetNode, ComfySwitchNode, Note, CR Text, SetNode, SetNode, TextEncodeQwenImage21, easy cleanGpuUsed, VAEDecode, SaveImage, SaveImageAdvanced, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 337216826820044, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen-image2.1文生图_图片编辑多合一_2101867200528347138.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-image2.1文生图_图片编辑多合一_2101867200528347138.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（83 个）：
- `VAELoader`
- `孤海注释`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `SetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLatentImage` ★核心
- `GetNode`
- `easy boolean`
- `SetNode`
- `easy boolean`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `GetNode`
- `Any To String (mtb)`
- `llama_cpp_model_loader`
- `ImpactConditionalBranch`
- `ImpactConditionalBranch`
- `GetNode`
- `llama_cpp_instruct_adv`
- `XB_BatchImages`
- `ShowText|pysssss`
- `SetNode`
- `CR Text`
- `CR Text`
- `Fast Groups Muter (rgthree)`
- `ResolutionSelector`
- `SetNode`
- `SetNode`
- `QwenImage21Cache`
- `KSampler` ★核心
- `GetNode`
- `ComfySwitchNode`
- `Note`
- `CR Text`
- `SetNode`
- `SetNode`
- `TextEncodeQwenImage21`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImageAdvanced`
- `MarkdownNote`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `337216826820044`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **41%**（34/83）

**有卡**：`VAELoader`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`EmptyLatentImage`、`easy boolean`、`Any To String (mtb)`、`llama_cpp_model_loader`、`ImpactConditionalBranch`、`llama_cpp_instruct_adv`、`XB_BatchImages`、`CR Text`、`ResolutionSelector`、`QwenImage21Cache`、`KSampler`、`TextEncodeQwenImage21`、`easy cleanGpuUsed`、`VAEDecode`、`SaveImage`、`SaveImageAdvanced`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
