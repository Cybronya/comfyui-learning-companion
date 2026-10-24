---
key: 图片生成/图生图/图生长视频Ltx2.3+细化多镜头长时间+KJ版+图生视频时间分段剪辑++逻辑控制+自动计算帧数_2069651466062745602.json
name: 图生长视频Ltx2.3+细化多镜头长时间+KJ版+图生视频时间分段剪辑++逻辑控制+自动计算帧数_2069651466062745602
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图生长视频Ltx2.3+细化多镜头长时间+KJ版+图生视频时间分段剪辑++逻辑控制+自动计算帧数_2069651466062745602.json
hash: fe199ef2f2a8112c
coverage: 0.791667
learned_at: 2026-10-23 12:44:11
nodes: [LTXVAudioVAEDecode, SetNode, GetNode, LTX2SamplingPreviewOverride, LTXVSeparateAVLatent, VAEDecode, LTXVConcatAVLatent, KSamplerSelect, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, SetNode, PreviewImage, EmptyLTXVLatentVideo, LayerUtility: ImageScaleByAspectRatio V2, PromptRelayEncode, UNETLoader, PathchSageAttentionKJ, LTXVConditioning, SamplerCustom, LoraLoaderModelOnly, GetNode, VisualizeSigmasKJ, LTXVEmptyLatentAudio, GetNode, BasicScheduler, GetNode, LTXVImgToVideoInplaceKJ, ConditioningZeroOut, LTXVPreprocess, VHS_VideoCombine, ShowText|pysssss, ShowText|pysssss, ShowText|pysssss, CM_IntBinaryOperation, JWInteger, CM_IntBinaryOperation, LoadImage, CR Prompt Text, CR Prompt Text, llama_cpp_model_loader, llama_cpp_parameters, SomethingToString, llama_cpp_instruct_adv, JWStringConcat, easy cleanGpuUsed, SomethingToString, JWStringSplit]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 图片生成/图生图/图生长视频Ltx2.3+细化多镜头长时间+KJ版+图生视频时间分段剪辑++逻辑控制+自动计算帧数_2069651466062745602.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图生长视频Ltx2.3+细化多镜头长时间+KJ版+图生视频时间分段剪辑++逻辑控制+自动计算帧数_2069651466062745602.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `SetNode`
- `PreviewImage`
- `EmptyLTXVLatentVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PromptRelayEncode`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LTXVConditioning`
- `SamplerCustom` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `VisualizeSigmasKJ`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `BasicScheduler`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `ConditioningZeroOut`
- `LTXVPreprocess`
- `VHS_VideoCombine`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `CM_IntBinaryOperation`
- `JWInteger`
- `CM_IntBinaryOperation`
- `LoadImage`
- `CR Prompt Text`
- `CR Prompt Text`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `SomethingToString`
- `llama_cpp_instruct_adv`
- `JWStringConcat`
- `easy cleanGpuUsed`
- `SomethingToString`
- `JWStringSplit`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（38/48）

**有卡**：`LTXVAudioVAEDecode`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVConcatAVLatent`、`KSamplerSelect`、`VAELoaderKJ`、`DualCLIPLoader`、`EmptyLTXVLatentVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`PromptRelayEncode`、`UNETLoader`、`PathchSageAttentionKJ`、`LTXVConditioning`、`SamplerCustom`、`LoraLoaderModelOnly`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`BasicScheduler`、`LTXVImgToVideoInplaceKJ`、`ConditioningZeroOut`、`LTXVPreprocess`、`VHS_VideoCombine`、`CM_IntBinaryOperation`、`JWInteger`、`LoadImage`、`CR Prompt Text`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`SomethingToString`、`llama_cpp_instruct_adv`、`JWStringConcat`、`easy cleanGpuUsed`、`JWStringSplit`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
