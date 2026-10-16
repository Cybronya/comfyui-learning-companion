---
key: 视频生成/图生视频/wan2.2首帧生视频4steps加速工作流_2030866059493904385.json
name: wan2.2首帧生视频4steps加速工作流_2030866059493904385.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2030866059493904385.json
hash: 78e7c9305ccb9b2e
coverage: 0.966667
learned_at: 2026-10-15 22:35:28
nodes: [CreateVideo, UNETLoader, UNETLoader, ModelSamplingSD3, LoraLoaderModelOnly, ModelSamplingSD3, Note, WanImageToVideo, LayerUtility: ImageScaleByAspectRatio V2, SaveVideo, CLIPLoader, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, MathExpression|pysssss, VAELoader, LoraLoaderModelOnly, CLIPVisionLoader, LayerUtility: PurgeVRAM V2, Int, CM_IntToFloat, MathExpression|pysssss, LoadImage, CLIPTextEncode, Int, CLIPTextEncode, Int, Int, CM_IntToFloat, CLIPVisionEncode]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2首帧生视频4steps加速工作流_2030866059493904385.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2030866059493904385.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `CreateVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `Note`
- `WanImageToVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveVideo`
- `CLIPLoader`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `MathExpression|pysssss`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPVisionLoader`
- `LayerUtility: PurgeVRAM V2`
- `Int`
- `CM_IntToFloat`
- `MathExpression|pysssss`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `Int`
- `CLIPTextEncode` ★核心
- `Int`
- `Int`
- `CM_IntToFloat`
- `CLIPVisionEncode`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`CreateVideo`、`UNETLoader`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`WanImageToVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveVideo`、`CLIPLoader`、`VAEDecode`、`KSamplerAdvanced`、`MathExpression|pysssss`、`VAELoader`、`CLIPVisionLoader`、`LayerUtility: PurgeVRAM V2`、`Int`、`CM_IntToFloat`、`LoadImage`、`CLIPTextEncode`、`CLIPVisionEncode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
