---
name: unknown_workflow_video_sampler_clip_161
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.49025
common_nodes: [CLIPLoader, CLIPTextEncode, Fast Groups Bypasser (rgthree), ImageLoader, ImageResizeKJv2, KSamplerAdvanced, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, RIFE VFI, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/AA--图生视频-高动态-wan2.2 Remix-首尾帧--Qwen3反推自动图生视频--加速版_2006627267346173953.json, 视频生成/图生视频/【Work-FIsh】WAN2.2-RemixV2-I2V首尾帧视频_1986365562794213377.json, 视频生成/图生视频/首尾帧视频-rh-WAN2.2-RemixV2-I2V-模板_2022797713682735106.json, 视频生成/文生视频/漫剧最强工具WAN2.2最强首尾帧视频 （高动态）_2047997524845268994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_161

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/AA--图生视频-高动态-wan2.2 Remix-首尾帧--Qwen3反推自动图生视频--加速版_2006627267346173953.json、视频生成/图生视频/【Work-FIsh】WAN2.2-RemixV2-I2V首尾帧视频_1986365562794213377.json、视频生成/图生视频/首尾帧视频-rh-WAN2.2-RemixV2-I2V-模板_2022797713682735106.json、视频生成/文生视频/漫剧最强工具WAN2.2最强首尾帧视频 （高动态）_2047997524845268994.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：49%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Fast Groups Bypasser (rgthree)`
- `ImageLoader`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RIFE VFI`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 3/4 个有
- `Int` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `wanBlockSwap` —— 3/4 个有
- `GetNode` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `MultiplePathsInputPlus` —— 1/4 个有
- `Qwen3_VQA` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `easy int` —— 1/4 个有
- `easy saveText` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 6 | 4 | 81% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | normal | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 6，4 个样本，取值集中（一致性 81%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 normal，4 个样本，一致性 100%
