---
key: 视频生成/文生视频/LTX2.3_IT2V_Qwen3.5自动提示词_图文生视频(图文合优化并版)_2038990216597344257.json
name: LTX2.3_IT2V_Qwen3.5自动提示词_图文生视频(图文合优化并版)_2038990216597344257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3_IT2V_Qwen3.5自动提示词_图文生视频(图文合优化并版)_2038990216597344257.json
hash: e39bc2387135e93f
coverage: 0.565217
learned_at: 2026-10-11 19:49:38
nodes: [SamplerCustomAdvanced, ManualSigmas, LTXVConcatAVLatent, KSamplerSelect, CFGGuider, RandomNoise, SamplerCustomAdvanced, MarkdownNote, SetNode, ResizeImageMaskNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVAudioVAEDecode, LTXVSeparateAVLatent, LTXVSeparateAVLatent, LTXVCropGuides, GetNode, RandomNoise, CFGGuider, KSamplerSelect, EmptyLTXVLatentVideo, GetNode, ComfyMathExpression, ResizeImagesByLongerEdge, LTXVPreprocess, SetNode, LTXVEmptyLatentAudio, GetNode, GetNode, VAEDecodeTiled, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVImgToVideoInplace, LTXVConcatAVLatent, MathExpression|pysssss, FloatConstant, SetNode, SetNode, VAELoaderKJ, VAELoaderKJ, SetNode, SetNode, SetNode, SetNode, CreateVideo, GetNode, SaveVideo, LTXVImgToVideoInplace, LTXVLatentUpsampler, GetNode, GetNode, ManualSigmas, SigmasPreview, PainterVRAM, llama_cpp_model_loader, LoraLoaderModelOnly, DualCLIPLoader, LatentUpscaleModelLoader, PrimitiveBoolean, Note, Note, Note, LoadImage, PrimitiveStringMultiline, llama_cpp_instruct_adv, SetNode, SetNode, INTConstant, INTConstant, Note, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, VAELoader, GetNode, LTX2SamplingPreviewOverride, GetNode, CR Prompt Text, LTXVConditioning, LTX2_NAG, INTConstant, ShowText|pysssss, PrimitiveStringMultiline, JoinStrings]
patterns: []
missing: [MathExpression|pysssss, CR Prompt Text]
parameters: {"batch_size": 1, "height": 25, "width": 97}
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/LTX2.3_IT2V_Qwen3.5自动提示词_图文生视频(图文合优化并版)_2038990216597344257.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3_IT2V_Qwen3.5自动提示词_图文生视频(图文合优化并版)_2038990216597344257.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（92 个）：
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `MarkdownNote`
- `SetNode`
- `ResizeImageMaskNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `GetNode`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `EmptyLTXVLatentVideo`
- `GetNode`
- `ComfyMathExpression`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `MathExpression|pysssss`
- `FloatConstant`
- `SetNode`
- `SetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CreateVideo`
- `GetNode`
- `SaveVideo`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `SigmasPreview`
- `PainterVRAM`
- `llama_cpp_model_loader`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `PrimitiveBoolean`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `PrimitiveStringMultiline`
- `llama_cpp_instruct_adv`
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `Note`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `CR Prompt Text`
- `LTXVConditioning`
- `LTX2_NAG`
- `INTConstant`
- `ShowText|pysssss`
- `PrimitiveStringMultiline`
- `JoinStrings`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **57%**（52/92）

**有卡**：`SamplerCustomAdvanced`、`ManualSigmas`、`LTXVConcatAVLatent`、`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`ResizeImageMaskNode`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LTXVEmptyLatentAudio`、`VAEDecodeTiled`、`LTXVImgToVideoInplace`、`FloatConstant`、`VAELoaderKJ`、`CreateVideo`、`SaveVideo`、`LTXVLatentUpsampler`、`SigmasPreview`、`PainterVRAM`、`llama_cpp_model_loader`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`PrimitiveBoolean`、`LoadImage`、`llama_cpp_instruct_adv`、`INTConstant`、`UNETLoader`、`CLIPTextEncode`、`VAELoader`、`LTX2SamplingPreviewOverride`、`LTXVConditioning`、`LTX2_NAG`、`JoinStrings`

**缺卡**（2）：`MathExpression|pysssss`、`CR Prompt Text`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
