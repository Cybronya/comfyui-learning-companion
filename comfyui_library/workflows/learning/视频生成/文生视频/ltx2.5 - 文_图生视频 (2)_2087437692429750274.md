---
key: 视频生成/文生视频/ltx2.5 - 文_图生视频 (2)_2087437692429750274.json
name: ltx2.5 - 文_图生视频 (2)_2087437692429750274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx2.5 - 文_图生视频 (2)_2087437692429750274.json
hash: e1b9c7296adda4d8
coverage: 0.807692
learned_at: 2026-10-11 20:53:49
nodes: [PrimitiveFloat, LTXVSeparateAVLatent, LTXVImgToVideoInplace, SamplerCustomAdvanced, VAELoader, VAELoader, ManualSigmas, PrimitiveFloat, SamplerCustomAdvanced, CFGGuider, KSamplerSelect, LTXVConcatAVLatent, LTXVEmptyLatentAudio, UNETLoader, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveFloat, LTXFloatToInt, RH_LLMAPI_Pro_Node, CR Text, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVConcatAVLatent, LTXVImgToVideoInplace, ManualSigmas, KSamplerSelect, CFGGuider, RandomNoise, RandomNoise, LTXVAudioVAEDecode, VAEDecodeTiled, CreateVideo, CLIPTextEncode, CLIPTextEncode, LTXVPreprocess, EmptyLTXVLatentVideo, MarkdownNote, ComfyNotNode, PrimitiveInt, LTXVConditioning, PrimitiveStringMultiline, ResizeImageMaskNode, ComfyMathExpression, CLIPLoader, CLIPLoader, CR Text, easy showAnything, SaveVideo, LatentUpscaleModelLoader, PrimitiveBoolean, ResolutionSelector, LoadImage]
patterns: []
missing: [CR Text, CR Text]
parameters: {"batch_size": 1, "height": 25, "width": 121}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/ltx2.5 - 文_图生视频 (2)_2087437692429750274.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx2.5 - 文_图生视频 (2)_2087437692429750274.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（52 个）：
- `PrimitiveFloat`
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `VAELoader`
- `ManualSigmas`
- `PrimitiveFloat`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `PrimitiveFloat`
- `LTXFloatToInt`
- `RH_LLMAPI_Pro_Node`
- `CR Text`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `RandomNoise`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `MarkdownNote`
- `ComfyNotNode`
- `PrimitiveInt`
- `LTXVConditioning`
- `PrimitiveStringMultiline`
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `CLIPLoader`
- `CLIPLoader`
- `CR Text`
- `easy showAnything`
- `SaveVideo`
- `LatentUpscaleModelLoader`
- `PrimitiveBoolean`
- `ResolutionSelector`
- `LoadImage`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（42/52）

**有卡**：`LTXVSeparateAVLatent`、`LTXVImgToVideoInplace`、`SamplerCustomAdvanced`、`VAELoader`、`ManualSigmas`、`CFGGuider`、`KSamplerSelect`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`UNETLoader`、`LoraLoaderModelOnly`、`LTXFloatToInt`、`RH_LLMAPI_Pro_Node`、`LTXVLatentUpsampler`、`RandomNoise`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`CreateVideo`、`CLIPTextEncode`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`ComfyNotNode`、`LTXVConditioning`、`ResizeImageMaskNode`、`ComfyMathExpression`、`CLIPLoader`、`SaveVideo`、`LatentUpscaleModelLoader`、`PrimitiveBoolean`、`ResolutionSelector`、`LoadImage`

**缺卡**（2）：`CR Text`、`CR Text`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、CFGGuider

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
