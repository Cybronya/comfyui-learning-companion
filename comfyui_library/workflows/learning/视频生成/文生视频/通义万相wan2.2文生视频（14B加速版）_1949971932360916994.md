---
key: 视频生成/文生视频/通义万相wan2.2文生视频（14B加速版）_1949971932360916994.json
name: 通义万相wan2.2文生视频（14B加速版）_1949971932360916994.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/通义万相wan2.2文生视频（14B加速版）_1949971932360916994.json
hash: 304ff8ab34b6f3bb
coverage: 0.913043
learned_at: 2026-10-15 22:43:33
nodes: [CLIPTextEncode, EmptyHunyuanLatentVideo, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, JWInteger, JWInteger, JWInteger, PathchSageAttentionKJ, TeaCache, TeaCache, KSamplerAdvanced, Note, CLIPLoader, VHS_VideoCombine, VAEDecode, KSamplerAdvanced, Note, VAELoader, UNETLoader, UNETLoader, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/通义万相wan2.2文生视频（14B加速版）_1949971932360916994.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1949971932360916994.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（23 个）：
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `PathchSageAttentionKJ`
- `TeaCache`
- `TeaCache`
- `KSamplerAdvanced` ★核心
- `Note`
- `CLIPLoader`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `Note`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`JWInteger`、`TeaCache`、`KSamplerAdvanced`、`CLIPLoader`、`VHS_VideoCombine`、`VAEDecode`、`VAELoader`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、ModelSamplingSD3
