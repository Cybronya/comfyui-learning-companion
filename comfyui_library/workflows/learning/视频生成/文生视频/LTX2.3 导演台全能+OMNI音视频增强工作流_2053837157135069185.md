---
key: 视频生成/文生视频/LTX2.3 导演台全能+OMNI音视频增强工作流_2053837157135069185.json
name: LTX2.3 导演台全能+OMNI音视频增强工作流_2053837157135069185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 导演台全能+OMNI音视频增强工作流_2053837157135069185.json
hash: e29d2571a5dcf9ab
coverage: 0.846154
learned_at: 2026-10-11 19:49:37
nodes: [PlaySound|pysssss, PathchSageAttentionKJ, PlaySound|pysssss, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVAudioVAEDecode, CLIPTextEncode, LTXDirectorGuide, LTXVConditioning, CFGGuider, KSamplerSelect, BasicScheduler, LTXVSeparateAVLatent, LTXVCropGuides, SamplerCustomAdvanced, RandomNoise, CFGGuider, LTXVConcatAVLatent, LTXVChunkFeedForward, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVEnhanceAVideoKJ, Note, Note, VAEDecodeTiled, Reroute, VHS_VideoCombine, LTXVSeparateAVLatent, LTXVCropGuides, LTXDirectorGuide, LTXVLatentUpsampler, BasicScheduler, KSamplerSelect, LoraLoaderModelOnly, UNETLoader, VAELoaderKJ, VAELoaderKJ, DualCLIPLoaderGGUF, LatentUpscaleModelLoader, VAELoaderKJ, SamplerCustomAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, Label (rgthree), LTXVConcatAVLatent, Note, LTXDirector, ModelPatchTorchSettings, VHS_VideoCombine, RandomNoise, Note, LoraLoaderModelOnly]
patterns: []
missing: [Label (rgthree), PlaySound|pysssss, PlaySound|pysssss]
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3 导演台全能+OMNI音视频增强工作流_2053837157135069185.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 导演台全能+OMNI音视频增强工作流_2053837157135069185.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（52 个）：
- `PlaySound|pysssss`
- `PathchSageAttentionKJ`
- `PlaySound|pysssss`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LTXDirectorGuide`
- `LTXVConditioning`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `LTXVChunkFeedForward`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVEnhanceAVideoKJ`
- `Note`
- `Note`
- `VAEDecodeTiled` ★核心
- `Reroute`
- `VHS_VideoCombine`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXDirectorGuide`
- `LTXVLatentUpsampler` ★核心
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoaderGGUF`
- `LatentUpscaleModelLoader`
- `VAELoaderKJ`
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Label (rgthree)`
- `LTXVConcatAVLatent`
- `Note`
- `LTXDirector`
- `ModelPatchTorchSettings`
- `VHS_VideoCombine`
- `RandomNoise`
- `Note`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **85%**（44/52）

**有卡**：`PathchSageAttentionKJ`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`CLIPTextEncode`、`LTXDirectorGuide`、`LTXVConditioning`、`CFGGuider`、`KSamplerSelect`、`BasicScheduler`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVConcatAVLatent`、`LTXVChunkFeedForward`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`LTXVEnhanceAVideoKJ`、`VHS_VideoCombine`、`LTXVLatentUpsampler`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoaderGGUF`、`LatentUpscaleModelLoader`、`LTXDirector`、`ModelPatchTorchSettings`

**缺卡**（3）：`Label (rgthree)`、`PlaySound|pysssss`、`PlaySound|pysssss`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
