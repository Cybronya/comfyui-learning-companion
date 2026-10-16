---
key: 视频生成/图生视频/LTX2.3-best_faceid_ganloss-人脸高一致性_2083196415471345666.json
name: LTX2.3-best_faceid_ganloss-人脸高一致性_2083196415471345666
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-best_faceid_ganloss-人脸高一致性_2083196415471345666.json
hash: 32d6c30b88709c01
coverage: 0.489362
learned_at: 2026-10-16 19:17:11
nodes: [LTXVAudioVAEDecode, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, RandomNoise, GetNode, GetNode, GetNode, CFGGuider, SetNode, VAEDecode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, SetNode, SetNode, SetNode, SetNode, RandomNoise, GetNode, GetNode, SamplerCustomAdvanced, GetNode, KSamplerSelect, CFGGuider, SetNode, RMBG, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVCropGuides, LTXVLatentUpsamplerTiled, LTXVConcatAVLatent, ComfyMathExpression, VHS_VideoCombine, LTXVSeparateAVLatent, GetNode, BasicScheduler, ManualSigmas, LTXIdentityOverlapConditioning, KSamplerSelect, ComfyMathExpression, ComfyMathExpression, ImageResizeKJv2, PrimitiveStringMultiline, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, SimpleMath+, PrimitiveBoolean, Int, Int, Int, LTXTiledSampler, LTXVSeparateAVLatent, VAEDecodeTiled, VHS_VideoCombine, DualCLIPLoader, LatentUpscaleModelLoader, SetNode, SetNode, SetNode, VAELoaderKJ, VAELoaderKJ, Int, 孤海注释, MarkdownNote, PreviewImage, UNETLoader, LoraLoaderModelOnly, SetNode, LTXIdentityOverlapConditioning, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3-best_faceid_ganloss-人脸高一致性_2083196415471345666.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3-best_faceid_ganloss-人脸高一致性_2083196415471345666.json`

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
- `GetNode`
- `BasicScheduler`
- `ManualSigmas`
- `LTXIdentityOverlapConditioning`
- `KSamplerSelect` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ImageResizeKJv2`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
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
- `VAELoaderKJ`
- `VAELoaderKJ`
- `Int`
- `孤海注释`
- `MarkdownNote`
- `PreviewImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LTXIdentityOverlapConditioning`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **49%**（46/94）

**有卡**：`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`LTXVConditioning`、`RandomNoise`、`CFGGuider`、`VAEDecode`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`KSamplerSelect`、`RMBG`、`LTXVCropGuides`、`LTXVLatentUpsamplerTiled`、`ComfyMathExpression`、`VHS_VideoCombine`、`LTXVSeparateAVLatent`、`BasicScheduler`、`ManualSigmas`、`LTXIdentityOverlapConditioning`、`ImageResizeKJv2`、`SimpleMath+`、`PrimitiveBoolean`、`Int`、`LTXTiledSampler`、`VAEDecodeTiled`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
