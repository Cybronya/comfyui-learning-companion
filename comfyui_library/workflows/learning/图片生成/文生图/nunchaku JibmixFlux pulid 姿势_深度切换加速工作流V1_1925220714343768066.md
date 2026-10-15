---
key: 图片生成/文生图/nunchaku JibmixFlux pulid 姿势_深度切换加速工作流V1_1925220714343768066.json
name: nunchaku JibmixFlux pulid 姿势_深度切换加速工作流V1_1925220714343768066
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/nunchaku JibmixFlux pulid 姿势_深度切换加速工作流V1_1925220714343768066.json
hash: 6197acd40ad3d5aa
coverage: 0.809524
learned_at: 2026-10-15 22:27:51
nodes: [BasicScheduler, EmptySD3LatentImage, PrimitiveNode, DualCLIPLoader, VAELoader, CLIPTextEncode, KSamplerSelect, RandomNoise, PrimitiveNode, ModelSamplingFlux, ControlNetApplyAdvanced, FluxGuidance, BasicGuider, ImageConcanate, JWImageResizeByLongerSide, ImageConcanate, JWImageResizeByLongerSide, VAEDecode, LayerUtility: PurgeVRAM, SamplerCustomAdvanced, NunchakuFluxDiTLoader, DownloadAndLoadDepthAnythingV2Model, NunchakuPulidApply, NunchakuPulidLoader, SetUnionControlNetType, SetUnionControlNetType, ImpactSwitch, SaveImage, OpenposePreprocessor, DepthAnything_V2, ImpactSwitch, JWInteger, CLIPTextEncode, CR Prompt Text, Note, Note, SaveImage, LoadImage, Note, Note, ControlNetLoader, LoadImage]
patterns: []
missing: []
parameters: {"controlnet_strength": 0.6000000000000001}
---

# 图片生成/文生图/nunchaku JibmixFlux pulid 姿势_深度切换加速工作流V1_1925220714343768066.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/nunchaku JibmixFlux pulid 姿势_深度切换加速工作流V1_1925220714343768066.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `BasicScheduler`
- `EmptySD3LatentImage`
- `PrimitiveNode`
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `PrimitiveNode`
- `ModelSamplingFlux`
- `ControlNetApplyAdvanced` ★核心
- `FluxGuidance`
- `BasicGuider`
- `ImageConcanate`
- `JWImageResizeByLongerSide`
- `ImageConcanate`
- `JWImageResizeByLongerSide`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `SamplerCustomAdvanced` ★核心
- `NunchakuFluxDiTLoader`
- `DownloadAndLoadDepthAnythingV2Model`
- `NunchakuPulidApply`
- `NunchakuPulidLoader`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `ImpactSwitch`
- `SaveImage`
- `OpenposePreprocessor`
- `DepthAnything_V2`
- `ImpactSwitch`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `Note`
- `Note`
- `SaveImage`
- `LoadImage`
- `Note`
- `Note`
- `ControlNetLoader`
- `LoadImage`

## 关键参数

- `controlnet_strength` = `0.6000000000000001`

## 知识

覆盖率 **81%**（34/42）

**有卡**：`BasicScheduler`、`EmptySD3LatentImage`、`DualCLIPLoader`、`VAELoader`、`CLIPTextEncode`、`KSamplerSelect`、`RandomNoise`、`ModelSamplingFlux`、`ControlNetApplyAdvanced`、`FluxGuidance`、`BasicGuider`、`ImageConcanate`、`JWImageResizeByLongerSide`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`SamplerCustomAdvanced`、`NunchakuFluxDiTLoader`、`DownloadAndLoadDepthAnythingV2Model`、`NunchakuPulidApply`、`NunchakuPulidLoader`、`SetUnionControlNetType`、`SaveImage`、`OpenposePreprocessor`、`DepthAnything_V2`、`JWInteger`、`CR Prompt Text`、`LoadImage`、`ControlNetLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、OpenposePreprocessor、SetUnionControlNetType
