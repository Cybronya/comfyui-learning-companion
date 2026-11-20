---
key: 平台全量/wan2.2视频外扩_1957487678470156290.json
name: wan2.2视频外扩_1957487678470156290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2视频外扩_1957487678470156290.json
hash: d78cdc85deccee25
coverage: 0.896552
learned_at: 2026-11-14 01:19:50
nodes: [CLIPLoader, VAELoader, RHHiddenNodes, VAEDecode, ImageFromBatch+, JWInteger, CLIPTextEncode, MathExpression|pysssss, Int, Int, CM_IntToFloat, CLIPTextEncode, TrimVideoLatent, PrimitiveNode, Int, Int, Int, Int, Pick From Batch (mtb), LayerUtility: ImageScaleByAspectRatio V2, VHS_LoadVideo, VHS_VideoCombine, RH_Captioner, KSamplerAdvanced, KSamplerAdvanced, RHHiddenNodes, PrimitiveInt, MathExpression|pysssss, PrimitiveInt]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "randomize"}
---

# 平台全量/wan2.2视频外扩_1957487678470156290.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2视频外扩_1957487678470156290.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（29 个）：
- `CLIPLoader`
- `VAELoader`
- `RHHiddenNodes`
- `VAEDecode` ★核心
- `ImageFromBatch+`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `Int`
- `Int`
- `CM_IntToFloat`
- `CLIPTextEncode` ★核心
- `TrimVideoLatent`
- `PrimitiveNode`
- `Int`
- `Int`
- `Int`
- `Int`
- `Pick From Batch (mtb)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `RH_Captioner`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `RHHiddenNodes`
- `PrimitiveInt`
- `MathExpression|pysssss`
- `PrimitiveInt`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`CLIPLoader`、`VAELoader`、`RHHiddenNodes`、`VAEDecode`、`ImageFromBatch+`、`JWInteger`、`CLIPTextEncode`、`MathExpression|pysssss`、`Int`、`CM_IntToFloat`、`TrimVideoLatent`、`Pick From Batch (mtb)`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_LoadVideo`、`VHS_VideoCombine`、`RH_Captioner`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、KSamplerAdvanced、TrimVideoLatent、CM_IntToFloat、ImageFromBatch+
