---
name: unknown_workflow_video_lora_sampler_669
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.840667
common_nodes: [AdjustAudio, Any To Any, Audio Add Silence, AudioAdjustVolume, AudioCombine, AudioEncoderEncode, AudioEncoderLoader, BatchImagesNode, BerniniConditioning, BerniniPromptEnhancer, CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, CreateVideo, DF_Get_image_size, Float, GetVideoComponents, HunyuanVideoFoley, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchLoader, PainterAV2V, PainterAudioCut, PathchSageAttentionKJ, Qwen3_VQA, RHLLMChatNode, RunningHub_VoxCPM_Generate, RunningHub_VoxCPM_LoadModel, StringReplace, Text, UNETLoader, VAEDecode, VAELoader, VHS_SelectFilename, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2073819389966766081.json, 视频生成/图生视频/2073466408666746882.json, 视频生成/图生视频/2064697979495342081.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_669

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2073819389966766081.json、视频生成/图生视频/2073466408666746882.json、视频生成/图生视频/2064697979495342081.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `AdjustAudio`
- `Any To Any`
- `Audio Add Silence`
- `AudioAdjustVolume`
- `AudioCombine`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `BatchImagesNode`
- `BerniniConditioning`
- `BerniniPromptEnhancer`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `CreateVideo`
- `DF_Get_image_size`
- `Float`
- `GetVideoComponents`
- `HunyuanVideoFoley`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchLoader`
- `PainterAV2V`
- `PainterAudioCut`
- `PathchSageAttentionKJ`
- `Qwen3_VQA`
- `RHLLMChatNode`
- `RunningHub_VoxCPM_Generate`
- `RunningHub_VoxCPM_LoadModel`
- `StringReplace`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ACE_AudioCrop` —— 2/3 个有
- `EmptyAudio` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `SaveAudio` —— 2/3 个有
- `SaveVideo` —— 2/3 个有
- `AudioCrop` —— 1/3 个有
- `Bjornulf_ShowInt` —— 1/3 个有
- `DF_Int_to_Float` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `Int` —— 1/3 个有
- `Int to String` —— 1/3 个有
- `PreviewAudio` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `ResolutionStdSelector` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `easy imageRemBg` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 4 | 3 | 86% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | dpmpp_sde | - | 3 | 67% |
| 重绘幅度 | normal | - | 3 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 4，3 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_sde，3 个样本，一致性 67%
- 重绘幅度 最常用 normal，3 个样本，一致性 67%
