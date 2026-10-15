---
key: 视频生成/文生视频/LTX_Director_2_Workflow_iclora_edit_video_2070699701174890498.json
name: LTX_Director_2_Workflow_iclora_edit_video_2070699701174890498
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX_Director_2_Workflow_iclora_edit_video_2070699701174890498.json
hash: 338bd079004e5402
coverage: 0.970588
learned_at: 2026-10-15 22:45:19
nodes: [LTXDirectorCropGuides, LTXVConcatAVLatent, KSamplerSelect, BasicScheduler, LatentUpscaleModelLoader, LTXVLatentUpsampler, LTXVConditioning, ConditioningZeroOut, CFGGuider, LTXVConcatAVLatent, KSamplerSelect, BasicScheduler, VAEDecode, CreateVideo, SaveVideo, RandomNoise, CFGGuider, LTXVSeparateAVLatent, LTXDirectorCropGuides, LTXVSeparateAVLatent, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVAudioVAEDecode, DualCLIPLoader, VAELoader, VAELoader, LTXDirectorGuide, LTXDirectorGuide, VAELoaderKJ, MarkdownNote, LTXDirector, ModelPreviewOverrideKJ, UNETLoader, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 视频生成/文生视频/LTX_Director_2_Workflow_iclora_edit_video_2070699701174890498.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX_Director_2_Workflow_iclora_edit_video_2070699701174890498.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（34 个）：
- `LTXDirectorCropGuides`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `LTXVConditioning`
- `ConditioningZeroOut`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `RandomNoise`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `LTXDirectorCropGuides`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `VAELoader`
- `LTXDirectorGuide`
- `LTXDirectorGuide`
- `VAELoaderKJ`
- `MarkdownNote`
- `LTXDirector`
- `ModelPreviewOverrideKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **97%**（33/34）

**有卡**：`LTXDirectorCropGuides`、`LTXVConcatAVLatent`、`KSamplerSelect`、`BasicScheduler`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LTXVConditioning`、`ConditioningZeroOut`、`CFGGuider`、`VAEDecode`、`CreateVideo`、`SaveVideo`、`RandomNoise`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`DualCLIPLoader`、`VAELoader`、`LTXDirectorGuide`、`VAELoaderKJ`、`LTXDirector`、`ModelPreviewOverrideKJ`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、ConditioningZeroOut、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
