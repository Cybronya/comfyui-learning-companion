---
key: 视频生成/图生视频/LTX-2.5图生视频（提示词指南）_2087560099316453378.json
name: LTX-2.5图生视频（提示词指南）_2087560099316453378
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.5图生视频（提示词指南）_2087560099316453378.json
hash: 1722760d4d5ffd39
coverage: 0.763158
learned_at: 2026-10-16 21:27:31
nodes: [PrimitiveFloat, PrimitiveFloat, LTXVAudioVAEDecode, CreateVideo, SaveVideo, ComfyMathExpression, PrimitiveFloat, PrimitiveFloat, CLIPTextEncode, CLIPTextEncode, VAELoader, LTXVConcatAVLatent, LoadImage, LTXFloatToInt, CLIPLoader, MarkdownNote, VAEDecodeTiled, Int, RandomNoise, PreviewImage, PrimitiveStringMultiline, ResizeImageMaskNode, PrimitiveInt, DF_Get_image_size, LTXVEmptyLatentAudio, KSamplerSelect, SamplerCustomAdvanced, UNETLoader, PrimitiveStringMultiline, LTXVConditioning, LTXVSeparateAVLatent, LTXVImgToVideoInplace, VAELoader, LTXVPreprocess, EmptyLTXVLatentVideo, ManualSigmas, CFGGuider, LTXVImgToVideoInplace]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 121}
---

# 视频生成/图生视频/LTX-2.5图生视频（提示词指南）_2087560099316453378.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX-2.5图生视频（提示词指南）_2087560099316453378.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `PrimitiveFloat`
- `PrimitiveFloat`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LTXVConcatAVLatent`
- `LoadImage`
- `LTXFloatToInt`
- `CLIPLoader`
- `MarkdownNote`
- `VAEDecodeTiled` ★核心
- `Int`
- `RandomNoise`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `ResizeImageMaskNode`
- `PrimitiveInt`
- `DF_Get_image_size`
- `LTXVEmptyLatentAudio` ★核心
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `VAELoader`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `ManualSigmas`
- `CFGGuider`
- `LTXVImgToVideoInplace`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **76%**（29/38）

**有卡**：`LTXVAudioVAEDecode`、`CreateVideo`、`SaveVideo`、`ComfyMathExpression`、`CLIPTextEncode`、`VAELoader`、`LTXVConcatAVLatent`、`LoadImage`、`LTXFloatToInt`、`CLIPLoader`、`VAEDecodeTiled`、`Int`、`RandomNoise`、`ResizeImageMaskNode`、`DF_Get_image_size`、`LTXVEmptyLatentAudio`、`KSamplerSelect`、`SamplerCustomAdvanced`、`UNETLoader`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`ManualSigmas`、`CFGGuider`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
