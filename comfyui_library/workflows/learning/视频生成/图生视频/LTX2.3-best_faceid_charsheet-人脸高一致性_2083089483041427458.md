---
key: 视频生成/图生视频/LTX2.3-best_faceid_charsheet-人脸高一致性_2083089483041427458.json
name: LTX2.3-best_faceid_charsheet-人脸高一致性_2083089483041427458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-best_faceid_charsheet-人脸高一致性_2083089483041427458.json
hash: aaf4feebc3aa00f3
coverage: 0.489362
learned_at: 2026-10-16 01:17:11
nodes: [LTXVAudioVAEDecode, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, RandomNoise, GetNode, GetNode, GetNode, CFGGuider, SetNode, VAEDecode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, SetNode, SetNode, SetNode, SetNode, RandomNoise, GetNode, GetNode, SamplerCustomAdvanced, GetNode, KSamplerSelect, CFGGuider, SetNode, RMBG, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVCropGuides, LTXVLatentUpsamplerTiled, LTXVConcatAVLatent, ComfyMathExpression, VHS_VideoCombine, LTXVSeparateAVLatent, LTXIdentityOverlapConditioning, GetNode, BasicScheduler, ManualSigmas, LTXIdentityOverlapConditioning, KSamplerSelect, ComfyMathExpression, ComfyMathExpression, ImageResizeKJv2, PrimitiveStringMultiline, SetNode, UNETLoader, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, LoadImage, PreviewImage, SimpleMath+, PrimitiveBoolean, Int, Int, Int, LTXTiledSampler, LTXVSeparateAVLatent, VAEDecodeTiled, VHS_VideoCombine, DualCLIPLoader, LatentUpscaleModelLoader, SetNode, SetNode, SetNode, LoraLoaderModelOnly, VAELoaderKJ, VAELoaderKJ, Int, 孤海注释, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3-best_faceid_charsheet-人脸高一致性_2083089483041427458.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3-best_faceid_charsheet-人脸高一致性_2083089483041427458.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（94 个）：
- `LTXVAudioVAEDecode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
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
- `RandomNoise`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `SetNode`
- `RMBG`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `LTXVLatentUpsamplerTiled` ★核心
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `LTXVSeparateAVLatent`
- `LTXIdentityOverlapConditioning`
- `GetNode`
- `BasicScheduler`
- `ManualSigmas`
- `LTXIdentityOverlapConditioning`
- `KSamplerSelect` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ImageResizeKJv2`
- `PrimitiveStringMultiline`
- `SetNode`
- `UNETLoader` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `PreviewImage`
- `SimpleMath+`
- `PrimitiveBoolean`
- `Int`
- `Int`
- `Int`
- `LTXTiledSampler` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `Int`
- `孤海注释`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **49%**（46/94）

**有卡**：`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`LTXVConditioning`、`RandomNoise`、`CFGGuider`、`VAEDecode`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`KSamplerSelect`、`RMBG`、`LTXVCropGuides`、`LTXVLatentUpsamplerTiled`、`ComfyMathExpression`、`VHS_VideoCombine`、`LTXVSeparateAVLatent`、`LTXIdentityOverlapConditioning`、`BasicScheduler`、`ManualSigmas`、`ImageResizeKJv2`、`UNETLoader`、`LoadImage`、`SimpleMath+`、`PrimitiveBoolean`、`Int`、`LTXTiledSampler`、`VAEDecodeTiled`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`VAELoaderKJ`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
