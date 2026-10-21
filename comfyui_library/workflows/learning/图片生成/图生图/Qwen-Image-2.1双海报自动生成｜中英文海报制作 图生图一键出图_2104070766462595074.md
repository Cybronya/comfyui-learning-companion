---
key: 图片生成/图生图/Qwen-Image-2.1双海报自动生成｜中英文海报制作 图生图一键出图_2104070766462595074.json
name: Qwen-Image-2.1双海报自动生成｜中英文海报制作 图生图一键出图_2104070766462595074
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1双海报自动生成｜中英文海报制作 图生图一键出图_2104070766462595074.json
hash: 9c0804301b11959f
coverage: 0.886076
learned_at: 2026-10-21 00:43:17
nodes: [MemoryCleaner, Qwen3_VQA, MultiplePathsInput, RH_Translator, ImageLoader, UNETLoader, CLIPLoader, KSampler, VAEDecode, GetImageSizeAndCount, SaveImage, PreviewImage, easy saveText, AppendStringsToList, easy showAnything, TextEncodeQwenImage21, VAELoader, easy int, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, easy outputToList, TextGenerateLTX2Prompt, easy showAnything, PrimitiveBoolean, easy imageConcat, easy positive, StringFunction|pysssss, StringFunction|pysssss, easy positive, easy seed, easy int, easy anythingIndexSwitch, RH_LLMAPI_NODE, easy showAnything, ComfySwitchNode, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image-2.1双海报自动生成｜中英文海报制作 图生图一键出图_2104070766462595074.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1双海报自动生成｜中英文海报制作 图生图一键出图_2104070766462595074.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `MemoryCleaner`
- `Qwen3_VQA`
- `MultiplePathsInput`
- `RH_Translator`
- `ImageLoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `GetImageSizeAndCount`
- `SaveImage`
- `PreviewImage`
- `easy saveText`
- `AppendStringsToList`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `VAELoader`
- `easy int`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `easy outputToList`
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `PrimitiveBoolean`
- `easy imageConcat`
- `easy positive`
- `StringFunction|pysssss`
- `StringFunction|pysssss`
- `easy positive`
- `easy seed`
- `easy int`
- `easy anythingIndexSwitch`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `ComfySwitchNode`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（70/79）

**有卡**：`MemoryCleaner`、`Qwen3_VQA`、`MultiplePathsInput`、`RH_Translator`、`ImageLoader`、`UNETLoader`、`CLIPLoader`、`KSampler`、`VAEDecode`、`GetImageSizeAndCount`、`SaveImage`、`easy saveText`、`AppendStringsToList`、`TextEncodeQwenImage21`、`VAELoader`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy outputToList`、`TextGenerateLTX2Prompt`、`PrimitiveBoolean`、`easy imageConcat`、`easy positive`、`StringFunction|pysssss`、`easy seed`、`easy anythingIndexSwitch`、`RH_LLMAPI_NODE`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
