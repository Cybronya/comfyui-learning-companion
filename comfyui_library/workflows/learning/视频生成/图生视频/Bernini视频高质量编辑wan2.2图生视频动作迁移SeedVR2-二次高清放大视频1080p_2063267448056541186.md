---
key: 视频生成/图生视频/Bernini视频高质量编辑wan2.2图生视频动作迁移SeedVR2-二次高清放大视频1080p_2063267448056541186.json
name: Bernini视频高质量编辑wan2.2图生视频动作迁移SeedVR2-二次高清放大视频1080p_2063267448056541186.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Bernini视频高质量编辑wan2.2图生视频动作迁移SeedVR2-二次高清放大视频1080p_2063267448056541186.json
hash: 0632fa08df61cb70
coverage: 0.925
learned_at: 2026-10-15 22:39:12
nodes: [PathchSageAttentionKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, SamplerCustom, SamplerCustom, Float, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, PreviewAny, StringReplace, StringReplace, easy showAnything, ImageFromBatch, CLIPLoader, UNETLoader, VAELoader, LoraLoaderModelOnly, UNETLoader, KSamplerSelect, SplitSigmas, VAEDecode, ImageConcanate, JWInteger, MarkdownNote, ImageScaleToTotalPixels, ImageConcanate, LoadImage, LoadVideo, RHLLMChatNode, CLIPTextEncode, CLIPTextEncode, BerniniConditioning, BasicScheduler, BatchImagesNode, CR Prompt Text, SaveVideo, SeedVR2VideoUpscaler, VHS_VideoCombine, CreateVideo, GetVideoComponents]
patterns: []
missing: []
---

# 视频生成/图生视频/Bernini视频高质量编辑wan2.2图生视频动作迁移SeedVR2-二次高清放大视频1080p_2063267448056541186.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2063267448056541186.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `SamplerCustom` ★核心
- `SamplerCustom` ★核心
- `Float`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `PreviewAny`
- `StringReplace`
- `StringReplace`
- `easy showAnything`
- `ImageFromBatch`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `SplitSigmas`
- `VAEDecode` ★核心
- `ImageConcanate`
- `JWInteger`
- `MarkdownNote`
- `ImageScaleToTotalPixels`
- `ImageConcanate`
- `LoadImage`
- `LoadVideo`
- `RHLLMChatNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `BerniniConditioning`
- `BasicScheduler`
- `BatchImagesNode`
- `CR Prompt Text`
- `SaveVideo`
- `SeedVR2VideoUpscaler`
- `VHS_VideoCombine`
- `CreateVideo`
- `GetVideoComponents`

## 知识

覆盖率 **92%**（37/40）

**有卡**：`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`SamplerCustom`、`Float`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`StringReplace`、`ImageFromBatch`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`KSamplerSelect`、`SplitSigmas`、`VAEDecode`、`ImageConcanate`、`JWInteger`、`ImageScaleToTotalPixels`、`LoadImage`、`LoadVideo`、`RHLLMChatNode`、`CLIPTextEncode`、`BerniniConditioning`、`BasicScheduler`、`BatchImagesNode`、`CR Prompt Text`、`SaveVideo`、`SeedVR2VideoUpscaler`、`VHS_VideoCombine`、`CreateVideo`、`GetVideoComponents`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect
