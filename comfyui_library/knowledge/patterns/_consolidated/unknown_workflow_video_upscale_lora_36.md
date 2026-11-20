---
name: unknown_workflow_video_upscale_lora_36
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8425
common_nodes: [AddLabel, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPTextEncodeFlux, CR Image Grid Panel, ConditioningZeroOut, DownloadAndLoadGIMMVFIModel, DualCLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxGuidance, GIMMVFI_interpolate, GetNode, Image Comparer (rgthree), ImageListToBatch+, KSamplerSelect, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, LoraLoader, LoraLoaderModelOnly, LyingSigmaSampler, MathExpression|pysssss, ModelSamplingFlux, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, SomethingToString, UNETLoader, UltimateSDUpscaleCustomSample, UpscaleModelLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy batchAnything, easy cleanGpuUsed, easy float, easy forLoopEnd, easy forLoopStart, easy imageSize, easy outputToList]
problems: []
missing: []
members: [视频生成/图生视频/变毒液wan2.1万相图生视40工作流_1933388878445195265.json, 视频生成/图生视频/变毒液wan2.1万相图生视50工作流_1933379047416049666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_36

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/变毒液wan2.1万相图生视40工作流_1933388878445195265.json、视频生成/图生视频/变毒液wan2.1万相图生视50工作流_1933379047416049666.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `AddLabel`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `CR Image Grid Panel`
- `ConditioningZeroOut`
- `DownloadAndLoadGIMMVFIModel`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `GIMMVFI_interpolate`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageListToBatch+`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `LyingSigmaSampler`
- `MathExpression|pysssss`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `SomethingToString`
- `UNETLoader`
- `UltimateSDUpscaleCustomSample`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy float`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageSize`
- `easy outputToList`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
