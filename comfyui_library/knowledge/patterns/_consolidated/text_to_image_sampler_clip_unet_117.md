---
name: text_to_image_sampler_clip_unet_117
type: Text To Image
frequency: 6
level: moderate
coverage: 0.829333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/001.Z-image生图巅峰003.文生图_2033719257393012738.json, 图片生成/文生图/001.Z-image生图巅峰008.文生图-语义理解升级_2033732546902630402.json, 图片生成/文生图/Krea-2 高真实感与卓越美学文生图_2069683043954151426.json, 图片生成/文生图/Krea2 MJ风格图片生成_2113335543516979201.json, 图片生成/文生图/Krea2-全能文生图2K直出-MJ平替_2082660207729143809.json, 图片生成/文生图/Z-image-turbo文生图_2055253303348482049.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_117

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/001.Z-image生图巅峰003.文生图_2033719257393012738.json、图片生成/文生图/001.Z-image生图巅峰008.文生图-语义理解升级_2033732546902630402.json、图片生成/文生图/Krea-2 高真实感与卓越美学文生图_2069683043954151426.json、图片生成/文生图/Krea2 MJ风格图片生成_2113335543516979201.json、图片生成/文生图/Krea2-全能文生图2K直出-MJ平替_2082660207729143809.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：83%

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
- `CR Text` —— 3/6 个有
- `GetNode` —— 3/6 个有
- `ImpactInt` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `ResolutionSelector` —— 2/6 个有
- `Seed (rgthree)` —— 2/6 个有
- `ClipLoaderGGUF` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有
- `ModelSamplingSD3` —— 1/6 个有
- `String Literal` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 512 - 1280 | 6 | 70% |
| 高度 | 1152 | 512 - 1280 | 6 | 70% |
| 采样步数 | 8 | 8 - 12 | 6 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 6 | 44% |
| 采样算法 | er_sde | - | 6 | 50% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 512 - 1280，6 个样本
- 高度 中位数 1152，观测区间 512 - 1280，6 个样本
- 采样步数 中位数 8，观测区间 8 - 12，6 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，6 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 er_sde，6 个样本，一致性 50%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
