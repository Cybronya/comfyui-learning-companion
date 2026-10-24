---
name: unknown_workflow_video_sampler_clip_84
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.94075
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/DNR-wan2.2-官方文生视频_1952913163996041218.json, 视频生成/文生视频/Holocine——Wan2.2连续多分镜长视频生成_1982455092706197505.json, 视频生成/文生视频/Holocine电影分镜工作流_1982118673722818561.json, 视频生成/文生视频/Holocine电影分镜工作流（含提示词样例）_1987110613501587458.json, 视频生成/文生视频/Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1950043620181237761.json, 视频生成/文生视频/Wan2.2 14B+Teacache+Sage文生视频加速版工作流_1949879786422362114.json, 视频生成/文生视频/Wan2.2 14B-文生视频_1949911446906912770.json, 视频生成/文生视频/电影分镜创作test_1982334497687519233.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_84

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/DNR-wan2.2-官方文生视频_1952913163996041218.json、视频生成/文生视频/Holocine——Wan2.2连续多分镜长视频生成_1982455092706197505.json、视频生成/文生视频/Holocine电影分镜工作流_1982118673722818561.json、视频生成/文生视频/Holocine电影分镜工作流（含提示词样例）_1987110613501587458.json、视频生成/文生视频/Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1950043620181237761.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/8 个有
- `easy cleanGpuUsed` —— 5/8 个有
- `INTConstant` —— 4/8 个有
- `JWInteger` —— 3/8 个有
- `TeaCache` —— 2/8 个有
- `JjkText` —— 1/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `SeargePromptText` —— 1/8 个有
- `TextBox` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 62% |
| Prompt 约束强度(CFG) | 20 | 8 - 20 | 8 | 79% |
| 采样算法 | 3.5 | 1 - 3.5 | 8 | 74% |
| 调度器 | euler | - | 8 | 88% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 62%
- Prompt 约束强度(CFG) 中位数 20，观测区间 8 - 20，8 个样本
- 采样算法 中位数 3.5，观测区间 1 - 3.5，8 个样本
- 调度器 最常用 euler，8 个样本，一致性 88%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
