---
name: text_to_image_video_lora_sampler_136
type: Text To Image
frequency: 5
level: strong
coverage: 0.5534
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, DiffusionModelLoaderKJ, EmptyLatentImage, GetImageRangeFromBatch, ImageConcatMulti, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物替换工作流 角色一致性更强精准替换方案_2108985171918811138.json, 数字人/数字人/一键复刻爆款视频图生视频处理生成工作流工具_2101396084621926402.json, 数字人/数字人/一键复刻爆款视频｜数字人视频生视频 动作迁移照搬_2097579730450075650.json, 视频生成/图生视频/SCAIL-2双人动作模仿迁移｜双人同框动作复制视频生成_2113524373717086210.json, 视频生成/图生视频/Scail2动作迁移For循环一键模仿图生视频处理工具_2101394038732709889.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_136

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/人物替换工作流 角色一致性更强精准替换方案_2108985171918811138.json、数字人/数字人/一键复刻爆款视频图生视频处理生成工作流工具_2101396084621926402.json、数字人/数字人/一键复刻爆款视频｜数字人视频生视频 动作迁移照搬_2097579730450075650.json、视频生成/图生视频/SCAIL-2双人动作模仿迁移｜双人同框动作复制视频生成_2113524373717086210.json、视频生成/图生视频/Scail2动作迁移For循环一键模仿图生视频处理工具_2101394038732709889.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：55%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DiffusionModelLoaderKJ`
- `EmptyLatentImage`
- `GetImageRangeFromBatch`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 4/5 个有
- `easy forLoopEnd` —— 4/5 个有
- `easy forLoopStart` —— 4/5 个有
- `ComfyMathExpression` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `SaveImage` —— 3/5 个有
- `SingleBooleanTrigger` —— 3/5 个有
- `easy batchAnything` —— 3/5 个有
- `easy imageRemBg` —— 3/5 个有
- `BatchImagesNode` —— 2/5 个有
- `ColorTransfer` —— 2/5 个有
- `GetNode` —— 2/5 个有
- `Int` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `WanChunkFeedForward` —— 2/5 个有
- `ComfySwitchNode` —— 1/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `Context (rgthree)` —— 1/5 个有
- `Context Switch (rgthree)` —— 1/5 个有
- `Float` —— 1/5 个有
- `INTConstant` —— 1/5 个有
- `LayerMask: RemBgUltra` —— 1/5 个有
- `RMBG` —— 1/5 个有
- `SDVN Fast Groups Bypasser` —— 1/5 个有
- `SaveVideoNode` —— 1/5 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/5 个有
- `TextInput_` —— 1/5 个有
- `VAEEncode` —— 1/5 个有
- `VHS_GetImageCount` —— 1/5 个有
- `VHS_VideoInfo` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
