---
name: unknown_workflow_lora_sampler_clip_18
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.918333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [easy int]
members: [图片生成/文生图/1950418164367671297.json, 图片生成/文生图/1950531381078249473.json, 图片生成/文生图/1956141417343143938.json, 图片生成/文生图/1957735710319112194.json, 图片生成/文生图/1958426008351358977.json, 图片生成/文生图/1960618336759480321.json, 图片生成/文生图/1978391537375662082.json, 视频生成/文生视频/1950418164367671297.json, 视频生成/文生视频/1952591181077254146.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_18

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1950418164367671297.json、图片生成/文生图/1950531381078249473.json、图片生成/文生图/1956141417343143938.json、图片生成/文生图/1957735710319112194.json、图片生成/文生图/1958426008351358977.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 8/9 个有
- `GetImageRangeFromBatch` —— 6/9 个有
- `Text` —— 6/9 个有
- `Wan_video_prompt_generator` —— 6/9 个有
- `easy int` —— 6/9 个有
- `JWInteger` —— 3/9 个有
- `VHS_VideoCombine` —— 2/9 个有
- `LoadImage` —— 1/9 个有
- `LoadLatent` —— 1/9 个有
- `PMRF` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 9 | 67% |
| Prompt 约束强度(CFG) | 14 | 8 - 14 | 9 | 80% |
| 采样算法 | 3.5 | 1 - 3.5 | 9 | 56% |
| 调度器 | euler | - | 9 | 67% |
| 重绘幅度 | simple | - | 9 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，9 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 14，观测区间 8 - 14，9 个样本，取值集中（一致性 80%）
- 采样算法 中位数 3.5，观测区间 1 - 3.5，9 个样本
- 调度器 最常用 euler，9 个样本，一致性 67%
- 重绘幅度 最常用 simple，9 个样本，一致性 89%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：easy int
