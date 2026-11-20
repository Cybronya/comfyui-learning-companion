---
name: unknown_workflow_sampler_clip_unet_370
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.91375
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSamplerAdvanced, LatentColorMatch, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image文生图（多批次增加随机性）_2000461485551779841.json, 图片生成/文生图/z_image二采_2093223736949432322.json, 图片生成/文生图/z_image二采_2115620696171831297.json, 图片生成/文生图/z_image二采_2115668020759715842.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_370

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-image文生图（多批次增加随机性）_2000461485551779841.json、图片生成/文生图/z_image二采_2093223736949432322.json、图片生成/文生图/z_image二采_2115620696171831297.json、图片生成/文生图/z_image二采_2115668020759715842.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `LatentColorMatch`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 2/4 个有
- `ResolutionSelector` —— 2/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `easy promptList` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 10 | 10 - 20 | 4 | 65% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler_ancestral | - | 4 | 75% |
| 重绘幅度 | sgm_uniform | - | 4 | 100% |
| 宽度 | 1024 | 720 - 1024 | 4 | 86% |
| 高度 | 1024 | 1024 - 1280 | 4 | 90% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 10 - 20，4 个样本
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，4 个样本，一致性 75%
- 重绘幅度 最常用 sgm_uniform，4 个样本，一致性 100%
- 宽度 中位数 1024，观测区间 720 - 1024，4 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，观测区间 1024 - 1280，4 个样本，取值集中（一致性 90%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
