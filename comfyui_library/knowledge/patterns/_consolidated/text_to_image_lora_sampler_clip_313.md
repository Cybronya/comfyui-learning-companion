---
name: text_to_image_lora_sampler_clip_313
type: Text To Image
frequency: 6
level: moderate
coverage: 0.9185
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, PreviewImage, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/krea2-HD+realismVSkrea2_2077022883196522498.json, 图片生成/图生图/krea2-水彩+彩色速写+复古塔罗+动态模糊+紫色动漫+肌理抽象+雨窗+单色点彩风格_2070139026685915138.json, 图片生成/图生图/krea2-高清+写实文生图_2076997814403551233.json, 图片生成/图生图/千问qwen-image-2.1文生图工作流（不可商用）_2105059412837756929.json, 图片生成/图生图/简笔画风格_2058084894823243778.json, 图片生成/文生图/2029447461651091457.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_313

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/krea2-HD+realismVSkrea2_2077022883196522498.json、图片生成/图生图/krea2-水彩+彩色速写+复古塔罗+动态模糊+紫色动漫+肌理抽象+雨窗+单色点彩风格_2070139026685915138.json、图片生成/图生图/krea2-高清+写实文生图_2076997814403551233.json、图片生成/图生图/千问qwen-image-2.1文生图工作流（不可商用）_2105059412837756929.json、图片生成/图生图/简笔画风格_2058084894823243778.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 5/6 个有
- `AddLabel` —— 2/6 个有
- `CR Prompt Text` —— 2/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `ModelSamplingAuraFlow` —— 2/6 个有
- `EnhancedLoadDiffusionModel` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `String Literal` —— 1/6 个有
- `Text` —— 1/6 个有
- `TextConcatenate_UTK` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 50 | 6 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | beta | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1024 | 720 - 1440 | 6 | 74% |
| 高度 | 1280 | 720 - 1920 | 6 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 50，6 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 beta，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 720 - 1440，6 个样本
- 高度 中位数 1280，观测区间 720 - 1920，6 个样本
- 高发问题（16/6 个样本）：Steps较低可能导致细节不足
