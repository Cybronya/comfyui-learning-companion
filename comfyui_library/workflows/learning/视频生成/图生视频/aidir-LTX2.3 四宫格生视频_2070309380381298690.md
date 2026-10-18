---
key: 视频生成/图生视频/aidir-LTX2.3 四宫格生视频_2070309380381298690.json
name: aidir-LTX2.3 四宫格生视频_2070309380381298690.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/aidir-LTX2.3 四宫格生视频_2070309380381298690.json
hash: 568aadede225f59d
coverage: 0.491935
learned_at: 2026-10-15 22:40:36
nodes: [SetNode, INTConstant, SamplerCustomAdvanced, LTXVConcatAVLatent, LTXVEmptyLatentAudio, CM_FloatToInt, GetNode, GetNode, LTXVConditioning, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, LTXVCropGuides, llama_cpp_model_loader, llama_cpp_parameters, easy cleanGpuUsed, GetNode, CFGGuider, KSamplerSelect, RandomNoise, SetNode, INTConstant, SetNode, SetNode, MarkdownNote, Note, SetNode, SetNode, GetNode, PrimitiveFloat, SetNode, SimpleCalculatorKJ, GetNode, EmptyLTXVLatentVideo, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, easy cleanGpuUsed, VAEDecodeTiled, SetNode, easy cleanGpuUsed, LTXVAudioVAEDecode, SetNode, GetNode, ImageResizeKJv2, SetNode, ImageResizeKJv2, SetNode, ImageFromBatch+, ImageFromBatch+, GetNode, ImageFromBatch+, ImageFromBatch+, ImageResizeKJv2, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, GetNode, SetNode, GetNode, GetNode, SetNode, ManualSigmas, ShowText|pysssss, LatentUpscaleModelLoader, VAELoaderKJ, SetNode, SetNode, SetNode, LoadAudio, SetNode, RecordAudio, PrimitiveFloat, MarkdownNote, MarkdownNote, CLIPTextEncode, CLIPTextEncode, Label (rgthree), Label (rgthree), VAELoaderKJ, DualCLIPLoader, GetNode, GetNode, INTConstant, INTConstant, LTXVAddGuideMulti, RH_LLMAPI_Pro_Node, VHS_VideoCombine, SetNode, GetNode, SetNode, UNETLoader, LoraLoaderModelOnly, GuHaiAutoImageSplit, PreviewImage, LoadImage, LoadVideo, LoadImage, LoadVideo, LoadImage, LoadVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, VHS_VideoCombine, PrimitiveStringMultiline, LoadImage, PrimitiveStringMultiline, llama_cpp_instruct_adv]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 视频生成/图生视频/aidir-LTX2.3 四宫格生视频_2070309380381298690.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2070309380381298690.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（124 个）：
- `SetNode`
- `INTConstant`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `CM_FloatToInt`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVCropGuides`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `easy cleanGpuUsed`
- `GetNode`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SetNode`
- `INTConstant`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `Note`
- `SetNode`
- `SetNode`
- `GetNode`
- `PrimitiveFloat`
- `SetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `easy cleanGpuUsed`
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `GetNode`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ManualSigmas`
- `ShowText|pysssss`
- `LatentUpscaleModelLoader`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadAudio`
- `SetNode`
- `RecordAudio`
- `PrimitiveFloat`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Label (rgthree)`
- `Label (rgthree)`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `GetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `LTXVAddGuideMulti`
- `RH_LLMAPI_Pro_Node`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `SetNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `GuHaiAutoImageSplit`
- `PreviewImage`
- `LoadImage`
- `LoadVideo`
- `LoadImage`
- `LoadVideo`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `LoadImage`
- `PrimitiveStringMultiline`
- `llama_cpp_instruct_adv`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **49%**（61/124）

**有卡**：`INTConstant`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`CM_FloatToInt`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`easy cleanGpuUsed`、`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`SimpleCalculatorKJ`、`EmptyLTXVLatentVideo`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`ImageResizeKJv2`、`ImageFromBatch+`、`ManualSigmas`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`LoadAudio`、`RecordAudio`、`CLIPTextEncode`、`Label (rgthree)`、`DualCLIPLoader`、`LTXVAddGuideMulti`、`RH_LLMAPI_Pro_Node`、`VHS_VideoCombine`、`UNETLoader`、`LoraLoaderModelOnly`、`GuHaiAutoImageSplit`、`LoadImage`、`LoadVideo`、`llama_cpp_instruct_adv`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
