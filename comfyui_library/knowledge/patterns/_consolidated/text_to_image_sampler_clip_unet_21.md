---
name: text_to_image_sampler_clip_unet_21
type: Text To Image
frequency: 3
level: strong
coverage: 0.837667
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: PurgeVRAM, easy seed]
members: [图片生成/文生图/1951256241010061314.json, 图片生成/文生图/1951258671458234369.json, 图片生成/文生图/1951489939009646593.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_21

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1951256241010061314.json、图片生成/文生图/1951258671458234369.json、图片生成/文生图/1951489939009646593.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `ImageConcanate` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 720 | 512 - 768 | 3 | 83% |
| 高度 | 1024 | 512 - 1280 | 3 | 66% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 720，观测区间 512 - 768，3 个样本，取值集中（一致性 83%）
- 高度 中位数 1024，观测区间 512 - 1280，3 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM、easy seed
