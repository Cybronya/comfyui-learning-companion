---
key: 图片生成/文生图/Qwen Image 2.1角色设定卡一分钟出图工作流，角色设计文生图工具_2107186101369790465.json
name: Qwen Image 2.1角色设定卡一分钟出图工作流，角色设计文生图工具_2107186101369790465
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1角色设定卡一分钟出图工作流，角色设计文生图工具_2107186101369790465.json
hash: 0f427a277c457365
coverage: 0.7
learned_at: 2026-10-06 21:49:23
nodes: [Seed (rgthree), EmptyLatentImage, VAELoader, CLIPLoader, UNETLoader, VAEDecode, SaveImage, LoadImage, ResolutionSelector, llama_cpp_model_loader, LayerUtility: TextJoin, llama_cpp_parameters, PrimitiveStringMultiline, KSampler, LoraLoaderModelOnly, PrimitiveStringMultiline, TextEncodeQwenImage21, PreviewAny, llama_cpp_instruct_adv, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [Fast Groups Bypasser (rgthree), LayerUtility: TextJoin, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, PreviewAny, Seed (rgthree), solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识, 次要节点 `llama_cpp_instruct_adv` 知识库中没有该节点类型的任何知识, 次要节点 `llama_cpp_model_loader` 知识库中没有该节点类型的任何知识, 次要节点 `llama_cpp_parameters` 知识库中没有该节点类型的任何知识, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1角色设定卡一分钟出图工作流，角色设计文生图工具_2107186101369790465.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1角色设定卡一分钟出图工作流，角色设计文生图工具_2107186101369790465.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（50 个）：
- `Seed (rgthree)`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `ResolutionSelector`
- `llama_cpp_model_loader`
- `LayerUtility: TextJoin`
- `llama_cpp_parameters`
- `PrimitiveStringMultiline`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `TextEncodeQwenImage21`
- `PreviewAny`
- `llama_cpp_instruct_adv`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **70%**（35/50）

**有卡**：`EmptyLatentImage`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`VAEDecode`、`SaveImage`、`LoadImage`、`ResolutionSelector`、`KSampler`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`CLIPTextEncode`

**缺卡**（8）：`Fast Groups Bypasser (rgthree)`、`LayerUtility: TextJoin`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`PreviewAny`、`Seed (rgthree)`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识
- 次要节点 `llama_cpp_instruct_adv` 知识库中没有该节点类型的任何知识
- 次要节点 `llama_cpp_model_loader` 知识库中没有该节点类型的任何知识
- 次要节点 `llama_cpp_parameters` 知识库中没有该节点类型的任何知识
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
