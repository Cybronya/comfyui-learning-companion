---
name: text_to_image_sampler_clip_checkpoint_36
type: Text To Image
frequency: 2
level: weak
coverage: 0.638
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, GrowMaskWithBlur, ICLightConditioning, KSampler, LoadAndApplyICLightUnet, LoadImage, LoadImageMask, MaskToImage, PreviewImage, RemapMaskRange, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [平台全量/Relight with IC-Light - Product Photography religh_1886980817795837953.json, 平台全量/自定义光线重新给物品生成和打光_1831711796880101378.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_36

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Relight with IC-Light - Product Photography religh_1886980817795837953.json、平台全量/自定义光线重新给物品生成和打光_1831711796880101378.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `GrowMaskWithBlur`
- `ICLightConditioning`
- `KSampler`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `LoadImageMask`
- `MaskToImage`
- `PreviewImage`
- `RemapMaskRange`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 1/2 个有
- `ImageToMask` —— 1/2 个有
- `PreviewBridge` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 3.3 | - | 2 | 91% |
| 采样算法 | dpmpp_2m_sde | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 3.3，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- 采样算法 最常用 dpmpp_2m_sde，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
