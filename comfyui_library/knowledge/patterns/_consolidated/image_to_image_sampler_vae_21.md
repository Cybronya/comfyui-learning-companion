---
name: image_to_image_sampler_vae_21
type: Image To Image
frequency: 7
level: strong
coverage: 0.838143
common_nodes: [ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/个人用精修2_2061890865987153922.json, 图片生成/图生图/产品融入背景 真实光影_1957815415567216641.json, 图片生成/图生图/波光粼粼_2076044863581286402.json, 图片生成/图生图/矢量插画风格-一键转绘_1969793417184243714.json, 图片生成/图生图/移除物体_kontext版本（优化版）_1951337099012329474.json, 平台全量/fusion_1959885610045616129.json, 平台全量/溶图自动调整光影广告级——画萌萌_1960216252201512962.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_21

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/个人用精修2_2061890865987153922.json、图片生成/图生图/产品融入背景 真实光影_1957815415567216641.json、图片生成/图生图/波光粼粼_2076044863581286402.json、图片生成/图生图/矢量插画风格-一键转绘_1969793417184243714.json、图片生成/图生图/移除物体_kontext版本（优化版）_1951337099012329474.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 5/7 个有
- `Image Comparer (rgthree)` —— 5/7 个有
- `UNETLoader` —— 5/7 个有
- `Anything Everywhere` —— 4/7 个有
- `RHHiddenNodes` —— 4/7 个有
- `CR Text` —— 3/7 个有
- `SetNode` —— 3/7 个有
- `easy cleanGpuUsed` —— 3/7 个有
- `easy seed` —— 3/7 个有
- `LoraLoader` —— 2/7 个有
- `UnetLoaderGGUF` —— 2/7 个有
- `孤海图像缩放按像素` —— 2/7 个有
- `Anything Everywhere3` —— 1/7 个有
- `ApplyFBCacheOnModel` —— 1/7 个有
- `INPAINT_MaskedFill` —— 1/7 个有
- `Prompts Everywhere` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 7 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | beta | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，7 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 beta，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
