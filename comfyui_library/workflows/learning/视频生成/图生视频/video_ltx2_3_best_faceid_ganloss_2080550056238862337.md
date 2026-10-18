---
key: 视频生成/图生视频/video_ltx2_3_best_faceid_ganloss_2080550056238862337.json
name: video_ltx2_3_best_faceid_ganloss_2080550056238862337.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/video_ltx2_3_best_faceid_ganloss_2080550056238862337.json
hash: 67e44c9295cb55ac
coverage: 0.428571
learned_at: 2026-10-15 22:42:14
nodes: [MarkdownNote, MarkdownNote, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, ComfyMathExpression, SetNode, VAEDecode, GetNode, SetNode, SetNode, ComfyMathExpression, GetNode, GetNode, RandomNoise, GetNode, GetNode, GetNode, GetNode, ComfyMathExpression, SamplerCustomAdvanced, GetNode, SetNode, LTXVSeparateAVLatent, PrimitiveInt, PrimitiveInt, UNETLoader, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LatentUpscaleModelLoader, LoraLoaderModelOnly, ImageResizeKJv2, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, SetNode, SetNode, SetNode, SetNode, LTXIdentityOverlapConditioning, CFGGuider, KSamplerSelect, ManualSigmas, PreviewImage, VHS_VideoCombine, PrimitiveInt, PrimitiveInt, LoadImage, RMBG, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/video_ltx2_3_best_faceid_ganloss_2080550056238862337.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2080550056238862337.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
- `MarkdownNote`
- `MarkdownNote`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `PrimitiveInt`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXIdentityOverlapConditioning`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `PreviewImage`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `RMBG`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **43%**（27/63）

**有卡**：`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`LTXVConditioning`、`ComfyMathExpression`、`VAEDecode`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`LTXVConcatAVLatent`、`LTXIdentityOverlapConditioning`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`VHS_VideoCombine`、`LoadImage`、`RMBG`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
