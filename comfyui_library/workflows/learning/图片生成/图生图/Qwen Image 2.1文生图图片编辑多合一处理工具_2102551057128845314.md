---
key: 图片生成/图生图/Qwen Image 2.1文生图图片编辑多合一处理工具_2102551057128845314.json
name: Qwen Image 2.1文生图图片编辑多合一处理工具_2102551057128845314
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1文生图图片编辑多合一处理工具_2102551057128845314.json
hash: 1e76590741557f2e
coverage: 0.481481
learned_at: 2026-10-10 20:48:07
nodes: [VAELoader, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, LoadImage, LoadImage, UNETLoader, CLIPLoader, SetNode, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, GetNode, GetNode, GetNode, EmptyLatentImage, GetNode, easy boolean, SetNode, easy boolean, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, GetNode, Any To String (mtb), llama_cpp_model_loader, ImpactConditionalBranch, ImpactConditionalBranch, GetNode, llama_cpp_instruct_adv, XB_BatchImages, ShowText|pysssss, SetNode, CR Text, CR Text, Fast Groups Muter (rgthree), ResolutionSelector, SetNode, SetNode, QwenImage21Cache, KSampler, GetNode, ComfySwitchNode, CR Text, SetNode, SetNode, TextEncodeQwenImage21, easy cleanGpuUsed, VAEDecode, SaveImage, SaveImageAdvanced, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [Any To String (mtb), CR Text, CR Text, CR Text, easy boolean, easy boolean, easy cleanGpuUsed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1文生图图片编辑多合一处理工具_2102551057128845314.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1文生图图片编辑多合一处理工具_2102551057128845314.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（108 个）：
- `VAELoader`
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
- `CR Text`
- `SetNode`
- `SetNode`
- `TextEncodeQwenImage21`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImageAdvanced`
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

覆盖率 **48%**（52/108）

**有卡**：`VAELoader`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`EmptyLatentImage`、`llama_cpp_model_loader`、`ImpactConditionalBranch`、`llama_cpp_instruct_adv`、`XB_BatchImages`、`ResolutionSelector`、`QwenImage21Cache`、`KSampler`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImage`、`SaveImageAdvanced`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（7）：`Any To String (mtb)`、`CR Text`、`CR Text`、`CR Text`、`easy boolean`、`easy boolean`、`easy cleanGpuUsed`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
