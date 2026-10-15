---
key: 视频生成/文生视频/Wan2.2 HoloCine-无限时长-电影多镜头文生视频-自动提示词_1983679735324712962.json
name: Wan2.2 HoloCine-无限时长-电影多镜头文生视频-自动提示词_1983679735324712962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 HoloCine-无限时长-电影多镜头文生视频-自动提示词_1983679735324712962.json
hash: 249ea46df9ef7228
coverage: 0.860465
learned_at: 2026-10-15 22:47:09
nodes: [INTConstant, INTConstant, VHS_VideoCombine, MarkdownNote, MarkdownNote, easy ifElse, CR Text Replace, TextBox, CLIPLoader, ImageFromBatch+, ImageSharpen, easy cleanGpuUsed, VAELoader, RH_Prompter, PathchSageAttentionKJ, TorchCompileModel, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, PathchSageAttentionKJ, TorchCompileModel, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, JjkText, CLIPTextEncode, SimpleMath+, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, VAEDecode, KSamplerAdvanced, MarkdownNote, ShowText, PrimitiveBoolean, Int, JjkText, Int, Int]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 4, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2 HoloCine-无限时长-电影多镜头文生视频-自动提示词_1983679735324712962.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 HoloCine-无限时长-电影多镜头文生视频-自动提示词_1983679735324712962.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（43 个）：
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `MarkdownNote`
- `MarkdownNote`
- `easy ifElse`
- `CR Text Replace`
- `TextBox`
- `CLIPLoader`
- `ImageFromBatch+`
- `ImageSharpen`
- `easy cleanGpuUsed`
- `VAELoader`
- `RH_Prompter`
- `PathchSageAttentionKJ`
- `TorchCompileModel`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `TorchCompileModel`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `JjkText`
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `MarkdownNote`
- `ShowText`
- `PrimitiveBoolean`
- `Int`
- `JjkText`
- `Int`
- `Int`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `4`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **86%**（37/43）

**有卡**：`INTConstant`、`VHS_VideoCombine`、`CR Text Replace`、`TextBox`、`CLIPLoader`、`ImageFromBatch+`、`ImageSharpen`、`easy cleanGpuUsed`、`VAELoader`、`RH_Prompter`、`PathchSageAttentionKJ`、`TorchCompileModel`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPTextEncode`、`SimpleMath+`、`EmptyHunyuanLatentVideo`、`KSamplerAdvanced`、`VAEDecode`、`ShowText`、`PrimitiveBoolean`、`Int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
