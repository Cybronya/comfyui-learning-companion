---
key: 视频生成/图生视频/魔改_LTX2.3_导演台_全自动六宫格_双采版_2064568765139996673.json
name: 魔改_LTX2.3_导演台_全自动六宫格_双采版_2064568765139996673.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/魔改_LTX2.3_导演台_全自动六宫格_双采版_2064568765139996673.json
hash: 169b10e25ff327a0
coverage: 0.923077
learned_at: 2026-10-15 22:39:26
nodes: [BasicScheduler, KSamplerSelect, LTXVLatentUpsampler, LTXVConcatAVLatent, KSamplerSelect, BasicScheduler, CFGGuider, LTXVConcatAVLatent, CFGGuider, LTXVCropGuides, LTXVCropGuides, LTXVAudioVAEDecode, LTXVConditioning, ConditioningZeroOut, LTXVSeparateAVLatent, LTXVSeparateAVLatent, RandomNoise, VAELoaderKJ, VAELoaderKJ, Label (rgthree), VAEDecode, CreateVideo, SamplerCustomAdvanced, SamplerCustomAdvanced, VAELoaderKJ, LatentUpscaleModelLoader, LTX2SamplingPreviewOverride, Label (rgthree), ComfyMathExpression, INTConstant, INTConstant, GetImageRangeFromBatch, Label (rgthree), MarkdownNote, MarkdownNote, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveFloat, LoadImage, LoraLoaderModelOnly, DualCLIPLoader, SaveVideo, LTXDirectorGuide, LTXDirectorGuide, LTXDirectorGuide, LTXDirectorGuide, CS-LTXGridDirector, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 视频生成/图生视频/魔改_LTX2.3_导演台_全自动六宫格_双采版_2064568765139996673.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064568765139996673.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `LTXVCropGuides`
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `ConditioningZeroOut`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `Label (rgthree)`
- `VAEDecode` ★核心
- `CreateVideo`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `LTX2SamplingPreviewOverride`
- `Label (rgthree)`
- `ComfyMathExpression`
- `INTConstant`
- `INTConstant`
- `GetImageRangeFromBatch`
- `Label (rgthree)`
- `MarkdownNote`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `PrimitiveFloat`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `SaveVideo`
- `LTXDirectorGuide`
- `LTXDirectorGuide`
- `LTXDirectorGuide`
- `LTXDirectorGuide`
- `CS-LTXGridDirector`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **92%**（48/52）

**有卡**：`BasicScheduler`、`KSamplerSelect`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`CFGGuider`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`ConditioningZeroOut`、`LTXVSeparateAVLatent`、`RandomNoise`、`VAELoaderKJ`、`Label (rgthree)`、`VAEDecode`、`CreateVideo`、`SamplerCustomAdvanced`、`LatentUpscaleModelLoader`、`LTX2SamplingPreviewOverride`、`ComfyMathExpression`、`INTConstant`、`GetImageRangeFromBatch`、`LoraLoaderModelOnly`、`UNETLoader`、`LoadImage`、`DualCLIPLoader`、`SaveVideo`、`LTXDirectorGuide`、`CS-LTXGridDirector`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
