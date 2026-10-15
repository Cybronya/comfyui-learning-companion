---
key: 视频生成/文生视频/动图首选+wan2.2首尾帧+全节点注释_2061457988065513474.json
name: 动图首选+wan2.2首尾帧+全节点注释_2061457988065513474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/动图首选+wan2.2首尾帧+全节点注释_2061457988065513474.json
hash: f8056bb0aa2b77b0
coverage: 0.5
learned_at: 2026-10-15 22:48:14
nodes: [PathchSageAttentionKJ, UNETLoader, wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, CLIPTextEncode, CLIPVisionLoader, CLIPVisionEncode, CLIPVisionEncode, VAEDecode, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, MathExpression|pysssss, ImageResizeKJ, easy textSwitch, WanFirstLastFrameToVideo, VHS_VideoCombine, KSamplerAdvanced, UNETLoader, ImageConcanate, Images to RGB, LoadImage, ModelPatchTorchSettings, ModelPatchTorchSettings, KSamplerAdvanced, CLIPLoader, VAELoader, LoadImage, ModelSamplingSD3, ModelSamplingSD3, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadImage, CR Text, easy showAnything, CLIPTextEncode, Qwen3_VQA]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/动图首选+wan2.2首尾帧+全节点注释_2061457988065513474.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/动图首选+wan2.2首尾帧+全节点注释_2061457988065513474.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（72 个）：
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `VAEDecode` ★核心
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `MathExpression|pysssss`
- `ImageResizeKJ`
- `easy textSwitch`
- `WanFirstLastFrameToVideo`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `ImageConcanate`
- `Images to RGB`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `Qwen3_VQA`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **50%**（36/72）

**有卡**：`PathchSageAttentionKJ`、`UNETLoader`、`wanBlockSwap`、`CLIPTextEncode`、`CLIPVisionLoader`、`CLIPVisionEncode`、`VAEDecode`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`ImageResizeKJ`、`easy textSwitch`、`WanFirstLastFrameToVideo`、`VHS_VideoCombine`、`KSamplerAdvanced`、`ImageConcanate`、`Images to RGB`、`LoadImage`、`ModelPatchTorchSettings`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`CR Text`、`Qwen3_VQA`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
