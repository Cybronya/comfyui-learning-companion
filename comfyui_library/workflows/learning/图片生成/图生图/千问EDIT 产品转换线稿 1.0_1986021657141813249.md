---
key: 图片生成/图生图/千问EDIT 产品转换线稿 1.0_1986021657141813249.json
name: 千问EDIT 产品转换线稿 1.0_1986021657141813249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/千问EDIT 产品转换线稿 1.0_1986021657141813249.json
hash: 10b6865f322283b0
coverage: 0.875
learned_at: 2026-10-23 12:29:18
nodes: [NunchakuQwenImageDiTLoader, CLIPLoader, VAELoader, ConditioningZeroOut, ModelSamplingAuraFlow, CFGNorm, VAEDecode, Image Comparer (rgthree), TextEncodeQwenImageEditPlusAdvance_lrzjason, ZML_AddSolidColorBackground, LayerMask: RemBgUltra, LayerMask: RmBgUltra V2, FluxKontextImageScale, ImageRemoveBackground+, RemBGSession+, PreviewImage, SaveImage, LoadImage, easy positive, Primitive integer [Crystools], PrimitiveFloat, KSampler, LoadImage, RHHiddenNodes]
patterns: []
missing: []
parameters: {"cfg": 0, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 846998925178430, "steps": 10}
---

# 图片生成/图生图/千问EDIT 产品转换线稿 1.0_1986021657141813249.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/千问EDIT 产品转换线稿 1.0_1986021657141813249.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `NunchakuQwenImageDiTLoader`
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `ZML_AddSolidColorBackground`
- `LayerMask: RemBgUltra`
- `LayerMask: RmBgUltra V2`
- `FluxKontextImageScale`
- `ImageRemoveBackground+`
- `RemBGSession+`
- `PreviewImage`
- `SaveImage`
- `LoadImage`
- `easy positive`
- `Primitive integer [Crystools]`
- `PrimitiveFloat`
- `KSampler` ★核心
- `LoadImage`
- `RHHiddenNodes`

## 关键参数

- `seed` = `846998925178430`
- `steps` = `10`
- `cfg` = `0`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`NunchakuQwenImageDiTLoader`、`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`CFGNorm`、`VAEDecode`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`ZML_AddSolidColorBackground`、`LayerMask: RemBgUltra`、`LayerMask: RmBgUltra V2`、`FluxKontextImageScale`、`ImageRemoveBackground+`、`RemBGSession+`、`SaveImage`、`LoadImage`、`easy positive`、`Primitive integer [Crystools]`、`KSampler`、`RHHiddenNodes`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、LoadImage、CFGNorm、TextEncodeQwenImageEditPlusAdvance_lrzjason
