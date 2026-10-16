---
key: 视频生成/图生视频/Qwen3.5+LTX2.3-transition-lora-丝滑转场-首尾帧视频-自动提示词_2063264536383287297.json
name: Qwen3.5+LTX2.3-transition-lora-丝滑转场-首尾帧视频-自动提示词_2063264536383287297.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2063264536383287297.json
hash: 3c2e24a9e010fddc
coverage: 0.887097
learned_at: 2026-10-15 22:39:12
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, Reroute, SamplerCustomAdvanced, LTXVSeparateAVLatent, PrimitiveBoolean, ComfyMathExpression, EmptyLTXVLatentVideo, ResizeImageMaskNode, ResizeImagesByLongerEdge, ImageResizeKJv2, ResizeImagesByLongerEdge, LTXVPreprocess, LTXVPreprocess, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, LTXVLatentUpsampler, CreateVideo, ManualSigmas, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVImgToVideoInplace, CFGGuider, KSamplerSelect, LTXVCropGuides, ComfyMathExpression, PrimitiveStringMultiline, UNETLoader, LTXVAddGuideMulti, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVEmptyLatentAudio, ComfyMathExpression, LatentUpscaleModelLoader, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, LoraLoaderModelOnly, MarkdownNote, MarkdownNote, RH_LLMAPI_Pro_Node, JjkText, Dapao_LlamaCaptionOptions, SimpleMath+, Int, JWFloat, Int, Int, RegexReplace, Dapao_LlamaCaption, easy showAnything, easy showAnything, VHS_VideoCombine, VHS_VideoCombine, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/Qwen3.5+LTX2.3-transition-lora-丝滑转场-首尾帧视频-自动提示词_2063264536383287297.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2063264536383287297.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（62 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `PrimitiveBoolean`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVLatentUpsampler` ★核心
- `CreateVideo`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVCropGuides`
- `ComfyMathExpression`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `LTXVAddGuideMulti`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `ComfyMathExpression`
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `RH_LLMAPI_Pro_Node`
- `JjkText`
- `Dapao_LlamaCaptionOptions`
- `SimpleMath+`
- `Int`
- `JWFloat`
- `Int`
- `Int`
- `RegexReplace`
- `Dapao_LlamaCaption`
- `easy showAnything`
- `easy showAnything`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（55/62）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`PrimitiveBoolean`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`ImageResizeKJv2`、`LTXVPreprocess`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVLatentUpsampler`、`CreateVideo`、`LTXVImgToVideoInplace`、`LTXVCropGuides`、`UNETLoader`、`LTXVAddGuideMulti`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`LoraLoaderModelOnly`、`RH_LLMAPI_Pro_Node`、`Dapao_LlamaCaptionOptions`、`SimpleMath+`、`Int`、`JWFloat`、`RegexReplace`、`Dapao_LlamaCaption`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
