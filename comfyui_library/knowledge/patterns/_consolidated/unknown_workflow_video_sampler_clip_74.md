---
name: unknown_workflow_video_sampler_clip_74
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.585875
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/wan2.2图生成视频720_2012918046804942849.json, 图片生成/图生图/wan2.2首尾帧生成视频720p_2012896358499360770.json, 视频生成/图生视频/1119图生视频-1_1991093640317501442.json, 视频生成/图生视频/wan2.2图生成视频940_2012914151470927874.json, 视频生成/图生视频/wan2.2首尾帧生成视频_2012826950003331074.json, 视频生成/图生视频/wan2.2首尾帧生视频_2042865188126334978.json, 视频生成/图生视频/图生视频I2V  Wan2.2-Lightx2v加速_1987801301234987009.json, 视频生成/图生视频/图生视频流：首帧、首尾帧、首中尾帧 【大合集】_2016912682649128961.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_74

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/wan2.2图生成视频720_2012918046804942849.json、图片生成/图生图/wan2.2首尾帧生成视频720p_2012896358499360770.json、视频生成/图生视频/1119图生视频-1_1991093640317501442.json、视频生成/图生视频/wan2.2图生成视频940_2012914151470927874.json、视频生成/图生视频/wan2.2首尾帧生成视频_2012826950003331074.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/8 个有
- `INTConstant` —— 6/8 个有
- `LoadImageFromURL` —— 5/8 个有
- `ImageResizeKJv2` —— 4/8 个有
- `RIFE VFI` —— 4/8 个有
- `WanFirstLastFrameToVideo` —— 4/8 个有
- `LoadImage` —— 3/8 个有
- `PainterI2V_Wan2_2` —— 2/8 个有
- `WanImageToVideo` —— 2/8 个有
- `ImageBatchMulti` —— 1/8 个有
- `PainterI2V` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `WanMultiFrameRefToVideo` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 88% |
| Prompt 约束强度(CFG) | 4 | 4 - 8 | 8 | 71% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | normal | - | 8 | 88% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 88%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 8，8 个样本
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 normal，8 个样本，一致性 88%
