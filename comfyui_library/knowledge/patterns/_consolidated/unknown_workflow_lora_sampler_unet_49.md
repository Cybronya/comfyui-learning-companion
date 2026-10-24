---
name: unknown_workflow_lora_sampler_unet_49
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.972
common_nodes: [CLIPLoader, EmptyLatentImage, FluxKontextImageScale, FluxKontextMultiReferenceLatentMethod, KSampler, Krea2OstrisEditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeKrea2OstrisEdit, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2-风格参考迁移工作流_2099055746683064321.json, 图片生成/图生图/Krea2-风格参考迁移工作流_2099660682370306049.json, 图片生成/图生图/Krea2_Ostris_风格迁移工作流_2078078349246812162.json, 图片生成/图生图/Krea2_Ostris_风格迁移工作流_2079019378749825025.json, 图片生成/图生图/Krea2_Ostris_风格迁移工作流_2079401963980156929.json, 图片生成/图生图/Krea2编辑模型Remove移除（5750步）_2079277352131063809.json, 图片生成/图生图/Krea2编辑模型Remove移除（5750步）_2079758940988071937.json, 图片生成/图生图/Krea2编辑移除元素_2079366566331904001.json, 图片生成/图生图/krea2-多人姿态控制_2092223835184656385.json, 图片生成/图生图/krea2-最强姿态控制_2091531264733048833.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_49

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Krea2-风格参考迁移工作流_2099055746683064321.json、图片生成/图生图/Krea2-风格参考迁移工作流_2099660682370306049.json、图片生成/图生图/Krea2_Ostris_风格迁移工作流_2078078349246812162.json、图片生成/图生图/Krea2_Ostris_风格迁移工作流_2079019378749825025.json、图片生成/图生图/Krea2_Ostris_风格迁移工作流_2079401963980156929.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `FluxKontextImageScale`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `Krea2OstrisEditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeKrea2OstrisEdit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 8/10 个有
- `CR Prompt Text` —— 5/10 个有
- `BodyRatioMapperSDPoseRender` —— 2/10 个有
- `CheckpointLoaderSimple` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `PrimitiveStringMultiline` —— 2/10 个有
- `ResolutionSelector` —— 2/10 个有
- `SDPoseKeypointExtractor` —— 2/10 个有
- `BBoxYOLO` —— 1/10 个有
- `YOLOModelLoader` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 10 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 1024 | 752 - 1024 | 10 | 87% |
| 高度 | 1208 | 1024 - 1584 | 10 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，10 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 752 - 1024，10 个样本，取值集中（一致性 87%）
- 高度 中位数 1208，观测区间 1024 - 1584，10 个样本，取值集中（一致性 81%）
