---
name: unknown_workflow_video_clip_unet_12
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.8455
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/wan2.1基础文生视频001_1909164954489135106.json, 视频生成/文生视频/wan2.2-t2v-rapid-aio-最快文生视频_1950680019137941506.json, 视频生成/文生视频/wan2.2_t2v 文生视频_2058371729084469249.json, 视频生成/文生视频/wan2114BFusionx_text2videoFusionx-Y-Workflow_1934829108691935233.json, 视频生成/文生视频/wan2114BFusionx_text2videoFusionx-lora-Y-Workflow_1935539682874675202.json, 视频生成/文生视频/【官版】Wan2.2-Lightning4步加速文生视频_1955095898542018561.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_12

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/wan2.1基础文生视频001_1909164954489135106.json、视频生成/文生视频/wan2.2-t2v-rapid-aio-最快文生视频_1950680019137941506.json、视频生成/文生视频/wan2.2_t2v 文生视频_2058371729084469249.json、视频生成/文生视频/wan2114BFusionx_text2videoFusionx-Y-Workflow_1934829108691935233.json、视频生成/文生视频/wan2114BFusionx_text2videoFusionx-lora-Y-Workflow_1935539682874675202.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 5/6 个有
- `ModelSamplingSD3` —— 5/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `PrimitiveInt` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `ImpactSwitch` —— 1/6 个有
- `KSamplerAdvanced` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有
- `RH_LLMAPI_NODE` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 30 | 5 | 6% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 6 | 15% |
| 采样算法 | uni_pc | - | 6 | 33% |
| 调度器 | simple | - | 6 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 30，5 个样本，取值分散，一致性仅 6%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，6 个样本，取值分散，一致性仅 15%
- 采样算法 最常用 uni_pc，6 个样本，一致性 33%
- 调度器 最常用 simple，6 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
