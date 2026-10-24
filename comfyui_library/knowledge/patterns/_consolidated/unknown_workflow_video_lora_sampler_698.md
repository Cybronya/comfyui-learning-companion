---
name: unknown_workflow_video_lora_sampler_698
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.918333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, ImageToMask, JoinImageWithAlpha, KSampler, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Wan文生透明gif动态表情_1975150708154568706.json, 视频生成/文生视频/透明视频生成_1974339364606054402.json, 视频生成/文生视频/透明视频素材制作_1978705872639692801.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_698

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/Wan文生透明gif动态表情_1975150708154568706.json、视频生成/文生视频/透明视频生成_1974339364606054402.json、视频生成/文生视频/透明视频素材制作_1978705872639692801.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `ImageToMask`
- `JoinImageWithAlpha`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `CR Text Concatenate` —— 2/3 个有
- `InvertMask` —— 2/3 个有
- `SaveVideoRGBA` —— 2/3 个有
- `ImageFromBatch+` —— 1/3 个有
- `InvertMask (segment anything)` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `PrimitiveString` —— 1/3 个有
- `String` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
