---
key: 图片生成/图生图/一键动漫转真人（SD1.5）-模型效果很好_1912137373873045506.json
name: 一键动漫转真人（SD1.5）-模型效果很好_1912137373873045506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/一键动漫转真人（SD1.5）-模型效果很好_1912137373873045506.json
hash: cc01a1eeb7eae3ca
coverage: 0.725
learned_at: 2026-10-23 11:55:04
nodes: [VAEEncode, IterativeLatentUpscale, BboxDetectorSEGS, SetNode, GetNode, GetNode, VAEDecode, GetNode, SAMLoader, BNK_CLIPTextEncodeAdvanced, CLIPSetLastLayer, ConstrainImage|pysssss, VAELoader, LoadImage, DiffControlNetLoader, UpscaleModelLoader, UltralyticsDetectorProvider, GetNode, SetNode, VAEDecode, PreviewImage, DiffControlNetLoader, LineArtPreprocessor, SAMDetectorCombined, ImpactSegsAndMask, DWPreprocessor, ShowText|pysssss, ControlNetApplyAdvanced, PreviewImage, SetNode, VAEEncode, BNK_CLIPTextEncodeAdvanced, ControlNetApplyAdvanced, DetailerForEach, WD14Tagger|pysssss, GetNode, CheckpointLoaderSimple, PixelKSampleUpscalerProvider, SaveImage, KSampler //Inspire]
patterns: []
missing: []
parameters: {"cfg": 7, "checkpoint": "白泽MARS-Cyber_Realistic_S2.0.safetensors", "controlnet_strength": 1.0000000000000002, "denoise": 0.6000000000000001, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 536472042498467, "steps": 35}
---

# 图片生成/图生图/一键动漫转真人（SD1.5）-模型效果很好_1912137373873045506.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/一键动漫转真人（SD1.5）-模型效果很好_1912137373873045506.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `VAEEncode` ★核心
- `IterativeLatentUpscale`
- `BboxDetectorSEGS`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `SAMLoader`
- `BNK_CLIPTextEncodeAdvanced` ★核心
- `CLIPSetLastLayer`
- `ConstrainImage|pysssss`
- `VAELoader`
- `LoadImage`
- `DiffControlNetLoader`
- `UpscaleModelLoader`
- `UltralyticsDetectorProvider`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `PreviewImage`
- `DiffControlNetLoader`
- `LineArtPreprocessor`
- `SAMDetectorCombined`
- `ImpactSegsAndMask`
- `DWPreprocessor`
- `ShowText|pysssss`
- `ControlNetApplyAdvanced` ★核心
- `PreviewImage`
- `SetNode`
- `VAEEncode` ★核心
- `BNK_CLIPTextEncodeAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `DetailerForEach`
- `WD14Tagger|pysssss`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `PixelKSampleUpscalerProvider`
- `SaveImage`
- `KSampler //Inspire` ★核心

## 关键参数

- `controlnet_strength` = `1.0000000000000002`
- `checkpoint` = `白泽MARS-Cyber_Realistic_S2.0.safetensors`
- `seed` = `536472042498467`
- `steps` = `35`
- `cfg` = `7`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `0.6000000000000001`

## 知识

覆盖率 **72%**（29/40）

**有卡**：`VAEEncode`、`IterativeLatentUpscale`、`BboxDetectorSEGS`、`VAEDecode`、`SAMLoader`、`BNK_CLIPTextEncodeAdvanced`、`CLIPSetLastLayer`、`ConstrainImage|pysssss`、`VAELoader`、`LoadImage`、`DiffControlNetLoader`、`UpscaleModelLoader`、`UltralyticsDetectorProvider`、`LineArtPreprocessor`、`SAMDetectorCombined`、`ImpactSegsAndMask`、`DWPreprocessor`、`ControlNetApplyAdvanced`、`DetailerForEach`、`WD14Tagger|pysssss`、`CheckpointLoaderSimple`、`PixelKSampleUpscalerProvider`、`SaveImage`、`KSampler //Inspire`

**用到的条目**：VAEDecode、VAELoader、CheckpointLoaderSimple、LoadImage、ControlNetApplyAdvanced、DiffControlNetLoader、KSampler //Inspire、VAEEncode
