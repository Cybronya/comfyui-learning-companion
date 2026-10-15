---
key: 视频生成/文生视频/LTX-2.3+Qwen3.5生成宠物播客视频_2030535698637398018.json
name: LTX-2.3+Qwen3.5生成宠物播客视频_2030535698637398018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3+Qwen3.5生成宠物播客视频_2030535698637398018.json
hash: b7a9baa9715cff15
coverage: 0.851852
learned_at: 2026-10-15 22:44:39
nodes: [LTXVConcatAVLatent, LTXVAudioVAELoader, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVCropGuides, LoraLoaderModelOnly, ResizeImagesByLongerEdge, LTXVLatentUpsampler, LTXVImgToVideoInplace, ResizeImageMaskNode, KSamplerSelect, Reroute, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVAudioVAEDecode, CLIPTextEncode, LTXVConditioning, LTXVConcatAVLatent, LTXVEmptyLatentAudio, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LatentUpscaleModelLoader, CLIPTextEncode, CFGGuider, VAEDecodeTiled, LTXVPreprocess, MarkdownNote, CreateVideo, MarkdownNote, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, LTXAVTextEncoderLoader, PrimitiveInt, PrimitiveInt, LoadImage, PrimitiveInt, SaveVideo, PrimitiveBoolean, llama_cpp_parameters, PrimitiveInt, llama_cpp_model_loader, CheckpointLoaderSimple, RandomNoise, RandomNoise, CFGGuider, PreviewAny, Label (rgthree), Label (rgthree), llama_cpp_instruct_adv, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX-2.3+Qwen3.5生成宠物播客视频_2030535698637398018.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3+Qwen3.5生成宠物播客视频_2030535698637398018.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `LTXVConcatAVLatent`
- `LTXVAudioVAELoader`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LoraLoaderModelOnly` ★核心
- `ResizeImagesByLongerEdge`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `ResizeImageMaskNode`
- `KSamplerSelect` ★核心
- `Reroute`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `LTXVPreprocess`
- `MarkdownNote`
- `CreateVideo`
- `MarkdownNote`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXAVTextEncoderLoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `PrimitiveInt`
- `SaveVideo`
- `PrimitiveBoolean`
- `llama_cpp_parameters`
- `PrimitiveInt`
- `llama_cpp_model_loader`
- `CheckpointLoaderSimple` ★核心
- `RandomNoise`
- `RandomNoise`
- `CFGGuider`
- `PreviewAny`
- `Label (rgthree)`
- `Label (rgthree)`
- `llama_cpp_instruct_adv`
- `CR Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **85%**（46/54）

**有卡**：`LTXVConcatAVLatent`、`LTXVAudioVAELoader`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LoraLoaderModelOnly`、`ResizeImagesByLongerEdge`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`CFGGuider`、`VAEDecodeTiled`、`LTXVPreprocess`、`CreateVideo`、`ComfyMathExpression`、`LTXAVTextEncoderLoader`、`LoadImage`、`SaveVideo`、`PrimitiveBoolean`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`CheckpointLoaderSimple`、`RandomNoise`、`Label (rgthree)`、`llama_cpp_instruct_adv`、`CR Text`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
