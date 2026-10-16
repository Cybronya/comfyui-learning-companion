---
key: 视频生成/图生视频/全自动六宫格LTX2.3导演台（短剧使用）_2071479057736355841.json
name: 全自动六宫格LTX2.3导演台（短剧使用）_2071479057736355841.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2071479057736355841.json
hash: ee669cf2e7113817
coverage: 0.658537
learned_at: 2026-10-15 22:40:45
nodes: [VAELoaderKJ, VAELoaderKJ, SetNode, GetNode, LTXVConditioning, ConditioningZeroOut, SetNode, GetNode, LTXDirectorGuide, LTXVConcatAVLatent, RandomNoise, CFGGuider, KSamplerSelect, BasicScheduler, LTXVCropGuides, LTXVSeparateAVLatent, LTXVAudioVAEDecode, GetNode, GetNode, VAEDecodeTiled, easy cleanGpuUsed, GetNode, SamplerCustomAdvanced, SetNode, SetNode, SetNode, DualCLIPLoader, VHS_VideoCombine, LoraLoaderModelOnly, UNETLoader, MarkdownNote, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, TTResolutionSelector, GetNode, CS-LTXGridDirector, RH_LLMAPI_Pro_Node, LoadImage, PreviewAny]
patterns: []
missing: []
---

# 视频生成/图生视频/全自动六宫格LTX2.3导演台（短剧使用）_2071479057736355841.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2071479057736355841.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（41 个）：
- `VAELoaderKJ`
- `VAELoaderKJ`
- `SetNode`
- `GetNode`
- `LTXVConditioning`
- `ConditioningZeroOut`
- `SetNode`
- `GetNode`
- `LTXDirectorGuide`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `easy cleanGpuUsed`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `DualCLIPLoader`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `TTResolutionSelector`
- `GetNode`
- `CS-LTXGridDirector`
- `RH_LLMAPI_Pro_Node`
- `LoadImage`
- `PreviewAny`

## 知识

覆盖率 **66%**（27/41）

**有卡**：`VAELoaderKJ`、`LTXVConditioning`、`ConditioningZeroOut`、`LTXDirectorGuide`、`LTXVConcatAVLatent`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`BasicScheduler`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`easy cleanGpuUsed`、`SamplerCustomAdvanced`、`DualCLIPLoader`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`UNETLoader`、`TTResolutionSelector`、`CS-LTXGridDirector`、`RH_LLMAPI_Pro_Node`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
