---
key: 视频生成/文生视频/LTX_Director_2_Workflow_FL_frame1_2072131735323758594.json
name: LTX_Director_2_Workflow_FL_frame1_2072131735323758594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX_Director_2_Workflow_FL_frame1_2072131735323758594.json
hash: 035662f41f3d64a8
coverage: 0.969697
learned_at: 2026-10-15 22:45:19
nodes: [LTXDirectorCropGuides, LTXVConcatAVLatent, KSamplerSelect, BasicScheduler, LatentUpscaleModelLoader, LTXVLatentUpsampler, ConditioningZeroOut, VAEDecode, RandomNoise, CFGGuider, LTXVSeparateAVLatent, LTXDirectorCropGuides, LTXVSeparateAVLatent, SamplerCustomAdvanced, SamplerCustomAdvanced, MarkdownNote, LTXDirector, SaveVideo, LTXVAudioVAEDecode, CreateVideo, UNETLoader, DualCLIPLoader, VAELoader, VAELoader, VAELoaderKJ, ModelPreviewOverrideKJ, LTXVConditioning, LTXDirectorGuide, LTXDirectorGuide, CFGGuider, LTXVConcatAVLatent, KSamplerSelect, BasicScheduler]
patterns: []
missing: []
---

# 视频生成/文生视频/LTX_Director_2_Workflow_FL_frame1_2072131735323758594.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX_Director_2_Workflow_FL_frame1_2072131735323758594.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（33 个）：
- `LTXDirectorCropGuides`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `RandomNoise`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `LTXDirectorCropGuides`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `MarkdownNote`
- `LTXDirector`
- `SaveVideo`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `VAELoader`
- `VAELoaderKJ`
- `ModelPreviewOverrideKJ`
- `LTXVConditioning`
- `LTXDirectorGuide`
- `LTXDirectorGuide`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `BasicScheduler`

## 知识

覆盖率 **97%**（32/33）

**有卡**：`LTXDirectorCropGuides`、`LTXVConcatAVLatent`、`KSamplerSelect`、`BasicScheduler`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`ConditioningZeroOut`、`VAEDecode`、`RandomNoise`、`CFGGuider`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXDirector`、`SaveVideo`、`LTXVAudioVAEDecode`、`CreateVideo`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`ModelPreviewOverrideKJ`、`LTXVConditioning`、`LTXDirectorGuide`

**用到的条目**：VAEDecode、VAELoader、ConditioningZeroOut、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
