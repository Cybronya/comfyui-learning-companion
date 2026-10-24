---
name: text_to_image_sampler_clip_unet_211
type: Text To Image
frequency: 2
level: weak
coverage: 0.565
common_nodes: [Any Switch (rgthree), Bookmark (rgthree), CLIPTextEncode, DeepTranslatorTextNode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, GetNode, ImageResize+, KSampler, LoadImage, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, PrimitiveFloat, PrimitiveStringMultiline, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy int, easy seed]
problems: []
missing: []
members: [图片生成/文生图/FLUX Krea 文生图+图生图（合并版）_1958461737676730370.json, 图片生成/文生图/FLUX_krea_文图生图二合一_1952418269997273089.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_211

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/FLUX Krea 文生图+图生图（合并版）_1958461737676730370.json、图片生成/文生图/FLUX_krea_文图生图二合一_1952418269997273089.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Bookmark (rgthree)`
- `CLIPTextEncode`
- `DeepTranslatorTextNode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `GetNode`
- `ImageResize+`
- `KSampler`
- `LoadImage`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy int`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `GLM_Text_Chat` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 768 | - | 2 | 100% |
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
