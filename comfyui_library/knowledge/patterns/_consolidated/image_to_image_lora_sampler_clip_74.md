---
name: image_to_image_lora_sampler_clip_74
type: Image To Image
frequency: 4
level: moderate
coverage: 0.86225
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen.图生图-加速高清放大_1988499224629264385.json, 图片生成/图生图/krea2_风格转换_2082378604700327937.json, 图片生成/图生图/千问图生图（qwen2512高质量版）+提速+电影感_1978012925728280578.json, 图片生成/图生图/👾怪獸-千问图生图电影级质感👾_1980982250647011329.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_74

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen.图生图-加速高清放大_1988499224629264385.json、图片生成/图生图/krea2_风格转换_2082378604700327937.json、图片生成/图生图/千问图生图（qwen2512高质量版）+提速+电影感_1978012925728280578.json、图片生成/图生图/👾怪獸-千问图生图电影级质感👾_1980982250647011329.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `JWImageResizeByLongerSide` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `ImageUpscaleWithModel` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `Seed Everywhere` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | 6 - 8 | 4 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.525 | 0.4 - 1 | 4 | 62% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，观测区间 6 - 8，4 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.525，观测区间 0.4 - 1，4 个样本
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
