---
key: Qwen-image 2.1 高质量文生图 I 提示词增强_2103025192686669825.json
name: Qwen-image 2.1 高质量文生图 I 提示词增强_2103025192686669825
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-image 2.1 高质量文生图 I 提示词增强_2103025192686669825.json
hash: 84a5af7742aa189e
coverage: 0.533333
learned_at: 2026-10-10 20:59:05
nodes: [SeedVR2PostProcessing, KSampler, VAEEncodeTiled, SeedVR2Preprocess, SeedVR2Conditioning, QwenImage21Cache, easy cleanGpuUsed, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, GetNode, SetNode, VAELoader, SetNode, GetNode, KSampler, Note, Label (rgthree), SetNode, UNETLoader, VAELoader, UNETLoader, VAEDecode, GetNode, VAEDecodeTiled, SaveImage, Note, Image Comparer (rgthree), TextEncodeQwenImage21, llama_cpp_parameters, llama_cpp_instruct_adv, String Literal, easy showAnything, KepStringLiteral, EmptyLatentImage, String Literal, String Literal, easy seed, Fast Groups Bypasser (rgthree), INTConstant, Fast Groups Bypasser (rgthree), ResolutionSelector, llama_cpp_model_loader, Label (rgthree), SaveImage, PrimitiveStringMultiline]
patterns: []
missing: [Label (rgthree), Label (rgthree), LayerUtility: ImageScaleByAspectRatio V2, String Literal, String Literal, String Literal, easy cleanGpuUsed, easy seed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 505402118190697, "steps": 40, "width": 1024}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Qwen-image 2.1 高质量文生图 I 提示词增强_2103025192686669825.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-image 2.1 高质量文生图 I 提示词增强_2103025192686669825.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `SeedVR2PostProcessing`
- `KSampler` ★核心
- `VAEEncodeTiled` ★核心
- `SeedVR2Preprocess`
- `SeedVR2Conditioning`
- `QwenImage21Cache`
- `easy cleanGpuUsed`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `GetNode`
- `SetNode`
- `VAELoader`
- `SetNode`
- `GetNode`
- `KSampler` ★核心
- `Note`
- `Label (rgthree)`
- `SetNode`
- `UNETLoader` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `VAEDecodeTiled` ★核心
- `SaveImage`
- `Note`
- `Image Comparer (rgthree)`
- `TextEncodeQwenImage21`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `String Literal`
- `easy showAnything`
- `KepStringLiteral`
- `EmptyLatentImage` ★核心
- `String Literal`
- `String Literal`
- `easy seed`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `Fast Groups Bypasser (rgthree)`
- `ResolutionSelector`
- `llama_cpp_model_loader`
- `Label (rgthree)`
- `SaveImage`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `505402118190697`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **53%**（24/45）

**有卡**：`SeedVR2PostProcessing`、`KSampler`、`VAEEncodeTiled`、`SeedVR2Preprocess`、`SeedVR2Conditioning`、`QwenImage21Cache`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`VAEDecode`、`VAEDecodeTiled`、`SaveImage`、`TextEncodeQwenImage21`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`KepStringLiteral`、`EmptyLatentImage`、`INTConstant`、`ResolutionSelector`、`llama_cpp_model_loader`

**缺卡**（8）：`Label (rgthree)`、`Label (rgthree)`、`LayerUtility: ImageScaleByAspectRatio V2`、`String Literal`、`String Literal`、`String Literal`、`easy cleanGpuUsed`、`easy seed`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
