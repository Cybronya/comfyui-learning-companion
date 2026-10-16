---
key: 视频生成/图生视频/LTX-2.5 T2V_I2V单采样_2087377086850883585.json
name: LTX-2.5 T2V_I2V单采样_2087377086850883585
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.5 T2V_I2V单采样_2087377086850883585.json
hash: b9ff2e07d431b6de
coverage: 0.677966
learned_at: 2026-10-16 21:27:31
nodes: [KSamplerSelect, LTXVImgToVideoInplace, GemmaAPITextEncode, VAELoader, LTXVConditioning, CLIPTextEncode, ComfySwitchNode, PrimitiveStringMultiline, ComfySwitchNode, LTXVConcatAVLatent, LTXVAudioVAEDecode, LTXVPreprocess, EmptyLTXVLatentVideo, CLIPTextEncode, LTXVEmptyLatentAudio, GemmaAPITextEncode, LTXVDualCFGGuider, CFGGuider, ComfySwitchNode, StringContains, ComfySwitchNode, PrimitiveFloat, PrimitiveFloat, ComfyMathExpression, ComfyMathExpression, LTXFloatToInt, VAELoader, VAEDecodeTiled, PrimitiveBoolean, CLIPLoader, PrimitiveBoolean, PrimitiveInt, ResizeImageMaskNode, CLIPLoader, TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, ComfyNotNode, SaveVideo, MarkdownNote, MarkdownNote, MarkdownNote, Note, MarkdownNote, MarkdownNote, LTXVSeparateAVLatent, SamplerCustomAdvanced, DualCLIPLoader, PrimitiveStringMultiline, LoadImage, ResolutionSelector, PrimitiveFloat, PrimitiveFloat, RandomNoise, ManualSigmas, CreateVideo, Reroute, CLIPLoader, UNETLoader, PreviewAny]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 121}
---

# 视频生成/图生视频/LTX-2.5 T2V_I2V单采样_2087377086850883585.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX-2.5 T2V_I2V单采样_2087377086850883585.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（59 个）：
- `KSamplerSelect` ★核心
- `LTXVImgToVideoInplace`
- `GemmaAPITextEncode`
- `VAELoader`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `CLIPTextEncode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `GemmaAPITextEncode`
- `LTXVDualCFGGuider`
- `CFGGuider`
- `ComfySwitchNode`
- `StringContains`
- `ComfySwitchNode`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXFloatToInt`
- `VAELoader`
- `VAEDecodeTiled` ★核心
- `PrimitiveBoolean`
- `CLIPLoader`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `TextGenerateLTX2Prompt`
- `ComfyNotNode`
- `SaveVideo`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `Note`
- `MarkdownNote`
- `MarkdownNote`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `DualCLIPLoader`
- `PrimitiveStringMultiline`
- `LoadImage`
- `ResolutionSelector`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `RandomNoise`
- `ManualSigmas`
- `CreateVideo`
- `Reroute`
- `CLIPLoader`
- `UNETLoader` ★核心
- `PreviewAny`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **68%**（40/59）

**有卡**：`KSamplerSelect`、`LTXVImgToVideoInplace`、`GemmaAPITextEncode`、`VAELoader`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`LTXVAudioVAEDecode`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVDualCFGGuider`、`CFGGuider`、`StringContains`、`ComfyMathExpression`、`LTXFloatToInt`、`VAEDecodeTiled`、`PrimitiveBoolean`、`CLIPLoader`、`ResizeImageMaskNode`、`TextGenerateLTX2Prompt`、`ComfyNotNode`、`SaveVideo`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`DualCLIPLoader`、`LoadImage`、`ResolutionSelector`、`RandomNoise`、`ManualSigmas`、`CreateVideo`、`UNETLoader`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
