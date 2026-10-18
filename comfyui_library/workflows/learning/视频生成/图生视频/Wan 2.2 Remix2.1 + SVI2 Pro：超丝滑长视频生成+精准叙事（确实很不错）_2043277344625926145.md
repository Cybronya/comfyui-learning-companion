---
key: 视频生成/图生视频/Wan 2.2 Remix2.1 + SVI2 Pro：超丝滑长视频生成+精准叙事（确实很不错）_2043277344625926145.json
name: Wan 2.2 Remix2.1 + SVI2 Pro：超丝滑长视频生成+精准叙事（确实很不错）_2043277344625926145.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan 2.2 Remix2.1 + SVI2 Pro：超丝滑长视频生成+精准叙事（确实很不错）_2043277344625926145.json
hash: cc691b6e134d5277
coverage: 0.978723
learned_at: 2026-10-15 22:36:31
nodes: [KSamplerAdvanced, KSamplerAdvanced, DiffusionModelLoaderKJ, LoraLoaderModelOnly, VAELoader, CLIPLoader, DiffusionModelLoaderKJ, LoraLoaderModelOnly, VAEDecode, KSamplerAdvanced, WanImageToVideoSVIPro, GODMT_SplitString, StringToInt, MathExpression|pysssss, GODMT_ListGetByIndex, GODMT_ListGetByIndex, MathExpression|pysssss, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, GODMT_ListGetByIndex, easy promptLine, DF_Int_to_Float, CLIPTextEncode, WanImageToVideoSVIPro, CLIPTextEncode, KSamplerAdvanced, CLIPTextEncode, VAEDecode, ImageBatchExtendWithOverlap, JWInteger, easy forLoopStart, CLIPTextEncode, StringToInt, GODMT_ListGetByIndex, GODMT_SplitString, MathExpression|pysssss, WWAA-LineCount, MathExpression|pysssss, easy promptLine, LoraLoaderModelOnly, VHS_VideoCombine, MarkdownNote, VHS_VideoCombine, easy forLoopEnd, CR Text, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan 2.2 Remix2.1 + SVI2 Pro：超丝滑长视频生成+精准叙事（确实很不错）_2043277344625926145.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2043277344625926145.json`

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
- `MarkdownNote`
- `VHS_VideoCombine`
- `easy forLoopEnd`
- `CR Text`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **98%**（46/47）

**有卡**：`KSamplerAdvanced`、`DiffusionModelLoaderKJ`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`WanImageToVideoSVIPro`、`GODMT_SplitString`、`StringToInt`、`MathExpression|pysssss`、`GODMT_ListGetByIndex`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`easy promptLine`、`DF_Int_to_Float`、`CLIPTextEncode`、`ImageBatchExtendWithOverlap`、`easy forLoopStart`、`WWAA-LineCount`、`VHS_VideoCombine`、`easy forLoopEnd`、`CR Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode
