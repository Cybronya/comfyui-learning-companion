---
name: unknown_workflow_video_lora_sampler_469
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.85875
common_nodes: [ACE_AudioCrop, AdjustAudio, Any To Any, Audio Add Silence, AudioCombine, AudioEncoderEncode, AudioEncoderLoader, BerniniConditioning, BerniniPromptEnhancer, CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, CreateVideo, DF_Get_image_size, Float, GetVideoComponents, HunyuanVideoFoley, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchLoader, PainterAV2V, PainterAudioCut, PathchSageAttentionKJ, Qwen3_VQA, RunningHub_VoxCPM_Generate, RunningHub_VoxCPM_LoadModel, SaveVideo, StringReplace, UNETLoader, VAEDecode, VAELoader, VHS_SelectFilename, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2073466718235746306.json, 视频生成/图生视频/2065355953679196162.json, 视频生成/图生视频/2065634636939751425.json, 视频生成/图生视频/2064382860404019201.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_469

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2073466718235746306.json、视频生成/图生视频/2065355953679196162.json、视频生成/图生视频/2065634636939751425.json、视频生成/图生视频/2064382860404019201.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `ACE_AudioCrop`
- `AdjustAudio`
- `Any To Any`
- `Audio Add Silence`
- `AudioCombine`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
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
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchLoader`
- `PainterAV2V`
- `PainterAudioCut`
- `PathchSageAttentionKJ`
- `Qwen3_VQA`
- `RunningHub_VoxCPM_Generate`
- `RunningHub_VoxCPM_LoadModel`
- `SaveVideo`
- `StringReplace`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RHLLMChatNode` —— 3/4 个有
- `AudioAdjustVolume` —— 2/4 个有
- `CR Text` —— 2/4 个有
- `EmptyAudio` —— 2/4 个有
- `ImageFromBatch` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `JWInteger` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `SaveAudio` —— 2/4 个有
- `SimpleMath+` —— 2/4 个有
- `easy batchAnything` —— 2/4 个有
- `easy forLoopEnd` —— 2/4 个有
- `easy forLoopStart` —— 2/4 个有
- `easy imagesSplitImage` —— 2/4 个有
- `easy mergeVideosFromPaths` —— 2/4 个有
- `easy promptLine` —— 2/4 个有
- `easy timelineEditor` —— 2/4 个有
- `easy timelineInfoOutput` —— 2/4 个有
- `easy timelineSegmentCount` —— 2/4 个有
- `easy timelineSegmentOutput` —— 2/4 个有
- `Any To String (mtb)` —— 1/4 个有
- `GetImageRangeFromBatch` —— 1/4 个有
- `JWFloatToString` —— 1/4 个有
- `MaxNode` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `PreviewAudio` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `StringConcatenate` —— 1/4 个有
- `VHS_GetImageCount` —— 1/4 个有
- `VRAM_Debug` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 10 | 4 | 36% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | dpmpp_sde | - | 4 | 75% |
| 重绘幅度 | normal | - | 4 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 10，4 个样本，取值分散，一致性仅 36%
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_sde，4 个样本，一致性 75%
- 重绘幅度 最常用 normal，4 个样本，一致性 75%
