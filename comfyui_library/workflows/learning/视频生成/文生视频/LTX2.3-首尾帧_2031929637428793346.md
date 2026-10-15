---
key: 视频生成/文生视频/LTX2.3-首尾帧_2031929637428793346.json
name: LTX2.3-首尾帧_2031929637428793346
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3-首尾帧_2031929637428793346.json
hash: 42b1224e12ccab5c
coverage: 0.93617
learned_at: 2026-10-15 22:45:05
nodes: [RandomNoise, CFGGuider, KSamplerSelect, DualCLIPLoader, UNETLoader, VAELoaderKJ, LatentUpscaleModelLoader, CLIPTextEncode, VAELoaderKJ, LTXVConditioning, LTXVSeparateAVLatent, VAEDecodeTiled, RandomNoise, CFGGuider, KSamplerSelect, CreateVideo, LTXVAudioVAEDecode, ManualSigmas, ImageResizeKJv2, SimpleMath+, SimpleMath+, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, SamplerCustomAdvanced, LTXVLatentUpsampler, LTXVCropGuides, LTXVImgToVideoInplace, LTXVConcatAVLatent, ManualSigmas, ImageResizeKJv2, LTXVSeparateAVLatent, LTXVConcatAVLatent, LoadImage, LoadImage, CLIPTextEncode, SimpleMath+, Primitive float [Crystools], PrimitiveNode, PrimitiveNode, PrimitiveInt, SamplerCustomAdvanced, LTXVImgToVideoInplaceKJ, SimpleMath+, LTXVPreprocess, SaveImage, 1hew_SaveVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 121}
---

# 视频生成/文生视频/LTX2.3-首尾帧_2031929637428793346.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3-首尾帧_2031929637428793346.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `VAELoaderKJ`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `CreateVideo`
- `LTXVAudioVAEDecode` ★核心
- `ManualSigmas`
- `ImageResizeKJv2`
- `SimpleMath+`
- `SimpleMath+`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `ImageResizeKJv2`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `Primitive float [Crystools]`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveInt`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplaceKJ`
- `SimpleMath+`
- `LTXVPreprocess`
- `SaveImage`
- `1hew_SaveVideo`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（44/47）

**有卡**：`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`DualCLIPLoader`、`UNETLoader`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`CreateVideo`、`LTXVAudioVAEDecode`、`ManualSigmas`、`ImageResizeKJv2`、`SimpleMath+`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`LoadImage`、`Primitive float [Crystools]`、`LTXVImgToVideoInplaceKJ`、`SaveImage`、`1hew_SaveVideo`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
