---
name: unknown_workflow_video_sampler_clip_150
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.79375
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, ResolutionSelector, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/minimaxH3数字人_2084629238115823617.json, 数字人/数字人/minimaxH3数字人——8步极速版_2085194436836937730.json, 视频生成/图生视频/Minimax_h3_音乐MV+4步lora加速版_2085240329221005313.json, 视频生成/文生视频/Minimax_h3_产品广告视频+4步lora加速版_2085360762268250114.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_150

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/minimaxH3数字人_2084629238115823617.json、数字人/数字人/minimaxH3数字人——8步极速版_2085194436836937730.json、视频生成/图生视频/Minimax_h3_音乐MV+4步lora加速版_2085240329221005313.json、视频生成/文生视频/Minimax_h3_产品广告视频+4步lora加速版_2085360762268250114.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 3/4 个有
- `ComfyMathExpression` —— 3/4 个有
- `LoadAudio` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `MiniMaxH3SigmaShift` —— 3/4 个有
- `PathchSageAttentionKJ` —— 3/4 个有
- `SoundFlow_GetLength` —— 3/4 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `SimpleMath+` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `Float to Int` —— 1/4 个有
- `ImageFromBatch` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 4 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | normal | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 normal，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
