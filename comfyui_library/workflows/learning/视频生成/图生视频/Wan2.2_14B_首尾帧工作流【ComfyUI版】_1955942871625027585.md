---
key: 视频生成/图生视频/Wan2.2_14B_首尾帧工作流【ComfyUI版】_1955942871625027585.json
name: Wan2.2_14B_首尾帧工作流【ComfyUI版】_1955942871625027585.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2_14B_首尾帧工作流【ComfyUI版】_1955942871625027585.json
hash: f544ea183d591039
coverage: 0.96
learned_at: 2026-10-15 22:31:11
nodes: [ModelSamplingSD3, UNETLoader, UNETLoader, CLIPVisionEncode, CLIPVisionEncode, WanFirstLastFrameToVideo, CLIPLoader, VAELoader, CLIPVisionLoader, ModelSamplingSD3, LoadImage, CLIPTextEncode, LoadImage, CLIPTextEncode, VHS_VideoCombine, CR Text, MarkdownNote, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, WanVideoNAG]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2_14B_首尾帧工作流【ComfyUI版】_1955942871625027585.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1955942871625027585.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（25 个）：
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `WanFirstLastFrameToVideo`
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `ModelSamplingSD3`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `CR Text`
- `MarkdownNote`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `WanVideoNAG`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`ModelSamplingSD3`、`UNETLoader`、`CLIPVisionEncode`、`WanFirstLastFrameToVideo`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`LoadImage`、`CLIPTextEncode`、`VHS_VideoCombine`、`CR Text`、`KSamplerAdvanced`、`VAEDecode`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`WanVideoNAG`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
