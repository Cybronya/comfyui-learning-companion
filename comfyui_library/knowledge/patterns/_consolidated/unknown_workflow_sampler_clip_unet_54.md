---
name: unknown_workflow_sampler_clip_unet_54
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9556
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text]
members: [图片生成/文生图/1950509671901810689.json, 图片生成/文生图/1953829480836026370.json, 图片生成/文生图/1958551825752420353.json, 视频生成/文生视频/1949853875865042945.json, 视频生成/文生视频/1949831170026594305.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_54

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1950509671901810689.json、图片生成/文生图/1953829480836026370.json、图片生成/文生图/1958551825752420353.json、视频生成/文生视频/1949853875865042945.json、视频生成/文生视频/1949831170026594305.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyHunyuanLatentVideo` —— 4/5 个有
- `SaveImage` —— 4/5 个有
- `CR Text` —— 3/5 个有
- `PreviewImage` —— 2/5 个有
- `VHS_VideoCombine` —— 2/5 个有
- `EmptyLatentImage` —— 1/5 个有
- `JWInteger` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `LoraLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 60% |
| Prompt 约束强度(CFG) | 20 | 14 - 20 | 5 | 87% |
| 采样算法 | 3.5 | 1 - 3.5 | 5 | 67% |
| 调度器 | euler | - | 5 | 60% |
| 重绘幅度 | simple | - | 5 | 60% |
| 宽度 | 1280 | - | 1 | 100% |
| 高度 | 720 | - | 1 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 20，观测区间 14 - 20，5 个样本，取值集中（一致性 87%）
- 采样算法 中位数 3.5，观测区间 1 - 3.5，5 个样本
- 调度器 最常用 euler，5 个样本，一致性 60%
- 重绘幅度 最常用 simple，5 个样本，一致性 60%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text
