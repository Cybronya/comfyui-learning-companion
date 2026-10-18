---
key: 视频生成/图生视频/video_ltx2_3_FLframe_latent_injection_likeness1-2-c_2074509736741003266.json
name: video_ltx2_3_FLframe_latent_injection_likeness1-2-c_2074509736741003266.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/video_ltx2_3_FLframe_latent_injection_likeness1-2-c_2074509736741003266.json
hash: 9393ba8e8f0e2f74
coverage: 0.458333
learned_at: 2026-10-15 22:41:16
nodes: [RandomNoise, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, MarkdownNote, PrimitiveInt, MarkdownNote, LTXVLatentUpsamplerTiled, VAEDecodeTiled, LTXVAudioVAEDecode, ImageResizeKJv2, ResizeImageMaskNode, SetNode, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, VAELoaderKJ, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, SetNode, SetNode, SetNode, SetNode, UNETLoader, SetNode, SetNode, VAELoaderKJ, DualCLIPLoader, LatentUpscaleModelLoader, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXLatentAnchorAware, SetNode, SetNode, SetNode, SetNode, SetNode, STGGuiderAdvanced, SetNode, GetNode, LTXVImgToVideoInplaceKJ, RandomNoise, GetNode, GetNode, GetNode, CFGGuider, GetNode, GetNode, KSamplerSelect, ManualSigmas, Sigmas Easing, GetNode, GetNode, SetNode, GetNode, LTXLikenessAnchor, GetNode, GetNode, ComfyMathExpression, SetNode, GetNode, VAEDecode, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVConcatAVLatent, ManualSigmas, KSamplerSelect, LTXTiledSampler, LTXVSeparateAVLatent, GetNode, VHS_VideoCombine, PrimitiveStringMultiline, LoadImage, PrimitiveInt, PrimitiveInt, PrimitiveBoolean, LTXLikenessGuide, LTXVImgToVideoInplaceKJ, VHS_VideoCombine, LTXFaceDetector]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/video_ltx2_3_FLframe_latent_injection_likeness1-2-c_2074509736741003266.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2074509736741003266.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（96 个）：
- `RandomNoise`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `MarkdownNote`
- `PrimitiveInt`
- `MarkdownNote`
- `LTXVLatentUpsamplerTiled` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
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
- `GetNode`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `LTXLikenessGuide`
- `LTXVImgToVideoInplaceKJ`
- `VHS_VideoCombine`
- `LTXFaceDetector`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **46%**（44/96）

**有卡**：`RandomNoise`、`ComfyMathExpression`、`LTXVLatentUpsamplerTiled`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`ImageResizeKJv2`、`ResizeImageMaskNode`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`VAELoaderKJ`、`CLIPTextEncode`、`LTXVConditioning`、`UNETLoader`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`LTXVConcatAVLatent`、`LTXLatentAnchorAware`、`STGGuiderAdvanced`、`LTXVImgToVideoInplaceKJ`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`Sigmas Easing`、`LTXLikenessAnchor`、`VAEDecode`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXTiledSampler`、`VHS_VideoCombine`、`LoadImage`、`PrimitiveBoolean`、`LTXLikenessGuide`、`LTXFaceDetector`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXTiledSampler
