---
name: text_to_image_video_lora_sampler_108
type: Text To Image
frequency: 8
level: strong
coverage: 0.827625
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ComfyMathExpression, ContextWindowsManual, EmptyLatentImage, GetImageRangeFromBatch, ImageFromBatch, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveStringMultiline, ResizeImageMaskNode, SamplerCustom, TensorLoopClose, TensorLoopOpen, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanAnimate2Cache, WanAnimate2ToVideo, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Animate2数字人跳舞视频编辑唱歌动作迁移复刻动作无限时长，图生视频_2114989647444135937.json, 平台全量/Wan animate2循环流V1-视频编辑视频生视频工作流_2087372794312089602.json, 数字人/数字人/Animate2数字人跳舞视频编辑唱歌动作迁移复刻动作无限时长，图生视频_2106915189659619329.json, 视频生成/图生视频/Animate2 数字人一体机｜图生视频跳舞唱歌 复刻动作不限时_2097551273812914177.json, 视频生成/图生视频/Animate2 数字人全活｜跳舞唱歌动作迁移复刻 无限时长_2097537467590201346.json, 视频生成/图生视频/Animate2数字人跳舞视频编辑唱歌动作迁移图生视频_2088206618096918529.json, 视频生成/图生视频/Animate2数字人跳舞视频编辑唱歌动作迁移复刻动作无限时长，图生视频_2108369397894172673.json, 视频生成/文生视频/Animate2动作迁移 动作复刻视频生成方案_2105392312758132738.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_108

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Animate2数字人跳舞视频编辑唱歌动作迁移复刻动作无限时长，图生视频_2114989647444135937.json、平台全量/Wan animate2循环流V1-视频编辑视频生视频工作流_2087372794312089602.json、数字人/数字人/Animate2数字人跳舞视频编辑唱歌动作迁移复刻动作无限时长，图生视频_2106915189659619329.json、视频生成/图生视频/Animate2 数字人一体机｜图生视频跳舞唱歌 复刻动作不限时_2097551273812914177.json、视频生成/图生视频/Animate2 数字人全活｜跳舞唱歌动作迁移复刻 无限时长_2097537467590201346.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ComfyMathExpression`
- `ContextWindowsManual`
- `EmptyLatentImage`
- `GetImageRangeFromBatch`
- `ImageFromBatch`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `ResizeImageMaskNode`
- `SamplerCustom`
- `TensorLoopClose`
- `TensorLoopOpen`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanAnimate2Cache`
- `WanAnimate2ToVideo`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 7/8 个有
- `GetImageSize` —— 7/8 个有
- `GetImageSizeAndCount` —— 7/8 个有
- `ImageConcatMulti` —— 7/8 个有
- `ImageResizeKJv2` —— 7/8 个有
- `JWInteger` —— 7/8 个有
- `PrimitiveBoolean` —— 7/8 个有
- `easy int` —— 7/8 个有
- `GetNode` —— 6/8 个有
- `easy showAnything` —— 6/8 个有
- `孤海注释` —— 6/8 个有
- `SaveImage` —— 4/8 个有
- `EmptyImage` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `SetNode` —— 2/8 个有
- `Bookmark (rgthree)` —— 1/8 个有
- `Int` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `LoadVideo` —— 1/8 个有
- `PlaySound|pysssss` —— 1/8 个有
- `ShowAnything|Mie` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
