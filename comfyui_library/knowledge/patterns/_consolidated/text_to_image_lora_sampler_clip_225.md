---
name: text_to_image_lora_sampler_clip_225
type: Text To Image
frequency: 3
level: strong
coverage: 0.667333
common_nodes: [Anything Everywhere, Anything Everywhere3, CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Bypasser (rgthree), JjkText, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, SaveImage, ShowText|pysssss, Text Concatenate (JPS), UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [Fast Bypasser (rgthree), LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, Mute / Bypass Repeater (rgthree), Text Concatenate (JPS)]
members: [图片生成/文生图/1954164943279013889.json, 图片生成/文生图/1962523964402712577.json, 图片生成/文生图/1966158255494000641.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_225

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1954164943279013889.json、图片生成/文生图/1962523964402712577.json、图片生成/文生图/1966158255494000641.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Bypasser (rgthree)`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `SaveImage`
- `ShowText|pysssss`
- `Text Concatenate (JPS)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: JoyCaptionBeta1` —— 2/3 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 2/3 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 2/3 个有
- `RH_Captioner_Pro` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_2s | - | 3 | 100% |
| 调度器 | bong_tangent | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1536 | 1536 - 1536 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，3 个样本，一致性 100%
- 调度器 最常用 bong_tangent，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，3 个样本，取值集中（一致性 100%）
- 高发问题（12/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Fast Bypasser (rgthree)、LayerUtility: JoyCaptionBeta1、LayerUtility: JoyCaptionBeta1ExtraOptions、LayerUtility: LoadJoyCaptionBeta1Model、Mute / Bypass Repeater (rgthree)
