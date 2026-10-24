---
name: unknown_workflow_sampler_clip_unet_165
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.865875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image Base 文生图_2016498773949685761.json, 图片生成/文生图/Z-Image-Base-8steps 文生图_2063211651511443458.json, 图片生成/文生图/Z-Image-Base文生图V2（高画质版）_2016193102607818754.json, 图片生成/文生图/Z-Image-Turbo 极致写实文生图工作流_2084326650979905538.json, 图片生成/文生图/Z-Image-Turbo批量文生图_1993884946834145281.json, 图片生成/文生图/Z-image_zimage_文生图_超真实感_2042921269569527810.json, 图片生成/文生图/Z_Image_Turbo-文生图_2063504172338737154.json, 图片生成/文生图/【老金驿站】Qwen提速20%生成工作流_1953252280764141569.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_165

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Z-Image Base 文生图_2016498773949685761.json、图片生成/文生图/Z-Image-Base-8steps 文生图_2063211651511443458.json、图片生成/文生图/Z-Image-Base文生图V2（高画质版）_2016193102607818754.json、图片生成/文生图/Z-Image-Turbo 极致写实文生图工作流_2084326650979905538.json、图片生成/文生图/Z-Image-Turbo批量文生图_1993884946834145281.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 7/8 个有
- `PreviewImage` —— 5/8 个有
- `easy promptLine` —— 3/8 个有
- `LayerUtility: PurgeVRAM` —— 2/8 个有
- `MuyeSizeSelector` —— 1/8 个有
- `PathchSageAttentionKJ` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `WujiUpscaler` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 21 | 8 - 50 | 8 | 34% |
| Prompt 约束强度(CFG) | 2.25 | 1 - 4 | 8 | 48% |
| 采样算法 | euler | - | 8 | 50% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 21，观测区间 8 - 50，8 个样本，取值分散，一致性仅 34%
- Prompt 约束强度(CFG) 中位数 2.25，观测区间 1 - 4，8 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 euler，8 个样本，一致性 50%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
