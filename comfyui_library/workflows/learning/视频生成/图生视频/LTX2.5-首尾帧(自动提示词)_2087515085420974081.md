---
key: 视频生成/图生视频/LTX2.5-首尾帧(自动提示词)_2087515085420974081.json
name: LTX2.5-首尾帧(自动提示词)_2087515085420974081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5-首尾帧(自动提示词)_2087515085420974081.json
hash: d376290c0c008d60
coverage: 0.818182
learned_at: 2026-10-16 21:27:36
nodes: [MarkdownNote, MarkdownNote, LTXVConcatAVLatent, LTXVDualCFGGuider, RandomNoise, CLIPTextEncode, CLIPTextEncode, LTXVPreprocess, ResizeImageMaskNode, SamplerCustomAdvanced, LTXVSeparateAVLatent, CreateVideo, SaveVideo, ResizeImageMaskNode, LTXVPreprocess, GetImageSize, LoadImage, LoadImage, PrimitiveInt, PrimitiveInt, PrimitiveInt, ComfyMathExpression, ManualSigmas, SamplerEulerAncestral, LTXVAddGuide, LTXVConditioning, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVAddGuide, MarkdownNote, PrimitiveStringMultiline, llama_cpp_model_loader, ImageConcanate, Text, UNETLoader, VAELoader, VAELoader, CLIPLoader, llama_cpp_instruct_adv, PrimitiveInt, ComfyMathExpression, LTXVCropGuides, LTXVAudioVAEDecode, VAEDecodeTiled]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5-首尾帧(自动提示词)_2087515085420974081.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5-首尾帧(自动提示词)_2087515085420974081.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `MarkdownNote`
- `MarkdownNote`
- `LTXVConcatAVLatent`
- `LTXVDualCFGGuider`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `SaveVideo`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `GetImageSize`
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ManualSigmas`
- `SamplerEulerAncestral` ★核心
- `LTXVAddGuide`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVAddGuide`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `llama_cpp_model_loader`
- `ImageConcanate`
- `Text`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `llama_cpp_instruct_adv`
- `PrimitiveInt`
- `ComfyMathExpression`
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（36/44）

**有卡**：`LTXVConcatAVLatent`、`LTXVDualCFGGuider`、`RandomNoise`、`CLIPTextEncode`、`LTXVPreprocess`、`ResizeImageMaskNode`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`CreateVideo`、`SaveVideo`、`GetImageSize`、`LoadImage`、`ComfyMathExpression`、`ManualSigmas`、`SamplerEulerAncestral`、`LTXVAddGuide`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`llama_cpp_model_loader`、`ImageConcanate`、`Text`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`llama_cpp_instruct_adv`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、SamplerCustomAdvanced、SamplerEulerAncestral、LTXVDualCFGGuider
