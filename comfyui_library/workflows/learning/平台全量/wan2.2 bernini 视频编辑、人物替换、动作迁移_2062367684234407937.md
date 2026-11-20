---
key: 平台全量/wan2.2 bernini 视频编辑、人物替换、动作迁移_2062367684234407937.json
name: wan2.2 bernini 视频编辑、人物替换、动作迁移_2062367684234407937
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2 bernini 视频编辑、人物替换、动作迁移_2062367684234407937.json
hash: d430af07aead64bd
coverage: 0.918919
learned_at: 2026-11-14 01:19:20
nodes: [CLIPTextEncode, PathchSageAttentionKJ, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, BasicScheduler, CLIPLoader, CLIPTextEncode, INTConstant, INTConstant, KSamplerSelect, SplitSigmas, VAELoader, SaveVideo, BatchImagesNode, ImageFromBatch, VHS_VideoCombine, CreateVideo, Int, SamplerCustom, VAEDecode, SamplerCustom, GetVideoComponents, SimpleMath+, LoadImage, CR Text, MarkdownNote, MarkdownNote, ImageConcanate, ImageConcanate, BerniniConditioning, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadVideo, UNETLoader]
patterns: []
missing: []
---

# 平台全量/wan2.2 bernini 视频编辑、人物替换、动作迁移_2062367684234407937.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2 bernini 视频编辑、人物替换、动作迁移_2062367684234407937.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `INTConstant`
- `KSamplerSelect` ★核心
- `SplitSigmas`
- `VAELoader`
- `SaveVideo`
- `BatchImagesNode`
- `ImageFromBatch`
- `VHS_VideoCombine`
- `CreateVideo`
- `Int`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `SamplerCustom` ★核心
- `GetVideoComponents`
- `SimpleMath+`
- `LoadImage`
- `CR Text`
- `MarkdownNote`
- `MarkdownNote`
- `ImageConcanate`
- `ImageConcanate`
- `BerniniConditioning`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadVideo`
- `UNETLoader` ★核心

## 知识

覆盖率 **92%**（34/37）

**有卡**：`CLIPTextEncode`、`PathchSageAttentionKJ`、`UNETLoader`、`LoraLoaderModelOnly`、`BasicScheduler`、`CLIPLoader`、`INTConstant`、`KSamplerSelect`、`SplitSigmas`、`VAELoader`、`SaveVideo`、`BatchImagesNode`、`ImageFromBatch`、`VHS_VideoCombine`、`CreateVideo`、`Int`、`SamplerCustom`、`VAEDecode`、`GetVideoComponents`、`SimpleMath+`、`LoadImage`、`CR Text`、`ImageConcanate`、`BerniniConditioning`、`LoadVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect
