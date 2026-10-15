---
key: 视频生成/文生视频/ltx2.5双采文生+图生_2087504450205339650.json
name: ltx2.5双采文生+图生_2087504450205339650
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx2.5双采文生+图生_2087504450205339650.json
hash: 54b3adc3ed7d69d7
coverage: 0.773585
learned_at: 2026-10-15 22:47:23
nodes: [LTXVAudioVAEDecode, LTXFloatToInt, LTXVEmptyLatentAudio, LTXVConcatAVLatent, Note, SamplerCustomAdvanced, LTXVSeparateAVLatent, ComfySwitchNode, ComfySwitchNode, PrimitiveStringMultiline, LTXVAudioVAEDecode, CreateVideo, VAEDecodeTiled, LTXVPreprocess, LTXFloatToInt, ComfySwitchNode, ComfySwitchNode, PrimitiveFloat, ManualSigmas, KSamplerSelect, CFGGuider, RandomNoise, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, PrimitiveFloat, PrimitiveFloat, PrimitiveInt, ComfyMathExpression, RandomNoise, LTXVImgToVideoInplace, CFGGuider, KSamplerSelect, LTXVLatentUpsampler, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, PrimitiveFloat, PrimitiveInt, ComfyMathExpression, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXVSeparateAVLatent, SamplerCustomAdvanced, RandomNoise, Note, CFGGuider, KSamplerSelect, ManualSigmas, RandomNoise, CFGGuider, ManualSigmas, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVConcatAVLatent, KSamplerSelect, SamplerCustomAdvanced, LTXVSeparateAVLatent, MarkdownNote, CLIPLoader, CLIPLoader, LatentUpscaleModelLoader, UNETLoader, VAELoader, PrimitiveFloat, VAELoader, ResizeImageMaskNode, ComfyNotNode, PrimitiveBoolean, MarkdownNote, LTXVImgToVideoInplace, SaveVideo, PrimitiveFloat, LoadImage, ComfyNotNode, VAELoader, PrimitiveStringMultiline, PrimitiveStringMultiline, VAELoader, LatentUpscaleModelLoader, PrimitiveFloat, PrimitiveFloat, PrimitiveBoolean, LTXVImgToVideoInplace, ResizeImageMaskNode, LTXVPreprocess, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), EmptyLTXVLatentVideo, EmptyLTXVLatentVideo, Fast Groups Bypasser (rgthree), CLIPLoader, CLIPLoader, LoadImage, VAEDecodeTiled, CreateVideo, SaveVideo, UNETLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 121}
---

# 视频生成/文生视频/ltx2.5双采文生+图生_2087504450205339650.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx2.5双采文生+图生_2087504450205339650.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（106 个）：
- `LTXVAudioVAEDecode` ★核心
- `LTXFloatToInt`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `Note`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `LTXVPreprocess`
- `LTXFloatToInt`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PrimitiveFloat`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveInt`
- `ComfyMathExpression`
- `RandomNoise`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVLatentUpsampler` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `TextGenerateLTX2Prompt`
- `TextGenerateLTX2Prompt`
- `TextGenerateLTX2Prompt`
- `TextGenerateLTX2Prompt`
- `PrimitiveFloat`
- `PrimitiveInt`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `Note`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `CFGGuider`
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `MarkdownNote`
- `CLIPLoader`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `PrimitiveFloat`
- `VAELoader`
- `ResizeImageMaskNode`
- `ComfyNotNode`
- `PrimitiveBoolean`
- `MarkdownNote`
- `LTXVImgToVideoInplace`
- `SaveVideo`
- `PrimitiveFloat`
- `LoadImage`
- `ComfyNotNode`
- `VAELoader`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveBoolean`
- `LTXVImgToVideoInplace`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `EmptyLTXVLatentVideo`
- `EmptyLTXVLatentVideo`
- `Fast Groups Bypasser (rgthree)`
- `CLIPLoader`
- `CLIPLoader`
- `LoadImage`
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `SaveVideo`
- `UNETLoader` ★核心

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **77%**（82/106）

**有卡**：`LTXVAudioVAEDecode`、`LTXFloatToInt`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`CreateVideo`、`VAEDecodeTiled`、`LTXVPreprocess`、`ManualSigmas`、`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`CLIPTextEncode`、`LTXVConditioning`、`ComfyMathExpression`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`TextGenerateLTX2Prompt`、`CLIPLoader`、`LatentUpscaleModelLoader`、`UNETLoader`、`VAELoader`、`ResizeImageMaskNode`、`ComfyNotNode`、`PrimitiveBoolean`、`SaveVideo`、`LoadImage`、`EmptyLTXVLatentVideo`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
