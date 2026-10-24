---
key: 图片生成/图生图/nunchaku加速+JibmixFlux+pulid+姿势_深度切换工作流_1926094894618873857.json
name: nunchaku加速+JibmixFlux+pulid+姿势_深度切换工作流_1926094894618873857
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/nunchaku加速+JibmixFlux+pulid+姿势_深度切换工作流_1926094894618873857.json
hash: 36aa3db7339ca1bd
coverage: 0.77551
learned_at: 2026-10-23 11:41:23
nodes: [BasicScheduler, EmptySD3LatentImage, KSamplerSelect, ModelSamplingFlux, ControlNetApplyAdvanced, NunchakuPulidApply, NunchakuPulidLoader, VAELoader, DualCLIPLoader, SetUnionControlNetType, SetUnionControlNetType, JWImageResizeByLongerSide, ImageConcanate, Note, PrimitiveNode, PrimitiveNode, CLIPTextEncode, RandomNoise, FluxGuidance, BasicGuider, SamplerCustomAdvanced, LoadImage, Note, Note, Note, ImageConcanate, ImpactSwitch, JWImageResizeByLongerSide, ControlNetLoader, CLIPTextEncode, VAEDecode, LayerUtility: PurgeVRAM, SaveImage, SaveImage, CR Prompt Text, NunchakuFluxDiTLoader, CR Text Concatenate, ImpactSwitch, RH_Captioner, easy showAnything, DownloadAndLoadDepthAnythingV2Model, OpenposePreprocessor, JWInteger, LoadImage, DWPreprocessor, DepthAnything_V2, PreviewImage, PreviewImage, LoadImage]
patterns: []
missing: []
parameters: {"controlnet_strength": 0.6000000000000001}
---

# 图片生成/图生图/nunchaku加速+JibmixFlux+pulid+姿势_深度切换工作流_1926094894618873857.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/nunchaku加速+JibmixFlux+pulid+姿势_深度切换工作流_1926094894618873857.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `BasicScheduler`
- `EmptySD3LatentImage`
- `KSamplerSelect` ★核心
- `ModelSamplingFlux`
- `ControlNetApplyAdvanced` ★核心
- `NunchakuPulidApply`
- `NunchakuPulidLoader`
- `VAELoader`
- `DualCLIPLoader`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `JWImageResizeByLongerSide`
- `ImageConcanate`
- `Note`
- `PrimitiveNode`
- `PrimitiveNode`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `FluxGuidance`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `Note`
- `Note`
- `Note`
- `ImageConcanate`
- `ImpactSwitch`
- `JWImageResizeByLongerSide`
- `ControlNetLoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `SaveImage`
- `SaveImage`
- `CR Prompt Text`
- `NunchakuFluxDiTLoader`
- `CR Text Concatenate`
- `ImpactSwitch`
- `RH_Captioner`
- `easy showAnything`
- `DownloadAndLoadDepthAnythingV2Model`
- `OpenposePreprocessor`
- `JWInteger`
- `LoadImage`
- `DWPreprocessor`
- `DepthAnything_V2`
- `PreviewImage`
- `PreviewImage`
- `LoadImage`

## 关键参数

- `controlnet_strength` = `0.6000000000000001`

## 知识

覆盖率 **78%**（38/49）

**有卡**：`BasicScheduler`、`EmptySD3LatentImage`、`KSamplerSelect`、`ModelSamplingFlux`、`ControlNetApplyAdvanced`、`NunchakuPulidApply`、`NunchakuPulidLoader`、`VAELoader`、`DualCLIPLoader`、`SetUnionControlNetType`、`JWImageResizeByLongerSide`、`ImageConcanate`、`CLIPTextEncode`、`RandomNoise`、`FluxGuidance`、`BasicGuider`、`SamplerCustomAdvanced`、`LoadImage`、`ControlNetLoader`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`SaveImage`、`CR Prompt Text`、`NunchakuFluxDiTLoader`、`CR Text Concatenate`、`RH_Captioner`、`DownloadAndLoadDepthAnythingV2Model`、`OpenposePreprocessor`、`JWInteger`、`DWPreprocessor`、`DepthAnything_V2`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、OpenposePreprocessor、SetUnionControlNetType
