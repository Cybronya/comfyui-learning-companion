---
key: 视频生成/图生视频/wan2.2官方版图生视频_1992405756192550914.json
name: wan2.2官方版图生视频_1992405756192550914.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1992405756192550914.json
hash: d9780a4f103c3aa1
coverage: 0.925926
learned_at: 2026-10-15 22:33:16
nodes: [wanBlockSwap, wanBlockSwap, CLIPTextEncode, CLIPVisionEncode, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, KSamplerAdvanced, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, WanImageToVideo, MathExpression|pysssss, VAELoader, CLIPVisionLoader, UNETLoader, LoraLoaderModelOnly, UNETLoader, CLIPLoader, KSamplerAdvanced, ImpactInt, easy showAnything, LoadImage, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2官方版图生视频_1992405756192550914.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1992405756192550914.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `wanBlockSwap`
- `wanBlockSwap`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `WanImageToVideo`
- `MathExpression|pysssss`
- `VAELoader`
- `CLIPVisionLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `ImpactInt`
- `easy showAnything`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **93%**（25/27）

**有卡**：`wanBlockSwap`、`CLIPTextEncode`、`CLIPVisionEncode`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanImageToVideo`、`MathExpression|pysssss`、`VAELoader`、`CLIPVisionLoader`、`UNETLoader`、`CLIPLoader`、`ImpactInt`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
