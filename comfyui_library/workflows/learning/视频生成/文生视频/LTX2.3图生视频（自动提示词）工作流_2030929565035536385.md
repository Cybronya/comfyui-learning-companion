---
key: 视频生成/文生视频/LTX2.3图生视频（自动提示词）工作流_2030929565035536385.json
name: LTX2.3图生视频（自动提示词）工作流_2030929565035536385
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3图生视频（自动提示词）工作流_2030929565035536385.json
hash: cdefb18b604a77ba
coverage: 0.890909
learned_at: 2026-10-15 22:45:07
nodes: [EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, llama_cpp_instruct_adv, PreviewAny, llama_cpp_model_loader, ResizeImagesByLongerEdge, LTXVPreprocess, Resize, PrimitiveBoolean, UNETLoader, LoraLoaderModelOnly, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, LTXVLatentUpsampler, LTXVImgToVideoInplace, RandomNoise, ManualSigmas, LTXVConcatAVLatent, CLIPTextEncode, LTXVConditioning, PathchSageAttentionKJ, MuyeTextEditOutput, RandomNoise, KSamplerSelect, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, ManualSigmas, Reroute, CLIPTextEncode, ComfyMathExpression, LTXVConcatAVLatent, LTXVImgToVideoInplace, VAEDecodeTiled, VHS_VideoCombine, PrimitiveInt, LTXVAudioVAEDecode, LTXVSeparateAVLatent, RIFEInterpolation, PrimitiveInt, LoadImage, Int, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, easy showAnything, Int, Int, LatentUpscaleModelLoader, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.3图生视频（自动提示词）工作流_2030929565035536385.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3图生视频（自动提示词）工作流_2030929565035536385.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（55 个）：
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `llama_cpp_instruct_adv`
- `PreviewAny`
- `llama_cpp_model_loader`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `Resize`
- `PrimitiveBoolean`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `RandomNoise`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `PathchSageAttentionKJ`
- `MuyeTextEditOutput`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `ManualSigmas`
- `Reroute`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `PrimitiveInt`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `RIFEInterpolation`
- `PrimitiveInt`
- `LoadImage`
- `Int`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `easy showAnything`
- `Int`
- `Int`
- `LatentUpscaleModelLoader`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（49/55）

**有卡**：`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`Resize`、`PrimitiveBoolean`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoaderKJ`、`DualCLIPLoader`、`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`RandomNoise`、`ManualSigmas`、`LTXVConcatAVLatent`、`CLIPTextEncode`、`LTXVConditioning`、`PathchSageAttentionKJ`、`MuyeTextEditOutput`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`ComfyMathExpression`、`VAEDecodeTiled`、`VHS_VideoCombine`、`LTXVAudioVAEDecode`、`RIFEInterpolation`、`LoadImage`、`Int`、`LatentUpscaleModelLoader`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
