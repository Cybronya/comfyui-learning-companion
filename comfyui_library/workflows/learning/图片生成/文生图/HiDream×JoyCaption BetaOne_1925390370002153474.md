---
key: HiDream×JoyCaption BetaOne_1925390370002153474.json
name: HiDream×JoyCaption BetaOne_1925390370002153474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/HiDream×JoyCaption BetaOne_1925390370002153474.json
hash: 6e7dfab0afafea76
coverage: 0.6875
learned_at: 2026-10-10 20:58:39
nodes: [VAEDecode, ModelSamplingSD3, CLIPTextEncode, KSampler, VAELoader, SaveImage, LayerUtility: PurgeVRAM V2, EmptySD3LatentImage, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: JoyCaptionBeta1, easy showAnything, QuadrupleCLIPLoader, CLIPTextEncode, UNETLoader]
patterns: []
missing: [LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: PurgeVRAM V2]
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 722883505584244, "steps": 50}
discoveries: [次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: JoyCaptionBeta1ExtraOptions` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识]
---

# HiDream×JoyCaption BetaOne_1925390370002153474.json

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

覆盖率 **69%**（11/16）

**有卡**：`VAEDecode`、`ModelSamplingSD3`、`CLIPTextEncode`、`KSampler`、`VAELoader`、`SaveImage`、`EmptySD3LatentImage`、`LoadImage`、`QuadrupleCLIPLoader`、`UNETLoader`

**缺卡**（4）：`LayerUtility: JoyCaptionBeta1`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: PurgeVRAM V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、QuadrupleCLIPLoader、SaveImage

## 学习发现

- 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: JoyCaptionBeta1ExtraOptions` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
