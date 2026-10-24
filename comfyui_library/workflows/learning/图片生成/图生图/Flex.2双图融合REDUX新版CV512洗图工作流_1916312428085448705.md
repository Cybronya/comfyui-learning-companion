---
key: 图片生成/图生图/Flex.2双图融合REDUX新版CV512洗图工作流_1916312428085448705.json
name: Flex.2双图融合REDUX新版CV512洗图工作流_1916312428085448705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flex.2双图融合REDUX新版CV512洗图工作流_1916312428085448705.json
hash: ce3fdb8c39703e05
coverage: 0.878049
learned_at: 2026-10-23 10:56:02
nodes: [KSamplerSelect, VAEDecode, DF_Get_image_size, AdvancedVisionLoader, PrimitiveNode, AddLabel, ImageConcatMulti, ImageConcatMulti, PrimitiveNode, Note Plus (mtb), StyleModelLoader, CLIPVisionEncode, CLIPVisionEncode, StyleModelApply, LayerUtility: PurgeVRAM V2, JWImageResizeByLongerSide, DualCLIPLoader, StyleModelApply, CLIPTextEncode, FluxGuidance, ConditioningZeroOut, KSampler, VAELoader, UNETLoader, AddLabel, PrimitiveNode, Note, ApplyFBCacheOnModel, EmptySD3LatentImage, ModelSamplingFlux, JWImageResizeByLongerSide, JWImageResizeByLongerSide, SaveImage, StyleModelAdvancedApply, LoadImage, Flex2Conditioner, LoadImage, StyleModelAdvancedApply, ImpactSwitch, AddLabel, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "deis", "scheduler": "beta", "seed": 726210541184116, "steps": 25}
---

# 图片生成/图生图/Flex.2双图融合REDUX新版CV512洗图工作流_1916312428085448705.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flex.2双图融合REDUX新版CV512洗图工作流_1916312428085448705.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `DF_Get_image_size`
- `AdvancedVisionLoader`
- `PrimitiveNode`
- `AddLabel`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `PrimitiveNode`
- `Note Plus (mtb)`
- `StyleModelLoader`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `StyleModelApply`
- `LayerUtility: PurgeVRAM V2`
- `JWImageResizeByLongerSide`
- `DualCLIPLoader`
- `StyleModelApply`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `AddLabel`
- `PrimitiveNode`
- `Note`
- `ApplyFBCacheOnModel`
- `EmptySD3LatentImage`
- `ModelSamplingFlux`
- `JWImageResizeByLongerSide`
- `JWImageResizeByLongerSide`
- `SaveImage`
- `StyleModelAdvancedApply`
- `LoadImage`
- `Flex2Conditioner`
- `LoadImage`
- `StyleModelAdvancedApply`
- `ImpactSwitch`
- `AddLabel`
- `SaveImage`

## 关键参数

- `seed` = `726210541184116`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **88%**（36/41）

**有卡**：`KSamplerSelect`、`VAEDecode`、`DF_Get_image_size`、`AdvancedVisionLoader`、`AddLabel`、`ImageConcatMulti`、`Note Plus (mtb)`、`StyleModelLoader`、`CLIPVisionEncode`、`StyleModelApply`、`LayerUtility: PurgeVRAM V2`、`JWImageResizeByLongerSide`、`DualCLIPLoader`、`CLIPTextEncode`、`FluxGuidance`、`ConditioningZeroOut`、`KSampler`、`VAELoader`、`UNETLoader`、`ApplyFBCacheOnModel`、`EmptySD3LatentImage`、`ModelSamplingFlux`、`SaveImage`、`StyleModelAdvancedApply`、`LoadImage`、`Flex2Conditioner`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
