---
name: unknown_workflow_video_upscale_lora_33
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6625
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, ContextWindowsManual, DownloadAndLoadGIMMVFIModel, Fast Groups Bypasser (rgthree), Free_Video_Memory, GIMMVFI_interpolate, GetNode, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ModelSamplingSD3, Primitive string multiline [Crystools], SeargeIntegerConstant, SeedVR2, SeedVR2BlockSwap, SetNode, UNETLoader, UnloadAllModels, VAEDecode, VAELoader, VHS_LoadVideo, VHS_LoadVideoPath, VHS_VideoCombine, VHS_VideoInfo, VHS_VideoInfoLoaded, Video_Upscale_With_Model, WanSoundImageToVideo, WanVideoAddS2VEmbeds, WanVideoBlockSwap, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed, easy clearCacheAll]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1962460220972732417.json, 视频生成/图生视频/1962404930713686018.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_33

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1962460220972732417.json、视频生成/图生视频/1962404930713686018.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `ContextWindowsManual`
- `DownloadAndLoadGIMMVFIModel`
- `Fast Groups Bypasser (rgthree)`
- `Free_Video_Memory`
- `GIMMVFI_interpolate`
- `GetNode`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `ModelSamplingSD3`
- `Primitive string multiline [Crystools]`
- `SeargeIntegerConstant`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SetNode`
- `UNETLoader`
- `UnloadAllModels`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_LoadVideoPath`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `VHS_VideoInfoLoaded`
- `Video_Upscale_With_Model`
- `WanSoundImageToVideo`
- `WanVideoAddS2VEmbeds`
- `WanVideoBlockSwap`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | uni_pc | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
