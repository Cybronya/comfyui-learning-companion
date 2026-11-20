---
key: 平台全量/字节跳动 Bernini ai 视频编辑工作流 - 基于Want2.2架构_2064555014336634881.json
name: 字节跳动 Bernini ai 视频编辑工作流 - 基于Want2.2架构_2064555014336634881
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/字节跳动 Bernini ai 视频编辑工作流 - 基于Want2.2架构_2064555014336634881.json
hash: 8b799d0e75473d31
coverage: 0.851852
learned_at: 2026-11-14 01:59:33
nodes: [BasicScheduler, SplitSigmas, CLIPTextEncode, SamplerCustom, VAEDecode, SamplerCustom, PathchSageAttentionKJ, PathchSageAttentionKJ, SaveVideo, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, CLIPLoader, CreateVideo, Note, Note, BerniniConditioning, VAELoader, KSamplerSelect, GetVideoComponents, Note, BatchImagesNode, LoadVideo, LoadImage, CLIPTextEncode]
patterns: []
missing: []
---

# 平台全量/字节跳动 Bernini ai 视频编辑工作流 - 基于Want2.2架构_2064555014336634881.json

> 来源文件 `comfyui_library/workflows/平台全量/字节跳动 Bernini ai 视频编辑工作流 - 基于Want2.2架构_2064555014336634881.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `BasicScheduler`
- `SplitSigmas`
- `CLIPTextEncode` ★核心
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `SamplerCustom` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `SaveVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `CLIPLoader`
- `CreateVideo`
- `Note`
- `Note`
- `BerniniConditioning`
- `VAELoader`
- `KSamplerSelect` ★核心
- `GetVideoComponents`
- `Note`
- `BatchImagesNode`
- `LoadVideo`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **85%**（23/27）

**有卡**：`BasicScheduler`、`SplitSigmas`、`CLIPTextEncode`、`SamplerCustom`、`VAEDecode`、`PathchSageAttentionKJ`、`SaveVideo`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`CreateVideo`、`BerniniConditioning`、`VAELoader`、`KSamplerSelect`、`GetVideoComponents`、`BatchImagesNode`、`LoadVideo`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect
