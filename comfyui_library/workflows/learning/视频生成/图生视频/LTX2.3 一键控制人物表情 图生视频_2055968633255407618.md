---
key: 视频生成/图生视频/LTX2.3 一键控制人物表情 图生视频_2055968633255407618.json
name: LTX2.3 一键控制人物表情 图生视频_2055968633255407618.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2055968633255407618.json
hash: 30c2407e89fd65c5
coverage: 0.4
learned_at: 2026-10-15 22:38:00
nodes: [GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, VAELoaderKJ, DualCLIPLoader, VAELoader, SetNode, LTXVLatentUpsampler, LTXVSeparateAVLatent, KSamplerSelect, SetNode, EmptyLTXVLatentVideo, GetNode, GetNode, LatentUpscaleModelLoader, GetNode, LTXVAudioVAEDecode, CFGGuider, LTXVConcatAVLatent, SetNode, GetNode, RandomNoise, CFGGuider, GetNode, GetNode, GetNode, KSamplerSelect, ManualSigmas, GetNode, LTXVScheduler, GetNode, VAELoader, LoraLoaderModelOnly, GetNode, GetNode, SimpleCalculatorKJ, LTXVEmptyLatentAudio, SetNode, RandomNoise, LTXVSeparateAVLatent, LTX2_NAG, SetNode, GetNode, GetNode, GetNode, PrimitiveStringMultiline, PrimitiveStringMultiline, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, LTXVImgToVideoConditionOnly, GetNode, GetNode, GetNode, VAEDecodeTiled, SetNode, SetNode, ManualSigmas, SetNode, SamplerCustomAdvanced, GetNode, GetNode, VHS_VideoCombine, ModelPatchTorchSettings, SetNode, PathchSageAttentionKJ, PrimitiveStringMultiline, CR Text Concatenate, easy anythingIndexSwitch, SetNode, ShowText|pysssss, PrimitiveStringMultiline, CheckpointLoaderSimple, LTXVImgToVideoConditionOnly, LTXVConditioning, GetNode, LoraLoaderModelOnly, LTXVPreprocess, SetNode, GetImageSize, SetNode, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, GetNode, CLIPTextEncode, JjkText, PrimitiveStringMultiline, SamplerCustomAdvanced, GetNode, PrimitiveStringMultiline, LTXVConcatAVLatent, SetNode, SetNode, GetNode, GetNode, GetNode, CLIPTextEncode, ImageResizeKJv2, SetNode, SimpleCalculatorKJ, INTConstant, PrimitiveFloat, INTConstant, JWInteger, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 24, "width": 121}
---

# 视频生成/图生视频/LTX2.3 一键控制人物表情 图生视频_2055968633255407618.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2055968633255407618.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（120 个）：
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoader`
- `SetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `SetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `LatentUpscaleModelLoader`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SetNode`
- `GetNode`
- `RandomNoise`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `GetNode`
- `LTXVScheduler`
- `GetNode`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `LTXVEmptyLatentAudio` ★核心
- `SetNode`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTX2_NAG`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoConditionOnly`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `SetNode`
- `ManualSigmas`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `ModelPatchTorchSettings`
- `SetNode`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `CR Text Concatenate`
- `easy anythingIndexSwitch`
- `SetNode`
- `ShowText|pysssss`
- `PrimitiveStringMultiline`
- `CheckpointLoaderSimple` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXVConditioning`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LTXVPreprocess`
- `SetNode`
- `GetImageSize`
- `SetNode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `GetNode`
- `CLIPTextEncode` ★核心
- `JjkText`
- `PrimitiveStringMultiline`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `PrimitiveStringMultiline`
- `LTXVConcatAVLatent`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `SetNode`
- `SimpleCalculatorKJ`
- `INTConstant`
- `PrimitiveFloat`
- `INTConstant`
- `JWInteger`
- `LoadImage`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **40%**（48/120）

**有卡**：`VAELoaderKJ`、`DualCLIPLoader`、`VAELoader`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`KSamplerSelect`、`EmptyLTXVLatentVideo`、`LatentUpscaleModelLoader`、`LTXVAudioVAEDecode`、`CFGGuider`、`LTXVConcatAVLatent`、`RandomNoise`、`ManualSigmas`、`LTXVScheduler`、`LoraLoaderModelOnly`、`SimpleCalculatorKJ`、`LTXVEmptyLatentAudio`、`LTX2_NAG`、`LTXVImgToVideoConditionOnly`、`VAEDecodeTiled`、`SamplerCustomAdvanced`、`VHS_VideoCombine`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`CR Text Concatenate`、`easy anythingIndexSwitch`、`CheckpointLoaderSimple`、`LTXVConditioning`、`LTXVPreprocess`、`GetImageSize`、`CLIPTextEncode`、`ImageResizeKJv2`、`INTConstant`、`JWInteger`、`LoadImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
