---
key: 图片生成/图生图/生图-图片双海报自动(中英文)-Qwen-Image-2.1_2103796343163678721.json
name: 生图-图片双海报自动(中英文)-Qwen-Image-2.1_2103796343163678721
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/生图-图片双海报自动(中英文)-Qwen-Image-2.1_2103796343163678721.json
hash: 22cf83b757f3d13f
coverage: 0.861111
learned_at: 2026-10-21 00:55:07
nodes: [MemoryCleaner, Qwen3_VQA, MultiplePathsInput, RH_Translator, ImageLoader, UNETLoader, CLIPLoader, KSampler, VAEDecode, GetImageSizeAndCount, SaveImage, PreviewImage, easy saveText, easy showAnything, TextEncodeQwenImage21, VAELoader, easy int, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, TextGenerateLTX2Prompt, easy showAnything, PrimitiveBoolean, easy imageConcat, easy positive, StringFunction|pysssss, StringFunction|pysssss, easy positive, easy seed, easy int, easy anythingIndexSwitch, RH_LLMAPI_NODE, easy showAnything, AppendStringsToList, ComfySwitchNode, easy outputToList]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 494582927997632, "steps": 50}
---

# 图片生成/图生图/生图-图片双海报自动(中英文)-Qwen-Image-2.1_2103796343163678721.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/生图-图片双海报自动(中英文)-Qwen-Image-2.1_2103796343163678721.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
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
- `easy showAnything`
- `TextEncodeQwenImage21`
- `VAELoader`
- `easy int`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
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
- `AppendStringsToList`
- `ComfySwitchNode`
- `easy outputToList`

## 关键参数

- `seed` = `494582927997632`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（31/36）

**有卡**：`MemoryCleaner`、`Qwen3_VQA`、`MultiplePathsInput`、`RH_Translator`、`ImageLoader`、`UNETLoader`、`CLIPLoader`、`KSampler`、`VAEDecode`、`GetImageSizeAndCount`、`SaveImage`、`easy saveText`、`TextEncodeQwenImage21`、`VAELoader`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextGenerateLTX2Prompt`、`PrimitiveBoolean`、`easy imageConcat`、`easy positive`、`StringFunction|pysssss`、`easy seed`、`easy anythingIndexSwitch`、`RH_LLMAPI_NODE`、`AppendStringsToList`、`easy outputToList`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、SaveImage、UNETLoader、easy seed
