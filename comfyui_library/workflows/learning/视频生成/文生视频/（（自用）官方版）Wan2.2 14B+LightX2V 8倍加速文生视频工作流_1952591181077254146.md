---
key: 视频生成/文生视频/（（自用）官方版）Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1952591181077254146.json
name: （（自用）官方版）Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1952591181077254146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（（自用）官方版）Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1952591181077254146.json
hash: a330866e8f6a4a89
coverage: 0.933333
learned_at: 2026-10-10 23:14:47
nodes: [CLIPLoader, VAELoader, Note, CLIPTextEncode, CLIPTextEncode, VAEDecode, EmptyHunyuanLatentVideo, JWInteger, JWInteger, JWInteger, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, VHS_VideoCombine, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, LoadLatent, VAELoader, VAEDecode, SaveImage, LoadImage, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "uni_pc", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/（（自用）官方版）Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1952591181077254146.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（（自用）官方版）Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1952591181077254146.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（30 个）：
- `CLIPLoader`
- `VAELoader`
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
- `PathchSageAttentionKJ`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `LoadLatent`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **93%**（28/30）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`EmptyHunyuanLatentVideo`、`JWInteger`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VHS_VideoCombine`、`KSamplerAdvanced`、`LoadLatent`、`SaveImage`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
