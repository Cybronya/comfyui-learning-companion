---
key: 视频生成/文生视频/LTX2.3-GGUF-手动提示词版_2034561004020961282.json
name: LTX2.3-GGUF-手动提示词版_2034561004020961282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3-GGUF-手动提示词版_2034561004020961282.json
hash: 8924c548a22fa0f3
coverage: 0.811321
learned_at: 2026-10-11 03:48:35
nodes: [RandomNoise, UnetLoaderGGUF, VAELoaderKJ, CFGGuider, LTXVSeparateAVLatent, RandomNoise, LTXVAudioVAEDecode, VAEDecodeTiled, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, VAELoaderKJ, LatentUpscaleModelLoader, DualCLIPLoaderGGUF, LTXVConditioning, PrimitiveInt, PrimitiveInt, Note, LTXVImgToVideoInplace, PrimitiveBoolean, llama_cpp_model_loader, easy cleanGpuUsed, LTXVConcatAVLatent, ManualSigmas, KSamplerSelect, CFGGuider, LTXVLatentUpsampler, SamplerCustomAdvanced, KSamplerSelect, ManualSigmas, CreateVideo, LTXVPreprocess, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVEmptyLatentAudio, PrimitiveStringMultiline, llama_cpp_parameters, ShowText|pysssss, SaveVideo, Note, LoadImage, CLIPTextEncode, llama_cpp_instruct_adv, PrimitiveInt, PrimitiveInt, ResizeImagesByLongerEdge, ResizeImageMaskNode, CLIPTextEncode, Note]
patterns: []
missing: [easy cleanGpuUsed]
parameters: {"batch_size": 1, "height": 25, "width": 97}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3-GGUF-手动提示词版_2034561004020961282.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3-GGUF-手动提示词版_2034561004020961282.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `RandomNoise`
- `UnetLoaderGGUF` ★核心
- `VAELoaderKJ`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `DualCLIPLoaderGGUF`
- `LTXVConditioning`
- `PrimitiveInt`
- `PrimitiveInt`
- `Note`
- `LTXVImgToVideoInplace`
- `PrimitiveBoolean`
- `llama_cpp_model_loader`
- `easy cleanGpuUsed`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CreateVideo`
- `LTXVPreprocess`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `PrimitiveStringMultiline`
- `llama_cpp_parameters`
- `ShowText|pysssss`
- `SaveVideo`
- `Note`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `llama_cpp_instruct_adv`
- `PrimitiveInt`
- `PrimitiveInt`
- `ResizeImagesByLongerEdge`
- `ResizeImageMaskNode`
- `CLIPTextEncode` ★核心
- `Note`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（43/53）

**有卡**：`RandomNoise`、`UnetLoaderGGUF`、`VAELoaderKJ`、`CFGGuider`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LatentUpscaleModelLoader`、`DualCLIPLoaderGGUF`、`LTXVConditioning`、`LTXVImgToVideoInplace`、`PrimitiveBoolean`、`llama_cpp_model_loader`、`LTXVConcatAVLatent`、`ManualSigmas`、`KSamplerSelect`、`LTXVLatentUpsampler`、`CreateVideo`、`LTXVPreprocess`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`llama_cpp_parameters`、`SaveVideo`、`LoadImage`、`CLIPTextEncode`、`llama_cpp_instruct_adv`、`ResizeImagesByLongerEdge`、`ResizeImageMaskNode`

**缺卡**（1）：`easy cleanGpuUsed`

**用到的条目**：CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent、LTXVSeparateAVLatent

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
