---
key: 视频生成/图生视频/LTX-2.5 单图多参_2087502470892310529.json
name: LTX-2.5 单图多参_2087502470892310529
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.5 单图多参_2087502470892310529.json
hash: ecadec53a7a9914f
coverage: 0.809524
learned_at: 2026-10-16 21:27:31
nodes: [LTXVConditioning, GetImageSize, LTXVEmptyLatentAudio, RepeatImageBatch, LTXVAudioVAEDecode, CreateVideo, VAEDecodeTiled, VAELoader, VAELoader, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVConcatAVLatent, CFGGuider, KSamplerSelect, ManualSigmas, LTXVSeparateAVLatent, LTXVCropGuides, RandomNoise, SamplerCustomAdvanced, Note, ComfyMathExpression, PrimitiveInt, ResizeImageMaskNode, LTXVConditioning, GetVideoComponents, CreateVideo, CLIPTextEncode, CLIPTextEncode, SaveVideo, MarkdownNote, Reroute, PrimitiveFloat, PrimitiveFloat, PrimitiveStringMultiline, PrimitiveBoolean, LTXVImgToVideoInplace, UNETLoader, LTXICLoRALoaderModelOnly, CLIPLoader, LoadImage, PrimitiveStringMultiline, LTXAddVideoICLoRAGuide]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 121}
---

# 视频生成/图生视频/LTX-2.5 单图多参_2087502470892310529.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX-2.5 单图多参_2087502470892310529.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `LTXVConditioning`
- `GetImageSize`
- `LTXVEmptyLatentAudio` ★核心
- `RepeatImageBatch`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `VAELoader`
- `VAELoader`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `Note`
- `ComfyMathExpression`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `LTXVConditioning`
- `GetVideoComponents`
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `MarkdownNote`
- `Reroute`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`
- `LTXVImgToVideoInplace`
- `UNETLoader` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `CLIPLoader`
- `LoadImage`
- `PrimitiveStringMultiline`
- `LTXAddVideoICLoRAGuide`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（34/42）

**有卡**：`LTXVConditioning`、`GetImageSize`、`LTXVEmptyLatentAudio`、`RepeatImageBatch`、`LTXVAudioVAEDecode`、`CreateVideo`、`VAEDecodeTiled`、`VAELoader`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`RandomNoise`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`ResizeImageMaskNode`、`GetVideoComponents`、`CLIPTextEncode`、`SaveVideo`、`PrimitiveBoolean`、`LTXVImgToVideoInplace`、`UNETLoader`、`LTXICLoRALoaderModelOnly`、`CLIPLoader`、`LoadImage`、`LTXAddVideoICLoRAGuide`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
