---
key: 视频生成/图生视频/lix2.3图生视频（首帧）_2069607607387639810.json
name: lix2.3图生视频（首帧）_2069607607387639810.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/lix2.3图生视频（首帧）_2069607607387639810.json
hash: 7e5305dc082cd1bb
coverage: 0.911111
learned_at: 2026-10-15 22:40:30
nodes: [LTXVSeparateAVLatent, LTXVConditioning, RandomNoise, LTXVAudioVAELoader, LTXVPreprocess, CheckpointLoaderSimple, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, PrimitiveString, SamplerCustomAdvanced, GemmaAPITextEncode, KSamplerSelect, CLIPTextEncode, ClownSampler_Beta, GuiderParameters, CFGGuider, RandomNoise, PrimitiveBoolean, GemmaAPITextEncode, LTXVAudioVAEDecode, LTXVTiledVAEDecode, LTXVAudioVAEDecode, LTXVTiledVAEDecode, PrimitiveFloat, SaveVideo, CreateVideo, LTXFloatToInt, MarkdownNote, LoadImage, SaveVideo, MultimodalGuider, PrimitiveInt, GuiderParameters, LTXAVTextEncoderLoader, LTXVScheduler, LTXVEmptyLatentAudio, LTXVConcatAVLatent, CreateVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXVImgToVideoConditionOnly, EmptyLTXVLatentVideo, ResizeImageMaskNode, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/lix2.3图生视频（首帧）_2069607607387639810.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2069607607387639810.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（45 个）：
- `LTXVSeparateAVLatent`
- `LTXVConditioning`
- `RandomNoise`
- `LTXVAudioVAELoader`
- `LTXVPreprocess`
- `CheckpointLoaderSimple` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `PrimitiveString`
- `SamplerCustomAdvanced` ★核心
- `GemmaAPITextEncode`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `ClownSampler_Beta` ★核心
- `GuiderParameters`
- `CFGGuider`
- `RandomNoise`
- `PrimitiveBoolean`
- `GemmaAPITextEncode`
- `LTXVAudioVAEDecode` ★核心
- `LTXVTiledVAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVTiledVAEDecode` ★核心
- `PrimitiveFloat`
- `SaveVideo`
- `CreateVideo`
- `LTXFloatToInt`
- `MarkdownNote`
- `LoadImage`
- `SaveVideo`
- `MultimodalGuider`
- `PrimitiveInt`
- `GuiderParameters`
- `LTXAVTextEncoderLoader`
- `LTXVScheduler`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `CreateVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVImgToVideoConditionOnly`
- `EmptyLTXVLatentVideo`
- `ResizeImageMaskNode`
- `CLIPTextEncode` ★核心

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（41/45）

**有卡**：`LTXVSeparateAVLatent`、`LTXVConditioning`、`RandomNoise`、`LTXVAudioVAELoader`、`LTXVPreprocess`、`CheckpointLoaderSimple`、`ManualSigmas`、`SamplerCustomAdvanced`、`GemmaAPITextEncode`、`KSamplerSelect`、`CLIPTextEncode`、`ClownSampler_Beta`、`GuiderParameters`、`CFGGuider`、`PrimitiveBoolean`、`LTXVAudioVAEDecode`、`LTXVTiledVAEDecode`、`SaveVideo`、`CreateVideo`、`LTXFloatToInt`、`LoadImage`、`MultimodalGuider`、`LTXAVTextEncoderLoader`、`LTXVScheduler`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`LoraLoaderModelOnly`、`LTXVImgToVideoConditionOnly`、`EmptyLTXVLatentVideo`、`ResizeImageMaskNode`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、ClownSampler_Beta
