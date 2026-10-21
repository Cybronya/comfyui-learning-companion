---
name: unknown_workflow_video_sampler_clip_106
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6244
common_nodes: [CLIPLoader, CLIPTextEncode, ImageLoader, Int, KSamplerAdvanced, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/2042258477560631298.json, 视频生成/图生视频/1982684734805426178.json, 视频生成/图生视频/1982359410183946242.json, 视频生成/图生视频/2016050718058221570.json, 视频生成/文生视频/漫剧最强工具WAN2.2最强首尾帧视频 （高动态）_2047997524845268994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_106

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2042258477560631298.json、视频生成/图生视频/1982684734805426178.json、视频生成/图生视频/1982359410183946242.json、视频生成/图生视频/2016050718058221570.json、视频生成/文生视频/漫剧最强工具WAN2.2最强首尾帧视频 （高动态）_2047997524845268994.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageLoader`
- `Int`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 4/5 个有
- `ImageResizeKJv2` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `ModelPatchTorchSettings` —— 3/5 个有
- `MultiplePathsInput` —— 3/5 个有
- `Qwen3_VQA` —— 3/5 个有
- `RIFE VFI` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `Any To Any` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `CR Text Concatenate` —— 1/5 个有
- `ImageResize+` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `PainterI2V` —— 1/5 个有
- `VHS_SelectFilename` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 60% |
| Prompt 约束强度(CFG) | 4 | 4 - 8 | 5 | 67% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | normal | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 8，5 个样本
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 normal，5 个样本，一致性 100%
