---
key: 视频生成/图生视频/图生视频+Wan2.2_Enhanced 闪电V2_2014557623625981954.json
name: 图生视频+Wan2.2_Enhanced 闪电V2_2014557623625981954.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2014557623625981954.json
hash: 1abfb6c475ae13e3
coverage: 0.96875
learned_at: 2026-10-15 22:34:35
nodes: [CLIPLoader, Int, UNETLoader, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, Int, PathchSageAttentionKJ, easy float, UNETLoader, Int, easy float, VAELoader, FindPerfectResolution, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, PainterI2V, WanVideoNAG, easy cleanGpuUsed, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, LoadImage, ModelSamplingSD3, MathExpression|pysssss, DuckHideNode, SaveImage, VHS_VideoCombine, JjkText]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/图生视频+Wan2.2_Enhanced 闪电V2_2014557623625981954.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2014557623625981954.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（32 个）：
- `CLIPLoader`
- `Int`
- `UNETLoader` ★核心
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `Int`
- `PathchSageAttentionKJ`
- `easy float`
- `UNETLoader` ★核心
- `Int`
- `easy float`
- `VAELoader`
- `FindPerfectResolution`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `PainterI2V`
- `WanVideoNAG`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `ModelSamplingSD3`
- `MathExpression|pysssss`
- `DuckHideNode`
- `SaveImage`
- `VHS_VideoCombine`
- `JjkText`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（31/32）

**有卡**：`CLIPLoader`、`Int`、`UNETLoader`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`easy float`、`VAELoader`、`FindPerfectResolution`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`PainterI2V`、`WanVideoNAG`、`easy cleanGpuUsed`、`CLIPTextEncode`、`KSamplerAdvanced`、`VAEDecode`、`LoadImage`、`MathExpression|pysssss`、`DuckHideNode`、`SaveImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
