---
key: 视频生成/文生视频/LTX导演台2.0【Director】视频延长+编辑_2069229270215516161.json
name: LTX导演台2.0【Director】视频延长+编辑_2069229270215516161
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX导演台2.0【Director】视频延长+编辑_2069229270215516161.json
hash: c6559cdc9695e7e4
coverage: 0.863636
learned_at: 2026-10-15 22:45:19
nodes: [LTXDirectorCropGuides, LTXVConcatAVLatent, KSamplerSelect, BasicScheduler, LatentUpscaleModelLoader, LTXVLatentUpsampler, LTXVConditioning, ConditioningZeroOut, LTXVConcatAVLatent, KSamplerSelect, BasicScheduler, CFGGuider, LTXVSeparateAVLatent, LTXDirectorCropGuides, LTXVSeparateAVLatent, SamplerCustomAdvanced, VAELoader, VAELoader, MarkdownNote, SamplerCustomAdvanced, RandomNoise, VAEDecode, CLIPTextEncode, LTX2_NAG, LoraLoaderModelOnly, LoraLoaderModelOnly, CFGGuider, LoraLoaderModelOnly, UNETLoader, DualCLIPLoader, ModelPreviewOverrideKJ, VAELoaderKJ, LoraLoaderModelOnly, VHS_VideoCombine, LoadImage, LTXVAudioVAEDecode, Note, Reroute, Note, Note, LTXDirectorGuide, LTXDirectorGuide, LTXDirector, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/文生视频/LTX导演台2.0【Director】视频延长+编辑_2069229270215516161.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX导演台2.0【Director】视频延长+编辑_2069229270215516161.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（44 个）：
- `LTXDirectorCropGuides`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `LTXVConditioning`
- `ConditioningZeroOut`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `LTXDirectorCropGuides`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `VAELoader`
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CFGGuider`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `ModelPreviewOverrideKJ`
- `VAELoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `LTXVAudioVAEDecode` ★核心
- `Note`
- `Reroute`
- `Note`
- `Note`
- `LTXDirectorGuide`
- `LTXDirectorGuide`
- `LTXDirector`
- `MarkdownNote`

## 知识

覆盖率 **86%**（38/44）

**有卡**：`LTXDirectorCropGuides`、`LTXVConcatAVLatent`、`KSamplerSelect`、`BasicScheduler`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LTXVConditioning`、`ConditioningZeroOut`、`CFGGuider`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`VAELoader`、`RandomNoise`、`VAEDecode`、`CLIPTextEncode`、`LTX2_NAG`、`LoraLoaderModelOnly`、`UNETLoader`、`DualCLIPLoader`、`ModelPreviewOverrideKJ`、`VAELoaderKJ`、`VHS_VideoCombine`、`LoadImage`、`LTXVAudioVAEDecode`、`LTXDirectorGuide`、`LTXDirector`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、CFGGuider
