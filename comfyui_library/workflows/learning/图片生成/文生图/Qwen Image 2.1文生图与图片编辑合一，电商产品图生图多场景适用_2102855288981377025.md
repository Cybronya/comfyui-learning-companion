---
key: 图片生成/文生图/Qwen Image 2.1文生图与图片编辑合一，电商产品图生图多场景适用_2102855288981377025.json
name: Qwen Image 2.1文生图与图片编辑合一，电商产品图生图多场景适用_2102855288981377025
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图与图片编辑合一，电商产品图生图多场景适用_2102855288981377025.json
hash: bd1321e0fe73a390
coverage: 0.769231
learned_at: 2026-10-10 20:58:53
nodes: [KSampler, VAEDecode, QwenImage21Cache, UNETLoader, llama_cpp_instruct_adv, CLIPLoader, VAELoader, LoadImage, Fast Groups Muter (rgthree), ResolutionSelector, CR Text, EmptyLatentImage, easy boolean, CR Text, ComfySwitchNodeV2, llama_cpp_model_loader, INTConstant, INTConstant, ComfySwitchNodeV2, easy cleanGpuUsed, TextEncodeQwenImage21, XB_BatchImages, Image Comparer (rgthree), LoadImage, Fast Groups Bypasser (rgthree), llama_cpp_instruct_adv, ShowText|pysssss, ComfySwitchNodeV2, ComfySwitchNodeV2, SaveImage, CR Text, CR Text, easy boolean, LoadImage, LoadImage, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [CR Text, CR Text, CR Text, CR Text, easy boolean, easy boolean, easy cleanGpuUsed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1文生图与图片编辑合一，电商产品图生图多场景适用_2102855288981377025.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图与图片编辑合一，电商产品图生图多场景适用_2102855288981377025.json`

## 结构

**节点**（65 个）：
- `KSampler`
- `VAEDecode`
- `QwenImage21Cache`
- `UNETLoader`
- `llama_cpp_instruct_adv`
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `Fast Groups Muter (rgthree)`
- `ResolutionSelector`
- `CR Text`
- `EmptyLatentImage`
- `easy boolean`
- `CR Text`
- `ComfySwitchNodeV2`
- `llama_cpp_model_loader`
- `INTConstant`
- `INTConstant`
- `ComfySwitchNodeV2`
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
- `孤海注释`
- `孤海注释`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `KSampler`
- `EmptyLatentImage`
- `JjkText`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `solarL_SaveImagesToZip`
- `VAEDecode`
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4.5`
- `denoise` = `1`
- `height` = `80`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `seed` = `598626327129635`
- `steps` = `4`
- `width` = `80`

## 知识

覆盖率 **77%**（50/65）

**有卡**：`KSampler`、`VAEDecode`、`QwenImage21Cache`、`UNETLoader`、`llama_cpp_instruct_adv`、`CLIPLoader`、`VAELoader`、`LoadImage`、`Fast Groups Muter (rgthree)`、`ResolutionSelector`、`CR Text`、`EmptyLatentImage`、`easy boolean`、`ComfySwitchNodeV2`、`llama_cpp_model_loader`、`INTConstant`、`easy cleanGpuUsed`、`TextEncodeQwenImage21`、`XB_BatchImages`、`Image Comparer (rgthree)`、`Fast Groups Bypasser (rgthree)`、`ShowText|pysssss`、`SaveImage`、`孤海注释`、`LoraLoaderModelOnly`

**缺卡**（7）：`CR Text`、`CR Text`、`CR Text`、`CR Text`、`easy boolean`、`easy boolean`、`easy cleanGpuUsed`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
