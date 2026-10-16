---
key: 视频生成/图生视频/video_ltx2_3_FLframe_latent_injection_likeness1-2-c_2076879552093179906.json
name: video_ltx2_3_FLframe_latent_injection_likeness1-2-c_2076879552093179906.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2076879552093179906.json
hash: 6daac56bebefcb20
coverage: 0.463918
learned_at: 2026-10-15 22:41:34
nodes: [RandomNoise, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, MarkdownNote, PrimitiveInt, MarkdownNote, LTXVLatentUpsamplerTiled, ImageResizeKJv2, ResizeImageMaskNode, SetNode, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, VAELoaderKJ, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, SetNode, SetNode, SetNode, SetNode, UNETLoader, SetNode, SetNode, VAELoaderKJ, DualCLIPLoader, LatentUpscaleModelLoader, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXLatentAnchorAware, SetNode, SetNode, SetNode, SetNode, SetNode, STGGuiderAdvanced, SetNode, GetNode, LTXVImgToVideoInplaceKJ, RandomNoise, GetNode, GetNode, GetNode, CFGGuider, GetNode, GetNode, KSamplerSelect, ManualSigmas, Sigmas Easing, GetNode, GetNode, SetNode, GetNode, LTXLikenessAnchor, GetNode, GetNode, ComfyMathExpression, SetNode, GetNode, VAEDecode, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVConcatAVLatent, ManualSigmas, KSamplerSelect, LTXTiledSampler, LTXVSeparateAVLatent, PrimitiveInt, PrimitiveInt, PrimitiveBoolean, LTXLikenessGuide, LTXVImgToVideoInplaceKJ, LTXFaceDetector, VHS_VideoCombine, VHS_VideoCombine, VAEDecodeTiled, LTXVAudioVAEDecode, GetNode, VHS_VideoCombine, PrimitiveStringMultiline, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/video_ltx2_3_FLframe_latent_injection_likeness1-2-c_2076879552093179906.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2076879552093179906.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（97 个）：
- `RandomNoise`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `MarkdownNote`
- `PrimitiveInt`
- `MarkdownNote`
- `LTXVLatentUpsamplerTiled` ★核心
- `ImageResizeKJv2`
- `ResizeImageMaskNode`
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `VAELoaderKJ`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXLatentAnchorAware`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `STGGuiderAdvanced`
- `SetNode`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `Sigmas Easing`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXLikenessAnchor`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXTiledSampler` ★核心
- `LTXVSeparateAVLatent`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `LTXLikenessGuide`
- `LTXVImgToVideoInplaceKJ`
- `LTXFaceDetector`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **46%**（45/97）

**有卡**：`RandomNoise`、`ComfyMathExpression`、`LTXVLatentUpsamplerTiled`、`ImageResizeKJv2`、`ResizeImageMaskNode`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`VAELoaderKJ`、`CLIPTextEncode`、`LTXVConditioning`、`UNETLoader`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`LTXVConcatAVLatent`、`LTXLatentAnchorAware`、`STGGuiderAdvanced`、`LTXVImgToVideoInplaceKJ`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`Sigmas Easing`、`LTXLikenessAnchor`、`VAEDecode`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXTiledSampler`、`PrimitiveBoolean`、`LTXLikenessGuide`、`LTXFaceDetector`、`VHS_VideoCombine`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LoadImage`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXTiledSampler
