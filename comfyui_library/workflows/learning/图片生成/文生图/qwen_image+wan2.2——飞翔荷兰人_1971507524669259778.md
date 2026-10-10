---
key: qwen_image+wan2.2——飞翔荷兰人_1971507524669259778.json
name: qwen_image+wan2.2——飞翔荷兰人_1971507524669259778
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen_image+wan2.2——飞翔荷兰人_1971507524669259778.json
hash: 3c8a55cb3b4b8403
coverage: 0.686869
learned_at: 2026-10-10 20:59:25
nodes: [ImageStitch, easy showAnything, easy ifElse, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoModelLoader, CreateCFGScheduleFloatList, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoModelLoader, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoDecode, WanVideoVAELoader, WanVideoTextEncode, easy showAnything, WanVideoClipVisionEncode, WanVideoSLG, CogVideoEnhanceAVideo, SimpleMath+, LayerUtility: ImageMaskScaleAs, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSampler, easy cleanGpuUsed, WanVideoSampler, LayerUtility: ImageScaleByAspectRatio V2, RH_Captioner, LoadWanVideoClipTextEncoder, CLIPVisionLoader, Textbox, PrimitiveBoolean, easy int, easy cleanGpuUsed, WanVideoImageToVideoEncode, easy ifElse, CLIPTextEncode, easy cleanGpuUsed, CR Text Replace, RH_Captioner, VAELoader, Note, TextBox, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, CLIPLoader, TextBox, easy showAnything, SimpleMath+, easy int, ModelSamplingSD3, WanImageToVideo, ModelSamplingSD3, RH_Translator, easy showAnything, DF_Integer, VHS_VideoCombine, LoadImage, LoadImage, CLIPVisionEncode, CLIPVisionLoader, CLIPTextEncode, easy showAnything, KSamplerAdvanced, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, VAEDecode, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, TextBox, PrimitiveBoolean, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, CLIPLoader, UNETLoader, CLIPTextEncode, EmptySD3LatentImage, ModelSamplingAuraFlow, KSampler, VAEDecode, LoraLoaderModelOnly, AILab_MiniCPM_4_V, PathchSageAttentionKJ, UNETLoader, PreviewImage, DF_Integer, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: [CR Text Replace, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, SimpleMath+, SimpleMath+, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy int, easy int]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 283296236430492, "steps": 8}
discoveries: [次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageMaskScaleAs` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# qwen_image+wan2.2——飞翔荷兰人_1971507524669259778.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen_image+wan2.2——飞翔荷兰人_1971507524669259778.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（99 个）：
- `ImageStitch`
- `easy showAnything`
- `easy ifElse`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `CreateCFGScheduleFloatList`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `easy showAnything`
- `WanVideoClipVisionEncode`
- `WanVideoSLG`
- `CogVideoEnhanceAVideo`
- `SimpleMath+`
- `LayerUtility: ImageMaskScaleAs`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RH_Captioner`
- `LoadWanVideoClipTextEncoder` ★核心
- `CLIPVisionLoader`
- `Textbox`
- `PrimitiveBoolean`
- `easy int`
- `easy cleanGpuUsed`
- `WanVideoImageToVideoEncode`
- `easy ifElse`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `CR Text Replace`
- `RH_Captioner`
- `VAELoader`
- `Note`
- `TextBox`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `TextBox`
- `easy showAnything`
- `SimpleMath+`
- `easy int`
- `ModelSamplingSD3`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `RH_Translator`
- `easy showAnything`
- `DF_Integer`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `TextBox`
- `PrimitiveBoolean`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `AILab_MiniCPM_4_V`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `PreviewImage`
- `DF_Integer`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `283296236430492`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **69%**（68/99）

**有卡**：`ImageStitch`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoClipVisionEncode`、`WanVideoSLG`、`CogVideoEnhanceAVideo`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSampler`、`RH_Captioner`、`LoadWanVideoClipTextEncoder`、`CLIPVisionLoader`、`Textbox`、`PrimitiveBoolean`、`WanVideoImageToVideoEncode`、`CLIPTextEncode`、`VAELoader`、`TextBox`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CLIPLoader`、`ModelSamplingSD3`、`WanImageToVideo`、`RH_Translator`、`DF_Integer`、`VHS_VideoCombine`、`LoadImage`、`CLIPVisionEncode`、`KSamplerAdvanced`、`VAEDecode`、`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`KSampler`、`AILab_MiniCPM_4_V`

**缺卡**（22）：`CR Text Replace`、`LayerUtility: ImageMaskScaleAs`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`SimpleMath+`、`SimpleMath+`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy int`、`easy int`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageMaskScaleAs` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
