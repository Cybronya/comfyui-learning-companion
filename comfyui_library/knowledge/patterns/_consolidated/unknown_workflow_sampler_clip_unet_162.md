---
name: unknown_workflow_sampler_clip_unet_162
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.93625
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyLatentImage, KSamplerAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image-文生图-同一提示词多样性出图TEXT TO IMAGE_1999698893736734721.json, 图片生成/文生图/Z-image-文生图-同一提示词多样性出图TEXT TO IMAGE_1999746796563857409.json, 图片生成/文生图/Z-image文生图Beyond Reality 人像写真_2003868030209826818.json, 图片生成/文生图/人像写真(文生图)- Beyond Reality Z-image_2003840206602182657.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_162

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-image-文生图-同一提示词多样性出图TEXT TO IMAGE_1999698893736734721.json、图片生成/文生图/Z-image-文生图-同一提示词多样性出图TEXT TO IMAGE_1999746796563857409.json、图片生成/文生图/Z-image文生图Beyond Reality 人像写真_2003868030209826818.json、图片生成/文生图/人像写真(文生图)- Beyond Reality Z-image_2003840206602182657.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `easy seed` —— 2/4 个有
- `easy promptLine` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 4 | 100% |
| 高度 | 1520 | 1480 - 1920 | 4 | 89% |
| 采样步数 | fixed | - | 4 | 50% |
| Prompt 约束强度(CFG) | 12.5 | 10 - 15 | 4 | 80% |
| 采样算法 | 1.5 | 1 - 2 | 4 | 67% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1520，观测区间 1480 - 1920，4 个样本，取值集中（一致性 89%）
- 采样步数 最常用 fixed，4 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 12.5，观测区间 10 - 15，4 个样本，取值集中（一致性 80%）
- 采样算法 中位数 1.5，观测区间 1 - 2，4 个样本
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 15，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
