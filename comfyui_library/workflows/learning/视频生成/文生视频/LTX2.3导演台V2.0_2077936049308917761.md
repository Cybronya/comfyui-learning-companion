---
key: 视频生成/文生视频/LTX2.3导演台V2.0_2077936049308917761.json
name: LTX2.3导演台V2.0_2077936049308917761
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3导演台V2.0_2077936049308917761.json
hash: 2d61c45572c04c0a
coverage: 0.837838
learned_at: 2026-10-11 20:38:35
nodes: [VHS_VideoCombine, Label (rgthree), VAELoaderKJ, VAELoader, VAELoader, VAEDecode, LTXVAudioVAEDecode, Label (rgthree), SamplerCustomAdvanced, CFGGuider, LTXVConcatAVLatent, KSamplerSelect, LTXVLatentUpsampler, LTXVSeparateAVLatent, SamplerCustomAdvanced, CFGGuider, LTXVConcatAVLatent, KSamplerSelect, LatentUpscaleModelLoader, LTXDirectorCropGuides, BasicScheduler, LTXDirectorCropGuides, LTXVSeparateAVLatent, RandomNoise, LTXDirectorGuide, ModelPreviewOverrideKJ, BasicScheduler, LTXDirectorGuide, Text Multiline, Text Multiline, LTXVConditioning, MarkdownNote, Power Lora Loader (rgthree), CLIPTextEncode, LTXDirector, DualCLIPLoader, UNETLoader]
patterns: []
missing: [Label (rgthree), Label (rgthree), Text Multiline, Text Multiline, Power Lora Loader (rgthree)]
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/LTX2.3导演台V2.0_2077936049308917761.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3导演台V2.0_2077936049308917761.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（37 个）：
- `VHS_VideoCombine`
- `Label (rgthree)`
- `VAELoaderKJ`
- `VAELoader`
- `VAELoader`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `Label (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `LatentUpscaleModelLoader`
- `LTXDirectorCropGuides`
- `BasicScheduler`
- `LTXDirectorCropGuides`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `LTXDirectorGuide`
- `ModelPreviewOverrideKJ`
- `BasicScheduler`
- `LTXDirectorGuide`
- `Text Multiline`
- `Text Multiline`
- `LTXVConditioning`
- `MarkdownNote`
- `Power Lora Loader (rgthree)`
- `CLIPTextEncode` ★核心
- `LTXDirector`
- `DualCLIPLoader`
- `UNETLoader` ★核心

## 知识

覆盖率 **84%**（31/37）

**有卡**：`VHS_VideoCombine`、`VAELoaderKJ`、`VAELoader`、`VAEDecode`、`LTXVAudioVAEDecode`、`SamplerCustomAdvanced`、`CFGGuider`、`LTXVConcatAVLatent`、`KSamplerSelect`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`LTXDirectorCropGuides`、`BasicScheduler`、`RandomNoise`、`LTXDirectorGuide`、`ModelPreviewOverrideKJ`、`LTXVConditioning`、`CLIPTextEncode`、`LTXDirector`、`DualCLIPLoader`、`UNETLoader`

**缺卡**（5）：`Label (rgthree)`、`Label (rgthree)`、`Text Multiline`、`Text Multiline`、`Power Lora Loader (rgthree)`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
