---
key: 视频生成/图生视频/Wan 2.2 Remix2.1图生长视频 ：分镜时长+精准叙事_2016438828810117122.json
name: Wan 2.2 Remix2.1图生长视频 ：分镜时长+精准叙事_2016438828810117122.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2016438828810117122.json
hash: 50de9ecb047edd75
coverage: 0.978723
learned_at: 2026-10-15 22:34:42
nodes: [KSamplerAdvanced, KSamplerAdvanced, DiffusionModelLoaderKJ, LoraLoaderModelOnly, VAELoader, CLIPLoader, DiffusionModelLoaderKJ, LoraLoaderModelOnly, VAEDecode, KSamplerAdvanced, WanImageToVideoSVIPro, GODMT_SplitString, StringToInt, GODMT_ListGetByIndex, GODMT_ListGetByIndex, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, GODMT_ListGetByIndex, easy promptLine, DF_Int_to_Float, CLIPTextEncode, WanImageToVideoSVIPro, CLIPTextEncode, KSamplerAdvanced, CLIPTextEncode, VAEDecode, ImageBatchExtendWithOverlap, easy forLoopEnd, JWInteger, easy forLoopStart, CLIPTextEncode, StringToInt, GODMT_ListGetByIndex, GODMT_SplitString, MathExpression|pysssss, WWAA-LineCount, MathExpression|pysssss, easy promptLine, LoraLoaderModelOnly, VHS_VideoCombine, JWInteger, MathExpression|pysssss, VHS_VideoCombine, LoadImage, CR Text, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan 2.2 Remix2.1图生长视频 ：分镜时长+精准叙事_2016438828810117122.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2016438828810117122.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（47 个）：
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `WanImageToVideoSVIPro`
- `GODMT_SplitString`
- `StringToInt`
- `GODMT_ListGetByIndex`
- `GODMT_ListGetByIndex`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `GODMT_ListGetByIndex`
- `easy promptLine`
- `DF_Int_to_Float`
- `CLIPTextEncode` ★核心
- `WanImageToVideoSVIPro`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ImageBatchExtendWithOverlap`
- `easy forLoopEnd`
- `JWInteger`
- `easy forLoopStart`
- `CLIPTextEncode` ★核心
- `StringToInt`
- `GODMT_ListGetByIndex`
- `GODMT_SplitString`
- `MathExpression|pysssss`
- `WWAA-LineCount`
- `MathExpression|pysssss`
- `easy promptLine`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `JWInteger`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `LoadImage`
- `CR Text`
- `MarkdownNote`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **98%**（46/47）

**有卡**：`KSamplerAdvanced`、`DiffusionModelLoaderKJ`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`WanImageToVideoSVIPro`、`GODMT_SplitString`、`StringToInt`、`GODMT_ListGetByIndex`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`easy promptLine`、`DF_Int_to_Float`、`CLIPTextEncode`、`ImageBatchExtendWithOverlap`、`easy forLoopEnd`、`JWInteger`、`easy forLoopStart`、`WWAA-LineCount`、`VHS_VideoCombine`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode
