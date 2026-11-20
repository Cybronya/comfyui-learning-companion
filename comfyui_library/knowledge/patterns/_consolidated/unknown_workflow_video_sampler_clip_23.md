---
name: unknown_workflow_video_sampler_clip_23
type: Unknown Workflow
frequency: 17
level: strong
coverage: 0.785765
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, KSamplerAdvanced, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/wan2.2图生成视频720_2012918046804942849.json, 图片生成/图生图/wan2.2首尾帧生成视频720p_2012896358499360770.json, 视频生成/图生视频/1119图生视频-1_1991093640317501442.json, 视频生成/图生视频/1119图生视频_1991088603090759681.json, 视频生成/图生视频/DaSiWaWan2.2-动漫图生视频_2007793632560025602.json, 视频生成/图生视频/Wan2.2- Lightx2v 1030首、中、尾帧视频_1988980574498992130.json, 视频生成/图生视频/Wan2.2-Remix首、中、尾帧视频_1990058904107274241.json, 视频生成/图生视频/wan 首尾帧  图生视频   视频生成 wan2.2 wan22_2075187297317908481.json, 视频生成/图生视频/wan 首尾帧  图生视频   视频生成 wan2.2_2075871515157024769.json, 视频生成/图生视频/wan2.2 首尾帧  图生视频   视频生成 wan22_2078365547917570049.json, 视频生成/图生视频/wan2.2图生成视频940_2012914151470927874.json, 视频生成/图生视频/wan2.2首尾帧生成_2080463180828078082.json, 视频生成/图生视频/wan2.2首尾帧生成视频_2012826950003331074.json, 视频生成/图生视频/图生视频--SmoothMix-V2.0首尾多帧视频生成_2047195777209999362.json, 视频生成/图生视频/图生视频--SmoothMix-V2.0首尾多帧视频生成_2047212911168327682.json, 视频生成/图生视频/图生视频--SmoothMix-V2.0首尾多帧视频生成_2047468102497079298.json, 视频生成/图生视频/图生视频流：首帧、首尾帧、首中尾帧 【大合集】_2016912682649128961.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/wan2.2图生成视频720_2012918046804942849.json、图片生成/图生图/wan2.2首尾帧生成视频720p_2012896358499360770.json、视频生成/图生视频/1119图生视频-1_1991093640317501442.json、视频生成/图生视频/1119图生视频_1991088603090759681.json、视频生成/图生视频/DaSiWaWan2.2-动漫图生视频_2007793632560025602.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 16/17 个有
- `ModelPatchTorchSettings` —— 15/17 个有
- `ImageResizeKJv2` —— 13/17 个有
- `LoadImage` —— 12/17 个有
- `SimpleMath+` —— 10/17 个有
- `WanFirstMiddleLastFrameToVideo` —— 9/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/17 个有
- `LoadImageFromURL` —— 5/17 个有
- `RIFE VFI` —— 4/17 个有
- `PainterI2V_Wan2_2` —— 3/17 个有
- `WanFirstLastFrameToVideo` —— 3/17 个有
- `WanImageToVideo` —— 2/17 个有
- `ColorMatch_UTK` —— 1/17 个有
- `ImageBatchMulti` —— 1/17 个有
- `PainterI2V` —— 1/17 个有
- `WanMultiFrameRefToVideo` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 17 | 94% |
| Prompt 约束强度(CFG) | 6 | 4 - 6 | 17 | 81% |
| 采样算法 | 1 | 1 - 1 | 17 | 100% |
| 调度器 | euler | - | 17 | 100% |
| 重绘幅度 | normal | - | 17 | 41% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，17 个样本，一致性 94%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 6，17 个样本，取值集中（一致性 81%）
- 采样算法 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，17 个样本，一致性 100%
- 重绘幅度 最常用 normal，17 个样本，一致性 41%
