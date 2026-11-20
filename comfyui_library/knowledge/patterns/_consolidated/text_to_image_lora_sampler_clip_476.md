---
name: text_to_image_lora_sampler_clip_476
type: Text To Image
frequency: 4
level: strong
coverage: 0.97425
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Wan2.2 超真实文生图+放大_1950719208512491521.json, 图片生成/文生图/Wan2.2文生图v2.0_1951114718939389953.json, 图片生成/文生图/Wan2.2真实系INS风组合调度非常规文生图工作流（海外版）_1955547695828144130.json, 图片生成/文生图/Wan2.2超绝真实系组合调度非常规文生图工作流_1950528087563948034.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_476

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Wan2.2 超真实文生图+放大_1950719208512491521.json、图片生成/文生图/Wan2.2文生图v2.0_1951114718939389953.json、图片生成/文生图/Wan2.2真实系INS风组合调度非常规文生图工作流（海外版）_1955547695828144130.json、图片生成/文生图/Wan2.2超绝真实系组合调度非常规文生图工作流_1950528087563948034.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_TextToStringAndSeed` —— 3/4 个有
- `JWInteger` —— 3/4 个有
- `PMRF` —— 3/4 个有
- `JjkText` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `SeedVR2` —— 1/4 个有
- `SeedVR2BlockSwap` —— 1/4 个有
- `Seed_` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 512 | 512 - 720 | 4 | 84% |
| 高度 | 512 | 512 - 1280 | 4 | 53% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 720，4 个样本，取值集中（一致性 84%）
- 高度 中位数 512，观测区间 512 - 1280，4 个样本
