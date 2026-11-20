---
key: 平台全量/Bernini视频编辑-v2.0版本_2071571700168351746.json
name: Bernini视频编辑-v2.0版本_2071571700168351746
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Bernini视频编辑-v2.0版本_2071571700168351746.json
hash: 773175ed06d2a1ec
coverage: 0.897959
learned_at: 2026-11-14 00:20:42
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, VAELoader, easy setNode, easy setNode, easy setNode, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, SamplerCustom, BasicScheduler, KSamplerSelect, SplitSigmas, SamplerCustom, CLIPTextEncode, MathExpression|pysssss, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, BerniniConditioning, VAEDecode, CLIPLoader, easy setNode, easy setNode, LoadImage, LoadImage, VHS_VideoInfoLoaded, Int, Int, Note, RHLLMChatNode, PreviewAny, StringFunction|pysssss, PreviewAny, CreateVideo, VHS_LoadVideo, easy setNode, MarkdownNote, VHS_VideoCombine, LoadImage, easy seed, MarkdownNote, CLIPTextEncode, BerniniPromptEnhancer, RHLLMChatNode]
patterns: []
missing: []
---

# 平台全量/Bernini视频编辑-v2.0版本_2071571700168351746.json

> 来源文件 `comfyui_library/workflows/平台全量/Bernini视频编辑-v2.0版本_2071571700168351746.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（49 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `VAELoader`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SamplerCustom` ★核心
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `SplitSigmas`
- `SamplerCustom` ★核心
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `BerniniConditioning`
- `VAEDecode` ★核心
- `CLIPLoader`
- `easy setNode`
- `easy setNode`
- `LoadImage`
- `LoadImage`
- `VHS_VideoInfoLoaded`
- `Int`
- `Int`
- `Note`
- `RHLLMChatNode`
- `PreviewAny`
- `StringFunction|pysssss`
- `PreviewAny`
- `CreateVideo`
- `VHS_LoadVideo`
- `easy setNode`
- `MarkdownNote`
- `VHS_VideoCombine`
- `LoadImage`
- `easy seed`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `BerniniPromptEnhancer`
- `RHLLMChatNode`

## 知识

覆盖率 **90%**（44/49）

**有卡**：`PathchSageAttentionKJ`、`VAELoader`、`easy setNode`、`UNETLoader`、`LoraLoaderModelOnly`、`SamplerCustom`、`BasicScheduler`、`KSamplerSelect`、`SplitSigmas`、`CLIPTextEncode`、`MathExpression|pysssss`、`easy getNode`、`BerniniConditioning`、`VAEDecode`、`CLIPLoader`、`LoadImage`、`VHS_VideoInfoLoaded`、`Int`、`RHLLMChatNode`、`StringFunction|pysssss`、`CreateVideo`、`VHS_LoadVideo`、`VHS_VideoCombine`、`easy seed`、`BerniniPromptEnhancer`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、easy seed
