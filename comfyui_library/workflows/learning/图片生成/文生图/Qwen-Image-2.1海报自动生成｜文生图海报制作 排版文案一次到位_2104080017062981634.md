---
key: 图片生成/文生图/Qwen-Image-2.1海报自动生成｜文生图海报制作 排版文案一次到位_2104080017062981634.json
name: Qwen-Image-2.1海报自动生成｜文生图海报制作 排版文案一次到位_2104080017062981634
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1海报自动生成｜文生图海报制作 排版文案一次到位_2104080017062981634.json
hash: 8c9a1c93c5d713c1
coverage: 0.739726
learned_at: 2026-10-10 20:59:00
nodes: [easy int, EmptyImage, easy showAnything, UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, ImpactInt, ImpactInt, CLIPLoader, easy showAnything, SetNode, easy saveText, StringFunction|pysssss, GetImageSizeAndCount, easy showAnything, SaveImage, RH_LLMAPI_NODE, StringFunction|pysssss, Text Multiline, easy seed, easy showAnything, easy positive, KSampler, TextGenerateLTX2Prompt, easy int, easy int, easy anythingIndexSwitch, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [StringFunction|pysssss, StringFunction|pysssss, Text Multiline, easy anythingIndexSwitch, easy int, easy int, easy int, easy positive, easy saveText, easy seed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen-Image-2.1海报自动生成｜文生图海报制作 排版文案一次到位_2104080017062981634.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1海报自动生成｜文生图海报制作 排版文案一次到位_2104080017062981634.json`

## 结构

**节点**（73 个）：
- `easy int`
- `EmptyImage`
- `easy showAnything`
- `UNETLoader`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage`
- `VAEDecode`
- `ImpactInt`
- `ImpactInt`
- `CLIPLoader`
- `easy showAnything`
- `SetNode`
- `easy saveText`
- `StringFunction|pysssss`
- `GetImageSizeAndCount`
- `easy showAnything`
- `SaveImage`
- `RH_LLMAPI_NODE`
- `StringFunction|pysssss`
- `Text Multiline`
- `easy seed`
- `easy showAnything`
- `easy positive`
- `KSampler`
- `TextGenerateLTX2Prompt`
- `easy int`
- `easy int`
- `easy anythingIndexSwitch`
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

覆盖率 **74%**（54/73）

**有卡**：`easy int`、`EmptyImage`、`easy showAnything`、`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`ImpactInt`、`SetNode`、`easy saveText`、`StringFunction|pysssss`、`GetImageSizeAndCount`、`SaveImage`、`RH_LLMAPI_NODE`、`Text Multiline`、`easy seed`、`easy positive`、`KSampler`、`TextGenerateLTX2Prompt`、`easy anythingIndexSwitch`、`孤海注释`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`JjkText`、`LoraLoaderModelOnly`

**缺卡**（10）：`StringFunction|pysssss`、`StringFunction|pysssss`、`Text Multiline`、`easy anythingIndexSwitch`、`easy int`、`easy int`、`easy int`、`easy positive`、`easy saveText`、`easy seed`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
