---
key: 视频生成/图生视频/LTX2.3强化对口型 KJ版_2040052966710845441.json
name: LTX2.3强化对口型 KJ版_2040052966710845441.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2040052966710845441.json
hash: 033b20ba2c5facb0
coverage: 0.844444
learned_at: 2026-10-15 22:36:13
nodes: [RandomNoise, KSamplerSelect, CFGGuider, SamplerCustomAdvanced, LTXVLatentUpsampler, LTXVImgToVideoInplace, Reroute, PrimitiveInt, CLIPTextEncode, LTXVConditioning, ManualSigmas, SamplerCustomAdvanced, CLIPTextEncode, CFGGuider, RandomNoise, ManualSigmas, PrimitiveInt, LTXVConcatAVLatent, ResizeImagesByLongerEdge, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVCropGuides, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVConcatAVLatent, VHS_VideoCombine, ResizeImageMaskNode, LTXVImgToVideoInplace, ComfyMathExpression, MarkdownNote, KSamplerSelect, VAELoaderKJ, VAELoaderKJ, LatentUpscaleModelLoader, DualCLIPLoader, PrimitiveInt, PrimitiveInt, PrimitiveBoolean, LoraLoaderModelOnly, UNETLoader, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3强化对口型 KJ版_2040052966710845441.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2040052966710845441.json`

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
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `RandomNoise`
- `ManualSigmas`
- `PrimitiveInt`
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
- `KSamplerSelect` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（38/45）

**有卡**：`RandomNoise`、`KSamplerSelect`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`CLIPTextEncode`、`LTXVConditioning`、`ManualSigmas`、`LTXVConcatAVLatent`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`VHS_VideoCombine`、`ResizeImageMaskNode`、`ComfyMathExpression`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`PrimitiveBoolean`、`LoraLoaderModelOnly`、`UNETLoader`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
