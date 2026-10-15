---
key: 图片生成/文生图/HiDream×JoyCaption BetaOne_1925390370002153474.json
name: HiDream×JoyCaption BetaOne_1925390370002153474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/HiDream×JoyCaption BetaOne_1925390370002153474.json
hash: 6e7dfab0afafea76
coverage: 0.9375
learned_at: 2026-10-15 22:26:32
nodes: [VAEDecode, ModelSamplingSD3, CLIPTextEncode, KSampler, VAELoader, SaveImage, LayerUtility: PurgeVRAM V2, EmptySD3LatentImage, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: JoyCaptionBeta1, easy showAnything, QuadrupleCLIPLoader, CLIPTextEncode, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 722883505584244, "steps": 50}
---

# 图片生成/文生图/HiDream×JoyCaption BetaOne_1925390370002153474.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/HiDream×JoyCaption BetaOne_1925390370002153474.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `SaveImage`
- `LayerUtility: PurgeVRAM V2`
- `EmptySD3LatentImage`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LayerUtility: JoyCaptionBeta1`
- `easy showAnything`
- `QuadrupleCLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `722883505584244`
- `steps` = `50`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`VAEDecode`、`ModelSamplingSD3`、`CLIPTextEncode`、`KSampler`、`VAELoader`、`SaveImage`、`LayerUtility: PurgeVRAM V2`、`EmptySD3LatentImage`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LoadImage`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`LayerUtility: JoyCaptionBeta1`、`QuadrupleCLIPLoader`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、QuadrupleCLIPLoader、SaveImage
