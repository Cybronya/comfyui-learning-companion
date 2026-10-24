---
name: text_to_image_sampler_clip_unet_40
type: Text To Image
frequency: 13
level: moderate
coverage: 0.979692
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Nunchaku双截棍4秒出图_1911939065036636162.json, 图片生成/文生图/Z-image两条对比工作流，测试不同参数对图片生成的影响_2047213255990448130.json, 图片生成/文生图/Z-image两条对比工作流，测试不同参数对图片生成的影响_2077645152755208194.json, 图片生成/文生图/Z-image基础文生图_1995758425134993409.json, 图片生成/文生图/Z-image文生图   自然风格首选_1993896427099193345.json, 图片生成/文生图/Z-image文生图_1993860952581931009.json, 图片生成/文生图/Z-image文生图_1996854775096516609.json, 图片生成/文生图/Z-image文生图（最新加速版）_1996623220235182081.json, 图片生成/文生图/Z-image文生图（非收敛-随机种子生效版）_1996582595745955841.json, 图片生成/文生图/boogu turbo文生图加速版V1_2067837356199202818.json, 图片生成/文生图/boogu turbo文生图加速版V1_2068270357320126466.json, 图片生成/文生图/boogu turbo文生图加速版工作流_2067860195535052801.json, 图片生成/文生图/boogu turbo文生图加速版工作流_2067879436858511361.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_40

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Nunchaku双截棍4秒出图_1911939065036636162.json、图片生成/文生图/Z-image两条对比工作流，测试不同参数对图片生成的影响_2047213255990448130.json、图片生成/文生图/Z-image两条对比工作流，测试不同参数对图片生成的影响_2077645152755208194.json、图片生成/文生图/Z-image基础文生图_1995758425134993409.json、图片生成/文生图/Z-image文生图   自然风格首选_1993896427099193345.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 12/13 个有
- `ConditioningZeroOut` —— 11/13 个有
- `CR Prompt Text` —— 8/13 个有
- `easy promptLine` —— 4/13 个有
- `Image Comparer (rgthree)` —— 3/13 个有
- `DualCLIPLoader` —— 1/13 个有
- `LayerUtility: PurgeVRAM` —— 1/13 个有
- `MultiLinePrompt` —— 1/13 个有
- `NunchakuFluxDiTLoader` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 544 - 1920 | 13 | 64% |
| 高度 | 1080 | 960 - 1920 | 13 | 76% |
| 采样步数 | 10 | 4 - 25 | 13 | 42% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 69% |
| 调度器 | simple | - | 13 | 38% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 544 - 1920，13 个样本
- 高度 中位数 1080，观测区间 960 - 1920，13 个样本
- 采样步数 中位数 10，观测区间 4 - 25，13 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 69%
- 调度器 最常用 simple，13 个样本，一致性 38%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（8/13 个样本）：Steps较低可能导致细节不足
