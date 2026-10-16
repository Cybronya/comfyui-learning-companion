---
key: 视频生成/图生视频/【4月】Wan2.2 Dasiwa V10+ SVI2Pro全自动长视频（严格遵循提示词控制）_2042934269093355522.json
name: 【4月】Wan2.2 Dasiwa V10+ SVI2Pro全自动长视频（严格遵循提示词控制）_2042934269093355522.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2042934269093355522.json
hash: f1272c16cfb7206b
coverage: 0.978723
learned_at: 2026-10-15 22:36:30
nodes: [GODMT_SplitString, StringToInt, GODMT_ListGetByIndex, easy promptLine, GODMT_ListGetByIndex, CLIPTextEncode, MathExpression|pysssss, VAELoader, ModelSamplingSD3, GODMT_ListGetByIndex, GODMT_SplitString, MathExpression|pysssss, GODMT_ListGetByIndex, LoraLoaderModelOnly, StringToInt, easy promptLine, MathExpression|pysssss, JWInteger, easy forLoopStart, KSamplerAdvanced, WanAdvancedI2V, KSamplerAdvanced, LoadImage, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, WanAdvancedI2V, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, CLIPTextEncode, ImageBatchExtendWithOverlap, VHS_VideoCombine, VAEDecode, easy forLoopEnd, WWAA-LineCount, MathExpression|pysssss, KSamplerAdvanced, DF_Int_to_Float, VHS_VideoCombine, JWInteger, CR Text, UNETLoader, CLIPLoader, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/【4月】Wan2.2 Dasiwa V10+ SVI2Pro全自动长视频（严格遵循提示词控制）_2042934269093355522.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2042934269093355522.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（47 个）：
- `GODMT_SplitString`
- `StringToInt`
- `GODMT_ListGetByIndex`
- `easy promptLine`
- `GODMT_ListGetByIndex`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `VAELoader`
- `ModelSamplingSD3`
- `GODMT_ListGetByIndex`
- `GODMT_SplitString`
- `MathExpression|pysssss`
- `GODMT_ListGetByIndex`
- `LoraLoaderModelOnly` ★核心
- `StringToInt`
- `easy promptLine`
- `MathExpression|pysssss`
- `JWInteger`
- `easy forLoopStart`
- `KSamplerAdvanced` ★核心
- `WanAdvancedI2V`
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanAdvancedI2V`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `ImageBatchExtendWithOverlap`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `easy forLoopEnd`
- `WWAA-LineCount`
- `MathExpression|pysssss`
- `KSamplerAdvanced` ★核心
- `DF_Int_to_Float`
- `VHS_VideoCombine`
- `JWInteger`
- `CR Text`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `MarkdownNote`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **98%**（46/47）

**有卡**：`GODMT_SplitString`、`StringToInt`、`GODMT_ListGetByIndex`、`easy promptLine`、`CLIPTextEncode`、`MathExpression|pysssss`、`VAELoader`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`JWInteger`、`easy forLoopStart`、`KSamplerAdvanced`、`WanAdvancedI2V`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`VHS_VideoCombine`、`ImageBatchExtendWithOverlap`、`easy forLoopEnd`、`WWAA-LineCount`、`DF_Int_to_Float`、`CR Text`、`UNETLoader`、`CLIPLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
