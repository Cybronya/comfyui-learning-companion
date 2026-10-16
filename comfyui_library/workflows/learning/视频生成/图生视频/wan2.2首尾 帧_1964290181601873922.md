---
key: 视频生成/图生视频/wan2.2首尾 帧_1964290181601873922.json
name: wan2.2首尾 帧_1964290181601873922.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1964290181601873922.json
hash: b80671bf9a5911a4
coverage: 1
learned_at: 2026-10-15 22:31:34
nodes: [CLIPLoader, VAELoader, LoraLoaderModelOnly, UNETLoader, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, WanVideoNAG, WanVideoNAG, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAs, WanFirstLastFrameToVideo, WanMoeKSampler, VAEDecode, VHS_VideoCombine, LoadImage, CLIPTextEncode, CLIPTextEncode, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "euler", "sampler_name": 4, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2首尾 帧_1964290181601873922.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1964290181601873922.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（22 个）：
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `WanVideoNAG`
- `WanVideoNAG`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageMaskScaleAs`
- `WanFirstLastFrameToVideo`
- `WanMoeKSampler` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `4`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`PathchSageAttentionKJ`、`WanVideoNAG`、`ModelSamplingSD3`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAs`、`WanFirstLastFrameToVideo`、`WanMoeKSampler`、`VAEDecode`、`VHS_VideoCombine`、`LoadImage`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
