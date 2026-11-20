---
name: text_to_image_video_lora_sampler_164
type: Text To Image
frequency: 4
level: strong
coverage: 0.58475
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ComfyMathExpression, DiffusionModelLoaderKJ, EmptyLatentImage, FastGroupsBypassSwitch, GetNode, ImageCompositeMasked, ImageConcatMulti, ImageResizeKJv2, Int, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MmuuaiGroupBypass, PreviewImage, RIFE VFI, SAM3_TrackToMask, SAM3_VideoTrack, SCAIL2ColoredMask, SCAILAutoExtend, SetNode, Text, UNETLoader, VAEDecode, VAELoader, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, VideoInfoLoaded, easy ab, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Xgc四合一流｜自定义背景动作模仿人物替换全都有_2097193944114352130.json, 视频生成/图生视频/Xgc工作流四合一｜自定义背景动作模仿人物替换多人数自由选｜视频生视频_2099095513466490882.json, 视频生成/图生视频/自定义背景动作模仿人物替换 多人数选择图生视频_2098827389802467329.json, 视频生成/图生视频/自定义背景动作模仿人物替换｜多图多人选择视频生成_2097102720611213314.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_164

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Xgc四合一流｜自定义背景动作模仿人物替换全都有_2097193944114352130.json、视频生成/图生视频/Xgc工作流四合一｜自定义背景动作模仿人物替换多人数自由选｜视频生视频_2099095513466490882.json、视频生成/图生视频/自定义背景动作模仿人物替换 多人数选择图生视频_2098827389802467329.json、视频生成/图生视频/自定义背景动作模仿人物替换｜多图多人选择视频生成_2097102720611213314.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `DiffusionModelLoaderKJ`
- `EmptyLatentImage`
- `FastGroupsBypassSwitch`
- `GetNode`
- `ImageCompositeMasked`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `Int`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MmuuaiGroupBypass`
- `PreviewImage`
- `RIFE VFI`
- `SAM3_TrackToMask`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SCAILAutoExtend`
- `SetNode`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VideoInfoLoaded`
- `easy ab`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNodeV2` —— 2/4 个有
- `ImageBatchMulti` —— 2/4 个有
- `MaskCompositeRef` —— 2/4 个有
- `SaveImage` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
