---
name: unknown_workflow_video_sampler_clip_154
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.93175
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageResizeKJ, KSampler, LoadImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoEnhanceAVideoKJ, WanVideoTeaCacheKJ]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1-720P-SLG-图生视频_1902677106516733954.json, 视频生成/图生视频/Wan2.1-fun-Inp首尾帧视频_1911728190891720705.json, 视频生成/图生视频/【首尾帧】 wan2.1 首尾帧制作人像变化_1912684310967611393.json, 视频生成/图生视频/图生视频最-Wan2.1-Fun-Native +Reward-LoRA-最优实现_1912114565579243521.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_154

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Wan2.1-720P-SLG-图生视频_1902677106516733954.json、视频生成/图生视频/Wan2.1-fun-Inp首尾帧视频_1911728190891720705.json、视频生成/图生视频/【首尾帧】 wan2.1 首尾帧制作人像变化_1912684310967611393.json、视频生成/图生视频/图生视频最-Wan2.1-Fun-Native +Reward-LoRA-最优实现_1912114565579243521.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJ`
- `KSampler`
- `LoadImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoEnhanceAVideoKJ`
- `WanVideoTeaCacheKJ`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 3/4 个有
- `SkipLayerGuidanceWanVideo` —— 3/4 个有
- `TorchCompileModelWanVideo` —— 3/4 个有
- `WanFunInpaintToVideo` —— 3/4 个有
- `CFGZeroStarAndInit` —— 2/4 个有
- `INTConstant` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `PatchModelPatcherOrder` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `StringConstantMultiline` —— 2/4 个有
- `ImpactInt` —— 1/4 个有
- `WanImageToVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 4 | 80% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 4 | 100% |
| 采样算法 | uni_pc | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，4 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
