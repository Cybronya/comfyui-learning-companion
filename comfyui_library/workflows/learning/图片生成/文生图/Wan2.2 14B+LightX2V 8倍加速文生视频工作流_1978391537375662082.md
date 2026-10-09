---
key: 图片生成/文生图/Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1978391537375662082.json
name: Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1978391537375662082.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1978391537375662082.json
hash: 4a3b5b716bc61c70
coverage: 0.909091
learned_at: 2026-10-09 19:50:54
nodes: [CLIPTextEncode, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, PathchSageAttentionKJ, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, EmptyHunyuanLatentVideo, JWInteger, JWInteger, JWInteger, UNETLoader, Note, CLIPLoader, VAELoader, Note, VHS_VideoCombine, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "uni_pc", "seed": "disable", "steps": "fixed"}
---

# 图片生成/文生图/Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1978391537375662082.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1978391537375662082.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（22 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `EmptyHunyuanLatentVideo`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `UNETLoader` ★核心
- `Note`
- `CLIPLoader`
- `VAELoader`
- `Note`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`UNETLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`EmptyHunyuanLatentVideo`、`JWInteger`、`CLIPLoader`、`VAELoader`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
