---
key: 音频生成/音频生成/【原生 LTX 2.3】数字人说话 _ 唱歌工作流｜图 + 音一键驱动，人物零变形_2047015575972483074.json
name: 【原生 LTX 2.3】数字人说话 _ 唱歌工作流｜图 + 音一键驱动，人物零变形_2047015575972483074
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/【原生 LTX 2.3】数字人说话 _ 唱歌工作流｜图 + 音一键驱动，人物零变形_2047015575972483074.json
hash: d97d014020dacd6e
coverage: 0.428571
learned_at: 2026-10-18 03:05:00
nodes: [VAELoader, SetNode, SetNode, LatentUpscaleModelLoader, DualCLIPLoader, VAELoaderKJ, VAELoader, SetNode, SetNode, SetNode, GetNode, GetNode, LTX2_NAG, SetNode, GetNode, SamplerCustomAdvanced, GetNode, SimpleCalculatorKJ, GetNode, SetNode, SetNode, SetNode, LTXVConditioning, SetNode, GetNode, SimpleCalculatorKJ, RandomNoise, GetNode, SolidMask, GetNode, GetNode, SetNode, BasicScheduler, ModelSamplingSD3, GetNode, GetNode, LTXVConcatAVLatent, SetLatentNoiseMask, LTXVAudioVAEEncode, KSamplerSelect, VAEDecode, GetNode, LTXVSeparateAVLatent, SetNode, GetNode, LTX2SamplingPreviewOverride, SetNode, GetNode, GetNode, LTXVPreprocess, GetNode, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, GetNode, SetNode, SetNode, TrimAudioDuration, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, ImageResizeKJv2, UNETLoader, CFGGuider, SetNode, LTXVImgToVideoInplaceKJ, SetNode, INTConstant, GetNode, INTConstant, PrimitiveFloat, PrimitiveStringMultiline, LoadImage, LoadAudio, PrimitiveStringMultiline, VHS_VideoCombine, CLIPTextEncode, JoinStrings, CLIPTextEncode]
patterns: []
missing: []
---

# 音频生成/音频生成/【原生 LTX 2.3】数字人说话 _ 唱歌工作流｜图 + 音一键驱动，人物零变形_2047015575972483074.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/【原生 LTX 2.3】数字人说话 _ 唱歌工作流｜图 + 音一键驱动，人物零变形_2047015575972483074.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（84 个）：
- `VAELoader`
- `SetNode`
- `SetNode`
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTX2_NAG`
- `SetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVConditioning`
- `SetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `RandomNoise`
- `GetNode`
- `SolidMask`
- `GetNode`
- `GetNode`
- `SetNode`
- `BasicScheduler`
- `ModelSamplingSD3`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `LTXVSeparateAVLatent`
- `SetNode`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVPreprocess`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `SetNode`
- `SetNode`
- `TrimAudioDuration`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `CFGGuider`
- `SetNode`
- `LTXVImgToVideoInplaceKJ`
- `SetNode`
- `INTConstant`
- `GetNode`
- `INTConstant`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadAudio`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `JoinStrings`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **43%**（36/84）

**有卡**：`VAELoader`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`LTX2_NAG`、`SamplerCustomAdvanced`、`SimpleCalculatorKJ`、`LTXVConditioning`、`RandomNoise`、`SolidMask`、`BasicScheduler`、`ModelSamplingSD3`、`LTXVConcatAVLatent`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`KSamplerSelect`、`VAEDecode`、`LTXVSeparateAVLatent`、`LTX2SamplingPreviewOverride`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`TrimAudioDuration`、`ImageResizeKJv2`、`UNETLoader`、`CFGGuider`、`LTXVImgToVideoInplaceKJ`、`INTConstant`、`LoadImage`、`LoadAudio`、`VHS_VideoCombine`、`CLIPTextEncode`、`JoinStrings`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
