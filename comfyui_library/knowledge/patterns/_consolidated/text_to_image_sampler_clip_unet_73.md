---
name: text_to_image_sampler_clip_unet_73
type: Text To Image
frequency: 9
level: moderate
coverage: 0.927111
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/001.Z-image生图巅峰009.Z-回车批量文生图+flux-vae_2033738805638860802.json, 图片生成/文生图/1.阿清的z-image工作流_2037804089450438658.json, 图片生成/文生图/33号特工：Z-image小钢炮，文生图+本地解码+彩图_2046531810259116033.json, 图片生成/文生图/5.其他类型-6.NSF+-09.Z-image生图002.Z-image批量文生图.json_2021966315602317313.json, 图片生成/文生图/Krea-2 高真实感与卓越美学文生图_2069624809176256513.json, 图片生成/文生图/LH-DMT版本-2.生图片类-029.Z-image智能改词文生图-NF_2016493278639693826.json, 图片生成/文生图/Zimage-turbo保暖内衣_2051484069925531650.json, 图片生成/文生图/krea2+z_image+boogu模型测试对比_2069616764018843650.json, 图片生成/文生图/zimage+krea2+boogu三模型对比_2069599329727373314.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_73

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/001.Z-image生图巅峰009.Z-回车批量文生图+flux-vae_2033738805638860802.json、图片生成/文生图/1.阿清的z-image工作流_2037804089450438658.json、图片生成/文生图/33号特工：Z-image小钢炮，文生图+本地解码+彩图_2046531810259116033.json、图片生成/文生图/5.其他类型-6.NSF+-09.Z-image生图002.Z-image批量文生图.json_2021966315602317313.json、图片生成/文生图/Krea-2 高真实感与卓越美学文生图_2069624809176256513.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImpactInt` —— 8/9 个有
- `String Literal` —— 8/9 个有
- `easy showAnything` —— 8/9 个有
- `CR Prompt List` —— 7/9 个有
- `CR Text` —— 4/9 个有
- `Dapao_LlamaCaption` —— 4/9 个有
- `Dapao_LlamaCaptionOptions` —— 4/9 个有
- `LoadImage` —— 4/9 个有
- `RegexReplace` —— 4/9 个有
- `easy cleanGpuUsed` —— 3/9 个有
- `LayerUtility: ImageReel` —— 2/9 个有
- `LayerUtility: ImageReelComposit` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `LoraLoaderModelOnly` —— 1/9 个有
- `ProcessString` —— 1/9 个有
- `TT_img_enc_v2` —— 1/9 个有
- `easy promptList` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 720 - 1280 | 9 | 78% |
| 高度 | 1280 | 720 - 1280 | 9 | 86% |
| 采样步数 | 9 | 4 - 20 | 9 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.1 | 9 | 97% |
| 采样算法 | euler | - | 9 | 33% |
| 调度器 | simple | - | 9 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 720 - 1280，9 个样本
- 高度 中位数 1280，观测区间 720 - 1280，9 个样本，取值集中（一致性 86%）
- 采样步数 中位数 9，观测区间 4 - 20，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.1，9 个样本，取值集中（一致性 97%）
- 采样算法 最常用 euler，9 个样本，一致性 33%
- 调度器 最常用 simple，9 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（11/9 个样本）：Steps较低可能导致细节不足
