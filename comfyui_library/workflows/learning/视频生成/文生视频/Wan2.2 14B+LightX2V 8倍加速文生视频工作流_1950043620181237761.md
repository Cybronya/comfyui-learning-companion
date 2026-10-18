---
key: 视频生成/文生视频/Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1950043620181237761.json
name: Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1950043620181237761.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1950043620181237761.json
hash: 0eb0393c80adb3b2
coverage: 0.909091
learned_at: 2026-10-15 22:43:34
nodes: [CLIPLoader, VAELoader, Note, Note, CLIPTextEncode, CLIPTextEncode, VAEDecode, EmptyHunyuanLatentVideo, JWInteger, JWInteger, JWInteger, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, VHS_VideoCombine, KSamplerAdvanced, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "uni_pc", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1950043620181237761.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950043620181237761.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（22 个）：
- `CLIPLoader`
- `VAELoader`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `EmptyHunyuanLatentVideo`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`EmptyHunyuanLatentVideo`、`JWInteger`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`UNETLoader`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
