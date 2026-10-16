---
key: 视频生成/图生视频/wan2.2动漫模型DasiwaV10-图生视频_2041336224299884545.json
name: wan2.2动漫模型DasiwaV10-图生视频_2041336224299884545.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2041336224299884545.json
hash: 28035b9a303bef2e
coverage: 0.945946
learned_at: 2026-10-15 22:36:18
nodes: [LoadImage, easy int, RIFE VFI, MathExpression|pysssss, Int, Int, LoadImage, Int, Reroute, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, KSamplerAdvanced, LoadImage, CR Text Replace, CLIPTextEncode, IntToString, VAEDecode, MathExpression|pysssss, RHHiddenNodes, ImageResizeKJv2, CR Text Concatenate, Text, Text, CR Text, VHS_VideoCombine, Int, CLIPLoader, CLIPVisionLoader, CLIPLoader, CLIPVisionEncode, CLIPVisionLoader, VAELoader, CLIPTextEncode, PreviewAny, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2动漫模型DasiwaV10-图生视频_2041336224299884545.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041336224299884545.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（37 个）：
- `LoadImage`
- `easy int`
- `RIFE VFI`
- `MathExpression|pysssss`
- `Int`
- `Int`
- `LoadImage`
- `Int`
- `Reroute`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `CR Text Replace`
- `CLIPTextEncode` ★核心
- `IntToString`
- `VAEDecode` ★核心
- `MathExpression|pysssss`
- `RHHiddenNodes`
- `ImageResizeKJv2`
- `CR Text Concatenate`
- `Text`
- `Text`
- `CR Text`
- `VHS_VideoCombine`
- `Int`
- `CLIPLoader`
- `CLIPVisionLoader`
- `CLIPLoader`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（35/37）

**有卡**：`LoadImage`、`easy int`、`RIFE VFI`、`MathExpression|pysssss`、`Int`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`KSamplerAdvanced`、`CR Text Replace`、`CLIPTextEncode`、`IntToString`、`VAEDecode`、`RHHiddenNodes`、`ImageResizeKJv2`、`CR Text Concatenate`、`Text`、`CR Text`、`VHS_VideoCombine`、`CLIPLoader`、`CLIPVisionLoader`、`CLIPVisionEncode`、`VAELoader`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`llama_cpp_parameters`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、CLIPVisionEncode、PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1
