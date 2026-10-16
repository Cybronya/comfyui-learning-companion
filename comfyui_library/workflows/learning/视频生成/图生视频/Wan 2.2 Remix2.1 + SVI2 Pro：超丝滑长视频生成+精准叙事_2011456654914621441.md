---
key: 视频生成/图生视频/Wan 2.2 Remix2.1 + SVI2 Pro：超丝滑长视频生成+精准叙事_2011456654914621441.json
name: Wan 2.2 Remix2.1 + SVI2 Pro：超丝滑长视频生成+精准叙事_2011456654914621441.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2011456654914621441.json
hash: dd0bfb0f159301d0
coverage: 0.978723
learned_at: 2026-10-15 22:34:23
nodes: [KSamplerAdvanced, KSamplerAdvanced, DiffusionModelLoaderKJ, LoraLoaderModelOnly, VAELoader, CLIPLoader, DiffusionModelLoaderKJ, LoraLoaderModelOnly, VAEDecode, VHS_VideoCombine, KSamplerAdvanced, WanImageToVideoSVIPro, GODMT_SplitString, StringToInt, MathExpression|pysssss, GODMT_ListGetByIndex, GODMT_ListGetByIndex, MathExpression|pysssss, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, GODMT_ListGetByIndex, easy promptLine, DF_Int_to_Float, CLIPTextEncode, WanImageToVideoSVIPro, CLIPTextEncode, KSamplerAdvanced, CLIPTextEncode, VAEDecode, ImageBatchExtendWithOverlap, easy forLoopEnd, JWInteger, MarkdownNote, easy forLoopStart, LoadImage, CLIPTextEncode, StringToInt, GODMT_ListGetByIndex, GODMT_SplitString, MathExpression|pysssss, WWAA-LineCount, MathExpression|pysssss, CR Text, easy promptLine, LoraLoaderModelOnly, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan 2.2 Remix2.1 + SVI2 Pro：超丝滑长视频生成+精准叙事_2011456654914621441.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2011456654914621441.json`

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
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `WanImageToVideoSVIPro`
- `GODMT_SplitString`
- `StringToInt`
- `MathExpression|pysssss`
- `GODMT_ListGetByIndex`
- `GODMT_ListGetByIndex`
- `MathExpression|pysssss`
- `JWInteger`
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
- `MarkdownNote`
- `easy forLoopStart`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `StringToInt`
- `GODMT_ListGetByIndex`
- `GODMT_SplitString`
- `MathExpression|pysssss`
- `WWAA-LineCount`
- `MathExpression|pysssss`
- `CR Text`
- `easy promptLine`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **98%**（46/47）

**有卡**：`KSamplerAdvanced`、`DiffusionModelLoaderKJ`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`VHS_VideoCombine`、`WanImageToVideoSVIPro`、`GODMT_SplitString`、`StringToInt`、`MathExpression|pysssss`、`GODMT_ListGetByIndex`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`easy promptLine`、`DF_Int_to_Float`、`CLIPTextEncode`、`ImageBatchExtendWithOverlap`、`easy forLoopEnd`、`easy forLoopStart`、`LoadImage`、`WWAA-LineCount`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode
