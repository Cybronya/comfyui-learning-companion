---
key: 平台全量/nunchaku-flux-krea-pulid_1990700940913250305.json
name: nunchaku-flux-krea-pulid_1990700940913250305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/nunchaku-flux-krea-pulid_1990700940913250305.json
hash: 95fd884abf83bc99
coverage: 1
learned_at: 2026-11-14 01:15:31
nodes: [FluxGuidance, KSamplerSelect, VAEDecode, BasicGuider, SamplerCustomAdvanced, ModelSamplingFlux, VAELoader, BasicScheduler, RandomNoise, NunchakuFluxPuLIDApplyV2, LayerUtility: ImageScaleByAspectRatio V2, NunchakuFluxDiTLoader, NunchakuTextEncoderLoaderV2, NunchakuPuLIDLoaderV2, SaveImage, EmptySD3LatentImage, LoadImage, CLIPTextEncode]
patterns: []
missing: []
---

# 平台全量/nunchaku-flux-krea-pulid_1990700940913250305.json

> 来源文件 `comfyui_library/workflows/平台全量/nunchaku-flux-krea-pulid_1990700940913250305.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `FluxGuidance`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `ModelSamplingFlux`
- `VAELoader`
- `BasicScheduler`
- `RandomNoise`
- `NunchakuFluxPuLIDApplyV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoaderV2`
- `NunchakuPuLIDLoaderV2`
- `SaveImage`
- `EmptySD3LatentImage`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **100%**（18/18）

**有卡**：`FluxGuidance`、`KSamplerSelect`、`VAEDecode`、`BasicGuider`、`SamplerCustomAdvanced`、`ModelSamplingFlux`、`VAELoader`、`BasicScheduler`、`RandomNoise`、`NunchakuFluxPuLIDApplyV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`NunchakuFluxDiTLoader`、`NunchakuTextEncoderLoaderV2`、`NunchakuPuLIDLoaderV2`、`SaveImage`、`EmptySD3LatentImage`、`LoadImage`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、NunchakuTextEncoderLoaderV2
