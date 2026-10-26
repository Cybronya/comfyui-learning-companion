---
name: image_to_image_lora_sampler_clip_18
type: Image To Image
frequency: 10
level: strong
coverage: 0.9402
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/图片黑白渲染变成彩色_1979817875533893634.json, 图片生成/图生图/增加自然光影（无光影家具空间生成真实自然光影效果kontext_全能溶图打光_）_1986703454842384386.json, 图片生成/图生图/空白工作流_2077308039287361538.json, 图片生成/图生图/精修-金属类-kontxet_1959152559569186818.json, 图片生成/图生图/老照片修复flux_kontext全自动修复_2095321572251881474.json, 图片生成/图生图/老照片修复flux_kontext全自动修复_2095425023170400258.json, 图片生成/图生图/老照片修复（flux kontext全自动修复）_1990974918315679745.json, 图片生成/图生图/老照片修复（flux kontext全自动修复））_2017623484586790914.json, 图片生成/图生图/自动溶图_Kontext_1950812344156880897.json, 图片生成/图生图/课件20：kontext老照片一键修复_2099656538049826818.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_18

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/图片黑白渲染变成彩色_1979817875533893634.json、图片生成/图生图/增加自然光影（无光影家具空间生成真实自然光影效果kontext_全能溶图打光_）_1986703454842384386.json、图片生成/图生图/空白工作流_2077308039287361538.json、图片生成/图生图/精修-金属类-kontxet_1959152559569186818.json、图片生成/图生图/老照片修复flux_kontext全自动修复_2095321572251881474.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 7/10 个有
- `RepeatLatentBatch` —— 5/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/10 个有
- `ConstrainImage|pysssss` —— 2/10 个有
- `RH_Translator` —— 2/10 个有
- `ACE_TextGoogleTranslate` —— 1/10 个有
- `ImpactInt` —— 1/10 个有
- `JoinStrings` —— 1/10 个有
- `String` —— 1/10 个有
- `Text` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 10 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 0.8 - 1 | 10 | 94% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，10 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，10 个样本，取值集中（一致性 94%）
