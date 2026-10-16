---
key: 视频生成/图生视频/Wan2.2_14B_官方强推-图生视频（强烈推荐）_1956203344467558401.json
name: Wan2.2_14B_官方强推-图生视频（强烈推荐）_1956203344467558401.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1956203344467558401.json
hash: e2eb45742fc55c7e
coverage: 0.956522
learned_at: 2026-10-15 22:31:12
nodes: [TorchCompileModelWanVideoV2, CLIPLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, TorchCompileModelWanVideoV2, VAELoader, MathExpression|pysssss, WanImageToVideo, CLIPTextEncode, MarkdownNote, LoraLoaderModelOnly, WanMoeKSampler, VHS_VideoCombine, ImageSharpen, VAEDecode, LoadImage, ttN int, ttN int, ttN int, CLIPTextEncode, LoadImage, UNETLoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "euler", "sampler_name": 4, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2_14B_官方强推-图生视频（强烈推荐）_1956203344467558401.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956203344467558401.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（23 个）：
- `TorchCompileModelWanVideoV2`
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `TorchCompileModelWanVideoV2`
- `VAELoader`
- `MathExpression|pysssss`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `WanMoeKSampler` ★核心
- `VHS_VideoCombine`
- `ImageSharpen`
- `VAEDecode` ★核心
- `LoadImage`
- `ttN int`
- `ttN int`
- `ttN int`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `4`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **96%**（22/23）

**有卡**：`TorchCompileModelWanVideoV2`、`CLIPLoader`、`PathchSageAttentionKJ`、`VAELoader`、`MathExpression|pysssss`、`WanImageToVideo`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`WanMoeKSampler`、`VHS_VideoCombine`、`ImageSharpen`、`VAEDecode`、`LoadImage`、`ttN int`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
