---
key: 图片生成/图生图/Qwen-image2.1文生图+图片编辑_2102309777262075906.json
name: Qwen-image2.1文生图+图片编辑_2102309777262075906
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1文生图+图片编辑_2102309777262075906.json
hash: 7acc7a14135204f4
coverage: 0.675676
learned_at: 2026-10-10 20:48:09
nodes: [KSampler, VAEDecode, QwenImage21Cache, UNETLoader, llama_cpp_instruct_adv, CLIPLoader, VAELoader, LoadImage, Fast Groups Muter (rgthree), ResolutionSelector, CR Text, EmptyLatentImage, easy boolean, CR Text, ComfySwitchNodeV2, llama_cpp_model_loader, INTConstant, INTConstant, ComfySwitchNodeV2, Note, easy cleanGpuUsed, TextEncodeQwenImage21, XB_BatchImages, Image Comparer (rgthree), LoadImage, Fast Groups Bypasser (rgthree), llama_cpp_instruct_adv, ShowText|pysssss, ComfySwitchNodeV2, ComfySwitchNodeV2, SaveImage, CR Text, CR Text, easy boolean, LoadImage, LoadImage, LoadImage]
patterns: []
missing: [CR Text, CR Text, CR Text, CR Text, easy boolean, easy boolean, easy cleanGpuUsed]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 105165641583100, "steps": 25, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/Qwen-image2.1文生图+图片编辑_2102309777262075906.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1文生图+图片编辑_2102309777262075906.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `llama_cpp_instruct_adv`
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `Fast Groups Muter (rgthree)`
- `ResolutionSelector`
- `CR Text`
- `EmptyLatentImage` ★核心
- `easy boolean`
- `CR Text`
- `ComfySwitchNodeV2`
- `llama_cpp_model_loader`
- `INTConstant`
- `INTConstant`
- `ComfySwitchNodeV2`
- `Note`
- `easy cleanGpuUsed`
- `TextEncodeQwenImage21`
- `XB_BatchImages`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `llama_cpp_instruct_adv`
- `ShowText|pysssss`
- `ComfySwitchNodeV2`
- `ComfySwitchNodeV2`
- `SaveImage`
- `CR Text`
- `CR Text`
- `easy boolean`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `105165641583100`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **68%**（25/37）

**有卡**：`KSampler`、`VAEDecode`、`QwenImage21Cache`、`UNETLoader`、`llama_cpp_instruct_adv`、`CLIPLoader`、`VAELoader`、`LoadImage`、`ResolutionSelector`、`EmptyLatentImage`、`ComfySwitchNodeV2`、`llama_cpp_model_loader`、`INTConstant`、`TextEncodeQwenImage21`、`XB_BatchImages`、`SaveImage`

**缺卡**（7）：`CR Text`、`CR Text`、`CR Text`、`CR Text`、`easy boolean`、`easy boolean`、`easy cleanGpuUsed`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
