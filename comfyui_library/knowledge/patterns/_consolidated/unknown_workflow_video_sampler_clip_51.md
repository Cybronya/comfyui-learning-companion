---
name: unknown_workflow_video_sampler_clip_51
type: Unknown Workflow
frequency: 11
level: weak
coverage: 0.918818
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/wan2.2-i2v-rapid-aio-最快图生视频_1950686610079830017.json, 视频生成/图生视频/wan2.2-i2v图生视频_1951804301834440706.json, 视频生成/图生视频/wan2.2-ti2v-5B图生视频-与小时候的自己一起散步_1987307533339701250.json, 视频生成/图生视频/wan2.2-ti2v-5B图生视频_1951277844100009986.json, 视频生成/图生视频/图生视频工作流_1991844034222288897.json, 视频生成/图生视频/超简单--Wan2.2 All-in-on 目前最快2.2文生视频+图生视频工作流_2043858986851639297.json, 视频生成/图生视频/超简单--Wan2.2 All-in-on 目前最快2.2文生视频+图生视频工作流_2043862678724157442.json, 视频生成/文生视频/Aiwood-Wan2.2 All-in-on 目前最快2.2文生视频+图生视频工作流_1950654567312740354.json, 视频生成/文生视频/Wan2.2-t2v-rapid-AIO融合模型文生视频+4步快速生成_1951970286314926081.json, 视频生成/文生视频/Wan2.2官网14B图生视频&文生视频&5B文or图生视频_1950378020252073986.json, 视频生成/文生视频/wan2.2-t2v-rapid-aio-最快文生视频_1950680019137941506.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_51

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/wan2.2-i2v-rapid-aio-最快图生视频_1950686610079830017.json、视频生成/图生视频/wan2.2-i2v图生视频_1951804301834440706.json、视频生成/图生视频/wan2.2-ti2v-5B图生视频-与小时候的自己一起散步_1987307533339701250.json、视频生成/图生视频/wan2.2-ti2v-5B图生视频_1951277844100009986.json、视频生成/图生视频/图生视频工作流_1991844034222288897.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 9/11 个有
- `WanImageToVideo` —— 7/11 个有
- `EmptyHunyuanLatentVideo` —— 6/11 个有
- `PrimitiveInt` —— 3/11 个有
- `PrimitiveStringMultiline` —— 3/11 个有
- `Wan22ImageToVideoLatent` —— 3/11 个有
- `KSamplerAdvanced` —— 1/11 个有
- `Note Plus (mtb)` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 30 | 11 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 11 | 15% |
| 采样算法 | sa_solver | - | 11 | 73% |
| 调度器 | beta | - | 11 | 73% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 30，11 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，11 个样本，取值分散，一致性仅 15%
- 采样算法 最常用 sa_solver，11 个样本，一致性 73%
- 调度器 最常用 beta，11 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
