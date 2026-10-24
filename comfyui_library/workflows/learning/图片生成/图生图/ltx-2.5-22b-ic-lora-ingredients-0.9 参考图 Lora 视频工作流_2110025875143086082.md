---
key: 图片生成/图生图/ltx-2.5-22b-ic-lora-ingredients-0.9 参考图 Lora 视频工作流_2110025875143086082.json
name: ltx-2.5-22b-ic-lora-ingredients-0.9 参考图 Lora 视频工作流_2110025875143086082
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/ltx-2.5-22b-ic-lora-ingredients-0.9 参考图 Lora 视频工作流_2110025875143086082.json
hash: a56613aacc62f756
coverage: 0.809524
learned_at: 2026-10-23 11:40:57
nodes: [LTXVCropGuides, ComfyMathExpression, ComfyMathExpression, MarkdownNote, SamplerCustomAdvanced, CFGGuider, RandomNoise, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, Note, CLIPTextEncode, CLIPTextEncode, PrimitiveStringMultiline, LTXICLoRALoaderModelOnly, Label (rgthree), LTXVConditioning, PrimitiveInt, ComfyMathExpression, LTXAddVideoICLoRAGuide, ComfyMathExpression, LTXVEmptyLatentAudio, VAELoader, VAELoader, PrimitiveFloat, PrimitiveFloat, ComfyMathExpression, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CLIPLoader, PrimitiveStringMultiline, PrimitiveInt, GetImageSize, UNETLoader, LoadImage, CreateVideo, SaveVideo, ComfyMathExpression, ImageScale, RepeatImageBatch, EmptyLTXVLatentVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 图片生成/图生图/ltx-2.5-22b-ic-lora-ingredients-0.9 参考图 Lora 视频工作流_2110025875143086082.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/ltx-2.5-22b-ic-lora-ingredients-0.9 参考图 Lora 视频工作流_2110025875143086082.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `LTXVCropGuides`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `LTXICLoRALoaderModelOnly` ★核心
- `Label (rgthree)`
- `LTXVConditioning`
- `PrimitiveInt`
- `ComfyMathExpression`
- `LTXAddVideoICLoRAGuide`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `VAELoader`
- `VAELoader`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `GetImageSize`
- `UNETLoader` ★核心
- `LoadImage`
- `CreateVideo`
- `SaveVideo`
- `ComfyMathExpression`
- `ImageScale`
- `RepeatImageBatch`
- `EmptyLTXVLatentVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（34/42）

**有卡**：`LTXVCropGuides`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`CFGGuider`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`CLIPTextEncode`、`LTXICLoRALoaderModelOnly`、`Label (rgthree)`、`LTXVConditioning`、`LTXAddVideoICLoRAGuide`、`LTXVEmptyLatentAudio`、`VAELoader`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CLIPLoader`、`GetImageSize`、`UNETLoader`、`LoadImage`、`CreateVideo`、`SaveVideo`、`ImageScale`、`RepeatImageBatch`、`EmptyLTXVLatentVideo`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
