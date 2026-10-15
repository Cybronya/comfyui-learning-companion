---
key: 视频生成/文生视频/LTX 2.3 文生视频工作流_2065135919526662145.json
name: LTX 2.3 文生视频工作流_2065135919526662145
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.3 文生视频工作流_2065135919526662145.json
hash: 222d27eb45d401e4
coverage: 0.517544
learned_at: 2026-10-15 22:44:33
nodes: [LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVConcatAVLatent, ResizeImagesByLongerEdge, EmptyLTXVLatentVideo, LTXVConcatAVLatent, LTXVEmptyLatentAudio, SimpleCalculatorKJ, LTXVImgToVideoInplace, LTXVLatentUpsampler, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, VAEDecodeTiled, GetNode, GetNode, SetNode, SetNode, SetNode, LTXVPreprocess, SetNode, SetNode, SetNode, SetNode, SamplerCustom, SamplerCustom, SetNode, PrimitiveFloat, GetImageSize, ImageResizeKJv2, JDC_ResizeFactor, SetNode, SetNode, SetNode, LTXVScheduler, ManualSigmas, KSamplerSelect, KSamplerSelect, LTXVAudioVAEDecode, GetNode, VHS_VideoCombine, Seed (rgthree), VAELoaderKJ, VAELoader, DualCLIPLoader, SetNode, GetNode, GetNode, SetNode, LatentUpscaleModelLoader, SetNode, LTXVScheduler, PathchSageAttentionKJ, SetNode, SetNode, GetNode, SetNode, GetNode, LTXVChunkFeedForward, LoraLoaderModelOnly, LTX2SamplingPreviewOverride, GetNode, VHS_VideoCombine, FlashVSRInitPipe, FlashVSRNodeAdv, LTX2SamplingPreviewOverride, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, INTConstant, INTConstant, INTConstant, SimpleCalculatorKJ, SetNode, PrimitiveBoolean, CLIPTextEncode, CLIPTextEncode, LTX2_NAG, GetNode, ManualSigmas, GetNode, GetNode, LoadImage, SetNode, CR Text, GetNode, LTXVConditioning, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 121}
---

# 视频生成/文生视频/LTX 2.3 文生视频工作流_2065135919526662145.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.3 文生视频工作流_2065135919526662145.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（114 个）：
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `ResizeImagesByLongerEdge`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `SimpleCalculatorKJ`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVPreprocess`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SamplerCustom` ★核心
- `SamplerCustom` ★核心
- `SetNode`
- `PrimitiveFloat`
- `GetImageSize`
- `ImageResizeKJv2`
- `JDC_ResizeFactor`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVScheduler`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `Seed (rgthree)`
- `VAELoaderKJ`
- `VAELoader`
- `DualCLIPLoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `LTXVScheduler`
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVChunkFeedForward`
- `LoraLoaderModelOnly` ★核心
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `VHS_VideoCombine`
- `FlashVSRInitPipe`
- `FlashVSRNodeAdv`
- `LTX2SamplingPreviewOverride`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `SimpleCalculatorKJ`
- `SetNode`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `GetNode`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `LoadImage`
- `SetNode`
- `CR Text`
- `GetNode`
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **52%**（59/114）

**有卡**：`LTXVImgToVideoInplace`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`ResizeImagesByLongerEdge`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`SimpleCalculatorKJ`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVPreprocess`、`SamplerCustom`、`GetImageSize`、`ImageResizeKJv2`、`JDC_ResizeFactor`、`LTXVScheduler`、`ManualSigmas`、`KSamplerSelect`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`Seed (rgthree)`、`VAELoaderKJ`、`VAELoader`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`LoraLoaderModelOnly`、`LTX2SamplingPreviewOverride`、`FlashVSRInitPipe`、`FlashVSRNodeAdv`、`UNETLoader`、`INTConstant`、`PrimitiveBoolean`、`CLIPTextEncode`、`LTX2_NAG`、`LoadImage`、`CR Text`、`LTXVConditioning`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVLatentUpsampler
