---
name: unknown_workflow_video_sampler_clip_97
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.829143
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSampler, LoadImage, ModelSamplingSD3, PrimitiveInt, VAEDecode, WanVaceToVideo, WanVideoVACEStartToEndFrame]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/wan2.2-rapid-mega-aio-v12_1996131644778168321.json, 视频生成/文生视频/wan2.2文生视频_2021070799720943618.json, 视频生成/文生视频/▶Wan2.2-AllInOne-Mega-V12首尾帧、文生视频、图生视频工作流【好奇漫步】_1970121529851867137.json, 视频生成/文生视频/文生视频-AIO-MegaV7_1968182535878488065.json, 视频生成/文生视频/文生视频-AIO-MegaV7_2041408782072287234.json, 视频生成/文生视频/文生视频Wan2.2-MegaAIO_1968902178624741378.json, 视频生成/文生视频/文生视频千里江山图_2048964410516967425.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_97

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/wan2.2-rapid-mega-aio-v12_1996131644778168321.json、视频生成/文生视频/wan2.2文生视频_2021070799720943618.json、视频生成/文生视频/▶Wan2.2-AllInOne-Mega-V12首尾帧、文生视频、图生视频工作流【好奇漫步】_1970121529851867137.json、视频生成/文生视频/文生视频-AIO-MegaV7_1968182535878488065.json、视频生成/文生视频/文生视频-AIO-MegaV7_2041408782072287234.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `PrimitiveInt`
- `VAEDecode`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 6/7 个有
- `INTConstant` —— 4/7 个有
- `DuckHideNode` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `ShellAgentPluginInputInteger` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler_ancestral | - | 7 | 57% |
| 调度器 | beta | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，7 个样本，一致性 57%
- 调度器 最常用 beta，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
