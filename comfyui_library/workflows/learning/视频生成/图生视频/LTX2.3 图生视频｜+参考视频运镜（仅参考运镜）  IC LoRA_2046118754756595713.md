---
key: 视频生成/图生视频/LTX2.3 图生视频｜+参考视频运镜（仅参考运镜）  IC LoRA_2046118754756595713.json
name: LTX2.3 图生视频｜+参考视频运镜（仅参考运镜）  IC LoRA_2046118754756595713.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 图生视频｜+参考视频运镜（仅参考运镜）  IC LoRA_2046118754756595713.json
hash: 10f1d3ab0d527105
coverage: 0.757576
learned_at: 2026-10-15 22:36:54
nodes: [Note, Note, VAELoaderKJ, VAELoader, Note, DualCLIPLoader, Note, Note, Note, Note, Note, Note, PrimitiveFloat, PrimitiveFloat, ImageResizeKJv2, easy cleanGpuUsed, GetImageSizeAndCount, ImageResizeKJv2, PreviewImage, PathchSageAttentionKJ, LTXVChunkFeedForward, ModelPatchTorchSettings, easy cleanGpuUsed, MemoryCleaner, VHS_VideoCombine, SimpleCalculatorKJ, SimpleCalculatorKJ, easy showAnything, LTXVPreprocess, GetImageSizeAndCount, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVAudioVAEDecode, VAEDecode, LTXVCropGuides, LTXVSeparateAVLatent, easy cleanGpuUsed, SamplerCustomAdvanced, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, LTX2SamplingPreviewOverride, Seed (rgthree), AddLabel, LTXVImgToVideoConditionOnly, LTXVConditioning, LTX2_NAG, LoadImage, CLIPTextEncode, RH_Captioner, PrimitiveInt, UNETLoader, LTXAddVideoICLoRAGuide, CLIPTextEncode, VHS_LoadVideo, VAELoaderKJ, LTXICLoRALoaderModelOnly, RandomNoise, Note, CR Text Concatenate, PrimitiveStringMultiline, RH_Translator, ImageConcanate, VHS_VideoCombine, AddLabel]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 图生视频｜+参考视频运镜（仅参考运镜）  IC LoRA_2046118754756595713.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046118754756595713.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
- `Note`
- `Note`
- `VAELoaderKJ`
- `VAELoader`
- `Note`
- `DualCLIPLoader`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `ImageResizeKJv2`
- `easy cleanGpuUsed`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `PreviewImage`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `ModelPatchTorchSettings`
- `easy cleanGpuUsed`
- `MemoryCleaner`
- `VHS_VideoCombine`
- `SimpleCalculatorKJ`
- `SimpleCalculatorKJ`
- `easy showAnything`
- `LTXVPreprocess`
- `GetImageSizeAndCount`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `LTX2SamplingPreviewOverride`
- `Seed (rgthree)`
- `AddLabel`
- `LTXVImgToVideoConditionOnly`
- `LTXVConditioning`
- `LTX2_NAG`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `RH_Captioner`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `LTXAddVideoICLoRAGuide`
- `CLIPTextEncode` ★核心
- `VHS_LoadVideo`
- `VAELoaderKJ`
- `LTXICLoRALoaderModelOnly` ★核心
- `RandomNoise`
- `Note`
- `CR Text Concatenate`
- `PrimitiveStringMultiline`
- `RH_Translator`
- `ImageConcanate`
- `VHS_VideoCombine`
- `AddLabel`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **76%**（50/66）

**有卡**：`VAELoaderKJ`、`VAELoader`、`DualCLIPLoader`、`ImageResizeKJv2`、`easy cleanGpuUsed`、`GetImageSizeAndCount`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`MemoryCleaner`、`VHS_VideoCombine`、`SimpleCalculatorKJ`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVAudioVAEDecode`、`VAEDecode`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`LTX2SamplingPreviewOverride`、`Seed (rgthree)`、`AddLabel`、`LTXVImgToVideoConditionOnly`、`LTXVConditioning`、`LTX2_NAG`、`LoadImage`、`CLIPTextEncode`、`RH_Captioner`、`UNETLoader`、`LTXAddVideoICLoRAGuide`、`VHS_LoadVideo`、`LTXICLoRALoaderModelOnly`、`RandomNoise`、`CR Text Concatenate`、`RH_Translator`、`ImageConcanate`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
