---
key: 视频生成/图生视频/龙明wan2.1 运镜lora_1934983961166684161.json
name: 龙明wan2.1 运镜lora_1934983961166684161.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/龙明wan2.1 运镜lora_1934983961166684161.json
hash: 429dcb65aabcac03
coverage: 0.884615
learned_at: 2026-10-15 22:30:20
nodes: [CLIPTextEncode, CLIPVisionLoader, VAELoader, CLIPVisionEncode, WanImageToVideo, Florence2ModelLoader, ImageResizeKJv2, PreviewImage, CLIPTextEncode, CLIPLoader, CR Text Concatenate, Florence2Run, easy showAnything, ModelSamplingSD3, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, PrimitiveNode, WanVideoTeaCacheKJ, INTConstant, KSampler, VAEDecode, VHS_VideoCombine, INTConstant, INTConstant, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 219978186113939, "steps": 20}
---

# 视频生成/图生视频/龙明wan2.1 运镜lora_1934983961166684161.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1934983961166684161.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `VAELoader`
- `CLIPVisionEncode`
- `WanImageToVideo`
- `Florence2ModelLoader`
- `ImageResizeKJv2`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CR Text Concatenate`
- `Florence2Run`
- `easy showAnything`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveNode`
- `WanVideoTeaCacheKJ`
- `INTConstant`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `LoadImage`

## 关键参数

- `seed` = `219978186113939`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（23/26）

**有卡**：`CLIPTextEncode`、`CLIPVisionLoader`、`VAELoader`、`CLIPVisionEncode`、`WanImageToVideo`、`Florence2ModelLoader`、`ImageResizeKJv2`、`CLIPLoader`、`CR Text Concatenate`、`Florence2Run`、`ModelSamplingSD3`、`UNETLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`WanVideoTeaCacheKJ`、`INTConstant`、`KSampler`、`VAEDecode`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
