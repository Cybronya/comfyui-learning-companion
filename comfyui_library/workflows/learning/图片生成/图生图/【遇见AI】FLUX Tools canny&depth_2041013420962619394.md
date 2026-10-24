---
key: 图片生成/图生图/【遇见AI】FLUX Tools canny&depth_2041013420962619394.json
name: 【遇见AI】FLUX Tools canny&depth_2041013420962619394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】FLUX Tools canny&depth_2041013420962619394.json
hash: edf6c18b23985668
coverage: 0.857143
learned_at: 2026-10-23 11:51:52
nodes: [PreviewImage, BasicGuider, VAEDecode, KSamplerSelect, BasicScheduler, ModelSamplingFlux, CLIPTextEncodeFlux, InstructPixToPixConditioning, Note, ConditioningZeroOut, SamplerCustomAdvanced, RandomNoise, AIO_Preprocessor, SaveImage, Note, LoadImage, LoadImage, UNETLoader, DualCLIPLoader, VAELoader, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/【遇见AI】FLUX Tools canny&depth_2041013420962619394.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】FLUX Tools canny&depth_2041013420962619394.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（21 个）：
- `PreviewImage`
- `BasicGuider`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ModelSamplingFlux`
- `CLIPTextEncodeFlux` ★核心
- `InstructPixToPixConditioning`
- `Note`
- `ConditioningZeroOut`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `AIO_Preprocessor`
- `SaveImage`
- `Note`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LoadImage`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`BasicGuider`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`ModelSamplingFlux`、`CLIPTextEncodeFlux`、`InstructPixToPixConditioning`、`ConditioningZeroOut`、`SamplerCustomAdvanced`、`RandomNoise`、`AIO_Preprocessor`、`SaveImage`、`LoadImage`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、ConditioningZeroOut、LoadImage、KSamplerSelect、SamplerCustomAdvanced、CLIPTextEncodeFlux
