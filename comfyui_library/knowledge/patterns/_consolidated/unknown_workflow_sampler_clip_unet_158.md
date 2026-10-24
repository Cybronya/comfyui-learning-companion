---
name: unknown_workflow_sampler_clip_unet_158
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.850375
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/AI分镜脚本生成器工作流_2098422425359839233.json, 图片生成/文生图/AI漫剧分镜生成器-故事文案转提示词_2094268434623320065.json, 图片生成/文生图/Dark Beast Z 黑兽 V2.5_2009627862525026305.json, 图片生成/文生图/Ernie 生图工作流(PE)_2048933090613010434.json, 图片生成/文生图/Ernie-Turbo 8步生图_2048944617202130945.json, 图片生成/文生图/ernie_image VS Z Image 文生图工作流_2045002159774769154.json, 图片生成/文生图/ernie_image_turbo_2046738945270095873.json, 图片生成/文生图/基于 Ernie-Image-Turbo 的高效文生图应用_2053669288694824961.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_158

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/AI分镜脚本生成器工作流_2098422425359839233.json、图片生成/文生图/AI漫剧分镜生成器-故事文案转提示词_2094268434623320065.json、图片生成/文生图/Dark Beast Z 黑兽 V2.5_2009627862525026305.json、图片生成/文生图/Ernie 生图工作流(PE)_2048933090613010434.json、图片生成/文生图/Ernie-Turbo 8步生图_2048944617202130945.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextGenerate` —— 7/8 个有
- `PreviewAny` —— 6/8 个有
- `PrimitiveStringMultiline` —— 6/8 个有
- `EmptyFlux2LatentImage` —— 5/8 个有
- `StringReplace` —— 5/8 个有
- `ConditioningZeroOut` —— 4/8 个有
- `EmptySD3LatentImage` —— 4/8 个有
- `ComfySwitchNode` —— 3/8 个有
- `JWInteger` —— 3/8 个有
- `PrimitiveBoolean` —— 3/8 个有
- `CR Prompt Text` —— 2/8 个有
- `TextEncodeQwenImageEditPlus` —— 2/8 个有
- `ModelSamplingAuraFlow` —— 1/8 个有
- `Seed (rgthree)` —— 1/8 个有
- `UnetLoaderGGUF` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 50 | 8 | 20% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 8 | 39% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 50，8 个样本，取值分散，一致性仅 20%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，8 个样本，取值分散，一致性仅 39%
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（5/8 个样本）：Steps较低可能导致细节不足
