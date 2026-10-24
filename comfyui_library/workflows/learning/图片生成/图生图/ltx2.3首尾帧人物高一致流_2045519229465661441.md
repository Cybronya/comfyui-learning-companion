---
key: 图片生成/图生图/ltx2.3首尾帧人物高一致流_2045519229465661441.json
name: ltx2.3首尾帧人物高一致流_2045519229465661441
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/ltx2.3首尾帧人物高一致流_2045519229465661441.json
hash: 346de6a0bd0f7dfd
coverage: 0.948718
learned_at: 2026-10-23 11:40:58
nodes: [LTXVPreprocess, RandomNoise, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVConditioning, GetImageSize, LTXVAddGuide, LTXVAddGuide, SamplerEulerAncestral, ManualSigmas, LTXVConcatAVLatent, ResizeImageMaskNode, Image Batch, LTXVCropGuides, VAEDecode, LTXVAudioVAEDecode, LTXVSeparateAVLatent, CFGGuider, SamplerCustomAdvanced, PrimitiveInt, PrimitiveInt, TTResolutionSelector, CreateVideo, VAELoader, LTX2SamplingPreviewOverride, ResizeImageMaskNode, LTXVEmptyLatentAudio, ComfyMathExpression, SaveVideo, VAELoader, VAELoaderKJ, LoadImage, UNETLoader, Power Lora Loader (rgthree), DualCLIPLoader, CLIPTextEncode, CLIPTextEncode, LoadImage, LoraLoader]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "height": 25, "lora_name": "LTX-2-Image2Vid-Adapter.safetensors", "strength_clip": 1, "strength_model": 1, "width": 97}
---

# 图片生成/图生图/ltx2.3首尾帧人物高一致流_2045519229465661441.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/ltx2.3首尾帧人物高一致流_2045519229465661441.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `LTXVPreprocess`
- `RandomNoise`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `GetImageSize`
- `LTXVAddGuide`
- `LTXVAddGuide`
- `SamplerEulerAncestral` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `ResizeImageMaskNode`
- `Image Batch`
- `LTXVCropGuides`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `TTResolutionSelector`
- `CreateVideo`
- `VAELoader`
- `LTX2SamplingPreviewOverride`
- `ResizeImageMaskNode`
- `LTXVEmptyLatentAudio` ★核心
- `ComfyMathExpression`
- `SaveVideo`
- `VAELoader`
- `VAELoaderKJ`
- `LoadImage`
- `UNETLoader` ★核心
- `Power Lora Loader (rgthree)`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoraLoader` ★核心

**识别到的模式**：lora

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `lora_name` = `LTX-2-Image2Vid-Adapter.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **95%**（37/39）

**有卡**：`LTXVPreprocess`、`RandomNoise`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`GetImageSize`、`LTXVAddGuide`、`SamplerEulerAncestral`、`ManualSigmas`、`LTXVConcatAVLatent`、`ResizeImageMaskNode`、`Image Batch`、`LTXVCropGuides`、`VAEDecode`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`CFGGuider`、`SamplerCustomAdvanced`、`TTResolutionSelector`、`CreateVideo`、`VAELoader`、`LTX2SamplingPreviewOverride`、`LTXVEmptyLatentAudio`、`ComfyMathExpression`、`SaveVideo`、`VAELoaderKJ`、`LoadImage`、`UNETLoader`、`Power Lora Loader (rgthree)`、`DualCLIPLoader`、`CLIPTextEncode`、`LoraLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、SamplerCustomAdvanced、SamplerEulerAncestral
