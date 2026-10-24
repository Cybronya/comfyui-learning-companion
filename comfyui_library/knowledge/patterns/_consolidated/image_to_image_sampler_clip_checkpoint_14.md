---
name: image_to_image_sampler_clip_checkpoint_14
type: Image To Image
frequency: 2
level: weak
coverage: 0.7945
common_nodes: [CLIPTextEncode, CR Simple Image Compare, CheckpointLoaderSimple, JoinStrings, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, PreviewImage, Qwen3_VQA, SaveImage, ShowText|pysssss, Text Multiline, VAEDecode, VAEEncode, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/RedCraft⚡️红潮造相 AIO V1.5 图生图（去网红去AI化洗图）_2050933632906346498.json, 图片生成/图生图/Z-Image：RedCraft⚡️红潮造相 AIO V1.5 图生图（去网红去AI化洗图）_1998728693025492993.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_checkpoint_14

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/RedCraft⚡️红潮造相 AIO V1.5 图生图（去网红去AI化洗图）_2050933632906346498.json、图片生成/图生图/Z-Image：RedCraft⚡️红潮造相 AIO V1.5 图生图（去网红去AI化洗图）_1998728693025492993.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Simple Image Compare`
- `CheckpointLoaderSimple`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `PreviewImage`
- `Qwen3_VQA`
- `SaveImage`
- `ShowText|pysssss`
- `Text Multiline`
- `VAEDecode`
- `VAEEncode`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_cfg_pp | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 0.7 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_cfg_pp，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
