---
name: unknown_workflow_video_lora_sampler_617
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.986
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 图生视频-极速版_1950032039593558017.json, 视频生成/图生视频/Wan2.2 图生视频_1950814134864642049.json, 视频生成/图生视频/wan2.2-360旋转_1955685244381773826.json, 视频生成/图生视频/wan2.2极速图生视频+推理增强版_2029088291949121537.json, 视频生成/图生视频/恶灵骑士wan2.2_1954715963700736001.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_617

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 图生视频-极速版_1950032039593558017.json、视频生成/图生视频/Wan2.2 图生视频_1950814134864642049.json、视频生成/图生视频/wan2.2-360旋转_1955685244381773826.json、视频生成/图生视频/wan2.2极速图生视频+推理增强版_2029088291949121537.json、视频生成/图生视频/恶灵骑士wan2.2_1954715963700736001.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `SimpleMath+` —— 4/5 个有
- `LayerUtility: PurgeVRAM` —— 3/5 个有
- `easy int` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `CR Text Concatenate` —— 2/5 个有
- `CLIPVisionEncode` —— 1/5 个有
- `CLIPVisionLoader` —— 1/5 个有
- `FL_RIFE` —— 1/5 个有
- `ImageResize+` —— 1/5 个有
- `JWInteger` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `Text` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 40% |
| Prompt 约束强度(CFG) | 8 | 6 - 14 | 5 | 62% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | lcm | - | 5 | 60% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 40%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 14，5 个样本
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，5 个样本，一致性 60%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
