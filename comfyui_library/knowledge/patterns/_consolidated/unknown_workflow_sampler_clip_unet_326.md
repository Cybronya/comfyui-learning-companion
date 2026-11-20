---
name: unknown_workflow_sampler_clip_unet_326
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.856
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSamplerAdvanced, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image-文生图-同一提示词多样性出图TEXT TO IMAGE_1999698893736734721.json, 图片生成/文生图/Z-image-文生图-同一提示词多样性出图TEXT TO IMAGE_1999746796563857409.json, 图片生成/文生图/Z-image-文生图-多样性出图-海报电商二次元等_2028421841517285377.json, 图片生成/文生图/z-image-turbo 无限制模型 + 图形4倍放大 工作流_2018231007891169281.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_326

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-image-文生图-同一提示词多样性出图TEXT TO IMAGE_1999698893736734721.json、图片生成/文生图/Z-image-文生图-同一提示词多样性出图TEXT TO IMAGE_1999746796563857409.json、图片生成/文生图/Z-image-文生图-多样性出图-海报电商二次元等_2028421841517285377.json、图片生成/文生图/z-image-turbo 无限制模型 + 图形4倍放大 工作流_2018231007891169281.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 3/4 个有
- `CR Prompt Text` —— 3/4 个有
- `easy seed` —— 3/4 个有
- `CR Value` —— 1/4 个有
- `UltimateSDUpscale` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有
- `easy promptLine` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1052 | 576 - 1080 | 4 | 78% |
| 高度 | 1480 | 1024 - 1584 | 4 | 84% |
| 采样步数 | fixed | - | 4 | 75% |
| Prompt 约束强度(CFG) | 10 | 9 - 10 | 4 | 96% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 75% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1052，观测区间 576 - 1080，4 个样本
- 高度 中位数 1480，观测区间 1024 - 1584，4 个样本，取值集中（一致性 84%）
- 采样步数 最常用 fixed，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 10，观测区间 9 - 10，4 个样本，取值集中（一致性 96%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 75%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
