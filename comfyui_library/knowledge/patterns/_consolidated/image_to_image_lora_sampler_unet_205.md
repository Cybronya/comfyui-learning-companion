---
name: image_to_image_lora_sampler_unet_205
type: Image To Image
frequency: 3
level: moderate
coverage: 0.816
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/🥨千问 产品溶图 光影融合 put it here 🥨_1965204149518352386.json, 图片生成/文生图/【ComfyUI全注释】真人转动漫_卡通_漫画，3种风格一条流搞定_2060023079732072450.json, 视频生成/文生视频/真人转动漫++真人转卡通++真人转漫画++ (1)_2061990337312280578.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_205

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/🥨千问 产品溶图 光影融合 put it here 🥨_1965204149518352386.json、图片生成/文生图/【ComfyUI全注释】真人转动漫_卡通_漫画，3种风格一条流搞定_2060023079732072450.json、视频生成/文生视频/真人转动漫++真人转卡通++真人转漫画++ (1)_2061990337312280578.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `FastCanvas` —— 1/3 个有
- `FastCanvasTool` —— 1/3 个有
- `ImageScaleDownToSize` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `StringFunction|pysssss` —— 1/3 个有
- `easy imageRemBg` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 3 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 3 | 53% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
