---
name: text_to_image_upscale_latent_upscale_sampler
type: Text To Image
frequency: 3
level: moderate
coverage: 0.837667
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, JoinStrings, KSampler, LatentUpscaleBy, Prompts Everywhere, SaveImage, VAEDecode, easy positive, easy promptLine]
problems: []
missing: [easy positive, Prompts Everywhere, easy negative, easy promptLine]
members: [图片生成/文生图/1903338756966096897.json, 图片生成/文生图/二次元XL模型批量生图，2D日漫风格，内置大部分知名日漫IP人物_1997292709805244418.json, 图片生成/文生图/风格化二次元模型批量文生图_1998691179854225409.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_sampler

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1903338756966096897.json、图片生成/文生图/二次元XL模型批量生图，2D日漫风格，内置大部分知名日漫IP人物_1997292709805244418.json、图片生成/文生图/风格化二次元模型批量文生图_1998691179854225409.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `JoinStrings`
- `KSampler`
- `LatentUpscaleBy`
- `Prompts Everywhere`
- `SaveImage`
- `VAEDecode`
- `easy positive`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 2/3 个有
- `KSamplerAdvanced` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `easy negative` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 16 | 1 - 16 | 3 | 36% |
| 采样算法 | 2 | - | 2 | 100% |
| 调度器 | euler_ancestral | - | 3 | 67% |
| 重绘幅度 | normal | - | 3 | 67% |
| 宽度 | 720 | 720 - 1280 | 3 | 71% |
| 高度 | 1280 | 720 - 1280 | 3 | 76% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 0.8 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 16，观测区间 1 - 16，3 个样本，取值分散，一致性仅 36%
- 采样算法 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，3 个样本，一致性 67%
- 重绘幅度 最常用 normal，3 个样本，一致性 67%
- 宽度 中位数 720，观测区间 720 - 1280，3 个样本
- 高度 中位数 1280，观测区间 720 - 1280，3 个样本
- 风险：Prompt 约束强度(CFG) 观测到 16，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：easy positive、Prompts Everywhere、easy negative、easy promptLine
