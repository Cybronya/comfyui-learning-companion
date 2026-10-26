---
name: image_to_image_video_lora_sampler_9
type: Image To Image
frequency: 4
level: strong
coverage: 0.558
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, ComfySwitchNode, ConditioningZeroOut, Context (rgthree), Context Switch (rgthree), DiffusionModelLoaderKJ, GetImageRangeFromBatch, GetNode, ImageConcatMulti, ImageResizeKJv2, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, PrimitiveInt, RMBG, SAM3_VideoTrack, SCAIL2ColoredMask, SDVN Fast Groups Bypasser, SamplerCustom, SetNode, TextEncodeQwenImageEditPlusAdvance_lrzjason, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_GetImageCount, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanChunkFeedForward, WanSCAILToVideo, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/SCAIL-2双人动作模仿迁移 动作迁移 动作模仿_2113207427586945026.json, 视频生成/图生视频/SCAIL-2双人动作模仿迁移 动作迁移 动作模仿_2113236628188782593.json, 视频生成/图生视频/SCAIL-2双人动作模仿迁移_2079843393458491393.json, 视频生成/图生视频/SCAIL-2双人视频动作迁移_2064666647113330690.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_9

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/SCAIL-2双人动作模仿迁移 动作迁移 动作模仿_2113207427586945026.json、视频生成/图生视频/SCAIL-2双人动作模仿迁移 动作迁移 动作模仿_2113236628188782593.json、视频生成/图生视频/SCAIL-2双人动作模仿迁移_2079843393458491393.json、视频生成/图生视频/SCAIL-2双人视频动作迁移_2064666647113330690.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：56%

## 共有节点

全部 4 个 workflow 都包含：
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
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta57 | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta57，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
