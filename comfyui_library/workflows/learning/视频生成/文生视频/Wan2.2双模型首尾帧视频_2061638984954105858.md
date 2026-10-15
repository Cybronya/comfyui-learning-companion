---
key: 视频生成/文生视频/Wan2.2双模型首尾帧视频_2061638984954105858.json
name: Wan2.2双模型首尾帧视频_2061638984954105858
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2双模型首尾帧视频_2061638984954105858.json
hash: 2cba30e80c048e47
coverage: 0.973684
learned_at: 2026-10-15 22:47:14
nodes: [CLIPVisionLoader, CLIPLoader, VAELoader, JWInteger, UNETLoader, CLIPTextEncode, ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionEncode, wanBlockSwap, wanBlockSwap, ImageResizeKJ, Qwen3_VQA, CLIPVisionEncode, PathchSageAttentionKJ, PathchSageAttentionKJ, ImageConcanate, easy textSwitch, ModelPatchTorchSettings, ModelPatchTorchSettings, easy showAnything, CLIPTextEncode, WanFirstLastFrameToVideo, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, JWInteger, intToFloat _O, UNETLoader, VHS_VideoCombine, Images to RGB, ModelSamplingSD3, ModelSamplingSD3, JWInteger, MathExpression|pysssss, LoadImage, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/文生视频/Wan2.2双模型首尾帧视频_2061638984954105858.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2双模型首尾帧视频_2061638984954105858.json`

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
- `VAEDecode` ★核心
- `JWInteger`
- `intToFloat _O`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `Images to RGB`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `JWInteger`
- `MathExpression|pysssss`
- `LoadImage`
- `LoadImage`
- `CR Text`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（37/38）

**有卡**：`CLIPVisionLoader`、`CLIPLoader`、`VAELoader`、`JWInteger`、`UNETLoader`、`CLIPTextEncode`、`ImageConcanate`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionEncode`、`wanBlockSwap`、`ImageResizeKJ`、`Qwen3_VQA`、`PathchSageAttentionKJ`、`easy textSwitch`、`ModelPatchTorchSettings`、`WanFirstLastFrameToVideo`、`KSamplerAdvanced`、`VAEDecode`、`intToFloat _O`、`VHS_VideoCombine`、`Images to RGB`、`ModelSamplingSD3`、`MathExpression|pysssss`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
