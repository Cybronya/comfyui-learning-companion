---
name: image_to_image_video_lora_sampler_17
type: Image To Image
frequency: 2
level: weak
coverage: 0.558
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, ComfySwitchNode, ConditioningZeroOut, Context (rgthree), Context Switch (rgthree), DiffusionModelLoaderKJ, GetImageRangeFromBatch, GetNode, ImageConcatMulti, ImageResizeKJv2, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, PrimitiveInt, RMBG, SAM3_VideoTrack, SCAIL2ColoredMask, SDVN Fast Groups Bypasser, SamplerCustom, SetNode, TextEncodeQwenImageEditPlusAdvance_lrzjason, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_GetImageCount, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanChunkFeedForward, WanSCAILToVideo, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2079843393458491393.json, 视频生成/图生视频/2064666647113330690.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_17

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2079843393458491393.json、视频生成/图生视频/2064666647113330690.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ColorTransfer`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `Context (rgthree)`
- `Context Switch (rgthree)`
- `DiffusionModelLoaderKJ`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `PrimitiveInt`
- `RMBG`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SDVN Fast Groups Bypasser`
- `SamplerCustom`
- `SetNode`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_GetImageCount`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanChunkFeedForward`
- `WanSCAILToVideo`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta57 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta57，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
