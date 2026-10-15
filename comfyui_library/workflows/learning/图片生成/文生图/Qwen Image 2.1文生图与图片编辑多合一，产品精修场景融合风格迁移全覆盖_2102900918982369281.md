---
key: 图片生成/文生图/Qwen Image 2.1文生图与图片编辑多合一，产品精修场景融合风格迁移全覆盖_2102900918982369281.json
name: Qwen Image 2.1文生图与图片编辑多合一，产品精修场景融合风格迁移全覆盖_2102900918982369281
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图与图片编辑多合一，产品精修场景融合风格迁移全覆盖_2102900918982369281.json
hash: f5b1ded58410a4f6
coverage: 0.768116
learned_at: 2026-10-10 20:58:53
nodes: [VAELoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, llama_cpp_model_loader, ImpactConditionalBranch, llama_cpp_instruct_adv, XB_BatchImages, CR Text, CR Text, ResolutionSelector, QwenImage21Cache, ComfySwitchNode, ImpactConditionalBranch, easy boolean, llama_cpp_instruct_adv, ShowText|pysssss, easy cleanGpuUsed, TextEncodeQwenImage21, easy boolean, UNETLoader, CLIPLoader, ComfySwitchNode, INTConstant, EmptyLatentImage, VAEDecode, LoadImage, INTConstant, Image Comparer (rgthree), KSampler, Fast Groups Bypasser (rgthree), Fast Groups Muter (rgthree), CR Text, SaveImage, LoadImage, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [CR Text, CR Text, CR Text, easy boolean, easy boolean, easy cleanGpuUsed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1文生图与图片编辑多合一，产品精修场景融合风格迁移全覆盖_2102900918982369281.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图与图片编辑多合一，产品精修场景融合风格迁移全覆盖_2102900918982369281.json`

## 结构

**节点**（69 个）：
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
- `UNETLoader`
- `CLIPLoader`
- `ComfySwitchNode`
- `INTConstant`
- `EmptyLatentImage`
- `VAEDecode`
- `LoadImage`
- `INTConstant`
- `Image Comparer (rgthree)`
- `KSampler`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Muter (rgthree)`
- `CR Text`
- `SaveImage`
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

覆盖率 **77%**（53/69）

**有卡**：`VAELoader`、`LoadImage`、`llama_cpp_model_loader`、`ImpactConditionalBranch`、`llama_cpp_instruct_adv`、`XB_BatchImages`、`CR Text`、`ResolutionSelector`、`QwenImage21Cache`、`ComfySwitchNode`、`easy boolean`、`ShowText|pysssss`、`easy cleanGpuUsed`、`TextEncodeQwenImage21`、`UNETLoader`、`CLIPLoader`、`INTConstant`、`EmptyLatentImage`、`VAEDecode`、`Image Comparer (rgthree)`、`KSampler`、`Fast Groups Bypasser (rgthree)`、`Fast Groups Muter (rgthree)`、`SaveImage`、`孤海注释`、`LoraLoaderModelOnly`

**缺卡**（6）：`CR Text`、`CR Text`、`CR Text`、`easy boolean`、`easy boolean`、`easy cleanGpuUsed`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
