---
key: 图片生成/图生图/Wan2.2双模型首尾帧视频 (1)_2085273690295590914.json
name: Wan2.2双模型首尾帧视频 (1)_2085273690295590914
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2双模型首尾帧视频 (1)_2085273690295590914.json
hash: 2e90a76600ea72a7
coverage: 0.973684
learned_at: 2026-10-23 11:28:20
nodes: [CLIPVisionLoader, CLIPLoader, VAELoader, JWInteger, UNETLoader, CLIPTextEncode, ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionEncode, wanBlockSwap, wanBlockSwap, ImageResizeKJ, Qwen3_VQA, CLIPVisionEncode, PathchSageAttentionKJ, PathchSageAttentionKJ, ImageConcanate, easy textSwitch, ModelPatchTorchSettings, ModelPatchTorchSettings, easy showAnything, CLIPTextEncode, WanFirstLastFrameToVideo, KSamplerAdvanced, KSamplerAdvanced, JWInteger, intToFloat _O, UNETLoader, VHS_VideoCombine, ModelSamplingSD3, ModelSamplingSD3, JWInteger, MathExpression|pysssss, LoadImage, LoadImage, CR Text, VAEDecode, Images to RGB]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 图片生成/图生图/Wan2.2双模型首尾帧视频 (1)_2085273690295590914.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2双模型首尾帧视频 (1)_2085273690295590914.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（38 个）：
- `CLIPVisionLoader`
- `CLIPLoader`
- `VAELoader`
- `JWInteger`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ImageConcanate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionEncode`
- `wanBlockSwap`
- `wanBlockSwap`
- `ImageResizeKJ`
- `Qwen3_VQA`
- `CLIPVisionEncode`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ImageConcanate`
- `easy textSwitch`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `WanFirstLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `JWInteger`
- `intToFloat _O`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `JWInteger`
- `MathExpression|pysssss`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `VAEDecode` ★核心
- `Images to RGB`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（37/38）

**有卡**：`CLIPVisionLoader`、`CLIPLoader`、`VAELoader`、`JWInteger`、`UNETLoader`、`CLIPTextEncode`、`ImageConcanate`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionEncode`、`wanBlockSwap`、`ImageResizeKJ`、`Qwen3_VQA`、`PathchSageAttentionKJ`、`easy textSwitch`、`ModelPatchTorchSettings`、`WanFirstLastFrameToVideo`、`KSamplerAdvanced`、`intToFloat _O`、`VHS_VideoCombine`、`ModelSamplingSD3`、`MathExpression|pysssss`、`LoadImage`、`CR Text`、`VAEDecode`、`Images to RGB`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
