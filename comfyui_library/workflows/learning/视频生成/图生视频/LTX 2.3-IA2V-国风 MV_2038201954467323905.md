---
key: 视频生成/图生视频/LTX 2.3-IA2V-国风 MV_2038201954467323905.json
name: LTX 2.3-IA2V-国风 MV_2038201954467323905.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX 2.3-IA2V-国风 MV_2038201954467323905.json
hash: 83e8ca587aa18ef5
coverage: 0.813953
learned_at: 2026-10-15 22:36:01
nodes: [RecordAudio, Reroute, VHS_VideoCombine, LTXVCropGuides, SamplerCustomAdvanced, RandomNoise, ManualSigmas, KSamplerSelect, LoadImage, PrimitiveInt, PrimitiveInt, PrimitiveInt, ComfyMathExpression, LTXVConcatAVLatent, SetLatentNoiseMask, SolidMask, ComfyMathExpression, LTXVAudioVAEDecode, LTXVConditioning, LTXVSeparateAVLatent, CFGGuider, VAEDecodeTiled, PrimitiveFloat, TrimAudioDuration, LoraLoaderModelOnly, UnetLoaderGGUF, LoadAudio, Anything Everywhere, DiffusionModelLoaderKJ, CLIPTextEncode, MarkdownNote, DualCLIPLoaderGGUF, ResizeImagesByLongerEdge, CLIPTextEncode, Anything Everywhere, LTXVAudioVAELoader, VAELoaderKJ, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVImgToVideoInplace, LTXVPreprocess, LTXVAudioVAEEncode, ResizeImageMaskNode]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX 2.3-IA2V-国风 MV_2038201954467323905.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2038201954467323905.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（43 个）：
- `RecordAudio`
- `Reroute`
- `VHS_VideoCombine`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `SolidMask`
- `ComfyMathExpression`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `PrimitiveFloat`
- `TrimAudioDuration`
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `LoadAudio`
- `Anything Everywhere`
- `DiffusionModelLoaderKJ`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `DualCLIPLoaderGGUF`
- `ResizeImagesByLongerEdge`
- `CLIPTextEncode` ★核心
- `Anything Everywhere`
- `LTXVAudioVAELoader`
- `VAELoaderKJ`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXVAudioVAEEncode` ★核心
- `ResizeImageMaskNode`

## 知识

覆盖率 **81%**（35/43）

**有卡**：`RecordAudio`、`VHS_VideoCombine`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`RandomNoise`、`ManualSigmas`、`KSamplerSelect`、`LoadImage`、`ComfyMathExpression`、`LTXVConcatAVLatent`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`CFGGuider`、`VAEDecodeTiled`、`TrimAudioDuration`、`LoraLoaderModelOnly`、`UnetLoaderGGUF`、`LoadAudio`、`DiffusionModelLoaderKJ`、`CLIPTextEncode`、`DualCLIPLoaderGGUF`、`ResizeImagesByLongerEdge`、`LTXVAudioVAELoader`、`VAELoaderKJ`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`LTXVAudioVAEEncode`、`ResizeImageMaskNode`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent
