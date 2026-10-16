---
key: 视频生成/图生视频/ltx2.3视频延长进阶版relayPrompt+高清优化_2050097870233190402.json
name: ltx2.3视频延长进阶版relayPrompt+高清优化_2050097870233190402.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2050097870233190402.json
hash: da2ceec21c5ed224
coverage: 0.904762
learned_at: 2026-10-15 22:37:17
nodes: [CFGGuider, KSamplerSelect, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, PrimitiveFloat, KSamplerSelect, RandomNoise, ManualSigmas, ManualSigmas, Float, UNETLoader, RandomNoise, LTXVConditioning, LTXVAudioVAEEncode, LoraLoaderModelOnly, LTXVConcatAVLatent, PathchSageAttentionKJ, PreviewAny, PrimitiveInt, LoraLoaderModelOnly, SimpleCalculatorKJ, MarkdownNote, ImageScaleBy, LatentUpscaleModelLoader, CLIPTextEncode, LTXVConcatAVLatent, LTXVAudioVAEDecode, LTXVSeparateAVLatent, LTXVImgToVideoInplace, CFGGuider, ResizeImagesByLongerEdge, EmptyLTXVLatentVideo, LTXVAudioVideoMask, Get resolution [Crystools], LTXVImgToVideoInplace, SamplerCustomAdvanced, ResizeImagesByLongerEdge, LTXVPreprocess, VHS_VideoCombine, LTXVAudioVAEDecode, LTXVSeparateAVLatent, VAEDecodeTiled, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVLatentUpsampler, ImageScaleBy, SamplerCustomAdvanced, Get resolution [Crystools], VHS_VideoInfo, VHS_VideoCombine, SeedVR2ExtraArgs, SeedVR2, VAEDecodeTiled, SeedVR2BlockSwap, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, VHS_LoadVideo, Int, VHS_VideoCombine, PromptRelayEncodeTimeline, MarkdownNote, PrimitiveFloat]
patterns: []
missing: []
---

# 视频生成/图生视频/ltx2.3视频延长进阶版relayPrompt+高清优化_2050097870233190402.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2050097870233190402.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（63 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `PrimitiveFloat`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `ManualSigmas`
- `ManualSigmas`
- `Float`
- `UNETLoader` ★核心
- `RandomNoise`
- `LTXVConditioning`
- `LTXVAudioVAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVConcatAVLatent`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `SimpleCalculatorKJ`
- `MarkdownNote`
- `ImageScaleBy`
- `LatentUpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `ResizeImagesByLongerEdge`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVideoMask`
- `Get resolution [Crystools]`
- `LTXVImgToVideoInplace`
- `SamplerCustomAdvanced` ★核心
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `VHS_VideoCombine`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `ImageScaleBy`
- `SamplerCustomAdvanced` ★核心
- `Get resolution [Crystools]`
- `VHS_VideoInfo`
- `VHS_VideoCombine`
- `SeedVR2ExtraArgs`
- `SeedVR2`
- `VAEDecodeTiled` ★核心
- `SeedVR2BlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_LoadVideo`
- `Int`
- `VHS_VideoCombine`
- `PromptRelayEncodeTimeline`
- `MarkdownNote`
- `PrimitiveFloat`

## 知识

覆盖率 **90%**（57/63）

**有卡**：`CFGGuider`、`KSamplerSelect`、`DualCLIPLoader`、`VAELoaderKJ`、`RandomNoise`、`ManualSigmas`、`Float`、`UNETLoader`、`LTXVConditioning`、`LTXVAudioVAEEncode`、`LoraLoaderModelOnly`、`LTXVConcatAVLatent`、`PathchSageAttentionKJ`、`SimpleCalculatorKJ`、`ImageScaleBy`、`LatentUpscaleModelLoader`、`CLIPTextEncode`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`LTXVImgToVideoInplace`、`ResizeImagesByLongerEdge`、`EmptyLTXVLatentVideo`、`LTXVAudioVideoMask`、`Get resolution [Crystools]`、`SamplerCustomAdvanced`、`LTXVPreprocess`、`VHS_VideoCombine`、`VAEDecodeTiled`、`LTXVLatentUpsampler`、`VHS_VideoInfo`、`SeedVR2ExtraArgs`、`SeedVR2`、`SeedVR2BlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_LoadVideo`、`Int`、`PromptRelayEncodeTimeline`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、SeedVR2
