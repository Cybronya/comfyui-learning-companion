---
key: 视频生成/图生视频/LTX2.3数字人对口型-16比9多机位成片版_2115832422628683777.json
name: LTX2.3数字人对口型-16比9多机位成片版_2115832422628683777
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3数字人对口型-16比9多机位成片版_2115832422628683777.json
hash: d6c9e247828db1f1
coverage: 0.832536
learned_at: 2026-10-30 17:57:37
nodes: [KSamplerSelect, LTXVConditioning, GetNode, PathchSageAttentionKJ, GetNode, LoadImage, LTX2SamplingPreviewOverride, LTX2_NAG, SetNode, SetNode, RandomNoise, BasicScheduler, ModelSamplingSD3, LTX2AttentionTunerPatch, INTConstant, SetNode, GetNode, SetNode, SetNode, SetNode, VAELoader, DualCLIPLoader, VAELoaderKJ, SetNode, VAELoader, UNETLoader, SetNode, SetNode, SetNode, PrimitiveFloat, GetNode, GetNode, GetNode, SolidMask, INTConstant, CLIPTextEncode, GetNode, PrimitiveStringMultiline, CLIPTextEncode, GetNode, GetNode, GetNode, PrimitiveFloat, SetNode, GetNode, ImageResizeKJv2, VHS_VideoCombine, JoinStrings, PrimitiveStringMultiline, VHS_LoadAudioUpload, INTConstant, LoadImage, LoadImage, ImageBatch, ImageBatch, ImageResizeKJv2, LTXVPreprocess, TrimAudioDuration, LTXVAudioVAEEncode, SetLatentNoiseMask, EmptyLTXVLatentVideo, ImageFromBatch, LTXVImgToVideoInplaceKJ, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecode, ImageFromBatch, PrimitiveStringMultiline, JoinStrings, CLIPTextEncode, LTXVConditioning, CFGGuider, TrimAudioDuration, LTXVAudioVAEEncode, SetLatentNoiseMask, EmptyLTXVLatentVideo, ImageFromBatch, LTXVImgToVideoInplaceKJ, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecode, ImageFromBatch, PrimitiveStringMultiline, JoinStrings, CLIPTextEncode, LTXVConditioning, CFGGuider, TrimAudioDuration, LTXVAudioVAEEncode, SetLatentNoiseMask, EmptyLTXVLatentVideo, ImageFromBatch, LTXVImgToVideoInplaceKJ, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecode, ImageFromBatch, PrimitiveStringMultiline, JoinStrings, CLIPTextEncode, LTXVConditioning, CFGGuider, TrimAudioDuration, LTXVAudioVAEEncode, SetLatentNoiseMask, EmptyLTXVLatentVideo, ImageFromBatch, LTXVImgToVideoInplaceKJ, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecode, ImageFromBatch, PrimitiveStringMultiline, JoinStrings, CLIPTextEncode, LTXVConditioning, CFGGuider, TrimAudioDuration, LTXVAudioVAEEncode, SetLatentNoiseMask, EmptyLTXVLatentVideo, ImageFromBatch, LTXVImgToVideoInplaceKJ, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecode, ImageFromBatch, PrimitiveStringMultiline, JoinStrings, CLIPTextEncode, LTXVConditioning, CFGGuider, TrimAudioDuration, LTXVAudioVAEEncode, SetLatentNoiseMask, EmptyLTXVLatentVideo, ImageFromBatch, LTXVImgToVideoInplaceKJ, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecode, ImageFromBatch, PrimitiveStringMultiline, JoinStrings, CLIPTextEncode, LTXVConditioning, CFGGuider, TrimAudioDuration, LTXVAudioVAEEncode, SetLatentNoiseMask, EmptyLTXVLatentVideo, ImageFromBatch, LTXVImgToVideoInplaceKJ, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecode, ImageFromBatch, PrimitiveStringMultiline, JoinStrings, CLIPTextEncode, LTXVConditioning, CFGGuider, TrimAudioDuration, LTXVAudioVAEEncode, SetLatentNoiseMask, EmptyLTXVLatentVideo, ImageFromBatch, LTXVImgToVideoInplaceKJ, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecode, ImageFromBatch, PrimitiveStringMultiline, JoinStrings, CLIPTextEncode, LTXVConditioning, CFGGuider, TrimAudioDuration, LTXVAudioVAEEncode, SetLatentNoiseMask, EmptyLTXVLatentVideo, ImageFromBatch, LTXVImgToVideoInplaceKJ, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecode, ImageFromBatch, PrimitiveStringMultiline, JoinStrings, CLIPTextEncode, LTXVConditioning, CFGGuider, ImageBatch, ImageBatch, ImageBatch, ImageBatch, ImageBatch, ImageBatch, ImageBatch, ImageBatch]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3数字人对口型-16比9多机位成片版_2115832422628683777.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3数字人对口型-16比9多机位成片版_2115832422628683777.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（209 个）：
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `GetNode`
- `PathchSageAttentionKJ`
- `GetNode`
- `LoadImage`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `SetNode`
- `SetNode`
- `RandomNoise`
- `BasicScheduler`
- `ModelSamplingSD3`
- `LTX2AttentionTunerPatch`
- `INTConstant`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `SetNode`
- `VAELoader`
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `GetNode`
- `GetNode`
- `GetNode`
- `SolidMask`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `GetNode`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveFloat`
- `SetNode`
- `GetNode`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `JoinStrings`
- `PrimitiveStringMultiline`
- `VHS_LoadAudioUpload`
- `INTConstant`
- `LoadImage`
- `LoadImage`
- `ImageBatch`
- `ImageBatch`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `TrimAudioDuration`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `EmptyLTXVLatentVideo`
- `ImageFromBatch`
- `LTXVImgToVideoInplaceKJ`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `PrimitiveStringMultiline`
- `JoinStrings`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CFGGuider`
- `TrimAudioDuration`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `EmptyLTXVLatentVideo`
- `ImageFromBatch`
- `LTXVImgToVideoInplaceKJ`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `PrimitiveStringMultiline`
- `JoinStrings`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CFGGuider`
- `TrimAudioDuration`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `EmptyLTXVLatentVideo`
- `ImageFromBatch`
- `LTXVImgToVideoInplaceKJ`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `PrimitiveStringMultiline`
- `JoinStrings`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CFGGuider`
- `TrimAudioDuration`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `EmptyLTXVLatentVideo`
- `ImageFromBatch`
- `LTXVImgToVideoInplaceKJ`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `PrimitiveStringMultiline`
- `JoinStrings`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CFGGuider`
- `TrimAudioDuration`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `EmptyLTXVLatentVideo`
- `ImageFromBatch`
- `LTXVImgToVideoInplaceKJ`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `PrimitiveStringMultiline`
- `JoinStrings`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CFGGuider`
- `TrimAudioDuration`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `EmptyLTXVLatentVideo`
- `ImageFromBatch`
- `LTXVImgToVideoInplaceKJ`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `PrimitiveStringMultiline`
- `JoinStrings`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CFGGuider`
- `TrimAudioDuration`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `EmptyLTXVLatentVideo`
- `ImageFromBatch`
- `LTXVImgToVideoInplaceKJ`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `PrimitiveStringMultiline`
- `JoinStrings`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CFGGuider`
- `TrimAudioDuration`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `EmptyLTXVLatentVideo`
- `ImageFromBatch`
- `LTXVImgToVideoInplaceKJ`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `PrimitiveStringMultiline`
- `JoinStrings`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CFGGuider`
- `TrimAudioDuration`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `EmptyLTXVLatentVideo`
- `ImageFromBatch`
- `LTXVImgToVideoInplaceKJ`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `ImageFromBatch`
- `PrimitiveStringMultiline`
- `JoinStrings`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CFGGuider`
- `ImageBatch`
- `ImageBatch`
- `ImageBatch`
- `ImageBatch`
- `ImageBatch`
- `ImageBatch`
- `ImageBatch`
- `ImageBatch`

## 知识

覆盖率 **83%**（174/209）

**有卡**：`KSamplerSelect`、`LTXVConditioning`、`PathchSageAttentionKJ`、`LoadImage`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`RandomNoise`、`BasicScheduler`、`ModelSamplingSD3`、`LTX2AttentionTunerPatch`、`INTConstant`、`VAELoader`、`DualCLIPLoader`、`VAELoaderKJ`、`UNETLoader`、`SolidMask`、`CLIPTextEncode`、`ImageResizeKJv2`、`VHS_VideoCombine`、`JoinStrings`、`VHS_LoadAudioUpload`、`ImageBatch`、`LTXVPreprocess`、`TrimAudioDuration`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`EmptyLTXVLatentVideo`、`ImageFromBatch`、`LTXVImgToVideoInplaceKJ`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`VAEDecode`、`CFGGuider`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
