---
name: unknown_workflow_clip_unet_vae_17
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.718
common_nodes: [Anything Everywhere, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, GetImageSize, ImageLoader, ImageScaleToTotalPixels, LayerUtility: PurgeVRAM V2, MaraScottIsEmptyOrNone_v1, PlaySound|pysssss, PreviewImage, QwenImageLatentAspectRatio, RHHiddenNodes, SaveImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, ShowAnything|Mie, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy ifElse, easy imageConcat, easy int, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/图片反推提示词 洗图 爆款图复刻模仿_2033926293561020418.json, 图片生成/图生图/爆款图重绘模仿洗图 z image再生图 seedvr2高清放大_2033910998129709057.json, 图片生成/文生图/重绘洗图+图片反推提示词z+image再生图+seedvr2高清放大+爆款图重绘模仿_2022333096535789570.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_17

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/图片反推提示词 洗图 爆款图复刻模仿_2033926293561020418.json、图片生成/图生图/爆款图重绘模仿洗图 z image再生图 seedvr2高清放大_2033910998129709057.json、图片生成/文生图/重绘洗图+图片反推提示词z+image再生图+seedvr2高清放大+爆款图重绘模仿_2022333096535789570.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize`
- `ImageLoader`
- `ImageScaleToTotalPixels`
- `LayerUtility: PurgeVRAM V2`
- `MaraScottIsEmptyOrNone_v1`
- `PlaySound|pysssss`
- `PreviewImage`
- `QwenImageLatentAspectRatio`
- `RHHiddenNodes`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `ShowAnything|Mie`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy ifElse`
- `easy imageConcat`
- `easy int`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 544 | 544 - 544 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 544，观测区间 544 - 544，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
