---
key: 图片生成/图生图/FLUX Union-CN控制器+REDUX风格迁移 V1.1_1928351640892358657.json
name: FLUX Union-CN控制器+REDUX风格迁移 V1.1_1928351640892358657
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX Union-CN控制器+REDUX风格迁移 V1.1_1928351640892358657.json
hash: 0c472a0f426b5967
coverage: 0.923077
learned_at: 2026-10-23 10:53:33
nodes: [KSamplerSelect, BasicScheduler, UNETLoader, RandomNoise, DualCLIPLoader, CLIPTextEncode, VAELoader, SetUnionControlNetType, ControlNetLoader, Note, BasicGuider, SaveImage, DepthAnythingPreprocessor, FluxGuidance, StyleModelLoader, CLIPVisionLoader, ReduxAdvanced, EmptySD3LatentImage, LoadImage, VAEDecode, ColorMatch, PreviewImage, SamplerCustomAdvanced, ControlNetApplySD3, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"controlnet_strength": 0.6000000000000001}
---

# 图片生成/图生图/FLUX Union-CN控制器+REDUX风格迁移 V1.1_1928351640892358657.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX Union-CN控制器+REDUX风格迁移 V1.1_1928351640892358657.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `UNETLoader` ★核心
- `RandomNoise`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `SetUnionControlNetType`
- `ControlNetLoader`
- `Note`
- `BasicGuider`
- `SaveImage`
- `DepthAnythingPreprocessor`
- `FluxGuidance`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `ReduxAdvanced`
- `EmptySD3LatentImage`
- `LoadImage`
- `VAEDecode` ★核心
- `ColorMatch`
- `PreviewImage`
- `SamplerCustomAdvanced` ★核心
- `ControlNetApplySD3` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `controlnet_strength` = `0.6000000000000001`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`KSamplerSelect`、`BasicScheduler`、`UNETLoader`、`RandomNoise`、`DualCLIPLoader`、`CLIPTextEncode`、`VAELoader`、`SetUnionControlNetType`、`ControlNetLoader`、`BasicGuider`、`SaveImage`、`DepthAnythingPreprocessor`、`FluxGuidance`、`StyleModelLoader`、`CLIPVisionLoader`、`ReduxAdvanced`、`EmptySD3LatentImage`、`LoadImage`、`VAEDecode`、`ColorMatch`、`SamplerCustomAdvanced`、`ControlNetApplySD3`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、ControlNetLoader、SetUnionControlNetType、DepthAnythingPreprocessor
