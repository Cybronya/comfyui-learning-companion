---
key: 图片生成/文生图/Qwen Image 2.1场景4K 超高清场景图生成_2105424857071710209.json
name: Qwen Image 2.1场景4K 超高清场景图生成_2105424857071710209
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1场景4K 超高清场景图生成_2105424857071710209.json
hash: 6d2dd176ffcb53ec
coverage: 0.77551
learned_at: 2026-10-10 20:58:52
nodes: [CR Text, CR Text Concatenate, easy seed, QZ_ResolutionPreset, SimpleMathDual+, EmptyLatentImage, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, KSampler, VAEDecode, PreviewImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SimpleMathDual+, SeedVR2VideoUpscaler, ImageScale, SaveImage, CR Text, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [CR Text, CR Text, CR Text Concatenate, SimpleMathDual+, SimpleMathDual+, easy seed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMathDual+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMathDual+` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1场景4K 超高清场景图生成_2105424857071710209.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1场景4K 超高清场景图生成_2105424857071710209.json`

## 结构

**节点**（49 个）：
- `CR Text`
- `CR Text Concatenate`
- `easy seed`
- `QZ_ResolutionPreset`
- `SimpleMathDual+`
- `EmptyLatentImage`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `KSampler`
- `VAEDecode`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SimpleMathDual+`
- `SeedVR2VideoUpscaler`
- `ImageScale`
- `SaveImage`
- `CR Text`
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

覆盖率 **78%**（38/49）

**有卡**：`CR Text`、`CR Text Concatenate`、`easy seed`、`QZ_ResolutionPreset`、`SimpleMathDual+`、`EmptyLatentImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`PreviewImage`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`ImageScale`、`SaveImage`、`孤海注释`、`LoraLoaderModelOnly`

**缺卡**（6）：`CR Text`、`CR Text`、`CR Text Concatenate`、`SimpleMathDual+`、`SimpleMathDual+`、`easy seed`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMathDual+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMathDual+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
