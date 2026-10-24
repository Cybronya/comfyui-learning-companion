---
key: 图片生成/图生图/片场探班首尾帧驱动一镜到底运镜Smooth Mix Wan 2.2 I2V High_2004828661687742466.json
name: 片场探班首尾帧驱动一镜到底运镜Smooth Mix Wan 2.2 I2V High_2004828661687742466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/片场探班首尾帧驱动一镜到底运镜Smooth Mix Wan 2.2 I2V High_2004828661687742466.json
hash: e90df9d01af4865e
coverage: 0.61194
learned_at: 2026-10-23 13:14:20
nodes: [SetNode, GetNode, GetNode, KSamplerAdvanced, CLIPTextEncode, CLIPLoader, ShowText|pysssss, ModelSamplingSD3, SetNode, SetNode, SetNode, SetNode, WanFirstLastFrameToVideo, CR Integer To String, MathExpression|pysssss, GetNode, GetNode, SetNode, Note, SetNode, GetNode, GetNode, VAELoader, INTConstant, INTConstant, VHS_VideoCombine, VHS_VideoCombine, MultiplePathsInput, GetNode, Qwen3_VQA, PathchSageAttentionKJ, ImageLoader, ImageLoader, CLIPTextEncode, easy showAnything, wanBlockSwap, LoraLoaderModelOnly, VAEDecode, LayerUtility: PurgeVRAM, KSamplerAdvanced, LoraLoaderModelOnly, Float, GetNode, ShowText|pysssss, CR Prompt Text, UNETLoader, ModelSamplingSD3, Int, CR Prompt Text, YC_textReplaceNode, SetNode, ImageConcatMulti, ImageConcatMulti, SetNode, GetNode, GetNode, Float, PreviewImage, ImageResizeKJv2, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, GetNode, UNETLoader, wanBlockSwap, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 图片生成/图生图/片场探班首尾帧驱动一镜到底运镜Smooth Mix Wan 2.2 I2V High_2004828661687742466.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/片场探班首尾帧驱动一镜到底运镜Smooth Mix Wan 2.2 I2V High_2004828661687742466.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（67 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `ShowText|pysssss`
- `ModelSamplingSD3`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanFirstLastFrameToVideo`
- `CR Integer To String`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `SetNode`
- `Note`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAELoader`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MultiplePathsInput`
- `GetNode`
- `Qwen3_VQA`
- `PathchSageAttentionKJ`
- `ImageLoader`
- `ImageLoader`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `wanBlockSwap`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `Float`
- `GetNode`
- `ShowText|pysssss`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `Int`
- `CR Prompt Text`
- `YC_textReplaceNode`
- `SetNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `SetNode`
- `GetNode`
- `GetNode`
- `Float`
- `PreviewImage`
- `ImageResizeKJv2`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `UNETLoader` ★核心
- `wanBlockSwap`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **61%**（41/67）

**有卡**：`KSamplerAdvanced`、`CLIPTextEncode`、`CLIPLoader`、`ModelSamplingSD3`、`WanFirstLastFrameToVideo`、`CR Integer To String`、`MathExpression|pysssss`、`VAELoader`、`INTConstant`、`VHS_VideoCombine`、`MultiplePathsInput`、`Qwen3_VQA`、`PathchSageAttentionKJ`、`ImageLoader`、`wanBlockSwap`、`LoraLoaderModelOnly`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`Float`、`CR Prompt Text`、`UNETLoader`、`Int`、`YC_textReplaceNode`、`ImageConcatMulti`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
