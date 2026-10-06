---
key: 图片生成/文生图/Qwen image2.1角色设定卡，1分钟出图！！！_2106588771755061250.json
name: Qwen image2.1角色设定卡，1分钟出图！！！_2106588771755061250
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image2.1角色设定卡，1分钟出图！！！_2106588771755061250.json
hash: 5c31f2f2d34c2415
coverage: 0.478261
learned_at: 2026-10-06 21:49:49
nodes: [Seed (rgthree), EmptyLatentImage, VAELoader, CLIPLoader, UNETLoader, VAEDecode, SaveImage, LoadImage, ResolutionSelector, llama_cpp_model_loader, LayerUtility: TextJoin, llama_cpp_parameters, PrimitiveStringMultiline, MarkdownNote, KSampler, LoraLoaderModelOnly, PrimitiveStringMultiline, MarkdownNote, TextEncodeQwenImage21, PreviewAny, llama_cpp_instruct_adv, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline]
patterns: []
missing: [Fast Groups Bypasser (rgthree), LayerUtility: TextJoin, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, PreviewAny, Seed (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 256206046827805, "steps": 8, "width": 1024}
discoveries: [次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识, 次要节点 `llama_cpp_instruct_adv` 知识库中没有该节点类型的任何知识, 次要节点 `llama_cpp_model_loader` 知识库中没有该节点类型的任何知识, 次要节点 `llama_cpp_parameters` 知识库中没有该节点类型的任何知识, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen image2.1角色设定卡，1分钟出图！！！_2106588771755061250.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image2.1角色设定卡，1分钟出图！！！_2106588771755061250.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（23 个）：
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
- `MarkdownNote`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `TextEncodeQwenImage21`
- `PreviewAny`
- `llama_cpp_instruct_adv`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `256206046827805`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **48%**（11/23）

**有卡**：`EmptyLatentImage`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`VAEDecode`、`SaveImage`、`LoadImage`、`ResolutionSelector`、`KSampler`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`

**缺卡**（7）：`Fast Groups Bypasser (rgthree)`、`LayerUtility: TextJoin`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`PreviewAny`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识
- 次要节点 `llama_cpp_instruct_adv` 知识库中没有该节点类型的任何知识
- 次要节点 `llama_cpp_model_loader` 知识库中没有该节点类型的任何知识
- 次要节点 `llama_cpp_parameters` 知识库中没有该节点类型的任何知识
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
