---
name: text_to_image_sampler_clip_unet_112
type: Text To Image
frequency: 6
level: weak
coverage: 0.906167
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/BOOGU测试_2069366790278434817.json, 图片生成/文生图/Boogu Image 0.1 Turbo Fast Text-to-Image_2072998834151923712.json, 图片生成/文生图/Boogu 满血版文生图_2068176743512502273.json, 图片生成/文生图/Qwen image 2512 文生图_2006546319086723074.json, 图片生成/文生图/krea 2双采工作流_2072894117721497602.json, 图片生成/文生图/既生瑜何生亮，Zimage_VS_2512_2006333323450261505.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_112

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/BOOGU测试_2069366790278434817.json、图片生成/文生图/Boogu Image 0.1 Turbo Fast Text-to-Image_2072998834151923712.json、图片生成/文生图/Boogu 满血版文生图_2068176743512502273.json、图片生成/文生图/Qwen image 2512 文生图_2006546319086723074.json、图片生成/文生图/krea 2双采工作流_2072894117721497602.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/6 个有
- `easy promptList` —— 5/6 个有
- `ImageConcanate` —— 4/6 个有
- `AddLabel` —— 2/6 个有
- `CR Seed` —— 2/6 个有
- `easy globalSeed` —— 2/6 个有
- `LatentUpscaleBy` —— 1/6 个有
- `ProcessString` —— 1/6 个有
- `SizeSelector` —— 1/6 个有
- `VAEDecodeTiled` —— 1/6 个有
- `easy promptLine` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 50 | 6 | 1% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 6 | 29% |
| 采样算法 | lcm | - | 6 | 33% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 1 | 0.55 - 1 | 6 | 82% |
| 宽度 | 1024 | 928 - 1024 | 6 | 95% |
| 高度 | 1536 | 1024 - 1664 | 6 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 50，6 个样本，取值分散，一致性仅 1%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，6 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 lcm，6 个样本，一致性 33%
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.55 - 1，6 个样本，取值集中（一致性 82%）
- 宽度 中位数 1024，观测区间 928 - 1024，6 个样本，取值集中（一致性 95%）
- 高度 中位数 1536，观测区间 1024 - 1664，6 个样本，取值集中（一致性 80%）
- 高发问题（9/6 个样本）：Steps较低可能导致细节不足
