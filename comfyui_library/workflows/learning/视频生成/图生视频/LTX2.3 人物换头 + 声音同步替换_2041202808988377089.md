---
key: 视频生成/图生视频/LTX2.3 人物换头 + 声音同步替换_2041202808988377089.json
name: LTX2.3 人物换头 + 声音同步替换_2041202808988377089.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 人物换头 + 声音同步替换_2041202808988377089.json
hash: 61bec81f2268dadd
coverage: 0.348837
learned_at: 2026-10-15 22:36:18
nodes: [SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SimpleCalculatorKJ, GetImageSize, SolidMask, LTXVAudioVAEEncode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, CLIPTextEncode, GetNode, ComfySwitchNode, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, SetNode, SetNode, GetNode, SetNode, GetNode, LTXVConditioning, GetNode, VAEEncode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, SetNode, SetNode, ImageConcanate, GetNode, GetNode, GetNode, SetNode, PreviewAny, ComfySwitchNode, PreviewAny, CFGGuider, GetNode, PrimitiveNode, GetNode, GetNode, CreateVideo, GetNode, GetNode, SetNode, SetNode, SetNode, VAEDecode, LTXVConcatAVLatent, SetNode, SetLatentNoiseMask, GetNode, SetNode, RandomNoise, ImageResizeKJv2, GetNode, GetNode, SetNode, VHS_VideoCombine, GetNode, GetNode, SamplerCustomAdvanced, GetNode, SetNode, LoraLoaderModelOnly, Note, PrimitiveStringMultiline, PrimitiveNode, SetNode, LTXVAddGuideMulti, ManualSigmas, BasicScheduler, LTXVCropGuides, SetNode, KSamplerSelect, CLIPTextEncode, SetNode, Note, GetNode, LoraLoaderModelOnly, GetNode, GetNode, LatentUpscaleModelLoader, DualCLIPLoader, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, SetNode, TrimAudioDuration, SetNode, ReservedRegionFrameComposer, LoraLoaderModelOnly, VAELoaderKJ, VAELoaderKJ, UNETLoader, LoadImage, PreviewAny, LoraLoader, TextGenerateLTX2Prompt, PrimitiveInt, SetNode, RecordAudio, LoadAudio, PrimitiveFloat, PrimitiveFloat, GetNode, SetNode, SetNode, easy showAnything, VHS_LoadVideo, SaveVideo, GetNode, LoadVideo, RH_LLMAPI_Pro_Node, MarkdownNote, MarkdownNote]
patterns: [lora]
missing: []
parameters: {"lora_name": "gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 视频生成/图生视频/LTX2.3 人物换头 + 声音同步替换_2041202808988377089.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041202808988377089.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（129 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SimpleCalculatorKJ`
- `GetImageSize`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `ComfySwitchNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVConditioning`
- `GetNode`
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SetNode`
- `SetNode`
- `ImageConcanate`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PreviewAny`
- `ComfySwitchNode`
- `PreviewAny`
- `CFGGuider`
- `GetNode`
- `PrimitiveNode`
- `GetNode`
- `GetNode`
- `CreateVideo`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `SetLatentNoiseMask`
- `GetNode`
- `SetNode`
- `RandomNoise`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `PrimitiveStringMultiline`
- `PrimitiveNode`
- `SetNode`
- `LTXVAddGuideMulti`
- `ManualSigmas`
- `BasicScheduler`
- `LTXVCropGuides`
- `SetNode`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `Note`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `TrimAudioDuration`
- `SetNode`
- `ReservedRegionFrameComposer`
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `LoadImage`
- `PreviewAny`
- `LoraLoader` ★核心
- `TextGenerateLTX2Prompt`
- `PrimitiveInt`
- `SetNode`
- `RecordAudio`
- `LoadAudio`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `GetNode`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `VHS_LoadVideo`
- `SaveVideo`
- `GetNode`
- `LoadVideo`
- `RH_LLMAPI_Pro_Node`
- `MarkdownNote`
- `MarkdownNote`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **35%**（45/129）

**有卡**：`SimpleCalculatorKJ`、`GetImageSize`、`SolidMask`、`LTXVAudioVAEEncode`、`CLIPTextEncode`、`LTXVConditioning`、`VAEEncode`、`LTXVSeparateAVLatent`、`ImageConcanate`、`CFGGuider`、`CreateVideo`、`VAEDecode`、`LTXVConcatAVLatent`、`SetLatentNoiseMask`、`RandomNoise`、`ImageResizeKJv2`、`VHS_VideoCombine`、`SamplerCustomAdvanced`、`LoraLoaderModelOnly`、`LTXVAddGuideMulti`、`ManualSigmas`、`BasicScheduler`、`LTXVCropGuides`、`KSamplerSelect`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`TrimAudioDuration`、`ReservedRegionFrameComposer`、`VAELoaderKJ`、`UNETLoader`、`LoadImage`、`LoraLoader`、`TextGenerateLTX2Prompt`、`RecordAudio`、`LoadAudio`、`VHS_LoadVideo`、`SaveVideo`、`LoadVideo`、`RH_LLMAPI_Pro_Node`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
