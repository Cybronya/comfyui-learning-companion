---
key: 视频生成/图生视频/数字人直播、影视预演，情绪演绎 表情调节 人物表情控制，视频生成ltx2.3_2082710649158848514.json
name: 数字人直播、影视预演，情绪演绎 表情调节 人物表情控制，视频生成ltx2.3_2082710649158848514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/数字人直播、影视预演，情绪演绎 表情调节 人物表情控制，视频生成ltx2.3_2082710649158848514.json
hash: 7cfb3d0846e59423
coverage: 0.401639
learned_at: 2026-10-16 01:17:14
nodes: [GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, VAELoaderKJ, DualCLIPLoader, VAELoader, SetNode, LTXVLatentUpsampler, LTXVSeparateAVLatent, KSamplerSelect, SetNode, EmptyLTXVLatentVideo, GetNode, GetNode, LatentUpscaleModelLoader, GetNode, LTXVAudioVAEDecode, CFGGuider, LTXVConcatAVLatent, SetNode, GetNode, RandomNoise, CFGGuider, GetNode, GetNode, GetNode, KSamplerSelect, ManualSigmas, GetNode, LTXVScheduler, GetNode, VAELoader, LoraLoaderModelOnly, GetNode, GetNode, SimpleCalculatorKJ, LTXVEmptyLatentAudio, SetNode, RandomNoise, LTXVSeparateAVLatent, LTX2_NAG, SetNode, GetNode, GetNode, GetNode, PrimitiveStringMultiline, PrimitiveStringMultiline, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, LTXVImgToVideoConditionOnly, GetNode, GetNode, GetNode, VAEDecodeTiled, SetNode, SetNode, ManualSigmas, SetNode, SamplerCustomAdvanced, GetNode, GetNode, PrimitiveStringMultiline, CR Text Concatenate, easy anythingIndexSwitch, SetNode, ShowText|pysssss, LTXVImgToVideoConditionOnly, LTXVConditioning, GetNode, SetNode, GetImageSize, SetNode, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, GetNode, CLIPTextEncode, PrimitiveStringMultiline, SamplerCustomAdvanced, GetNode, LTXVConcatAVLatent, SetNode, SetNode, GetNode, GetNode, GetNode, CLIPTextEncode, ImageResizeKJv2, SetNode, SimpleCalculatorKJ, LTXVPreprocess, PathchSageAttentionKJ, ModelPatchTorchSettings, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, CheckpointLoaderSimple, PrimitiveStringMultiline, PrimitiveStringMultiline, JjkText, JWInteger, PrimitiveStringMultiline, MarkdownNote, VHS_VideoCombine, INTConstant, INTConstant, PrimitiveFloat, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 24, "width": 121}
---

# 视频生成/图生视频/数字人直播、影视预演，情绪演绎 表情调节 人物表情控制，视频生成ltx2.3_2082710649158848514.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/数字人直播、影视预演，情绪演绎 表情调节 人物表情控制，视频生成ltx2.3_2082710649158848514.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（122 个）：
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
- `PrimitiveStringMultiline`
- `CR Text Concatenate`
- `easy anythingIndexSwitch`
- `SetNode`
- `ShowText|pysssss`
- `LTXVImgToVideoConditionOnly`
- `LTXVConditioning`
- `GetNode`
- `SetNode`
- `GetImageSize`
- `SetNode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `GetNode`
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
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
- `LTXVPreprocess`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `JjkText`
- `JWInteger`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `PrimitiveFloat`
- `LoadImage`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **40%**（49/122）

**有卡**：`VAELoaderKJ`、`DualCLIPLoader`、`VAELoader`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`KSamplerSelect`、`EmptyLTXVLatentVideo`、`LatentUpscaleModelLoader`、`LTXVAudioVAEDecode`、`CFGGuider`、`LTXVConcatAVLatent`、`RandomNoise`、`ManualSigmas`、`LTXVScheduler`、`LoraLoaderModelOnly`、`SimpleCalculatorKJ`、`LTXVEmptyLatentAudio`、`LTX2_NAG`、`LTXVImgToVideoConditionOnly`、`VAEDecodeTiled`、`SamplerCustomAdvanced`、`CR Text Concatenate`、`easy anythingIndexSwitch`、`LTXVConditioning`、`GetImageSize`、`CLIPTextEncode`、`ImageResizeKJv2`、`LTXVPreprocess`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CheckpointLoaderSimple`、`JWInteger`、`VHS_VideoCombine`、`INTConstant`、`LoadImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
