---
key: 视频生成/图生视频/wan2.2-Camera运镜控制_1968658740180340737.json
name: wan2.2-Camera运镜控制_1968658740180340737.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2-Camera运镜控制_1968658740180340737.json
hash: bd86d17ee53fa917
coverage: 1
learned_at: 2026-10-15 22:31:46
nodes: [CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, Int, LoadImage, CLIPTextEncode, Int, KSamplerAdvanced, UNETLoader, MathExpression|pysssss, MathExpression|pysssss, WanCameraImageToVideo, VAEDecode, VHS_VideoCombine, WanCameraEmbedding, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2-Camera运镜控制_1968658740180340737.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1968658740180340737.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（22 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `Int`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `Int`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `WanCameraImageToVideo`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `WanCameraEmbedding`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`Int`、`LoadImage`、`MathExpression|pysssss`、`WanCameraImageToVideo`、`VAEDecode`、`VHS_VideoCombine`、`WanCameraEmbedding`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
