---
key: 视频生成/图生视频/video_wan2_2_14B_i2v_FLframe_transition_1986333463185948673.json
name: video_wan2_2_14B_i2v_FLframe_transition_1986333463185948673.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/video_wan2_2_14B_i2v_FLframe_transition_1986333463185948673.json
hash: 5096b530a86b7a64
coverage: 0.5
learned_at: 2026-10-15 22:32:54
nodes: [PathchSageAttentionKJ, CFGZeroStar, SetNode, SetNode, GetNode, ModelSamplingSD3, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, WanVideoNAG, CLIPTextEncode, SetNode, SetNode, ModelSamplingSD3, GetNode, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, SetNode, INTConstant, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, WanFirstLastFrameToVideo, PreviewAny, CLIPVisionLoader, GetNode, VAEDecode, VHS_VideoCombine, LoadImage, ImageResizeKJv2, LoadImage, INTConstant, ImageResizeKJv2, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, CLIPVisionEncode, CLIPVisionEncode, LoraLoaderModelOnly, AILab_QwenVL]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/video_wan2_2_14B_i2v_FLframe_transition_1986333463185948673.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1986333463185948673.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（60 个）：
- `PathchSageAttentionKJ`
- `CFGZeroStar`
- `SetNode`
- `SetNode`
- `GetNode`
- `ModelSamplingSD3`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoNAG`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `ModelSamplingSD3`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `INTConstant`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanFirstLastFrameToVideo`
- `PreviewAny`
- `CLIPVisionLoader`
- `GetNode`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `ImageResizeKJv2`
- `LoadImage`
- `INTConstant`
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `LoraLoaderModelOnly` ★核心
- `AILab_QwenVL`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **50%**（30/60）

**有卡**：`PathchSageAttentionKJ`、`CFGZeroStar`、`ModelSamplingSD3`、`WanVideoNAG`、`CLIPTextEncode`、`KSamplerAdvanced`、`INTConstant`、`WanFirstLastFrameToVideo`、`CLIPVisionLoader`、`VAEDecode`、`VHS_VideoCombine`、`LoadImage`、`ImageResizeKJv2`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`CLIPVisionEncode`、`AILab_QwenVL`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
