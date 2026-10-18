---
key: 视频生成/图生视频/LTX2.3 图生视频｜+参考视频运镜（仅参考运镜）  IC LoRA_2042074773987008513.json
name: LTX2.3 图生视频｜+参考视频运镜（仅参考运镜）  IC LoRA_2042074773987008513.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 图生视频｜+参考视频运镜（仅参考运镜）  IC LoRA_2042074773987008513.json
hash: 7ff2c6073f546b4b
coverage: 0.758065
learned_at: 2026-10-15 22:36:24
nodes: [Note, Note, Note, GetImageSizeAndCount, LTXVPreprocess, Note, PathchSageAttentionKJ, Note, EmptyLTXVLatentVideo, LTXVImgToVideoConditionOnly, CFGGuider, ManualSigmas, LTXVConcatAVLatent, LTXVEmptyLatentAudio, SamplerCustomAdvanced, easy cleanGpuUsed, LTXVSeparateAVLatent, LTXVCropGuides, VAEDecode, LTXVAudioVAEDecode, ImageConcanate, AddLabel, easy showAnything, KSamplerSelect, Note, VHS_VideoCombine, GetImageSizeAndCount, SimpleCalculatorKJ, PrimitiveFloat, LTXVConditioning, LTX2_NAG, LTXAddVideoICLoRAGuide, ModelPatchTorchSettings, LTXVChunkFeedForward, CLIPTextEncode, LTX2SamplingPreviewOverride, Note, ImageResizeKJv2, RandomNoise, Seed (rgthree), easy cleanGpuUsed, easy cleanGpuUsed, MemoryCleaner, PrimitiveInt, ImageResizeKJv2, Note, Note, CLIPTextEncode, Note, VHS_VideoCombine, AddLabel, PrimitiveFloat, Note, VHS_LoadVideo, LoadImage, DualCLIPLoader, VAELoader, VAELoaderKJ, VAELoaderKJ, UNETLoader, LTXICLoRALoaderModelOnly, SimpleCalculatorKJ]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 图生视频｜+参考视频运镜（仅参考运镜）  IC LoRA_2042074773987008513.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2042074773987008513.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（62 个）：
- `Note`
- `Note`
- `Note`
- `GetImageSizeAndCount`
- `LTXVPreprocess`
- `Note`
- `PathchSageAttentionKJ`
- `Note`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoConditionOnly`
- `CFGGuider`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `ImageConcanate`
- `AddLabel`
- `easy showAnything`
- `KSamplerSelect` ★核心
- `Note`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `SimpleCalculatorKJ`
- `PrimitiveFloat`
- `LTXVConditioning`
- `LTX2_NAG`
- `LTXAddVideoICLoRAGuide`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `CLIPTextEncode` ★核心
- `LTX2SamplingPreviewOverride`
- `Note`
- `ImageResizeKJv2`
- `RandomNoise`
- `Seed (rgthree)`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `MemoryCleaner`
- `PrimitiveInt`
- `ImageResizeKJv2`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `Note`
- `VHS_VideoCombine`
- `AddLabel`
- `PrimitiveFloat`
- `Note`
- `VHS_LoadVideo`
- `LoadImage`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `SimpleCalculatorKJ`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **76%**（47/62）

**有卡**：`GetImageSizeAndCount`、`LTXVPreprocess`、`PathchSageAttentionKJ`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoConditionOnly`、`CFGGuider`、`ManualSigmas`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`SamplerCustomAdvanced`、`easy cleanGpuUsed`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`VAEDecode`、`LTXVAudioVAEDecode`、`ImageConcanate`、`AddLabel`、`KSamplerSelect`、`VHS_VideoCombine`、`SimpleCalculatorKJ`、`LTXVConditioning`、`LTX2_NAG`、`LTXAddVideoICLoRAGuide`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`CLIPTextEncode`、`LTX2SamplingPreviewOverride`、`ImageResizeKJv2`、`RandomNoise`、`Seed (rgthree)`、`MemoryCleaner`、`VHS_LoadVideo`、`LoadImage`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`UNETLoader`、`LTXICLoRALoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
