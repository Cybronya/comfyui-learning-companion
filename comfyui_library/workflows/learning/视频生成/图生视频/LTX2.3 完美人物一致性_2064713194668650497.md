---
key: 视频生成/图生视频/LTX2.3 完美人物一致性_2064713194668650497.json
name: LTX2.3 完美人物一致性_2064713194668650497.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2064713194668650497.json
hash: e92a792b2205e888
coverage: 0.892857
learned_at: 2026-10-15 22:39:29
nodes: [LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, RandomNoise, Reroute, ResizeImagesByLongerEdge, LTXVChunkFeedForward, ModelPatchTorchSettings, ComfyMathExpression, RandomNoise, CFGGuider, LTXVSeparateAVLatent, LTXVCropGuides, ComfyMathExpression, LTXVAudioVAEDecode, LTXVLatentUpsampler, LatentUpscaleModelLoader, LTXVImgToVideoInplace, ManualSigmas, LTXVConditioning, LTXVPreprocess, CFGGuider, SamplerCustomAdvanced, ManualSigmas, KSamplerSelect, KSamplerSelect, LatentUpscaleModelLoader, LTXVImgToVideoInplace, LTXVConcatAVLatent, PathchSageAttentionKJ, PrimitiveInt, PrimitiveInt, ComfyMathExpression, LayerUtility: PurgeVRAM, VAEDecodeTiled, LTXVLatentUpsampler, VHS_VideoCombine, LTXVConcatAVLatent, LTXVSeparateAVLatent, CLIPTextEncode, LTXTiledSampler, ManualSigmas, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, DualCLIPLoader, VAELoaderKJ, LTX2_NAG, UNETLoader, VAELoaderKJ, LoraLoaderModelOnly, LoadImage, ComfyMathExpression, PrimitiveInt, PrimitiveInt, ComfyMathExpression, PromptRelayEncode, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 44, "width": 97}
---

# 视频生成/图生视频/LTX2.3 完美人物一致性_2064713194668650497.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064713194668650497.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（56 个）：
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `RandomNoise`
- `Reroute`
- `ResizeImagesByLongerEdge`
- `LTXVChunkFeedForward`
- `ModelPatchTorchSettings`
- `ComfyMathExpression`
- `RandomNoise`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `ComfyMathExpression`
- `LTXVAudioVAEDecode` ★核心
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `LTXVImgToVideoInplace`
- `ManualSigmas`
- `LTXVConditioning`
- `LTXVPreprocess`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `LatentUpscaleModelLoader`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `LayerUtility: PurgeVRAM`
- `VAEDecodeTiled` ★核心
- `LTXVLatentUpsampler` ★核心
- `VHS_VideoCombine`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `LTXTiledSampler` ★核心
- `ManualSigmas`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VAELoaderKJ`
- `LTX2_NAG`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `ComfyMathExpression`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `PromptRelayEncode`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `44`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（50/56）

**有卡**：`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`RandomNoise`、`ResizeImagesByLongerEdge`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`ComfyMathExpression`、`CFGGuider`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`LTXVImgToVideoInplace`、`ManualSigmas`、`LTXVConditioning`、`LTXVPreprocess`、`SamplerCustomAdvanced`、`KSamplerSelect`、`LTXVConcatAVLatent`、`PathchSageAttentionKJ`、`LayerUtility: PurgeVRAM`、`VAEDecodeTiled`、`VHS_VideoCombine`、`CLIPTextEncode`、`LTXTiledSampler`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`VAELoaderKJ`、`LTX2_NAG`、`UNETLoader`、`LoadImage`、`PromptRelayEncode`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
