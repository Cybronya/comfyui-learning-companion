---
key: 平台全量/Bernini-视频编辑-字节开源-基于wan2.2_2065440184044445698.json
name: Bernini-视频编辑-字节开源-基于wan2.2_2065440184044445698
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Bernini-视频编辑-字节开源-基于wan2.2_2065440184044445698.json
hash: e762c45b734fc48c
coverage: 0.926829
learned_at: 2026-11-14 00:20:17
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, KSamplerSelect, SplitSigmas, CLIPTextEncode, MathExpression|pysssss, CLIPLoader, VAELoader, easy setNode, easy setNode, easy setNode, easy getNode, easy setNode, BasicScheduler, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy setNode, easy setNode, UNETLoader, UNETLoader, SamplerCustom, SamplerCustom, LoraLoaderModelOnly, Int, Int, VAEDecode, VHS_VideoInfoLoaded, VHS_LoadVideo, CLIPTextEncode, LoadImage, VHS_VideoCombine, VHS_VideoCombine, BerniniConditioning, LoadImage, LoraLoaderModelOnly, MarkdownNote, MarkdownNote, MarkdownNote]
patterns: []
missing: []
---

# 平台全量/Bernini-视频编辑-字节开源-基于wan2.2_2065440184044445698.json

> 来源文件 `comfyui_library/workflows/平台全量/Bernini-视频编辑-字节开源-基于wan2.2_2065440184044445698.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（41 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `KSamplerSelect` ★核心
- `SplitSigmas`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `CLIPLoader`
- `VAELoader`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `easy getNode`
- `easy setNode`
- `BasicScheduler`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `easy setNode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `SamplerCustom` ★核心
- `SamplerCustom` ★核心
- `LoraLoaderModelOnly` ★核心
- `Int`
- `Int`
- `VAEDecode` ★核心
- `VHS_VideoInfoLoaded`
- `VHS_LoadVideo`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `BerniniConditioning`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`

## 知识

覆盖率 **93%**（38/41）

**有卡**：`PathchSageAttentionKJ`、`KSamplerSelect`、`SplitSigmas`、`CLIPTextEncode`、`MathExpression|pysssss`、`CLIPLoader`、`VAELoader`、`easy setNode`、`easy getNode`、`BasicScheduler`、`UNETLoader`、`SamplerCustom`、`LoraLoaderModelOnly`、`Int`、`VAEDecode`、`VHS_VideoInfoLoaded`、`VHS_LoadVideo`、`LoadImage`、`VHS_VideoCombine`、`BerniniConditioning`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect
