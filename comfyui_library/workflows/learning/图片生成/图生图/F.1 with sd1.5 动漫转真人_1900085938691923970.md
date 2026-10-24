---
key: 图片生成/图生图/F.1 with sd1.5 动漫转真人_1900085938691923970.json
name: F.1 with sd1.5 动漫转真人_1900085938691923970
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.1 with sd1.5 动漫转真人_1900085938691923970.json
hash: a28a85e18fdb0c7a
coverage: 0.730769
learned_at: 2026-10-23 10:52:35
nodes: [KSamplerSelect, ModelSamplingFlux, FluxGuidance, BasicGuider, Note, PerturbedAttentionGuidance, KSampler, ControlNetApplyAdvanced, CLIPTextEncode, Note, CLIPTextEncode, PrimitiveNode, PrimitiveNode, Note, EmptySD3LatentImage, Reroute, BasicScheduler, Note, Note, RandomNoise, ImageScaleBy, Note, StringFunction|pysssss, easy promptReplace, Fast Groups Bypasser (rgthree), VAEEncode, Reroute, Reroute, PrimitiveNode, CheckpointLoaderSimple, ControlNetLoader, UNETLoader, DualCLIPLoader, VAELoader, Note, SamplerCustomAdvanced, VAEEncode, ImageScaleBy, VAEDecode, StringFunction|pysssss, CLIPTextEncode, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, EG_CYQ_JB, VAEDecode, easy humanSegmentation, SaveImage, SaveImage, LoadImage, SaveImage, LayerUtility: Florence2Image2Prompt, LayerMask: LoadFlorence2Model]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 8, "checkpoint": "TQing v3.4_v3.4.safetensors", "controlnet_strength": 0.3, "denoise": 0.45, "sampler_name": "euler", "scheduler": "simple", "seed": 893861564900293, "steps": 22}
---

# 图片生成/图生图/F.1 with sd1.5 动漫转真人_1900085938691923970.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.1 with sd1.5 动漫转真人_1900085938691923970.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `KSamplerSelect` ★核心
- `ModelSamplingFlux`
- `FluxGuidance`
- `BasicGuider`
- `Note`
- `PerturbedAttentionGuidance`
- `KSampler` ★核心
- `ControlNetApplyAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `Note`
- `EmptySD3LatentImage`
- `Reroute`
- `BasicScheduler`
- `Note`
- `Note`
- `RandomNoise`
- `ImageScaleBy`
- `Note`
- `StringFunction|pysssss`
- `easy promptReplace`
- `Fast Groups Bypasser (rgthree)`
- `VAEEncode` ★核心
- `Reroute`
- `Reroute`
- `PrimitiveNode`
- `CheckpointLoaderSimple` ★核心
- `ControlNetLoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `Note`
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `ImageScaleBy`
- `VAEDecode` ★核心
- `StringFunction|pysssss`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EG_CYQ_JB`
- `VAEDecode` ★核心
- `easy humanSegmentation`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `SaveImage`
- `LayerUtility: Florence2Image2Prompt`
- `LayerMask: LoadFlorence2Model`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `893861564900293`
- `steps` = `22`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.45`
- `controlnet_strength` = `0.3`
- `checkpoint` = `TQing v3.4_v3.4.safetensors`

## 知识

覆盖率 **73%**（38/52）

**有卡**：`KSamplerSelect`、`ModelSamplingFlux`、`FluxGuidance`、`BasicGuider`、`PerturbedAttentionGuidance`、`KSampler`、`ControlNetApplyAdvanced`、`CLIPTextEncode`、`EmptySD3LatentImage`、`BasicScheduler`、`RandomNoise`、`ImageScaleBy`、`StringFunction|pysssss`、`easy promptReplace`、`VAEEncode`、`CheckpointLoaderSimple`、`ControlNetLoader`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`SamplerCustomAdvanced`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`EG_CYQ_JB`、`easy humanSegmentation`、`SaveImage`、`LoadImage`、`LayerUtility: Florence2Image2Prompt`、`LayerMask: LoadFlorence2Model`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced
