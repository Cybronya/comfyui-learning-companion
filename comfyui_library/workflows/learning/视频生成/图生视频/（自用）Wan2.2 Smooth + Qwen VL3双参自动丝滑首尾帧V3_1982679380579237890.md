---
key: 视频生成/图生视频/（自用）Wan2.2 Smooth + Qwen VL3双参自动丝滑首尾帧V3_1982679380579237890.json
name: （自用）Wan2.2 Smooth + Qwen VL3双参自动丝滑首尾帧V3_1982679380579237890.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/（自用）Wan2.2 Smooth + Qwen VL3双参自动丝滑首尾帧V3_1982679380579237890.json
hash: 9ac1769306af1554
coverage: 0.944444
learned_at: 2026-10-15 22:32:42
nodes: [CLIPTextEncode, Int, MultiplePathsInput, ModelSamplingSD3, ModelSamplingSD3, LayerUtility: ImageScaleByAspectRatio V2, WanFirstLastFrameToVideo, PathchSageAttentionKJ, PathchSageAttentionKJ, ImageResizeKJv2, CLIPTextEncode, VAELoader, CLIPLoader, easy showAnything, wanBlockSwap, LoraLoaderModelOnly, wanBlockSwap, easy showAnything, ImageLoader, CR Prompt Text, Int, UNETLoader, VHS_VideoCombine, TT_img_enc, SaveImage, TT_img_enc_v2, SaveImage, KSamplerAdvanced, LoraLoaderModelOnly, UNETLoader, KSamplerAdvanced, Qwen3_VQA, SaveImage, DuckHideNode, VAEDecode, ImageLoader]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/（自用）Wan2.2 Smooth + Qwen VL3双参自动丝滑首尾帧V3_1982679380579237890.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1982679380579237890.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `CLIPTextEncode` ★核心
- `Int`
- `MultiplePathsInput`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanFirstLastFrameToVideo`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `easy showAnything`
- `wanBlockSwap`
- `LoraLoaderModelOnly` ★核心
- `wanBlockSwap`
- `easy showAnything`
- `ImageLoader`
- `CR Prompt Text`
- `Int`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `TT_img_enc`
- `SaveImage`
- `TT_img_enc_v2`
- `SaveImage`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `Qwen3_VQA`
- `SaveImage`
- `DuckHideNode`
- `VAEDecode` ★核心
- `ImageLoader`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **94%**（34/36）

**有卡**：`CLIPTextEncode`、`Int`、`MultiplePathsInput`、`ModelSamplingSD3`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanFirstLastFrameToVideo`、`PathchSageAttentionKJ`、`ImageResizeKJv2`、`VAELoader`、`CLIPLoader`、`wanBlockSwap`、`LoraLoaderModelOnly`、`ImageLoader`、`CR Prompt Text`、`UNETLoader`、`VHS_VideoCombine`、`TT_img_enc`、`SaveImage`、`TT_img_enc_v2`、`KSamplerAdvanced`、`Qwen3_VQA`、`DuckHideNode`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
