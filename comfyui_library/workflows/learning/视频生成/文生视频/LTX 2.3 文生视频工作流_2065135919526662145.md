---
key: 视频生成/文生视频/LTX 2.3 文生视频工作流_2065135919526662145.json
name: LTX 2.3 文生视频工作流_2065135919526662145
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.3 文生视频工作流_2065135919526662145.json
hash: 222d27eb45d401e4
coverage: 0.5
learned_at: 2026-10-11 20:21:24
nodes: [LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVConcatAVLatent, ResizeImagesByLongerEdge, EmptyLTXVLatentVideo, LTXVConcatAVLatent, LTXVEmptyLatentAudio, SimpleCalculatorKJ, LTXVImgToVideoInplace, LTXVLatentUpsampler, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, VAEDecodeTiled, GetNode, GetNode, SetNode, SetNode, SetNode, LTXVPreprocess, SetNode, SetNode, SetNode, SetNode, SamplerCustom, SamplerCustom, SetNode, PrimitiveFloat, GetImageSize, ImageResizeKJv2, JDC_ResizeFactor, SetNode, SetNode, SetNode, LTXVScheduler, ManualSigmas, KSamplerSelect, KSamplerSelect, LTXVAudioVAEDecode, GetNode, VHS_VideoCombine, Seed (rgthree), VAELoaderKJ, VAELoader, DualCLIPLoader, SetNode, GetNode, GetNode, SetNode, LatentUpscaleModelLoader, SetNode, LTXVScheduler, PathchSageAttentionKJ, SetNode, SetNode, GetNode, SetNode, GetNode, LTXVChunkFeedForward, LoraLoaderModelOnly, LTX2SamplingPreviewOverride, GetNode, VHS_VideoCombine, FlashVSRInitPipe, FlashVSRNodeAdv, LTX2SamplingPreviewOverride, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, INTConstant, INTConstant, INTConstant, SimpleCalculatorKJ, SetNode, PrimitiveBoolean, CLIPTextEncode, CLIPTextEncode, LTX2_NAG, GetNode, ManualSigmas, GetNode, GetNode, LoadImage, SetNode, CR Text, GetNode, LTXVConditioning, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode]
patterns: []
missing: [CR Text, Seed (rgthree)]
parameters: {"batch_size": 1, "height": 24, "width": 121}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
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

覆盖率 **50%**（57/114）

**有卡**：`LTXVImgToVideoInplace`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`ResizeImagesByLongerEdge`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`SimpleCalculatorKJ`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVPreprocess`、`SamplerCustom`、`GetImageSize`、`ImageResizeKJv2`、`JDC_ResizeFactor`、`LTXVScheduler`、`ManualSigmas`、`KSamplerSelect`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`VAELoaderKJ`、`VAELoader`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`LoraLoaderModelOnly`、`LTX2SamplingPreviewOverride`、`FlashVSRInitPipe`、`FlashVSRNodeAdv`、`UNETLoader`、`INTConstant`、`PrimitiveBoolean`、`CLIPTextEncode`、`LTX2_NAG`、`LoadImage`、`LTXVConditioning`

**缺卡**（2）：`CR Text`、`Seed (rgthree)`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVLatentUpsampler

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
