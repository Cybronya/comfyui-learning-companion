---
key: 平台全量/wan2.2人物替换_1957481455775576065.json
name: wan2.2人物替换_1957481455775576065
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2人物替换_1957481455775576065.json
hash: bff8fa9a59c0f6b4
coverage: 0.888889
learned_at: 2026-11-14 01:19:39
nodes: [CLIPTextEncode, CLIPLoader, VAELoader, DeepTranslatorTextNode, LayerMask: LoadSegmentAnythingModels, MathExpression|pysssss, PrimitiveInt, RHHiddenNodes, PrimitiveNode, KSamplerAdvanced, LayerMask: SegmentAnythingUltra V3, LayerUtility: ImageScaleByAspectRatio V2, KSamplerAdvanced, VHS_VideoCombine, VAEDecode, TrimVideoLatent, JWInteger, LoadImage, CLIPTextEncode, MathExpression|pysssss, Int, PrimitiveInt, Int, CM_IntToFloat, VHS_VideoCombine, RH_Captioner, JjkText, VHS_LoadVideo, WanVaceToVideo, InvertMask, MaskToImage, ImageCompositeMasked, Blend, DWPreprocessor, GrowMask, ImageFromBatch+]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "randomize"}
---

# 平台全量/wan2.2人物替换_1957481455775576065.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2人物替换_1957481455775576065.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（36 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `DeepTranslatorTextNode`
- `LayerMask: LoadSegmentAnythingModels`
- `MathExpression|pysssss`
- `PrimitiveInt`
- `RHHiddenNodes`
- `PrimitiveNode`
- `KSamplerAdvanced` ★核心
- `LayerMask: SegmentAnythingUltra V3`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `JWInteger`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `Int`
- `PrimitiveInt`
- `Int`
- `CM_IntToFloat`
- `VHS_VideoCombine`
- `RH_Captioner`
- `JjkText`
- `VHS_LoadVideo`
- `WanVaceToVideo`
- `InvertMask`
- `MaskToImage`
- `ImageCompositeMasked`
- `Blend`
- `DWPreprocessor`
- `GrowMask`
- `ImageFromBatch+`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`DeepTranslatorTextNode`、`LayerMask: LoadSegmentAnythingModels`、`MathExpression|pysssss`、`RHHiddenNodes`、`KSamplerAdvanced`、`LayerMask: SegmentAnythingUltra V3`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`VAEDecode`、`TrimVideoLatent`、`JWInteger`、`LoadImage`、`Int`、`CM_IntToFloat`、`RH_Captioner`、`VHS_LoadVideo`、`WanVaceToVideo`、`InvertMask`、`MaskToImage`、`ImageCompositeMasked`、`Blend`、`DWPreprocessor`、`GrowMask`、`ImageFromBatch+`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、KSamplerAdvanced、TrimVideoLatent、Blend
