---
name: unknown_workflow_video_sampler_clip_133
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9348
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2图生视频添加自定义动态字幕_1983546218196443137.json, 视频生成/图生视频/wan2.2-360旋转_1955685244381773826.json, 视频生成/图生视频/wan2.2图生视频加速流_1950004160121978881.json, 视频生成/图生视频/恶灵骑士wan2.2_1954715963700736001.json, 视频生成/图生视频/🐳wan2.2 图生视频 加速出图版🦋【官方模型】_1950018274672164866.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_133

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan2.2图生视频添加自定义动态字幕_1983546218196443137.json、视频生成/图生视频/wan2.2-360旋转_1955685244381773826.json、视频生成/图生视频/wan2.2图生视频加速流_1950004160121978881.json、视频生成/图生视频/恶灵骑士wan2.2_1954715963700736001.json、视频生成/图生视频/🐳wan2.2 图生视频 加速出图版🦋【官方模型】_1950018274672164866.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `PathchSageAttentionKJ` —— 4/5 个有
- `easy int` —— 3/5 个有
- `CR Text Concatenate` —— 2/5 个有
- `HAIGC_VideoSubtitleEnhanced` —— 1/5 个有
- `ImpactInt` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `孤海-取色器` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 100% |
| Prompt 约束强度(CFG) | 14 | 8 - 14 | 5 | 81% |
| 采样算法 | 1 | 1 - 1.5 | 5 | 82% |
| 调度器 | euler | - | 5 | 80% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 14，观测区间 8 - 14，5 个样本，取值集中（一致性 81%）
- 采样算法 中位数 1，观测区间 1 - 1.5，5 个样本，取值集中（一致性 82%）
- 调度器 最常用 euler，5 个样本，一致性 80%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
