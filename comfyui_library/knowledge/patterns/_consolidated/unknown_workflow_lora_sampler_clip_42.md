---
name: unknown_workflow_lora_sampler_clip_42
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.858556
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image极致真实美女V3_1983588226168463361.json, 图片生成/文生图/Qwen-Image千问超美感人像 美女工作流_1966026218137096193.json, 图片生成/文生图/Qwen-Image极致真实美女V3_1983414394384228354.json, 图片生成/文生图/Qwen-Image极致真实美女V3版_1983878313116631041.json, 图片生成/文生图/Qwen-Image极致美感美女_1959887822478061569.json, 图片生成/文生图/Qwen-Image极致美感美女_1970348297275777025.json, 图片生成/文生图/QwenImage-RebalanceV1现实增强 VS 原版_1984151149953646593.json, 图片生成/文生图/qwenimage2512工作流_2006373077126483969.json, 图片生成/文生图/极致真实的人像质感(Qwen Image 文生图），三方案对比版_1984179316147847170.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_42

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen-Image极致真实美女V3_1983588226168463361.json、图片生成/文生图/Qwen-Image千问超美感人像 美女工作流_1966026218137096193.json、图片生成/文生图/Qwen-Image极致真实美女V3_1983414394384228354.json、图片生成/文生图/Qwen-Image极致真实美女V3版_1983878313116631041.json、图片生成/文生图/Qwen-Image极致美感美女_1959887822478061569.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 8/9 个有
- `LayerUtility: ImageReel` —— 7/9 个有
- `LayerUtility: ImageReelComposit` —— 7/9 个有
- `Text Multiline` —— 6/9 个有
- `AILab_QwenVL` —— 5/9 个有
- `LoadImage` —— 5/9 个有
- `ShowText|pysssss` —— 5/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `Any Switch (rgthree)` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 3/9 个有
- `LayerUtility: PurgeVRAM V2` —— 2/9 个有
- `PrimitiveInt` —— 2/9 个有
- `Text Concatenate` —— 2/9 个有
- `CustomAddLabel` —— 1/9 个有
- `Image Comparer (rgthree)` —— 1/9 个有
- `ImageBatchOneOrMore` —— 1/9 个有
- `Seed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 6 - 30 | 9 | 63% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 9 | 63% |
| 采样算法 | euler_ancestral | - | 9 | 78% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 6 - 30，9 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，9 个样本
- 采样算法 最常用 euler_ancestral，9 个样本，一致性 78%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
