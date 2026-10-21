---
key: 图片生成/图生图/Qwen_Image_2.1文生图与图片编辑多合一，产品精修场景融合风格迁移全覆盖_2104735854735482881.json
name: Qwen_Image_2.1文生图与图片编辑多合一，产品精修场景融合风格迁移全覆盖_2104735854735482881
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1文生图与图片编辑多合一，产品精修场景融合风格迁移全覆盖_2104735854735482881.json
hash: da927b852df44a73
coverage: 0.869565
learned_at: 2026-10-21 00:43:57
nodes: [VAELoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, llama_cpp_model_loader, ImpactConditionalBranch, llama_cpp_instruct_adv, XB_BatchImages, CR Text, CR Text, ResolutionSelector, QwenImage21Cache, ComfySwitchNode, ImpactConditionalBranch, easy boolean, llama_cpp_instruct_adv, ShowText|pysssss, easy cleanGpuUsed, TextEncodeQwenImage21, easy boolean, UNETLoader, CLIPLoader, ComfySwitchNode, INTConstant, EmptyLatentImage, VAEDecode, LoadImage, INTConstant, Image Comparer (rgthree), KSampler, Fast Groups Bypasser (rgthree), Fast Groups Muter (rgthree), CR Text, SaveImage, LoadImage, LoadImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen_Image_2.1文生图与图片编辑多合一，产品精修场景融合风格迁移全覆盖_2104735854735482881.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1文生图与图片编辑多合一，产品精修场景融合风格迁移全覆盖_2104735854735482881.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

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
- `Fast Groups Muter (rgthree)`
- `CR Text`
- `SaveImage`
- `LoadImage`
- `LoadImage`
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
- `EmptyImage`
- `PreviewImage`

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

覆盖率 **87%**（60/69）

**有卡**：`VAELoader`、`LoadImage`、`llama_cpp_model_loader`、`ImpactConditionalBranch`、`llama_cpp_instruct_adv`、`XB_BatchImages`、`CR Text`、`ResolutionSelector`、`QwenImage21Cache`、`easy boolean`、`easy cleanGpuUsed`、`TextEncodeQwenImage21`、`UNETLoader`、`CLIPLoader`、`INTConstant`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
