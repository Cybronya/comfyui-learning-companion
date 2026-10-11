---
key: 视频生成/文生视频/LTX 2.5 Director 2.0 导演台视频生成工作流_2092109248682618881.json
name: LTX 2.5 Director 2.0 导演台视频生成工作流_2092109248682618881
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.5 Director 2.0 导演台视频生成工作流_2092109248682618881.json
hash: d5f9e8d1ad8e80eb
coverage: 0.740741
learned_at: 2026-10-11 21:19:41
nodes: [LTXVCropGuides, MarkdownNote, MarkdownNote, RandomNoise, SamplerCustomAdvanced, LTXVAudioVAEDecode, LTXVSeparateAVLatent, LTXVConditioning, ConditioningZeroOut, LTXVConcatAVLatent, KSamplerSelect, Power Lora Loader (rgthree), MarkdownNote, MarkdownNote, LTXVChunkFeedForward, BasicScheduler, CFGGuider, LTXDirectorGuide, VAEDecodeTiled, MarkdownNote, DiffusionModelLoaderKJ, CLIPLoader, VAELoader, VAELoader, LTXDirector, Label (rgthree), VHS_VideoCombine]
patterns: []
missing: [Label (rgthree), Power Lora Loader (rgthree)]
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/LTX 2.5 Director 2.0 导演台视频生成工作流_2092109248682618881.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.5 Director 2.0 导演台视频生成工作流_2092109248682618881.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（27 个）：
- `LTXVCropGuides`
- `MarkdownNote`
- `MarkdownNote`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConditioning`
- `ConditioningZeroOut`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `Power Lora Loader (rgthree)`
- `MarkdownNote`
- `MarkdownNote`
- `LTXVChunkFeedForward`
- `BasicScheduler`
- `CFGGuider`
- `LTXDirectorGuide`
- `VAEDecodeTiled` ★核心
- `MarkdownNote`
- `DiffusionModelLoaderKJ`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LTXDirector`
- `Label (rgthree)`
- `VHS_VideoCombine`

## 知识

覆盖率 **74%**（20/27）

**有卡**：`LTXVCropGuides`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`LTXVConditioning`、`ConditioningZeroOut`、`LTXVConcatAVLatent`、`KSamplerSelect`、`LTXVChunkFeedForward`、`BasicScheduler`、`CFGGuider`、`LTXDirectorGuide`、`VAEDecodeTiled`、`DiffusionModelLoaderKJ`、`CLIPLoader`、`VAELoader`、`LTXDirector`、`VHS_VideoCombine`

**缺卡**（2）：`Label (rgthree)`、`Power Lora Loader (rgthree)`

**用到的条目**：VAELoader、CLIPLoader、ConditioningZeroOut、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
