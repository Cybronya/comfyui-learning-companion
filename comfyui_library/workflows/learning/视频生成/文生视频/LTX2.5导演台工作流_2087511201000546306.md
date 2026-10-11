---
key: 视频生成/文生视频/LTX2.5导演台工作流_2087511201000546306.json
name: LTX2.5导演台工作流_2087511201000546306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5导演台工作流_2087511201000546306.json
hash: 62e9a76352ddc033
coverage: 0.891892
learned_at: 2026-10-11 20:53:38
nodes: [AudioCrop, MelBandRoFormerModelLoader, LoadImage, LoadImage, LiconMSR, LoadImage, CFGGuider, RandomNoise, LoadImage, VHS_VideoCombine, TTResolutionSelector, LTXVConcatAVLatent, LoadAudio, PreviewAudio, MelBandRoFormerSampler, YusuLTXDirectorGuide, ConditioningZeroOut, LTXVConditioning, LTXVSeparateAVLatent, YusuLTXDirectorCropGuides, BasicScheduler, CreateVideo, LTXVAudioVAEDecode, VAEDecodeTiled, YusuLTXDirector, CLIPLoader, VAELoaderKJ, VAELoaderKJ, TTResolutionSelector, SamplerCustomAdvanced, KSamplerSelect, Label (rgthree), Label (rgthree), Label (rgthree), DiffusionModelLoaderKJ, Fast Groups Bypasser (rgthree), SaveVideo]
patterns: []
missing: [Label (rgthree), Label (rgthree), Label (rgthree)]
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.5导演台工作流_2087511201000546306.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5导演台工作流_2087511201000546306.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（37 个）：
- `AudioCrop`
- `MelBandRoFormerModelLoader`
- `LoadImage`
- `LoadImage`
- `LiconMSR`
- `LoadImage`
- `CFGGuider`
- `RandomNoise`
- `LoadImage`
- `VHS_VideoCombine`
- `TTResolutionSelector`
- `LTXVConcatAVLatent`
- `LoadAudio`
- `PreviewAudio`
- `MelBandRoFormerSampler` ★核心
- `YusuLTXDirectorGuide`
- `ConditioningZeroOut`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `YusuLTXDirectorCropGuides`
- `BasicScheduler`
- `CreateVideo`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `YusuLTXDirector`
- `CLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `TTResolutionSelector`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `DiffusionModelLoaderKJ`
- `Fast Groups Bypasser (rgthree)`
- `SaveVideo`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`AudioCrop`、`MelBandRoFormerModelLoader`、`LoadImage`、`LiconMSR`、`CFGGuider`、`RandomNoise`、`VHS_VideoCombine`、`TTResolutionSelector`、`LTXVConcatAVLatent`、`LoadAudio`、`PreviewAudio`、`MelBandRoFormerSampler`、`YusuLTXDirectorGuide`、`ConditioningZeroOut`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`YusuLTXDirectorCropGuides`、`BasicScheduler`、`CreateVideo`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`YusuLTXDirector`、`CLIPLoader`、`VAELoaderKJ`、`SamplerCustomAdvanced`、`KSamplerSelect`、`DiffusionModelLoaderKJ`、`SaveVideo`

**缺卡**（3）：`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`

**用到的条目**：CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
