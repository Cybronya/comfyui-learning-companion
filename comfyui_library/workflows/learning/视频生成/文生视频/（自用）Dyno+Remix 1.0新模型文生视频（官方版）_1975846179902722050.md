---
key: 视频生成/文生视频/（自用）Dyno+Remix 1.0新模型文生视频（官方版）_1975846179902722050.json
name: （自用）Dyno+Remix 1.0新模型文生视频（官方版）_1975846179902722050
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（自用）Dyno+Remix 1.0新模型文生视频（官方版）_1975846179902722050.json
hash: a3cb1d2b25eb7167
coverage: 1
learned_at: 2026-10-10 23:14:31
nodes: [CLIPTextEncode, PathchSageAttentionKJ, EmptyHunyuanLatentVideo, INTConstant, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, KSamplerAdvanced, VAELoader, CLIPLoader, INTConstant, CLIPTextEncode, TT_img_enc, SaveImage, JWInteger, JWInteger, JWInteger, UNETLoader, UNETLoader, LoadImage, SaveImage, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/（自用）Dyno+Remix 1.0新模型文生视频（官方版）_1975846179902722050.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（自用）Dyno+Remix 1.0新模型文生视频（官方版）_1975846179902722050.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（23 个）：
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `EmptyHunyuanLatentVideo`
- `INTConstant`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `CLIPLoader`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `TT_img_enc`
- `SaveImage`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `SaveImage`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`CLIPTextEncode`、`PathchSageAttentionKJ`、`EmptyHunyuanLatentVideo`、`INTConstant`、`KSamplerAdvanced`、`ModelSamplingSD3`、`VAELoader`、`CLIPLoader`、`TT_img_enc`、`SaveImage`、`JWInteger`、`UNETLoader`、`LoadImage`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
