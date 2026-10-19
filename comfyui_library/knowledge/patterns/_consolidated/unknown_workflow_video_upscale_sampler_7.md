---
name: unknown_workflow_video_upscale_sampler_7
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.912
common_nodes: [CLIPLoader, CLIPTextEncode, CR Upscale Image, Fast Bypasser (rgthree), Int, JjkText, KSamplerAdvanced, ModelPatchTorchSettings, ModelSamplingSD3, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, PrimitiveBoolean, RIFE VFI, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy ifElse, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/1980265954401824770.json, 视频生成/图生视频/1980235190960369666.json, 视频生成/文生视频/Smooth Mix wan2.2 电影质画质-加速版+自动提示词+视频放大+插帧-文生视频_1980255161958490113.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_7

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1980265954401824770.json、视频生成/图生视频/1980235190960369666.json、视频生成/文生视频/Smooth Mix wan2.2 电影质画质-加速版+自动提示词+视频放大+插帧-文生视频_1980255161958490113.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Upscale Image`
- `Fast Bypasser (rgthree)`
- `Int`
- `JjkText`
- `KSamplerAdvanced`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `RIFE VFI`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy ifElse`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 2/3 个有
- `CLIPVisionLoader` —— 2/3 个有
- `CR Text Replace` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `ShowText` —— 2/3 个有
- `WanImageToVideo` —— 2/3 个有
- `easy seed` —— 2/3 个有
- `CR Seed` —— 1/3 个有
- `CustomAddLabel` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `ImageStitch` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `RH_Prompter` —— 1/3 个有
- `TextBox` —— 1/3 个有
- `TextBox1` —— 1/3 个有
- `WanFirstLastFrameToVideo` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler_ancestral | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
