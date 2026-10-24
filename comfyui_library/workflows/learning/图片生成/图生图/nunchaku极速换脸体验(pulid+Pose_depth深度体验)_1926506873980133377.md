---
key: 图片生成/图生图/nunchaku极速换脸体验(pulid+Pose_depth深度体验)_1926506873980133377.json
name: nunchaku极速换脸体验(pulid+Pose_depth深度体验)_1926506873980133377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/nunchaku极速换脸体验(pulid+Pose_depth深度体验)_1926506873980133377.json
hash: 7180ccce50e60c38
coverage: 0.883721
learned_at: 2026-10-23 11:41:26
nodes: [BasicScheduler, VAELoader, KSamplerSelect, RandomNoise, ModelSamplingFlux, SamplerCustomAdvanced, ImpactSwitch, JWImageResizeByLongerSide, ImageConcanate, SetUnionControlNetType, SetUnionControlNetType, NunchakuPulidApply, Reroute, CropFace, PreviewImage, NunchakuPulidLoader, ControlNetLoader, ImageConcanate, JWImageResizeByLongerSide, RH_Captioner, Text Multiline, LoadImage, DualCLIPLoader, CLIPTextEncode, BasicGuider, SaveImage, SaveImage, Text Concatenate, CLIPTextEncode, FluxGuidance, NunchakuFluxDiTLoader, CR SDXL Aspect Ratio, Note, ControlNetApplyAdvanced, VAEDecode, LayerUtility: PurgeVRAM, AIO_Preprocessor, easy anythingIndexSwitch, PreviewImage, AIO_Preprocessor, LoadImage, ImageBlend, JWInteger]
patterns: []
missing: []
parameters: {"controlnet_strength": 0.6000000000000001}
---

# 图片生成/图生图/nunchaku极速换脸体验(pulid+Pose_depth深度体验)_1926506873980133377.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/nunchaku极速换脸体验(pulid+Pose_depth深度体验)_1926506873980133377.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `BasicScheduler`
- `VAELoader`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `ModelSamplingFlux`
- `SamplerCustomAdvanced` ★核心
- `ImpactSwitch`
- `JWImageResizeByLongerSide`
- `ImageConcanate`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `NunchakuPulidApply`
- `Reroute`
- `CropFace`
- `PreviewImage`
- `NunchakuPulidLoader`
- `ControlNetLoader`
- `ImageConcanate`
- `JWImageResizeByLongerSide`
- `RH_Captioner`
- `Text Multiline`
- `LoadImage`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `BasicGuider`
- `SaveImage`
- `SaveImage`
- `Text Concatenate`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `NunchakuFluxDiTLoader`
- `CR SDXL Aspect Ratio`
- `Note`
- `ControlNetApplyAdvanced` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `AIO_Preprocessor`
- `easy anythingIndexSwitch`
- `PreviewImage`
- `AIO_Preprocessor`
- `LoadImage`
- `ImageBlend`
- `JWInteger`

## 关键参数

- `controlnet_strength` = `0.6000000000000001`

## 知识

覆盖率 **88%**（38/43）

**有卡**：`BasicScheduler`、`VAELoader`、`KSamplerSelect`、`RandomNoise`、`ModelSamplingFlux`、`SamplerCustomAdvanced`、`JWImageResizeByLongerSide`、`ImageConcanate`、`SetUnionControlNetType`、`NunchakuPulidApply`、`CropFace`、`NunchakuPulidLoader`、`ControlNetLoader`、`RH_Captioner`、`Text Multiline`、`LoadImage`、`DualCLIPLoader`、`CLIPTextEncode`、`BasicGuider`、`SaveImage`、`Text Concatenate`、`FluxGuidance`、`NunchakuFluxDiTLoader`、`CR SDXL Aspect Ratio`、`ControlNetApplyAdvanced`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`AIO_Preprocessor`、`easy anythingIndexSwitch`、`ImageBlend`、`JWInteger`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、SetUnionControlNetType、FluxGuidance
