---
name: unknown_workflow_video_sampler_clip_80
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.951875
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/Wan 2.2 Image to Video_2037082773323780097.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_2114564471111905282.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_2114671381353943042.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 图生视频加速版_1950026797163438082.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 图生视频（工作室自用）_2027632357276131329.json, 视频生成/图生视频/Wan2.2 14B+LightX2V超极速图生视频_1952642819863318529.json, 视频生成/图生视频/Wan2.2 图生视频-极速版_1950032039593558017.json, 视频生成/图生视频/wan2.2极速图生视频+推理增强版_2029088291949121537.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_80

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/Wan 2.2 Image to Video_2037082773323780097.json、视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_2114564471111905282.json、视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_2114671381353943042.json、视频生成/图生视频/Wan2.2 14B+LightX2V 图生视频加速版_1950026797163438082.json、视频生成/图生视频/Wan2.2 14B+LightX2V 图生视频（工作室自用）_2027632357276131329.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `JWInteger` —— 3/8 个有
- `SimpleMath+` —— 2/8 个有
- `easy int` —— 2/8 个有
- `CLIPVisionEncode` —— 1/8 个有
- `CLIPVisionLoader` —— 1/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `FL_RIFE` —— 1/8 个有
- `ImageResize+` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `Text` —— 1/8 个有
- `UnetLoaderGGUF` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 88% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 8 | 89% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | lcm | - | 8 | 88% |
| 重绘幅度 | simple | - | 8 | 88% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 88%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，8 个样本，取值集中（一致性 89%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，8 个样本，一致性 88%
- 重绘幅度 最常用 simple，8 个样本，一致性 88%
