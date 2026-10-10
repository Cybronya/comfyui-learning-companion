---
key: 视频生成/文生视频/LTX2.3 文生_图生视频 KJ版_2030578285100408833.json
name: LTX2.3 文生_图生视频 KJ版_2030578285100408833
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 文生_图生视频 KJ版_2030578285100408833.json
hash: 2820f52975e89197
coverage: 0.822222
learned_at: 2026-10-11 03:16:46
nodes: [RandomNoise, KSamplerSelect, CFGGuider, SamplerCustomAdvanced, LTXVLatentUpsampler, LTXVImgToVideoInplace, Reroute, PrimitiveInt, PrimitiveBoolean, CLIPTextEncode, LTXVConditioning, ManualSigmas, SamplerCustomAdvanced, CLIPTextEncode, CFGGuider, RandomNoise, LoadImage, ManualSigmas, PrimitiveInt, UNETLoader, LTXVConcatAVLatent, ResizeImagesByLongerEdge, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVCropGuides, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVConcatAVLatent, VHS_VideoCombine, ResizeImageMaskNode, LTXVImgToVideoInplace, ComfyMathExpression, MarkdownNote, MarkdownNote, KSamplerSelect, VAELoaderKJ, VAELoaderKJ, LatentUpscaleModelLoader, DualCLIPLoader, PrimitiveInt, PrimitiveInt, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.3 文生_图生视频 KJ版_2030578285100408833.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 文生_图生视频 KJ版_2030578285100408833.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（45 个）：
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `Reroute`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `RandomNoise`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `LTXVConcatAVLatent`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `VHS_VideoCombine`
- `ResizeImageMaskNode`
- `LTXVImgToVideoInplace`
- `ComfyMathExpression`
- `MarkdownNote`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（37/45）

**有卡**：`RandomNoise`、`KSamplerSelect`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`PrimitiveBoolean`、`CLIPTextEncode`、`LTXVConditioning`、`ManualSigmas`、`LoadImage`、`UNETLoader`、`LTXVConcatAVLatent`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`VHS_VideoCombine`、`ResizeImageMaskNode`、`ComfyMathExpression`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`DualCLIPLoader`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
