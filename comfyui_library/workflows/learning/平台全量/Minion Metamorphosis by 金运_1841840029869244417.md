---
key: 平台全量/Minion Metamorphosis by 金运_1841840029869244417.json
name: Minion Metamorphosis by 金运_1841840029869244417
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Minion Metamorphosis by 金运_1841840029869244417.json
hash: 04738eaae766c083
coverage: 0.956522
learned_at: 2026-11-14 00:46:20
nodes: [SaveImage, SaveImage, VAEDecode, SamplerCustomAdvanced, LatentUpscaleBy, VAEDecode, VAEEncode, BasicScheduler, SamplerCustomAdvanced, ModelSamplingFlux, VAEEncode, BasicScheduler, KSamplerSelect, BasicGuider, FluxGuidance, RandomNoise, SDXLEmptyLatentSizePicker+, CLIPTextEncode, Note, UNETLoader, DualCLIPLoader, VAELoader, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 0, "height": 1, "width": "1024x1024 (1.0)"}
---

# 平台全量/Minion Metamorphosis by 金运_1841840029869244417.json

> 来源文件 `comfyui_library/workflows/平台全量/Minion Metamorphosis by 金运_1841840029869244417.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LatentUpscaleBy`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `ModelSamplingFlux`
- `VAEEncode` ★核心
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `FluxGuidance`
- `RandomNoise`
- `SDXLEmptyLatentSizePicker+` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LoadImage`

## 关键参数

- `width` = `1024x1024 (1.0)`
- `height` = `1`
- `batch_size` = `0`

## 知识

覆盖率 **96%**（22/23）

**有卡**：`SaveImage`、`VAEDecode`、`SamplerCustomAdvanced`、`LatentUpscaleBy`、`VAEEncode`、`BasicScheduler`、`ModelSamplingFlux`、`KSamplerSelect`、`BasicGuider`、`FluxGuidance`、`RandomNoise`、`SDXLEmptyLatentSizePicker+`、`CLIPTextEncode`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
