---
name: text_to_image_upscale_latent_upscale_lora_9
type: Text To Image
frequency: 5
level: moderate
coverage: 0.95
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, LatentUpscaleBy, LoraLoader, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/二分爱良配_2049140660023861250.json, 图片生成/文生图/儿童卡通绘本_1928363238206128129.json, 图片生成/文生图/剪影块面分割_2061724652694757378.json, 图片生成/文生图/质感笔触干练_2060512709078241281.json, 图片生成/文生图/赛博废土带笔触场景_2063495974462513153.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_9

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/二分爱良配_2049140660023861250.json、图片生成/文生图/儿童卡通绘本_1928363238206128129.json、图片生成/文生图/剪影块面分割_2061724652694757378.json、图片生成/文生图/质感笔触干练_2060512709078241281.json、图片生成/文生图/赛博废土带笔触场景_2063495974462513153.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `LatentUpscaleBy`
- `LoraLoader`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `KSampler //Inspire` —— 4/5 个有
- `CLIPSetLastLayer` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `TextCombinerTwo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.35 | 0.35 - 1.15 | 5 | 45% |
| LoRA 文本强度 | 0.35 | 0.35 - 1 | 5 | 52% |
| 采样步数 | 30 | 20 - 40 | 5 | 79% |
| Prompt 约束强度(CFG) | 8 | 7 - 8 | 5 | 95% |
| 采样算法 | euler | - | 5 | 40% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 0.5 - 1 | 5 | 78% |
| 宽度 | 720 | 512 - 1568 | 5 | 59% |
| 高度 | 880 | 512 - 1280 | 5 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.35，观测区间 0.35 - 1.15，5 个样本，取值分散，一致性仅 45%
- LoRA 文本强度 中位数 0.35，观测区间 0.35 - 1，5 个样本
- 采样步数 中位数 30，观测区间 20 - 40，5 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 7 - 8，5 个样本，取值集中（一致性 95%）
- 采样算法 最常用 euler，5 个样本，一致性 40%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，5 个样本
- 宽度 中位数 720，观测区间 512 - 1568，5 个样本
- 高度 中位数 880，观测区间 512 - 1280，5 个样本
