---
name: unknown_workflow_video_sampler_clip_37
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.931929
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Wan 2.2 Image to Video_2037082773323780097.json, 视频生成/图生视频/kone专属图生视频_2007088250229366786.json, 视频生成/图生视频/wan2.2 图生视频_2030667044726771713.json, 视频生成/图生视频/wan2_2_14B_I2V _4步加速_1998388818095013889.json, 视频生成/图生视频/wan2_2_14B_I2V图生视频加速工作流_1969634228759633922.json, 视频生成/图生视频/wan2_2_子弹时间 极速版_1984472483812229122.json, 视频生成/图生视频/万相 Wan2.2  sage+lightx2V加速 图生视频_1949865527068024834.json, 视频生成/图生视频/图生视频I2V  Wan2.2-Lightx2v加速_1987801301234987009.json, 视频生成/图生视频/首尾帧SmoothMix-V2.0_1977014698942046209.json, 视频生成/图生视频/首尾帧_多帧视频生成_SmoothMix2.0_2020439963401195521.json, 视频生成/图生视频/首尾帧图生视频流畅版_2079086796184571905.json, 视频生成/图生视频/首尾帧新版本   wan2.2 wan22  图生视频   视频生成_2078441258510536706.json, 视频生成/图生视频/首尾帧视频生成_多帧视频生成_SmoothMix2.0_2020867158913323009.json, 视频生成/图生视频/首尾帧视频生成_多帧视频生成_SmoothMix2.0_2046411920428769281.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_37

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/Wan 2.2 Image to Video_2037082773323780097.json、视频生成/图生视频/kone专属图生视频_2007088250229366786.json、视频生成/图生视频/wan2.2 图生视频_2030667044726771713.json、视频生成/图生视频/wan2_2_14B_I2V _4步加速_1998388818095013889.json、视频生成/图生视频/wan2_2_14B_I2V图生视频加速工作流_1969634228759633922.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 13/14 个有
- `ModelPatchTorchSettings` —— 12/14 个有
- `ImageResizeKJv2` —— 11/14 个有
- `UNETLoader` —— 8/14 个有
- `WanImageToVideo` —— 8/14 个有
- `INTConstant` —— 6/14 个有
- `SimpleMath+` —— 6/14 个有
- `UnetLoaderGGUF` —— 6/14 个有
- `WanFirstMiddleLastFrameToVideo` —— 6/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/14 个有
- `easy int` —— 2/14 个有
- `ConditioningZeroOut` —— 1/14 个有
- `ImageConcatMulti` —— 1/14 个有
- `easy float` —— 1/14 个有
- `easy showAnything` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 14 | 71% |
| Prompt 约束强度(CFG) | 6 | 4 - 8 | 14 | 78% |
| 采样算法 | 1 | 1 - 3.5 | 14 | 45% |
| 调度器 | euler | - | 14 | 100% |
| 重绘幅度 | simple | - | 14 | 79% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，14 个样本，一致性 71%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 8，14 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，14 个样本，取值分散，一致性仅 45%
- 调度器 最常用 euler，14 个样本，一致性 100%
- 重绘幅度 最常用 simple，14 个样本，一致性 79%
