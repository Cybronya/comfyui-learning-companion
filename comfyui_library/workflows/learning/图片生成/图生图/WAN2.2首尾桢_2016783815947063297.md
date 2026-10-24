---
key: 图片生成/图生图/WAN2.2首尾桢_2016783815947063297.json
name: WAN2.2首尾桢_2016783815947063297
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/WAN2.2首尾桢_2016783815947063297.json
hash: 71a29674084c1850
coverage: 0.815385
learned_at: 2026-10-23 11:27:32
nodes: [ModelSamplingSD3, SetNode, SetNode, easy getNode, RIFE VFI, CLIPTextEncode, GetNode, CLIPTextEncode, easy setNode, MathExpression|pysssss, PreviewImage, easy setNode, easy setNode, LoadUpscalerTensorrtModel, KSamplerAdvanced, KSamplerAdvanced, easy setNode, easy setNode, easy setNode, WanFirstLastFrameToVideo, easy getNode, easy getNode, CLIPVisionEncode, easy getNode, easy getNode, easy getNode, CLIPVisionEncode, GetNode, GetNode, easy getNode, wanBlockSwap, UpscalerTensorrt, LoadImage, easy setNode, easy setNode, ModelSamplingSD3, JWInteger, JWInteger, UNETLoader, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, wanBlockSwap, PathchSageAttentionKJ, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPLoader, SetNode, CLIPVisionLoader, JWInteger, ModelPatchTorchSettings, SetNode, ModelPatchTorchSettings, VAELoader, GetNode, GetNode, LoadImage, VHS_VideoCombine, VAEDecodeTiled, easy getNode, GetNode, StringFunction|pysssss]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 图片生成/图生图/WAN2.2首尾桢_2016783815947063297.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/WAN2.2首尾桢_2016783815947063297.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（65 个）：
- `ModelSamplingSD3`
- `SetNode`
- `SetNode`
- `easy getNode`
- `RIFE VFI`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `easy setNode`
- `MathExpression|pysssss`
- `PreviewImage`
- `easy setNode`
- `easy setNode`
- `LoadUpscalerTensorrtModel`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `WanFirstLastFrameToVideo`
- `easy getNode`
- `easy getNode`
- `CLIPVisionEncode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `CLIPVisionEncode`
- `GetNode`
- `GetNode`
- `easy getNode`
- `wanBlockSwap`
- `UpscalerTensorrt`
- `LoadImage`
- `easy setNode`
- `easy setNode`
- `ModelSamplingSD3`
- `JWInteger`
- `JWInteger`
- `UNETLoader` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `SetNode`
- `CLIPVisionLoader`
- `JWInteger`
- `ModelPatchTorchSettings`
- `SetNode`
- `ModelPatchTorchSettings`
- `VAELoader`
- `GetNode`
- `GetNode`
- `LoadImage`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `easy getNode`
- `GetNode`
- `StringFunction|pysssss`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **82%**（53/65）

**有卡**：`ModelSamplingSD3`、`easy getNode`、`RIFE VFI`、`CLIPTextEncode`、`easy setNode`、`MathExpression|pysssss`、`LoadUpscalerTensorrtModel`、`KSamplerAdvanced`、`WanFirstLastFrameToVideo`、`CLIPVisionEncode`、`wanBlockSwap`、`UpscalerTensorrt`、`LoadImage`、`JWInteger`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CLIPLoader`、`CLIPVisionLoader`、`ModelPatchTorchSettings`、`VAELoader`、`VHS_VideoCombine`、`VAEDecodeTiled`、`StringFunction|pysssss`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、VAEDecodeTiled
