---
key: 视频生成/图生视频/Wan2.2-I2V-图生视频-视频提示词全自动反推-工作流_2041409564251262978.json
name: Wan2.2-I2V-图生视频-视频提示词全自动反推-工作流_2041409564251262978.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-I2V-图生视频-视频提示词全自动反推-工作流_2041409564251262978.json
hash: 003f7301381670e9
coverage: 0.935484
learned_at: 2026-10-15 22:36:19
nodes: [CLIPTextEncode, CLIPTextEncode, INTConstant, INTConstant, WanImageToVideo, wanBlockSwap, wanBlockSwap, CR Prompt Text, easy showAnything, Text Concatenate, ModelSamplingSD3, INTConstant, JWInteger, MathExpression|pysssss, Note, ImageResizeKJv2, TextInput_, LayerUtility: TextJoin, LoraLoaderModelOnly, LoadImage, VHS_VideoCombine, KSamplerAdvanced, VAEDecode, Qwen3_VQA, ModelSamplingSD3, LoraLoaderModelOnly, UNETLoader, UNETLoader, CLIPLoader, VAELoader, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2-I2V-图生视频-视频提示词全自动反推-工作流_2041409564251262978.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041409564251262978.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（31 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `INTConstant`
- `INTConstant`
- `WanImageToVideo`
- `wanBlockSwap`
- `wanBlockSwap`
- `CR Prompt Text`
- `easy showAnything`
- `Text Concatenate`
- `ModelSamplingSD3`
- `INTConstant`
- `JWInteger`
- `MathExpression|pysssss`
- `Note`
- `ImageResizeKJv2`
- `TextInput_`
- `LayerUtility: TextJoin`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `Qwen3_VQA`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **94%**（29/31）

**有卡**：`CLIPTextEncode`、`INTConstant`、`WanImageToVideo`、`wanBlockSwap`、`CR Prompt Text`、`Text Concatenate`、`ModelSamplingSD3`、`JWInteger`、`MathExpression|pysssss`、`ImageResizeKJv2`、`TextInput_`、`LayerUtility: TextJoin`、`LoraLoaderModelOnly`、`LoadImage`、`VHS_VideoCombine`、`KSamplerAdvanced`、`VAEDecode`、`Qwen3_VQA`、`UNETLoader`、`CLIPLoader`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
