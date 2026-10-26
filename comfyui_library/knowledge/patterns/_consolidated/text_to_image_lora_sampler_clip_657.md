---
name: text_to_image_lora_sampler_clip_657
type: Text To Image
frequency: 2
level: weak
coverage: 0.958
common_nodes: [CLIPLoader, CLIPTextEncode, CR Color Panel, CR Overlay Text, EmptyLatentImage, ImageCompositeMasked, InvertMask, JjkText, KSampler, LayerMask: DrawRoundedRectangle, LoadImage, LoraLoaderModelOnly, MaskComposite, SaveImage, SolidMask, TextOverlayImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/宝宝睡衣套图海报制作｜电商加字与品牌Logo排版，6张一键出图_2104487878914043906.json, 图片生成/图生图/宝宝睡衣套图电商排版 加字与品牌Logo排版6张_2104721348781232130.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_657

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/宝宝睡衣套图海报制作｜电商加字与品牌Logo排版，6张一键出图_2104487878914043906.json、图片生成/图生图/宝宝睡衣套图电商排版 加字与品牌Logo排版6张_2104721348781232130.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Color Panel`
- `CR Overlay Text`
- `EmptyLatentImage`
- `ImageCompositeMasked`
- `InvertMask`
- `JjkText`
- `KSampler`
- `LayerMask: DrawRoundedRectangle`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskComposite`
- `SaveImage`
- `SolidMask`
- `TextOverlayImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
