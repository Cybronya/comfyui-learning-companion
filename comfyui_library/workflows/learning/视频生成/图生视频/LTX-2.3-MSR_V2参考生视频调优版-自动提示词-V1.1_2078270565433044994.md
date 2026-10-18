---
key: 视频生成/图生视频/LTX-2.3-MSR_V2参考生视频调优版-自动提示词-V1.1_2078270565433044994.json
name: LTX-2.3-MSR_V2参考生视频调优版-自动提示词-V1.1_2078270565433044994.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3-MSR_V2参考生视频调优版-自动提示词-V1.1_2078270565433044994.json
hash: 6717c6db9559af9a
coverage: 0.459459
learned_at: 2026-10-15 22:41:50
nodes: [GetNode, GetNode, RandomNoise, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, CFGGuider, GetNode, SetNode, SetNode, LTXVConditioning, ComfyMathExpression, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, EmptyLTXVLatentVideo, LTXVConcatAVLatent, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, LTXAddVideoICLoRAGuide, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, GetNode, ComfyMathExpression, VAEDecode, LTXVCropGuides, SetNode, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, JjkText, JjkText, PreviewAny, CR Text Concatenate, CR Text Concatenate, ProcessString, PurgeVRAM_UTK, SomethingToString, SetNode, PreviewAny, GetNode, GetNode, ExtractLinesByIndex, SetNode, Any Switch (rgthree), GetNode, CR Text Concatenate, llama_cpp_parameters, GetNode, GetNode, GetNode, PreviewAny, SetNode, SetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree), llama_cpp_model_loader, llama_cpp_instruct_adv, LoadImage, LoadImage, LoadImage, LoadImage, BatchImagesNode, LiconMSR, SetNode, SetNode, PreviewImage, PreviewAny, GetNode, KSamplerSelect, ManualSigmas, LoadImage, VHS_VideoCombine, PreviewAny, VHS_VideoCombine, CheckpointLoaderSimple, SetNode, SetNode, SetNode, INTConstant, INTConstant, INTConstant, INTConstant, ComfyMathExpression, SetNode, Note, LTXICLoRALoaderModelOnly, LoraLoaderModelOnly, GetNode, GetNode, LTXVEmptyLatentAudio, SetNode, LTXICLoRALoaderModelOnly, LoraLoaderModelOnly, PrimitiveStringMultiline, PromptRelayEncode, JjkText, LTX2_NAG, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 24, "width": 145}
---

# 视频生成/图生视频/LTX-2.3-MSR_V2参考生视频调优版-自动提示词-V1.1_2078270565433044994.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2078270565433044994.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（111 个）：
- `GetNode`
- `GetNode`
- `RandomNoise`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `GetNode`
- `SetNode`
- `SetNode`
- `LTXVConditioning`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `LTXAddVideoICLoRAGuide`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `ComfyMathExpression`
- `VAEDecode` ★核心
- `LTXVCropGuides`
- `SetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `JjkText`
- `JjkText`
- `PreviewAny`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `ProcessString`
- `PurgeVRAM_UTK`
- `SomethingToString`
- `SetNode`
- `PreviewAny`
- `GetNode`
- `GetNode`
- `ExtractLinesByIndex`
- `SetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `CR Text Concatenate`
- `llama_cpp_parameters`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewAny`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `BatchImagesNode`
- `LiconMSR`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `PreviewAny`
- `GetNode`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LoadImage`
- `VHS_VideoCombine`
- `PreviewAny`
- `VHS_VideoCombine`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `ComfyMathExpression`
- `SetNode`
- `Note`
- `LTXICLoRALoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `SetNode`
- `LTXICLoRALoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `PromptRelayEncode`
- `JjkText`
- `LTX2_NAG`
- `Note`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`
- `width` = `145`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **46%**（51/111）

**有卡**：`RandomNoise`、`CFGGuider`、`LTXVConditioning`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`LTXAddVideoICLoRAGuide`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecode`、`LTXVCropGuides`、`VAELoaderKJ`、`DualCLIPLoader`、`CR Text Concatenate`、`ProcessString`、`PurgeVRAM_UTK`、`SomethingToString`、`ExtractLinesByIndex`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`LoadImage`、`BatchImagesNode`、`LiconMSR`、`KSamplerSelect`、`ManualSigmas`、`VHS_VideoCombine`、`CheckpointLoaderSimple`、`INTConstant`、`LTXICLoRALoaderModelOnly`、`LoraLoaderModelOnly`、`LTXVEmptyLatentAudio`、`PromptRelayEncode`、`LTX2_NAG`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
