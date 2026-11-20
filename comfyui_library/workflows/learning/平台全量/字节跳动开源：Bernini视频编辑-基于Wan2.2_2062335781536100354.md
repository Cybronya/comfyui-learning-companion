---
key: 平台全量/字节跳动开源：Bernini视频编辑-基于Wan2.2_2062335781536100354.json
name: 字节跳动开源：Bernini视频编辑-基于Wan2.2_2062335781536100354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/字节跳动开源：Bernini视频编辑-基于Wan2.2_2062335781536100354.json
hash: 64070b696845463b
coverage: 0.906977
learned_at: 2026-11-14 01:59:34
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, VAEDecode, VHS_VideoCombine, KSamplerSelect, SplitSigmas, CLIPTextEncode, MathExpression|pysssss, CLIPLoader, VAELoader, VHS_VideoInfoLoaded, easy setNode, easy setNode, easy setNode, easy getNode, easy setNode, BasicScheduler, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy setNode, easy setNode, LoadImage, MarkdownNote, LoraLoaderModelOnly, Note, Fast Groups Muter (rgthree), UNETLoader, UNETLoader, LoraLoaderModelOnly, SamplerCustom, SamplerCustom, MarkdownNote, CLIPTextEncode, VHS_LoadVideo, BerniniConditioning, Int, Int, BatchImagesNode, LoadImage, LoadImage]
patterns: []
missing: []
---

# 平台全量/字节跳动开源：Bernini视频编辑-基于Wan2.2_2062335781536100354.json

> 来源文件 `comfyui_library/workflows/平台全量/字节跳动开源：Bernini视频编辑-基于Wan2.2_2062335781536100354.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（43 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `KSamplerSelect` ★核心
- `SplitSigmas`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `CLIPLoader`
- `VAELoader`
- `VHS_VideoInfoLoaded`
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
- `LoadImage`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Fast Groups Muter (rgthree)`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SamplerCustom` ★核心
- `SamplerCustom` ★核心
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `VHS_LoadVideo`
- `BerniniConditioning`
- `Int`
- `Int`
- `BatchImagesNode`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **91%**（39/43）

**有卡**：`PathchSageAttentionKJ`、`VAEDecode`、`VHS_VideoCombine`、`KSamplerSelect`、`SplitSigmas`、`CLIPTextEncode`、`MathExpression|pysssss`、`CLIPLoader`、`VAELoader`、`VHS_VideoInfoLoaded`、`easy setNode`、`easy getNode`、`BasicScheduler`、`LoadImage`、`LoraLoaderModelOnly`、`UNETLoader`、`SamplerCustom`、`VHS_LoadVideo`、`BerniniConditioning`、`Int`、`BatchImagesNode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect
