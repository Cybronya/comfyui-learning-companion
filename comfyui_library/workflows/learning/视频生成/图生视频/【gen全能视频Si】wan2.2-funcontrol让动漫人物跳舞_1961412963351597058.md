---
key: 视频生成/图生视频/【gen全能视频Si】wan2.2-funcontrol让动漫人物跳舞_1961412963351597058.json
name: 【gen全能视频Si】wan2.2-funcontrol让动漫人物跳舞_1961412963351597058.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【gen全能视频Si】wan2.2-funcontrol让动漫人物跳舞_1961412963351597058.json
hash: 6d4be3d09db33a0a
coverage: 0.5
learned_at: 2026-10-15 22:31:28
nodes: [SetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, DWPreprocessor, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetImageRangeFromBatch, GetNode, GetNode, PreviewImage, VHS_VideoCombine, GetNode, VAEDecode, INTConstant, INTConstant, GetNode, Wan22FunControlToVideo, GetNode, SetNode, LoadImage, ImageResizeKJv2, VHS_LoadVideo, KSamplerAdvanced, KSamplerAdvanced, GetNode, CLIPTextEncode, SetNode, SetNode, VHS_VideoCombine, ImageFromBatch+, RMBG, RIFE VFI, Note, VHS_VideoCombine, GetNode, MarkdownNote, Int, SetNode, SetNode, UNETLoader, UNETLoader, ModelSamplingSD3, SetNode, MathExpression|pysssss, SetNode, Note, wanBlockSwap, wanBlockSwap, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, SetNode, LoraLoaderModelOnly, PathchSageAttentionKJ, VAELoader, CLIPLoader, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/【gen全能视频Si】wan2.2-funcontrol让动漫人物跳舞_1961412963351597058.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1961412963351597058.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `DWPreprocessor`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `VHS_VideoCombine`
- `GetNode`
- `VAEDecode` ★核心
- `INTConstant`
- `INTConstant`
- `GetNode`
- `Wan22FunControlToVideo`
- `GetNode`
- `SetNode`
- `LoadImage`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `ImageFromBatch+`
- `RMBG`
- `RIFE VFI`
- `Note`
- `VHS_VideoCombine`
- `GetNode`
- `MarkdownNote`
- `Int`
- `SetNode`
- `SetNode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `SetNode`
- `MathExpression|pysssss`
- `SetNode`
- `Note`
- `wanBlockSwap`
- `wanBlockSwap`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **50%**（34/68）

**有卡**：`ImageResizeKJv2`、`DWPreprocessor`、`GetImageRangeFromBatch`、`VHS_VideoCombine`、`VAEDecode`、`INTConstant`、`Wan22FunControlToVideo`、`LoadImage`、`VHS_LoadVideo`、`KSamplerAdvanced`、`CLIPTextEncode`、`ImageFromBatch+`、`RMBG`、`RIFE VFI`、`Int`、`UNETLoader`、`ModelSamplingSD3`、`MathExpression|pysssss`、`wanBlockSwap`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`VAELoader`、`CLIPLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
