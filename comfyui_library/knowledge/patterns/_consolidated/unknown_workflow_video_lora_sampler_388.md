---
name: unknown_workflow_video_lora_sampler_388
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.992625
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2_ Motion调整运动速度_2007040869337145346.json, 视频生成/图生视频/Wan2.2_14B_图生视频 (4步加速)_1955097122862350338.json, 视频生成/图生视频/Wan2.2_14B_图生视频 (8步加速) + 提示词扩写_1952277132212948994.json, 视频生成/图生视频/Wan2.2_14B_图生视频 (8步加速)_1966753554679705601.json, 视频生成/图生视频/wan2.2图生视频加速流_1950004160121978881.json, 视频生成/文生视频/Wan2.2-14B-文生视频 (8步加速) + 提示词扩写_2064263911179898881.json, 视频生成/文生视频/Wan2.2_14B_文生视频 (8步加速) + 提示词扩写_1952277100332003330.json, 视频生成/文生视频/Wan2.2_14B_文生视频 (8步加速) + 提示词扩写_2063800321012494337.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_388

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/Wan2.2_ Motion调整运动速度_2007040869337145346.json、视频生成/图生视频/Wan2.2_14B_图生视频 (4步加速)_1955097122862350338.json、视频生成/图生视频/Wan2.2_14B_图生视频 (8步加速) + 提示词扩写_1952277132212948994.json、视频生成/图生视频/Wan2.2_14B_图生视频 (8步加速)_1966753554679705601.json、视频生成/图生视频/wan2.2图生视频加速流_1950004160121978881.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 7/8 个有
- `LayerUtility: PurgeVRAM V2` —— 6/8 个有
- `PathchSageAttentionKJ` —— 6/8 个有
- `LoadImage` —— 5/8 个有
- `SimpleMath+` —— 5/8 个有
- `WanImageToVideo` —— 5/8 个有
- `easy int` —— 5/8 个有
- `QwenLoader` —— 4/8 个有
- `TextBox` —— 4/8 个有
- `WanVideoPromptExtender` —— 4/8 个有
- `EmptyHunyuanLatentVideo` —— 3/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `WanMotionScale` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 75% |
| Prompt 约束强度(CFG) | 8 | 4 - 14 | 8 | 69% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4 - 14，8 个样本
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
