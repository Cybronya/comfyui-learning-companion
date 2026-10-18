---
key: 视频生成/图生视频/LTX2.3 双图首尾帧参考_2035556594234167298.json
name: LTX2.3 双图首尾帧参考_2035556594234167298.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 双图首尾帧参考_2035556594234167298.json
hash: 8a5fb6293cdb5e3e
coverage: 0.466667
learned_at: 2026-10-15 22:35:48
nodes: [GetNode, SetNode, SamplerCustomAdvanced, SetNode, CFGGuider, GetNode, GetNode, GetNode, LTXVLatentUpsampler, CFGGuider, KSamplerSelect, SetNode, SetNode, ManualSigmas, GetNode, LTXVAudioVAEDecode, GetNode, easy cleanGpuUsed, LTXVConcatAVLatent, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVConditioning, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, LTX2_NAG, VAELoaderKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, UNETLoader, SetNode, VAELoaderKJ, SetNode, SetNode, Anything Everywhere, SetNode, LatentUpscaleModelLoader, GetNode, LTXVEmptyLatentAudio, GetNode, KSamplerSelect, RandomNoise, GetNode, PathchSageAttentionKJ, RandomNoise, LTXVImgToVideoInplace, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, Note, PrimitiveBoolean, GetNode, SetNode, SetNode, LTXVPreprocess, LTXVPreprocess, MathExpression|pysssss, MathExpression|pysssss, SetNode, SetNode, LTXVConcatAVLatent, SetNode, GetNode, Note, SetNode, PrimitiveInt, ComfyMathExpression, PrimitiveInt, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, VHS_VideoCombine, SetNode, CLIPTextEncode, PrimitiveInt, PrimitiveInt, LoadImage, LoadImage, ComfyMathExpression, EmptyLTXVLatentVideo, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, LTXVCropGuides, ShowText|pysssss, GetNode, GetNode, CR Text, RH_LLMAPI_Pro_Node, LTXVImgToVideoInplaceKJ, DualCLIPLoader, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 双图首尾帧参考_2035556594234167298.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2035556594234167298.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（105 个）：
- `GetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `ManualSigmas`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `easy cleanGpuUsed`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVConditioning`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LTX2_NAG`
- `VAELoaderKJ`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `UNETLoader` ★核心
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `Anything Everywhere`
- `SetNode`
- `LatentUpscaleModelLoader`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `GetNode`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `LTXVImgToVideoInplace`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `Note`
- `PrimitiveBoolean`
- `GetNode`
- `SetNode`
- `SetNode`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `SetNode`
- `GetNode`
- `Note`
- `SetNode`
- `PrimitiveInt`
- `ComfyMathExpression`
- `PrimitiveInt`
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `LoadImage`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `ShowText|pysssss`
- `GetNode`
- `GetNode`
- `CR Text`
- `RH_LLMAPI_Pro_Node`
- `LTXVImgToVideoInplaceKJ`
- `DualCLIPLoader`
- `PrimitiveInt`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **47%**（49/105）

**有卡**：`SamplerCustomAdvanced`、`CFGGuider`、`LTXVLatentUpsampler`、`KSamplerSelect`、`ManualSigmas`、`LTXVAudioVAEDecode`、`easy cleanGpuUsed`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVConditioning`、`LTX2_NAG`、`VAELoaderKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`UNETLoader`、`LatentUpscaleModelLoader`、`LTXVEmptyLatentAudio`、`RandomNoise`、`PathchSageAttentionKJ`、`LTXVImgToVideoInplace`、`CLIPTextEncode`、`PrimitiveBoolean`、`LTXVPreprocess`、`MathExpression|pysssss`、`ComfyMathExpression`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`LoadImage`、`EmptyLTXVLatentVideo`、`LTXVCropGuides`、`CR Text`、`RH_LLMAPI_Pro_Node`、`LTXVImgToVideoInplaceKJ`、`DualCLIPLoader`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
