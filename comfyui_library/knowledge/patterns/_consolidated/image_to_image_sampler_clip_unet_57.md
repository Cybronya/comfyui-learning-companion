---
name: image_to_image_sampler_clip_unet_57
type: Image To Image
frequency: 9
level: strong
coverage: 0.927222
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/图片黑白渲染变成彩色_1979817875533893634.json, 图片生成/图生图/增加自然光影（无光影家具空间生成真实自然光影效果kontext_全能溶图打光_）_1986703454842384386.json, 图片生成/图生图/空白工作流_2077308039287361538.json, 图片生成/图生图/精修-金属类-kontxet_1959152559569186818.json, 图片生成/图生图/自动溶图_Kontext_1950812344156880897.json, 图片生成/图生图/超快水印去除【基础kontext】_1940590387251802114.json, 平台全量/Kontext全能场景白膜渲染_1966068920602062850.json, 平台全量/Kontext汽车专用户外场景白膜渲染_1978354076490555393.json, 平台全量/电商白模渲染  场景渲染 全能渲染 极致写实 光影艺术 Kontext_2009125843284529154.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_57

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/图片黑白渲染变成彩色_1979817875533893634.json、图片生成/图生图/增加自然光影（无光影家具空间生成真实自然光影效果kontext_全能溶图打光_）_1986703454842384386.json、图片生成/图生图/空白工作流_2077308039287361538.json、图片生成/图生图/精修-金属类-kontxet_1959152559569186818.json、图片生成/图生图/自动溶图_Kontext_1950812344156880897.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 8/9 个有
- `ConstrainImage|pysssss` —— 5/9 个有
- `JoinStrings` —— 4/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `String` —— 4/9 个有
- `ACE_TextGoogleTranslate` —— 3/9 个有
- `FluxKontextImageScale` —— 3/9 个有
- `Text` —— 3/9 个有
- `PixaromaLabel` —— 2/9 个有
- `Anything Everywhere3` —— 1/9 个有
- `ImpactInt` —— 1/9 个有
- `LayerUtility: ImageScaleRestore` —— 1/9 个有
- `MagCache` —— 1/9 个有
- `RH_Translator` —— 1/9 个有
- `ShowText|pysssss` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 9 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 0.8 - 1 | 9 | 94% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，9 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，9 个样本，取值集中（一致性 94%）
