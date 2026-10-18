---
key: 视频生成/图生视频/ltx2.3数字人-图生视频_2033035717600878594.json
name: ltx2.3数字人-图生视频_2033035717600878594.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/ltx2.3数字人-图生视频_2033035717600878594.json
hash: 17f8c792d82666ac
coverage: 0.956522
learned_at: 2026-10-15 22:35:37
nodes: [RandomNoise, AudioCropProcessUTK, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, EmptyLTXVLatentVideo, LTXVConditioning, TrimAudioDuration, VAEDecode, LayerUtility: PurgeVRAM V2, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, LTXVPreprocess, LoraLoaderModelOnly, KSamplerSelect, CheckpointLoaderSimple, ImageSharpen, LayerFilter: GaussianBlur, DualCLIPLoader, MathExpression|pysssss, CR Text, ManualSigmas, CR Text Concatenate, VHS_VideoCombine, PrimitiveFloat, easy float, easy float, LTXVAudioVAEEncode, SolidMask, SetLatentNoiseMask, VAELoaderKJ, CLIPTextEncode, CFGGuider, SamplerCustomAdvanced, LTXVImgToVideoInplace, PreviewAny, VAELoaderKJ, LTXVChunkFeedForward, PathchSageAttentionKJ, CLIPTextEncode, RH_LLMAPI_NODE, RH_LLMAPI_Pro_Node, LTXVConcatAVLatent, CR Text, LoadAudio]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 视频生成/图生视频/ltx2.3数字人-图生视频_2033035717600878594.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2033035717600878594.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（46 个）：
- `RandomNoise`
- `AudioCropProcessUTK`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `TrimAudioDuration`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `ModelPatchTorchSettings`
- `LTXVPreprocess`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `CheckpointLoaderSimple` ★核心
- `ImageSharpen`
- `LayerFilter: GaussianBlur`
- `DualCLIPLoader`
- `MathExpression|pysssss`
- `CR Text`
- `ManualSigmas`
- `CR Text Concatenate`
- `VHS_VideoCombine`
- `PrimitiveFloat`
- `easy float`
- `easy float`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `SetLatentNoiseMask`
- `VAELoaderKJ`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplace`
- `PreviewAny`
- `VAELoaderKJ`
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_Pro_Node`
- `LTXVConcatAVLatent`
- `CR Text`
- `LoadAudio`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **96%**（44/46）

**有卡**：`RandomNoise`、`AudioCropProcessUTK`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`TrimAudioDuration`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`LTXVSeparateAVLatent`、`LoadImage`、`LoraLoaderModelOnly`、`ModelPatchTorchSettings`、`LTXVPreprocess`、`KSamplerSelect`、`CheckpointLoaderSimple`、`ImageSharpen`、`LayerFilter: GaussianBlur`、`DualCLIPLoader`、`MathExpression|pysssss`、`CR Text`、`ManualSigmas`、`CR Text Concatenate`、`VHS_VideoCombine`、`easy float`、`LTXVAudioVAEEncode`、`SolidMask`、`SetLatentNoiseMask`、`VAELoaderKJ`、`CLIPTextEncode`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`RH_LLMAPI_NODE`、`RH_LLMAPI_Pro_Node`、`LTXVConcatAVLatent`、`LoadAudio`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
