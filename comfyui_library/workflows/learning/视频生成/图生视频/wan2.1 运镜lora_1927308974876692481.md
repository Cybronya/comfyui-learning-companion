---
key: 视频生成/图生视频/wan2.1 运镜lora_1927308974876692481.json
name: wan2.1 运镜lora_1927308974876692481.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1927308974876692481.json
hash: cab0b08a27f6f509
coverage: 0.884615
learned_at: 2026-10-15 22:29:54
nodes: [CLIPTextEncode, CLIPVisionLoader, VAELoader, CLIPVisionEncode, WanImageToVideo, Florence2ModelLoader, ImageResizeKJv2, PreviewImage, CLIPTextEncode, CLIPLoader, CR Text Concatenate, Florence2Run, easy showAnything, ModelSamplingSD3, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, PrimitiveNode, WanVideoTeaCacheKJ, INTConstant, KSampler, VAEDecode, VHS_VideoCombine, INTConstant, LoadImage, INTConstant]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 348163047833994, "steps": 20}
---

# 视频生成/图生视频/wan2.1 运镜lora_1927308974876692481.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1927308974876692481.json`

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
- `LoadImage`
- `INTConstant`

## 关键参数

- `seed` = `348163047833994`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（23/26）

**有卡**：`CLIPTextEncode`、`CLIPVisionLoader`、`VAELoader`、`CLIPVisionEncode`、`WanImageToVideo`、`Florence2ModelLoader`、`ImageResizeKJv2`、`CLIPLoader`、`CR Text Concatenate`、`Florence2Run`、`ModelSamplingSD3`、`UNETLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`WanVideoTeaCacheKJ`、`INTConstant`、`KSampler`、`VAEDecode`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
