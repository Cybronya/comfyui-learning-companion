---
name: unknown_workflow_sampler_clip_unet_71
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.965111
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/image_z_image_turbo文生图_2085969344235917313.json, 图片生成/文生图/image_z_image_turbo造像 去除ai油腻味文生图_1996224077834633218.json, 图片生成/文生图/image_z_turbo_文生图_原版无Lora_2004484063744454657.json, 图片生成/文生图/ovis-image-文生图工作流_1997464079977627649.json, 图片生成/文生图/qwen Image2512-文生图片生成视觉海报平面设计-封装优化版_2092630964051734530.json, 图片生成/文生图/qwen-image-2512工作流_2067229524982587394.json, 图片生成/文生图/qwen-文生图_2090010243379060737.json, 图片生成/文生图/qwen2512文生图_2058014938349785090.json, 图片生成/文生图/zimage base_电影级风格LORA测试_2059298671640010754.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_71

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/image_z_image_turbo文生图_2085969344235917313.json、图片生成/文生图/image_z_image_turbo造像 去除ai油腻味文生图_1996224077834633218.json、图片生成/文生图/image_z_turbo_文生图_原版无Lora_2004484063744454657.json、图片生成/文生图/ovis-image-文生图工作流_1997464079977627649.json、图片生成/文生图/qwen Image2512-文生图片生成视觉海报平面设计-封装优化版_2092630964051734530.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 7/9 个有
- `ConditioningZeroOut` —— 4/9 个有
- `LoraLoaderModelOnly` —— 4/9 个有
- `SDXLEmptyLatentSizePicker+` —— 2/9 个有
- `easy promptLine` —— 2/9 个有
- `AddLabel` —— 1/9 个有
- `CR Text` —— 1/9 个有
- `CR Text Concatenate` —— 1/9 个有
- `LoadImage` —— 1/9 个有
- `Primitive string multiline [Crystools]` —— 1/9 个有
- `easy imageConcat` —— 1/9 个有
- `easy promptConcat` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 50 | 9 | 30% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 9 | 33% |
| 采样算法 | euler | - | 9 | 56% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1024x1024 (1.0) | - | 2 | 50% |
| 高度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 50，9 个样本，取值分散，一致性仅 30%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，9 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，9 个样本，一致性 56%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 最常用 1024x1024 (1.0)，2 个样本，一致性 50%
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（8/9 个样本）：Steps较低可能导致细节不足
