---
key: 视频生成/文生视频/LTX导演台2.0【Director】优化工作流已修复_2060326139540885505.json
name: LTX导演台2.0【Director】优化工作流已修复_2060326139540885505
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX导演台2.0【Director】优化工作流已修复_2060326139540885505.json
hash: 44299e19be9f890c
coverage: 0.904762
learned_at: 2026-10-11 19:49:40
nodes: [LTXDirectorCropGuides, LTXVConcatAVLatent, KSamplerSelect, BasicScheduler, LatentUpscaleModelLoader, LTXVLatentUpsampler, LTXVConditioning, ConditioningZeroOut, LTXVConcatAVLatent, KSamplerSelect, BasicScheduler, CFGGuider, LTXVSeparateAVLatent, LTXDirectorCropGuides, LTXVSeparateAVLatent, SamplerCustomAdvanced, VAELoader, VAELoader, MarkdownNote, SamplerCustomAdvanced, RandomNoise, VAEDecode, CLIPTextEncode, LTX2_NAG, LoraLoaderModelOnly, LoraLoaderModelOnly, CFGGuider, LoraLoaderModelOnly, UNETLoader, DualCLIPLoader, ModelPreviewOverrideKJ, VAELoaderKJ, LoraLoaderModelOnly, LTXDirector, VHS_VideoCombine, LoadImage, LTXVAudioVAEDecode, LTXDirectorGuide, LTXDirectorGuide, Note, Reroute, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/文生视频/LTX导演台2.0【Director】优化工作流已修复_2060326139540885505.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX导演台2.0【Director】优化工作流已修复_2060326139540885505.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（42 个）：
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
- `LTXDirector`
- `VHS_VideoCombine`
- `LoadImage`
- `LTXVAudioVAEDecode` ★核心
- `LTXDirectorGuide`
- `LTXDirectorGuide`
- `Note`
- `Reroute`
- `MarkdownNote`

## 知识

覆盖率 **90%**（38/42）

**有卡**：`LTXDirectorCropGuides`、`LTXVConcatAVLatent`、`KSamplerSelect`、`BasicScheduler`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LTXVConditioning`、`ConditioningZeroOut`、`CFGGuider`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`VAELoader`、`RandomNoise`、`VAEDecode`、`CLIPTextEncode`、`LTX2_NAG`、`LoraLoaderModelOnly`、`UNETLoader`、`DualCLIPLoader`、`ModelPreviewOverrideKJ`、`VAELoaderKJ`、`LTXDirector`、`VHS_VideoCombine`、`LoadImage`、`LTXVAudioVAEDecode`、`LTXDirectorGuide`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、CFGGuider
