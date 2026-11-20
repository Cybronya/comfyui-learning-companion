---
key: 平台全量/视频-视频双海报自动(中英文)-Qwen-Image-2.1_2103796336226295810.json
name: 视频-视频双海报自动(中英文)-Qwen-Image-2.1_2103796336226295810
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频-视频双海报自动(中英文)-Qwen-Image-2.1_2103796336226295810.json
hash: 860eb65a7342ce13
coverage: 0.816327
learned_at: 2026-11-14 02:34:30
nodes: [RH_LLMAPI_NODE, easy int, StringFunction|pysssss, RH_Translator, easy saveText, VHS_VideoInfoLoaded, EmptyImage, StringFunction|pysssss, MathExpression|pysssss, easy int, easy int, MathExpression|pysssss, Float, Note, Reroute, Reroute, GetImageSizeAndCount, easy positive, LayerUtility: ImageScaleByAspectRatio V2, GetImageSizeAndCount, UNETLoader, CLIPLoader, KSampler, VAEDecode, CLIPLoader, TextGenerateLTX2Prompt, easy showAnything, GetImageSizeAndCount, easy anythingIndexSwitch, easy showAnything, ImageConcanate, GetImageSizeAndCount, GetImageSizeAndCount, easy positive, ImageResizeKJv2, VHS_VideoCombine, VAELoader, PreviewImage, easy seed, ImageResizeKJv2, PreviewImage, TextEncodeQwenImage21, GetImageSizeAndCount, VHS_LoadVideo, PrimitiveBoolean, easy showAnything, AppendStringsToList, ComfySwitchNode, easy outputToList]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 12183232895522, "steps": 50}
---

# 平台全量/视频-视频双海报自动(中英文)-Qwen-Image-2.1_2103796336226295810.json

> 来源文件 `comfyui_library/workflows/平台全量/视频-视频双海报自动(中英文)-Qwen-Image-2.1_2103796336226295810.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `RH_LLMAPI_NODE`
- `easy int`
- `StringFunction|pysssss`
- `RH_Translator`
- `easy saveText`
- `VHS_VideoInfoLoaded`
- `EmptyImage`
- `StringFunction|pysssss`
- `MathExpression|pysssss`
- `easy int`
- `easy int`
- `MathExpression|pysssss`
- `Float`
- `Note`
- `Reroute`
- `Reroute`
- `GetImageSizeAndCount`
- `easy positive`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSizeAndCount`
- `UNETLoader` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `GetImageSizeAndCount`
- `easy anythingIndexSwitch`
- `easy showAnything`
- `ImageConcanate`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `easy positive`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `VAELoader`
- `PreviewImage`
- `easy seed`
- `ImageResizeKJv2`
- `PreviewImage`
- `TextEncodeQwenImage21`
- `GetImageSizeAndCount`
- `VHS_LoadVideo`
- `PrimitiveBoolean`
- `easy showAnything`
- `AppendStringsToList`
- `ComfySwitchNode`
- `easy outputToList`

## 关键参数

- `seed` = `12183232895522`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（40/49）

**有卡**：`RH_LLMAPI_NODE`、`easy int`、`StringFunction|pysssss`、`RH_Translator`、`easy saveText`、`VHS_VideoInfoLoaded`、`EmptyImage`、`MathExpression|pysssss`、`Float`、`GetImageSizeAndCount`、`easy positive`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`CLIPLoader`、`KSampler`、`VAEDecode`、`TextGenerateLTX2Prompt`、`easy anythingIndexSwitch`、`ImageConcanate`、`ImageResizeKJv2`、`VHS_VideoCombine`、`VAELoader`、`easy seed`、`TextEncodeQwenImage21`、`VHS_LoadVideo`、`PrimitiveBoolean`、`AppendStringsToList`、`easy outputToList`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、LayerUtility: ImageScaleByAspectRatio V2、UNETLoader、easy seed
