---
key: 平台全量/LTX2.3 重新聚焦｜消除镜头模糊、恢复焦点｜IC LoRA Refocus_2046630393142579202.json
name: LTX2.3 重新聚焦｜消除镜头模糊、恢复焦点｜IC LoRA Refocus_2046630393142579202
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3 重新聚焦｜消除镜头模糊、恢复焦点｜IC LoRA Refocus_2046630393142579202.json
hash: ecf136be9b40785d
coverage: 0.777778
learned_at: 2026-11-14 00:37:51
nodes: [VHS_VideoInfo, KSamplerSelect, CFGGuider, ManualSigmas, LTXVSeparateAVLatent, LTXVCropGuides, LTXVConcatAVLatent, RandomNoise, LTXAVTextEncoderLoader, easy cleanGpuUsed, LoraLoaderModelOnly, CheckpointLoaderSimple, LoraLoaderModelOnly, CLIPTextEncode, Note, Note, easy showAnything, VHS_VideoCombine, LTXVEmptyLatentAudio, SimpleCalculatorKJ, VHS_LoadVideo, LTXVAudioVAEDecode, Note, Note, PrimitiveFloat, SimpleCalculatorKJ, PrimitiveFloat, Float32ColorCorrect, PrimitiveInt, Note, Note, VHS_VideoCombine, VHS_VideoCombine, Float32ColorCorrect, EmptyLTXVLatentVideo, LTXAddVideoICLoRAGuide, ImageResizeKJv2, LTXVImgToVideoConditionOnly, VAEDecodeTiled, ImageConcanate, CLIPTextEncode, LTXVConditioning, LTXVAudioVAELoader, easy cleanGpuUsed, SamplerCustomAdvanced]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 平台全量/LTX2.3 重新聚焦｜消除镜头模糊、恢复焦点｜IC LoRA Refocus_2046630393142579202.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3 重新聚焦｜消除镜头模糊、恢复焦点｜IC LoRA Refocus_2046630393142579202.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（45 个）：
- `VHS_VideoInfo`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `LTXAVTextEncoderLoader`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `easy showAnything`
- `VHS_VideoCombine`
- `LTXVEmptyLatentAudio` ★核心
- `SimpleCalculatorKJ`
- `VHS_LoadVideo`
- `LTXVAudioVAEDecode` ★核心
- `Note`
- `Note`
- `PrimitiveFloat`
- `SimpleCalculatorKJ`
- `PrimitiveFloat`
- `Float32ColorCorrect`
- `PrimitiveInt`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Float32ColorCorrect`
- `EmptyLTXVLatentVideo`
- `LTXAddVideoICLoRAGuide`
- `ImageResizeKJv2`
- `LTXVImgToVideoConditionOnly`
- `VAEDecodeTiled` ★核心
- `ImageConcanate`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVAudioVAELoader`
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（35/45）

**有卡**：`VHS_VideoInfo`、`KSamplerSelect`、`CFGGuider`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVConcatAVLatent`、`RandomNoise`、`LTXAVTextEncoderLoader`、`easy cleanGpuUsed`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`VHS_VideoCombine`、`LTXVEmptyLatentAudio`、`SimpleCalculatorKJ`、`VHS_LoadVideo`、`LTXVAudioVAEDecode`、`Float32ColorCorrect`、`EmptyLTXVLatentVideo`、`LTXAddVideoICLoRAGuide`、`ImageResizeKJv2`、`LTXVImgToVideoConditionOnly`、`VAEDecodeTiled`、`ImageConcanate`、`LTXVConditioning`、`LTXVAudioVAELoader`、`SamplerCustomAdvanced`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、EmptyLTXVLatentVideo、LTXAVTextEncoderLoader
