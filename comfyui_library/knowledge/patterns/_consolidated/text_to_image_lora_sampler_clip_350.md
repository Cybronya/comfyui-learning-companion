---
name: text_to_image_lora_sampler_clip_350
type: Text To Image
frequency: 6
level: moderate
coverage: 0.858667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/▶▷MOSS-Image-生图turbo_2114617199683006465.json, 图片生成/文生图/东方阳台美女Qwen2512文生图真实人像质感御姐美女_2041499716185231362.json, 图片生成/文生图/俯视户外Qwen2512文生图真实人像质感御姐美女_2041474355028303873.json, 图片生成/文生图/动漫柔和光（Anima）_2073031688103485441.json, 图片生成/文生图/原神风格文生图场景设计_2100396348150472705.json, 图片生成/文生图/绝区零风格文生图场景设计_2100441031195062274.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_350

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/▶▷MOSS-Image-生图turbo_2114617199683006465.json、图片生成/文生图/东方阳台美女Qwen2512文生图真实人像质感御姐美女_2041499716185231362.json、图片生成/文生图/俯视户外Qwen2512文生图真实人像质感御姐美女_2041474355028303873.json、图片生成/文生图/动漫柔和光（Anima）_2073031688103485441.json、图片生成/文生图/原神风格文生图场景设计_2100396348150472705.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/6 个有
- `PrimitiveStringMultiline` —— 3/6 个有
- `PreviewImage` —— 2/6 个有
- `UpscaleModelLoader` —— 2/6 个有
- `Int` —— 1/6 个有
- `ResolutionSelector` —— 1/6 个有
- `easy seed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1536 | 6 | 71% |
| 高度 | 1024 | 768 - 1344 | 6 | 77% |
| 采样步数 | 19 | 8 - 30 | 6 | 42% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 6 | 40% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1536，6 个样本
- 高度 中位数 1024，观测区间 768 - 1344，6 个样本
- 采样步数 中位数 19，观测区间 8 - 30，6 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，6 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
