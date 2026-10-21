---
name: unknown_workflow_sampler_clip_unet_44
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.853091
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text, CR SDXL Aspect Ratio, easy cleanGpuUsed]
members: [图片生成/文生图/1952243963510075394.json, 图片生成/文生图/1952725589155319810.json, 图片生成/文生图/1952728050552270850.json, 图片生成/文生图/1952737054142697473.json, 图片生成/文生图/1952787828896952322.json, 图片生成/文生图/1952836741905510402.json, 图片生成/文生图/1952892525439873025.json, 图片生成/文生图/1952903251559649281.json, 图片生成/文生图/1954932098835496961.json, 图片生成/文生图/1973958786882908161.json, 图片生成/文生图/Z-image base开源 文生图_2016345667848900609.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_44

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/1952243963510075394.json、图片生成/文生图/1952725589155319810.json、图片生成/文生图/1952728050552270850.json、图片生成/文生图/1952737054142697473.json、图片生成/文生图/1952787828896952322.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 10/11 个有
- `EmptySD3LatentImage` —— 9/11 个有
- `CR Text` —— 5/11 个有
- `CR SDXL Aspect Ratio` —— 3/11 个有
- `PreviewImage` —— 2/11 个有
- `easy cleanGpuUsed` —— 2/11 个有
- `CLIPLoaderGGUF` —— 1/11 个有
- `DapaoImageRatioLimitNode` —— 1/11 个有
- `FluxEmptyLatentSizePicker` —— 1/11 个有
- `Note Plus (mtb)` —— 1/11 个有
- `UnetLoaderGGUF` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 35 | 11 | 75% |
| Prompt 约束强度(CFG) | 3.5 | 2.5 - 4 | 11 | 78% |
| 采样算法 | euler | - | 11 | 91% |
| 调度器 | simple | - | 11 | 73% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 832x1152 (0.96MP) - 3:4 | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 35，11 个样本
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 2.5 - 4，11 个样本
- 采样算法 最常用 euler，11 个样本，一致性 91%
- 调度器 最常用 simple，11 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR SDXL Aspect Ratio、easy cleanGpuUsed
