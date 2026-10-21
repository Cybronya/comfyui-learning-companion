---
name: unknown_workflow_sampler_clip_unet_91
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.965286
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerAdvanced, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [MathExpression|pysssss, easy cleanGpuUsed]
members: [图片生成/文生图/1950957566572568577.json, 图片生成/文生图/1957777125837303810.json, 视频生成/图生视频/1950898146819899393.json, 视频生成/图生视频/1950053385758269442.json, 视频生成/图生视频/1957799142709100545.json, 视频生成/图生视频/1956152665396969474.json, 视频生成/图生视频/1968502067780300801.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_91

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1950957566572568577.json、图片生成/文生图/1957777125837303810.json、视频生成/图生视频/1950898146819899393.json、视频生成/图生视频/1950053385758269442.json、视频生成/图生视频/1957799142709100545.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/7 个有
- `PathchSageAttentionKJ` —— 5/7 个有
- `LoadImage` —— 4/7 个有
- `EmptyHunyuanLatentVideo` —— 3/7 个有
- `MathExpression|pysssss` —— 3/7 个有
- `WanImageToVideo` —— 3/7 个有
- `Int` —— 2/7 个有
- `ModelPatchTorchSettings` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `INTConstant` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有
- `WanFunInpaintToVideo` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 57% |
| Prompt 约束强度(CFG) | 10 | 4 - 20 | 7 | 50% |
| 采样算法 | 1 | 1 - 3.5 | 7 | 40% |
| 调度器 | euler | - | 7 | 86% |
| 重绘幅度 | simple | - | 7 | 86% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 57%
- Prompt 约束强度(CFG) 中位数 10，观测区间 4 - 20，7 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，7 个样本，取值分散，一致性仅 40%
- 调度器 最常用 euler，7 个样本，一致性 86%
- 重绘幅度 最常用 simple，7 个样本，一致性 86%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：MathExpression|pysssss、easy cleanGpuUsed
