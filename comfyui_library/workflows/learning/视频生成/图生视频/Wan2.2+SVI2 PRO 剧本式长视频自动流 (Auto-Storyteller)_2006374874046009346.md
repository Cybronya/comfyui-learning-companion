---
key: 视频生成/图生视频/Wan2.2+SVI2 PRO 剧本式长视频自动流 (Auto-Storyteller)_2006374874046009346.json
name: Wan2.2+SVI2 PRO 剧本式长视频自动流 (Auto-Storyteller)_2006374874046009346.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2006374874046009346.json
hash: 982ce7585a85a4e4
coverage: 0.648352
learned_at: 2026-10-15 22:34:01
nodes: [CLIPTextEncode, ImageResizeKJv2, INTConstant, JWInteger, INTConstant, SetNode, SetNode, SetNode, SetNode, SetNode, DF_Int_to_Float, SetNode, GetImageRangeFromBatch, GetNode, GODMT_SplitString, GetNode, GetNode, GODMT_ListGetByIndex, GODMT_ListGetByIndex, StringToInt, MathExpression|pysssss, CLIPTextEncode, SetNode, GetNode, GetNode, VAEEncode, WanImageToVideoSVIPro, GetNode, GetNode, WanVideoNAG, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, ModelSamplingSD3, GetNode, LoraLoaderModelOnly, CFGZeroStar, SetNode, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, SetNode, CLIPLoader, VAELoader, CLIPVisionLoader, SetNode, SetNode, SetNode, LoraLoaderModelOnly, easy promptLine, GODMT_ListGetByIndex, MathExpression|pysssss, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GODMT_SplitString, StringToInt, GODMT_ListGetByIndex, CLIPTextEncode, VAEEncode, WanVideoNAG, ModelSamplingSD3, ModelSamplingSD3, WanImageToVideoSVIPro, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, ImageBatchExtendWithOverlap, VHS_VideoCombine, GetNode, GetNode, easy forLoopEnd, VHS_VideoCombine, MarkdownNote, LoadImage, easy promptLine, MathExpression|pysssss, CR Text, WWAA-LineCount, MathExpression|pysssss, SetNode, easy forLoopStart, GetNode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2+SVI2 PRO 剧本式长视频自动流 (Auto-Storyteller)_2006374874046009346.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2006374874046009346.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（91 个）：
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `INTConstant`
- `JWInteger`
- `INTConstant`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `DF_Int_to_Float`
- `SetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `GODMT_SplitString`
- `GetNode`
- `GetNode`
- `GODMT_ListGetByIndex`
- `GODMT_ListGetByIndex`
- `StringToInt`
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `WanImageToVideoSVIPro`
- `GetNode`
- `GetNode`
- `WanVideoNAG`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `CFGZeroStar`
- `SetNode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `easy promptLine`
- `GODMT_ListGetByIndex`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GODMT_SplitString`
- `StringToInt`
- `GODMT_ListGetByIndex`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `WanVideoNAG`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `WanImageToVideoSVIPro`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageBatchExtendWithOverlap`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `easy forLoopEnd`
- `VHS_VideoCombine`
- `MarkdownNote`
- `LoadImage`
- `easy promptLine`
- `MathExpression|pysssss`
- `CR Text`
- `WWAA-LineCount`
- `MathExpression|pysssss`
- `SetNode`
- `easy forLoopStart`
- `GetNode`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **65%**（59/91）

**有卡**：`CLIPTextEncode`、`ImageResizeKJv2`、`INTConstant`、`JWInteger`、`DF_Int_to_Float`、`GetImageRangeFromBatch`、`GODMT_SplitString`、`GODMT_ListGetByIndex`、`StringToInt`、`MathExpression|pysssss`、`VAEEncode`、`WanImageToVideoSVIPro`、`WanVideoNAG`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`CFGZeroStar`、`UNETLoader`、`PathchSageAttentionKJ`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`easy promptLine`、`ImageBatchExtendWithOverlap`、`easy forLoopEnd`、`LoadImage`、`CR Text`、`WWAA-LineCount`、`easy forLoopStart`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
