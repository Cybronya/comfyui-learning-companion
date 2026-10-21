---
name: text_to_image_sampler_clip_unet_37
type: Text To Image
frequency: 10
level: moderate
coverage: 0.9809
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Seed]
members: [图片生成/文生图/1950469653418184706.json, 图片生成/文生图/1950688204880039937.json, 图片生成/文生图/1951288817326215170.json, 图片生成/文生图/1951489939009646593.json, 图片生成/文生图/1951794471434399745.json, 图片生成/文生图/1953071206398365698.json, 图片生成/文生图/1953188609090326530.json, 图片生成/文生图/1962669092442386433.json, 图片生成/文生图/1968285554058113025.json, 图片生成/文生图/1973765930620727297.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_37

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/1950469653418184706.json、图片生成/文生图/1950688204880039937.json、图片生成/文生图/1951288817326215170.json、图片生成/文生图/1951489939009646593.json、图片生成/文生图/1951794471434399745.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 9/10 个有
- `FluxGuidance` —— 7/10 个有
- `LoraLoaderModelOnly` —— 6/10 个有
- `FluxResolutionNode` —— 2/10 个有
- `LoadImage` —— 2/10 个有
- `RH_Prompter` —— 2/10 个有
- `RH_Translator` —— 2/10 个有
- `CR Seed` —— 1/10 个有
- `ImageConcanate` —— 1/10 个有
- `PreviewImage` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1280 | 10 | 78% |
| 高度 | 1024 | 512 - 1536 | 10 | 72% |
| 采样步数 | 20 | 8 - 30 | 10 | 59% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 10 | 40% |
| 采样算法 | euler | - | 10 | 90% |
| 调度器 | simple | - | 10 | 70% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1280，10 个样本
- 高度 中位数 1024，观测区间 512 - 1536，10 个样本
- 采样步数 中位数 20，观测区间 8 - 30，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，10 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，10 个样本，一致性 90%
- 调度器 最常用 simple，10 个样本，一致性 70%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Seed
