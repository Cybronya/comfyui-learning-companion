---
key: 图片生成/文生图/Qwen Image 2.1 skills文生图加2K 4K放大，LoRA触发词场景增强方案_2103221327560790018.json
name: Qwen Image 2.1 skills文生图加2K 4K放大，LoRA触发词场景增强方案_2103221327560790018
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 skills文生图加2K 4K放大，LoRA触发词场景增强方案_2103221327560790018.json
hash: 312d0909af296adf
coverage: 0.754717
learned_at: 2026-10-10 20:58:51
nodes: [UNETLoader, CLIPLoader, VAEDecode, easy cleanGpuUsed, PreviewImage, Image Remove Alpha JK, VOSR2Upscale, VOSR2ModelLoader, ImageApplyLUT+, SaveImage, UNETLoader, CLIPLoader, TextEncodeQwenImage21, SaveImage, QwenImage21Cache, KSampler, ComfySwitchNode, EmptyLatentImage, VAELoader, ResolutionSelector, PlaySound|pysssss, Lora Loader Stack (rgthree), PrimitiveStringMultiline, easy imageChooser, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [Image Remove Alpha JK, ImageApplyLUT+, PlaySound|pysssss, easy cleanGpuUsed, easy imageChooser, Lora Loader Stack (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Image Remove Alpha JK` 知识库中没有该节点类型的任何知识, 次要节点 `ImageApplyLUT+` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageChooser` 知识库中没有该节点类型的任何知识, 次要节点 `Lora Loader Stack (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1 skills文生图加2K 4K放大，LoRA触发词场景增强方案_2103221327560790018.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 skills文生图加2K 4K放大，LoRA触发词场景增强方案_2103221327560790018.json`

## 结构

**节点**（53 个）：
- `UNETLoader`
- `CLIPLoader`
- `VAEDecode`
- `easy cleanGpuUsed`
- `PreviewImage`
- `Image Remove Alpha JK`
- `VOSR2Upscale`
- `VOSR2ModelLoader`
- `ImageApplyLUT+`
- `SaveImage`
- `UNETLoader`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `SaveImage`
- `QwenImage21Cache`
- `KSampler`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `VAELoader`
- `ResolutionSelector`
- `PlaySound|pysssss`
- `Lora Loader Stack (rgthree)`
- `PrimitiveStringMultiline`
- `easy imageChooser`
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

覆盖率 **75%**（40/53）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAEDecode`、`easy cleanGpuUsed`、`PreviewImage`、`Image Remove Alpha JK`、`VOSR2Upscale`、`VOSR2ModelLoader`、`ImageApplyLUT+`、`SaveImage`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`KSampler`、`ComfySwitchNode`、`EmptyLatentImage`、`VAELoader`、`ResolutionSelector`、`PlaySound|pysssss`、`Lora Loader Stack (rgthree)`、`PrimitiveStringMultiline`、`easy imageChooser`、`孤海注释`、`LoraLoaderModelOnly`

**缺卡**（6）：`Image Remove Alpha JK`、`ImageApplyLUT+`、`PlaySound|pysssss`、`easy cleanGpuUsed`、`easy imageChooser`、`Lora Loader Stack (rgthree)`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Image Remove Alpha JK` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageApplyLUT+` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageChooser` 知识库中没有该节点类型的任何知识
- 次要节点 `Lora Loader Stack (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
