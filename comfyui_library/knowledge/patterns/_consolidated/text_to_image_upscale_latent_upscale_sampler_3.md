---
name: text_to_image_upscale_latent_upscale_sampler_3
type: Text To Image
frequency: 4
level: moderate
coverage: 0.9215
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, JoinStrings, KSampler, LatentUpscaleBy, Prompts Everywhere, SaveImage, VAEDecode, easy positive, easy promptLine]
problems: []
missing: []
members: [图片生成/文生图/二次元XL模型批量生图，2D日漫风格，内置大部分知名日漫IP人物_1997292709805244418.json, 图片生成/文生图/网红量产美女_1903338756966096897.json, 图片生成/文生图/风格化二次元模型批量文生图_1998691179854225409.json, 平台全量/网红量产（PONY）_1906588439066906625.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_sampler_3

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/二次元XL模型批量生图，2D日漫风格，内置大部分知名日漫IP人物_1997292709805244418.json、图片生成/文生图/网红量产美女_1903338756966096897.json、图片生成/文生图/风格化二次元模型批量文生图_1998691179854225409.json、平台全量/网红量产（PONY）_1906588439066906625.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
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
- `Anything Everywhere` —— 2/4 个有
- `Anything Everywhere3` —— 2/4 个有
- `KSamplerAdvanced` —— 2/4 个有
- `LoraLoader` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `easy negative` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10.5 | - | 2 | 95% |
| Prompt 约束强度(CFG) | 8.5 | 1 - 16 | 4 | 12% |
| 采样算法 | 2 | - | 2 | 100% |
| 调度器 | euler_ancestral | - | 4 | 50% |
| 重绘幅度 | 0.7 | - | 2 | 57% |
| 宽度 | 720 | 720 - 1280 | 4 | 72% |
| 高度 | 1280 | 720 - 1280 | 4 | 79% |
| LoRA 模型强度 | 0.8 | - | 2 | 100% |
| LoRA 文本强度 | 0.8 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10.5，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 8.5，观测区间 1 - 16，4 个样本，取值分散，一致性仅 12%
- 采样算法 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，4 个样本，一致性 50%
- 重绘幅度 中位数 0.7，样本不足，未给区间，2 个样本
- 宽度 中位数 720，观测区间 720 - 1280，4 个样本
- 高度 中位数 1280，观测区间 720 - 1280，4 个样本
- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 16，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
