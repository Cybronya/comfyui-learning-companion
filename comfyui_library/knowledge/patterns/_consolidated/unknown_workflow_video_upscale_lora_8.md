---
name: unknown_workflow_video_upscale_lora_8
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.833833
common_nodes: [BasicScheduler, CLIPTextEncodeFlux, ConditioningZeroOut, DownloadAndLoadGIMMVFIModel, DualCLIPLoader, Fast Groups Bypasser (rgthree), GIMMVFI_interpolate, Image Comparer (rgthree), KSamplerSelect, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, LoraLoader, LyingSigmaSampler, ModelSamplingFlux, PreviewImage, UNETLoader, UltimateSDUpscaleCustomSample, UpscaleModelLoader, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader, easy imageSize]
problems: []
missing: []
members: [视频生成/图生视频/1932326595036348417.json, 视频生成/图生视频/1932439871766077442.json, 视频生成/图生视频/1939001698457473026.json, 视频生成/图生视频/1941180183246487554.json, 视频生成/图生视频/1935690347278163970.json, 视频生成/图生视频/1939032369221263361.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_8

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1932326595036348417.json、视频生成/图生视频/1932439871766077442.json、视频生成/图生视频/1939001698457473026.json、视频生成/图生视频/1941180183246487554.json、视频生成/图生视频/1935690347278163970.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DownloadAndLoadGIMMVFIModel`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `GIMMVFI_interpolate`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `LoraLoader`
- `LyingSigmaSampler`
- `ModelSamplingFlux`
- `PreviewImage`
- `UNETLoader`
- `UltimateSDUpscaleCustomSample`
- `UpscaleModelLoader`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToMegapixels` —— 4/6 个有
- `ImageSmartSharpen+` —— 4/6 个有
- `WanVideoExperimentalArgs` —— 4/6 个有
- `WanVideoTorchCompileSettings` —— 4/6 个有
- `easy cleanGpuUsed` —— 4/6 个有
- `ImageResizeKJ` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
