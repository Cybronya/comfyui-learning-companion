---
name: text_to_image_sampler_clip_unet_94
type: Text To Image
frequency: 5
level: moderate
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/anima_api_2075524651396198402.json, 图片生成/文生图/anima基础工作流_2050251032118210561.json, 图片生成/文生图/qwen_edit_2512_越真实文生图-真实去ai味_2010517531177521153.json, 图片生成/文生图/文生图千问qwen2512文生图阿里最新文生图开源模型_2006970243293388801.json, 图片生成/文生图/泳装系列Z-image真实人像质感御姐美女_2104743758045728769.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_94

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/anima_api_2075524651396198402.json、图片生成/文生图/anima基础工作流_2050251032118210561.json、图片生成/文生图/qwen_edit_2512_越真实文生图-真实去ai味_2010517531177521153.json、图片生成/文生图/文生图千问qwen2512文生图阿里最新文生图开源模型_2006970243293388801.json、图片生成/文生图/泳装系列Z-image真实人像质感御姐美女_2104743758045728769.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `FluxResolutionNode` —— 1/5 个有
- `LoaderGGUF` —— 1/5 个有
- `SeedNode` —— 1/5 个有
- `TT_img_enc` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 8 - 50 | 5 | 55% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 5 | 65% |
| 采样算法 | euler | - | 5 | 40% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 768 - 1080 | 5 | 85% |
| 高度 | 1344 | 1024 - 1920 | 5 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 8 - 50，5 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 40%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 768 - 1080，5 个样本，取值集中（一致性 85%）
- 高度 中位数 1344，观测区间 1024 - 1920，5 个样本
