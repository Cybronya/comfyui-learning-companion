---
name: image_to_image_sampler_clip_unet_126
type: Image To Image
frequency: 3
level: strong
coverage: 0.715333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LoadImage, PrimitiveFloat, Qwen3_VQA, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/反推提示词并使用提示词生图+全节点注释_2066420545037619201.json, 图片生成/图生图/001.Z-image生图巅峰011.反推洗图.json_2033741015990935554.json, 图片生成/图生图/001.Z-image生图巅峰016.文件夹批量反推洗图_2033752213864058881.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_126

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/反推提示词并使用提示词生图+全节点注释_2066420545037619201.json、图片生成/图生图/001.Z-image生图巅峰011.反推洗图.json_2033741015990935554.json、图片生成/图生图/001.Z-image生图巅峰016.文件夹批量反推洗图_2033752213864058881.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `PrimitiveFloat`
- `Qwen3_VQA`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImpactInt` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `DifferentialDiffusion` —— 1/3 个有
- `LatentFrequencyEnhancer_lrzjason` —— 1/3 个有
- `LoadImageListFromDir //Inspire` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RB_SaveImages` —— 1/3 个有
- `ResizeLongestToNode` —— 1/3 个有
- `easy forLoopEnd` —— 1/3 个有
- `easy forLoopStart` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 9 - 10 | 3 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 3 | 100% |
| 重绘幅度 | 0.9 | 0.9 - 1 | 3 | 95% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 9 - 10，3 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，3 个样本，一致性 100%
- 重绘幅度 中位数 0.9，观测区间 0.9 - 1，3 个样本，取值集中（一致性 95%）
