---
key: 视频生成/文生视频/全自动多宫格LTX2.3导演台+光锥多参生视频(0623修复）_2066670452965199873.json
name: 全自动多宫格LTX2.3导演台+光锥多参生视频(0623修复）_2066670452965199873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/全自动多宫格LTX2.3导演台+光锥多参生视频(0623修复）_2066670452965199873.json
hash: 42ef8a99790d513a
coverage: 0.631579
learned_at: 2026-10-15 22:48:01
nodes: [VAELoaderKJ, VAELoaderKJ, SetNode, GetNode, GetNode, GetNode, LTXVConditioning, ConditioningZeroOut, SetNode, GetNode, LTXVConcatAVLatent, RandomNoise, CFGGuider, KSamplerSelect, BasicScheduler, LTXVCropGuides, LTXVSeparateAVLatent, LTXVAudioVAEDecode, GetNode, GetNode, VAEDecodeTiled, easy cleanGpuUsed, GetNode, SamplerCustomAdvanced, SetNode, SetNode, SetNode, DualCLIPLoader, VHS_VideoCombine, UNETLoader, RH_LLMAPI_Pro_Node, MarkdownNote, PreviewAny, TTResolutionSelector, LoadImage, LoraLoaderModelOnly, CS-LTXGridDirector, CS-LTXDirectorGuide]
patterns: []
missing: []
---

# 视频生成/文生视频/全自动多宫格LTX2.3导演台+光锥多参生视频(0623修复）_2066670452965199873.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/全自动多宫格LTX2.3导演台+光锥多参生视频(0623修复）_2066670452965199873.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（38 个）：
- `VAELoaderKJ`
- `VAELoaderKJ`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `ConditioningZeroOut`
- `SetNode`
- `GetNode`
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
- `UNETLoader` ★核心
- `RH_LLMAPI_Pro_Node`
- `MarkdownNote`
- `PreviewAny`
- `TTResolutionSelector`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `CS-LTXGridDirector`
- `CS-LTXDirectorGuide`

## 知识

覆盖率 **63%**（24/38）

**有卡**：`VAELoaderKJ`、`LTXVConditioning`、`ConditioningZeroOut`、`LTXVConcatAVLatent`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`BasicScheduler`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`easy cleanGpuUsed`、`SamplerCustomAdvanced`、`DualCLIPLoader`、`VHS_VideoCombine`、`UNETLoader`、`RH_LLMAPI_Pro_Node`、`TTResolutionSelector`、`LoadImage`、`LoraLoaderModelOnly`、`CS-LTXGridDirector`、`CS-LTXDirectorGuide`

**用到的条目**：LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
