---
name: unknown_workflow_video_sampler_clip_124
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.8304
common_nodes: [CLIPLoader, CLIPTextEncode, JWInteger, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoadImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/2043903106605387777.json, 视频生成/图生视频/1949968677410136066.json, 视频生成/图生视频/2003117819518681089.json, 视频生成/图生视频/1952579457632669698.json, 视频生成/图生视频/1952589946924273666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_124

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2043903106605387777.json、视频生成/图生视频/1949968677410136066.json、视频生成/图生视频/2003117819518681089.json、视频生成/图生视频/1952579457632669698.json、视频生成/图生视频/1952589946924273666.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `ModelSamplingSD3` —— 4/5 个有
- `PathchSageAttentionKJ` —— 4/5 个有
- `SaveImage` —— 3/5 个有
- `LoadLatent` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `SaveLatent` —— 1/5 个有
- `TT_img_enc_v2` —— 1/5 个有
- `ZML_SwitchOutputFive` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 40 | 5 | 0% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | lcm | - | 5 | 60% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 40，5 个样本，取值分散，一致性仅 0%
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，5 个样本，一致性 60%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 40，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
