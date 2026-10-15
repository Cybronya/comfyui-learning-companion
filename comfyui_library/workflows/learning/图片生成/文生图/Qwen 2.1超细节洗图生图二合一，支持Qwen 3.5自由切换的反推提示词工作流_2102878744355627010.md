---
key: 图片生成/文生图/Qwen 2.1超细节洗图生图二合一，支持Qwen 3.5自由切换的反推提示词工作流_2102878744355627010.json
name: Qwen 2.1超细节洗图生图二合一，支持Qwen 3.5自由切换的反推提示词工作流_2102878744355627010
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen 2.1超细节洗图生图二合一，支持Qwen 3.5自由切换的反推提示词工作流_2102878744355627010.json
hash: 11b70ff05b0fee9a
coverage: 0.781818
learned_at: 2026-10-10 20:58:50
nodes: [TextEncodeQwenImage21, EmptyLatentImage, KSampler, TextGenerateLTX2Prompt, easy showAnything, ResolutionSelector, EmptyImage, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, VAEDecode, SaveImage, Text Multiline, CLIPLoader, VAELoader, CLIPLoader, LoraLoaderModelOnly, UNETLoader, easy seed, ShowText|pysssss, PrimitiveStringMultiline, llama_cpp_model_loader, llama_cpp_parameters, LoadImage, PrimitiveStringMultiline, Switch any [Crystools], llama_cpp_instruct_adv, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [LayerUtility: ImageScaleByAspectRatio V2, Switch any [Crystools], Text Multiline, easy seed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `Switch any [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen 2.1超细节洗图生图二合一，支持Qwen 3.5自由切换的反推提示词工作流_2102878744355627010.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen 2.1超细节洗图生图二合一，支持Qwen 3.5自由切换的反推提示词工作流_2102878744355627010.json`

## 结构

**节点**（55 个）：
- `TextEncodeQwenImage21`
- `EmptyLatentImage`
- `KSampler`
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `ResolutionSelector`
- `EmptyImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `VAEDecode`
- `SaveImage`
- `Text Multiline`
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `easy seed`
- `ShowText|pysssss`
- `PrimitiveStringMultiline`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `LoadImage`
- `PrimitiveStringMultiline`
- `Switch any [Crystools]`
- `llama_cpp_instruct_adv`
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

覆盖率 **78%**（43/55）

**有卡**：`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`TextGenerateLTX2Prompt`、`easy showAnything`、`ResolutionSelector`、`EmptyImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`INTConstant`、`VAEDecode`、`SaveImage`、`Text Multiline`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`easy seed`、`ShowText|pysssss`、`PrimitiveStringMultiline`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`LoadImage`、`Switch any [Crystools]`、`llama_cpp_instruct_adv`、`孤海注释`

**缺卡**（4）：`LayerUtility: ImageScaleByAspectRatio V2`、`Switch any [Crystools]`、`Text Multiline`、`easy seed`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Switch any [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
