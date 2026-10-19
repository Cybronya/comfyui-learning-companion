---
name: unknown_workflow_video_sampler_clip_60
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.922111
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/2037082773323780097.json, 视频生成/图生视频/2007088250229366786.json, 视频生成/图生视频/2030667044726771713.json, 视频生成/图生视频/1950004160121978881.json, 视频生成/图生视频/2029088291949121537.json, 视频生成/图生视频/1998388818095013889.json, 视频生成/图生视频/1969634228759633922.json, 视频生成/图生视频/1984472483812229122.json, 视频生成/图生视频/2009159986848473089.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_60

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2037082773323780097.json、视频生成/图生视频/2007088250229366786.json、视频生成/图生视频/2030667044726771713.json、视频生成/图生视频/1950004160121978881.json、视频生成/图生视频/2029088291949121537.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 8/9 个有
- `UnetLoaderGGUF` —— 6/9 个有
- `ImageResizeKJv2` —— 5/9 个有
- `ModelPatchTorchSettings` —— 5/9 个有
- `UNETLoader` —— 3/9 个有
- `JWInteger` —— 2/9 个有
- `LayerUtility: PurgeVRAM` —— 2/9 个有
- `SimpleMath+` —— 2/9 个有
- `easy int` —— 2/9 个有
- `ConditioningZeroOut` —— 1/9 个有
- `FL_RIFE` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 67% |
| Prompt 约束强度(CFG) | 6 | 4 - 14 | 9 | 50% |
| 采样算法 | 1 | 1 - 1 | 9 | 100% |
| 调度器 | euler | - | 9 | 78% |
| 重绘幅度 | simple | - | 9 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 14，9 个样本
- 采样算法 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，9 个样本，一致性 78%
- 重绘幅度 最常用 simple，9 个样本，一致性 89%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
