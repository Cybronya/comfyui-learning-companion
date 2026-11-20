---
key: 平台全量/wan2.2 首尾帧加插帧V2版_1985753196125724674.json
name: wan2.2 首尾帧加插帧V2版_1985753196125724674
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2 首尾帧加插帧V2版_1985753196125724674.json
hash: d15355e8d734d9f5
coverage: 0.804878
learned_at: 2026-11-14 01:19:23
nodes: [ImageBatchMultiple+, UNETLoader, wanBlockSwap, SetNode, SetNode, wanBlockSwap, CLIPTextEncode, easy showAnything, UNETLoader, PathchSageAttentionKJ, SetNode, PathchSageAttentionKJ, VAELoader, CLIPTextEncode, AILab_MiniCPM_4_V_Advanced, LoadImage, ImageResizeKJv2, ImageResizeKJv2, PreviewImage, VAEDecode, ImageResizeKJv2, VHS_VideoCombine, ImageConcatMulti, ImageStitch, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, GetNode, GetNode, CLIPLoader, WanFirstMiddleLastFrameToVideo, LoadImage, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, VHS_VideoCombine, ColorMatch]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 平台全量/wan2.2 首尾帧加插帧V2版_1985753196125724674.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2 首尾帧加插帧V2版_1985753196125724674.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `ImageBatchMultiple+`
- `UNETLoader` ★核心
- `wanBlockSwap`
- `SetNode`
- `SetNode`
- `wanBlockSwap`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `SetNode`
- `PathchSageAttentionKJ`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `AILab_MiniCPM_4_V_Advanced`
- `LoadImage`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `PreviewImage`
- `VAEDecode` ★核心
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageStitch`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPLoader`
- `WanFirstMiddleLastFrameToVideo`
- `LoadImage`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `VHS_VideoCombine`
- `ColorMatch`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **80%**（33/41）

**有卡**：`ImageBatchMultiple+`、`UNETLoader`、`wanBlockSwap`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`VAELoader`、`AILab_MiniCPM_4_V_Advanced`、`LoadImage`、`ImageResizeKJv2`、`VAEDecode`、`VHS_VideoCombine`、`ImageConcatMulti`、`ImageStitch`、`LoraLoaderModelOnly`、`CLIPLoader`、`WanFirstMiddleLastFrameToVideo`、`ModelSamplingSD3`、`KSamplerAdvanced`、`ColorMatch`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerAdvanced
