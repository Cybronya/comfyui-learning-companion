---
key: 平台全量/FLUX.1爆款复制器_1940591278377824257.json
name: FLUX.1爆款复制器_1940591278377824257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX.1爆款复制器_1940591278377824257.json
hash: db83cb9ca8cd70aa
coverage: 0.878788
learned_at: 2026-11-14 00:25:08
nodes: [CheckpointLoaderSimple, WD14Tagger|pysssss, easy promptConcat, easy promptConcat, VAELoader, DualCLIPLoaderGGUF, UnetLoaderGGUFAdvanced, UNETLoader, CLIPVisionLoader, ImageAndMaskResizeNode, StyleModelLoader, ReduxPromptStyler, Note, JoyCaptionAlpha2Online, LayerUtility: JoyCaption2ExtraOptions, CLIPTextEncodeFlux, easy setNode, easy setNode, easy setNode, easy getNode, KSampler //Inspire, easy getNode, ConditioningZeroOut, EmptyLatentImage, VAEDecode, easy getNode, PreviewImage, easy showAnything, easy showAnything, IPAdapterFluxLoaderAdvanced, ApplyIPAdapterFluxAdvanced, LoadImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "FLUX.1\\FLUX.1-S-FP16-官方混合.safetensors", "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 390475305275718, "steps": 25, "width": 1024}
---

# 平台全量/FLUX.1爆款复制器_1940591278377824257.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX.1爆款复制器_1940591278377824257.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（33 个）：
- `CheckpointLoaderSimple` ★核心
- `WD14Tagger|pysssss`
- `easy promptConcat`
- `easy promptConcat`
- `VAELoader`
- `DualCLIPLoaderGGUF`
- `UnetLoaderGGUFAdvanced` ★核心
- `UNETLoader` ★核心
- `CLIPVisionLoader`
- `ImageAndMaskResizeNode`
- `StyleModelLoader`
- `ReduxPromptStyler`
- `Note`
- `JoyCaptionAlpha2Online`
- `LayerUtility: JoyCaption2ExtraOptions`
- `CLIPTextEncodeFlux` ★核心
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `easy getNode`
- `KSampler //Inspire` ★核心
- `easy getNode`
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `easy getNode`
- `PreviewImage`
- `easy showAnything`
- `easy showAnything`
- `IPAdapterFluxLoaderAdvanced`
- `ApplyIPAdapterFluxAdvanced`
- `LoadImage`
- `SaveImage`

## 关键参数

- `checkpoint` = `FLUX.1\FLUX.1-S-FP16-官方混合.safetensors`
- `seed` = `390475305275718`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（29/33）

**有卡**：`CheckpointLoaderSimple`、`WD14Tagger|pysssss`、`easy promptConcat`、`VAELoader`、`DualCLIPLoaderGGUF`、`UnetLoaderGGUFAdvanced`、`UNETLoader`、`CLIPVisionLoader`、`ImageAndMaskResizeNode`、`StyleModelLoader`、`ReduxPromptStyler`、`JoyCaptionAlpha2Online`、`LayerUtility: JoyCaption2ExtraOptions`、`CLIPTextEncodeFlux`、`easy setNode`、`easy getNode`、`KSampler //Inspire`、`ConditioningZeroOut`、`EmptyLatentImage`、`VAEDecode`、`IPAdapterFluxLoaderAdvanced`、`ApplyIPAdapterFluxAdvanced`、`LoadImage`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage、KSampler //Inspire
