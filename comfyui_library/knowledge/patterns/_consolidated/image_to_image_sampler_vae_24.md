---
name: image_to_image_sampler_vae_24
type: Image To Image
frequency: 5
level: strong
coverage: 0.8488
common_nodes: [ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/个人用精修2_2061890865987153922.json, 图片生成/图生图/产品融入背景 真实光影_1957815415567216641.json, 图片生成/图生图/波光粼粼_2076044863581286402.json, 图片生成/图生图/矢量插画风格-一键转绘_1969793417184243714.json, 图片生成/图生图/移除物体_kontext版本（优化版）_1951337099012329474.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_24

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/个人用精修2_2061890865987153922.json、图片生成/图生图/产品融入背景 真实光影_1957815415567216641.json、图片生成/图生图/波光粼粼_2076044863581286402.json、图片生成/图生图/矢量插画风格-一键转绘_1969793417184243714.json、图片生成/图生图/移除物体_kontext版本（优化版）_1951337099012329474.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `CLIPTextEncode` —— 3/5 个有
- `RHHiddenNodes` —— 3/5 个有
- `Anything Everywhere` —— 2/5 个有
- `CR Text` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `easy seed` —— 2/5 个有
- `INPAINT_MaskedFill` —— 1/5 个有
- `LoraLoader` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有
- `孤海图像缩放按像素` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 5 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | beta | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
