---
name: text_to_image_sampler_clip_checkpoint_26
type: Text To Image
frequency: 2
level: weak
coverage: 0.6785
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConditioningSetTimestepRange, EmptyLatentImage, GetNode, ImageScaleBy, Int, KSampler, Label (rgthree), LayerUtility: PurgeVRAM, PreviewImage, SaveImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, SetNode, Text Multiline, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/AI代码侠土豆-Red-Z-Image_AIO文生图_1998316363712225282.json, 图片生成/文生图/ZX文生图工作流搭建_2079128535050051585.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_26

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/AI代码侠土豆-Red-Z-Image_AIO文生图_1998316363712225282.json、图片生成/文生图/ZX文生图工作流搭建_2079128535050051585.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningSetTimestepRange`
- `EmptyLatentImage`
- `GetNode`
- `ImageScaleBy`
- `Int`
- `KSampler`
- `Label (rgthree)`
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SetNode`
- `Text Multiline`
- `VAEDecode`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_cfg_pp | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_cfg_pp，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
