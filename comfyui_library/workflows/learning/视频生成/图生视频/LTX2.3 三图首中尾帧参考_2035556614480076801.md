---
key: 视频生成/图生视频/LTX2.3 三图首中尾帧参考_2035556614480076801.json
name: LTX2.3 三图首中尾帧参考_2035556614480076801.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 三图首中尾帧参考_2035556614480076801.json
hash: bdfbbf59edba69c6
coverage: 0.46087
learned_at: 2026-10-15 22:35:49
nodes: [GetNode, SetNode, SamplerCustomAdvanced, SetNode, CFGGuider, GetNode, GetNode, GetNode, LTXVLatentUpsampler, CFGGuider, KSamplerSelect, SetNode, SetNode, ManualSigmas, GetNode, LTXVAudioVAEDecode, GetNode, easy cleanGpuUsed, LTXVConcatAVLatent, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVConditioning, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, PrimitiveInt, PrimitiveInt, LTX2_NAG, VAELoaderKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, UNETLoader, SetNode, VAELoaderKJ, SetNode, SetNode, Anything Everywhere, SetNode, LatentUpscaleModelLoader, GetNode, LTXVEmptyLatentAudio, GetNode, KSamplerSelect, RandomNoise, GetNode, PathchSageAttentionKJ, RandomNoise, LTXVImgToVideoInplace, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, Note, PrimitiveBoolean, GetNode, SetNode, SetNode, LTXVPreprocess, LTXVPreprocess, LTXVPreprocess, MathExpression|pysssss, MathExpression|pysssss, SetNode, SetNode, SetNode, LTXVConcatAVLatent, SetNode, EmptyLTXVLatentVideo, GetNode, GetNode, Note, SetNode, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, PrimitiveInt, SetNode, GetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, LoadImage, ComfyMathExpression, VHS_VideoCombine, LoadImage, LoadImage, SetNode, Note, CLIPTextEncode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, LTXVCropGuides, GetNode, GetNode, GetNode, RH_LLMAPI_Pro_Node, GetNode, LTXVImgToVideoInplaceKJ, CR Text, DualCLIPLoader, PrimitiveInt, ShowText|pysssss]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 三图首中尾帧参考_2035556614480076801.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2035556614480076801.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（115 个）：
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
- `PrimitiveInt`
- `PrimitiveInt`
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
- `LTXVPreprocess`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `Note`
- `SetNode`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PrimitiveInt`
- `SetNode`
- `GetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `LoadImage`
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `Note`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `GetNode`
- `RH_LLMAPI_Pro_Node`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `CR Text`
- `DualCLIPLoader`
- `PrimitiveInt`
- `ShowText|pysssss`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **46%**（53/115）

**有卡**：`SamplerCustomAdvanced`、`CFGGuider`、`LTXVLatentUpsampler`、`KSamplerSelect`、`ManualSigmas`、`LTXVAudioVAEDecode`、`easy cleanGpuUsed`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVConditioning`、`LTX2_NAG`、`VAELoaderKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`UNETLoader`、`LatentUpscaleModelLoader`、`LTXVEmptyLatentAudio`、`RandomNoise`、`PathchSageAttentionKJ`、`LTXVImgToVideoInplace`、`CLIPTextEncode`、`PrimitiveBoolean`、`LTXVPreprocess`、`MathExpression|pysssss`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`VHS_VideoCombine`、`LTXVCropGuides`、`RH_LLMAPI_Pro_Node`、`LTXVImgToVideoInplaceKJ`、`CR Text`、`DualCLIPLoader`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
