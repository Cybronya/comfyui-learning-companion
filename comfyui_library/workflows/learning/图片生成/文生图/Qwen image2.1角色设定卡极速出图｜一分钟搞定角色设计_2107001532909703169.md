---
key: 图片生成/文生图/Qwen image2.1角色设定卡极速出图｜一分钟搞定角色设计_2107001532909703169.json
name: Qwen image2.1角色设定卡极速出图｜一分钟搞定角色设计_2107001532909703169
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image2.1角色设定卡极速出图｜一分钟搞定角色设计_2107001532909703169.json
hash: 80b19f4e8f73571f
coverage: 0.828125
learned_at: 2026-10-10 20:58:57
nodes: [Seed (rgthree), EmptyLatentImage, VAELoader, CLIPLoader, UNETLoader, VAEDecode, SaveImage, LoadImage, ResolutionSelector, llama_cpp_model_loader, LayerUtility: TextJoin, llama_cpp_parameters, PrimitiveStringMultiline, KSampler, LoraLoaderModelOnly, PrimitiveStringMultiline, TextEncodeQwenImage21, PreviewAny, llama_cpp_instruct_adv, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [LayerUtility: TextJoin, Seed (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen image2.1角色设定卡极速出图｜一分钟搞定角色设计_2107001532909703169.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image2.1角色设定卡极速出图｜一分钟搞定角色设计_2107001532909703169.json`

## 结构

**节点**（64 个）：
- `Seed (rgthree)`
- `EmptyLatentImage`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader`
- `VAEDecode`
- `SaveImage`
- `LoadImage`
- `ResolutionSelector`
- `llama_cpp_model_loader`
- `LayerUtility: TextJoin`
- `llama_cpp_parameters`
- `PrimitiveStringMultiline`
- `KSampler`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `TextEncodeQwenImage21`
- `PreviewAny`
- `llama_cpp_instruct_adv`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `VAELoader`
- `EmptyLatentImage`
- `KSampler`
- `VAEDecode`
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode`
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

覆盖率 **83%**（53/64）

**有卡**：`Seed (rgthree)`、`EmptyLatentImage`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`VAEDecode`、`SaveImage`、`LoadImage`、`ResolutionSelector`、`llama_cpp_model_loader`、`LayerUtility: TextJoin`、`llama_cpp_parameters`、`PrimitiveStringMultiline`、`KSampler`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`PreviewAny`、`llama_cpp_instruct_adv`、`Fast Groups Bypasser (rgthree)`、`孤海注释`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`JjkText`

**缺卡**（2）：`LayerUtility: TextJoin`、`Seed (rgthree)`

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
