---
name: unknown_workflow_sampler_clip_unet_8
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.875687
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [easy cleanGpuUsed, easy stylesSelector]
members: [图片生成/文生图/1938596846677712898.json, 图片生成/文生图/1944002361066946562.json, 图片生成/文生图/1946266988476030978.json, 图片生成/文生图/1948069349862060033.json, 图片生成/文生图/1950582399950327809.json, 图片生成/文生图/1952538030328492034.json, 图片生成/文生图/1954565922696654850.json, 图片生成/文生图/1954567812612288513.json, 图片生成/文生图/1955214645163278337.json, 图片生成/文生图/1955444043092299778.json, 图片生成/文生图/1955600731353989122.json, 图片生成/文生图/1955900129352011777.json, 图片生成/文生图/1959790560150237186.json, 图片生成/文生图/1986046293481050114.json, 图片生成/文生图/Qwen+朋友圈、海报设计+V1.0文生图_2100404141968412674.json, 图片生成/文生图/Qwen+朋友圈、海报设计+V1.0文生图_2100492455136288770.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_8

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/文生图/1938596846677712898.json、图片生成/文生图/1944002361066946562.json、图片生成/文生图/1946266988476030978.json、图片生成/文生图/1948069349862060033.json、图片生成/文生图/1950582399950327809.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 14/16 个有
- `ModelSamplingAuraFlow` —— 12/16 个有
- `LoraLoader` —— 11/16 个有
- `PreviewImage` —— 6/16 个有
- `UltimateSDUpscale` —— 5/16 个有
- `UpscaleModelLoader` —— 5/16 个有
- `easy cleanGpuUsed` —— 4/16 个有
- `JjkText` —— 3/16 个有
- `EmptyHunyuanLatentVideo` —— 2/16 个有
- `TeaCache` —— 1/16 个有
- `easy stylesSelector` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 4 - 30 | 16 | 58% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 5.5 | 16 | 55% |
| 采样算法 | euler | - | 16 | 88% |
| 调度器 | simple | - | 16 | 69% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| LoRA 模型强度 | 1 | 0.8 - 1 | 11 | 89% |
| LoRA 文本强度 | 1 | 0.8 - 1 | 11 | 90% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 4 - 30，16 个样本
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 5.5，16 个样本
- 采样算法 最常用 euler，16 个样本，一致性 88%
- 调度器 最常用 simple，16 个样本，一致性 69%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，11 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，观测区间 0.8 - 1，11 个样本，取值集中（一致性 90%）
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed、easy stylesSelector
