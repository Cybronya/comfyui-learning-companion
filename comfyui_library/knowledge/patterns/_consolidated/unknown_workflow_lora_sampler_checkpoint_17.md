---
name: unknown_workflow_lora_sampler_checkpoint_17
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.857
common_nodes: [CR Text, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, ImpactSwitch, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlusPro_lrzjason, VAEDecode, easy promptLine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen分镜（角色、场景、动作一致性）_2001820121402359810.json, 视频生成/图生视频/摄影师-机位调度（Qwen）_2001859404263747586.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_checkpoint_17

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen分镜（角色、场景、动作一致性）_2001820121402359810.json、视频生成/图生视频/摄影师-机位调度（Qwen）_2001859404263747586.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImpactSwitch`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlusPro_lrzjason`
- `VAEDecode`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `ProcessString` —— 1/2 个有
- `RH_Jimeng4_Image2Image` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `RH_Nano_Banana2_Image2Image` —— 1/2 个有
- `ShowAnything|Mie` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1920 | - | 2 | 100% |
| 高度 | 1080 | - | 2 | 100% |
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_2s | - | 2 | 50% |
| 调度器 | bong_tangent | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1080，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，2 个样本，一致性 50%
- 调度器 最常用 bong_tangent，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
