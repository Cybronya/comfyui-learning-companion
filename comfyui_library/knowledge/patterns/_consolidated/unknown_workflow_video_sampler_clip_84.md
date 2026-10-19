---
name: unknown_workflow_video_sampler_clip_84
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.962143
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageResizeKJv2, ImpactInt, KSamplerAdvanced, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/1985980018524336129.json, 视频生成/图生视频/2004910059593367554.json, 视频生成/图生视频/2010579095784001537.json, 视频生成/图生视频/1981312323858104321.json, 视频生成/图生视频/1986671035942662146.json, 视频生成/图生视频/1986030132559314946.json, 视频生成/文生视频/高动态电影探班短视频复刻首尾帧Wan2.2-Smooth Mix_1999803744537673729.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_84

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1985980018524336129.json、视频生成/图生视频/2004910059593367554.json、视频生成/图生视频/2010579095784001537.json、视频生成/图生视频/1981312323858104321.json、视频生成/图生视频/1986671035942662146.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `ImpactInt`
- `KSamplerAdvanced`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Fast Bypasser (rgthree)` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `Mute / Bypass Repeater (rgthree)` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `Seed (rgthree)` —— 6/7 个有
- `wanBlockSwap` —— 6/7 个有
- `ImageScaleBy` —— 5/7 个有
- `RIFE VFI` —— 5/7 个有
- `RHHiddenNodes` —— 3/7 个有
- `AILab_QwenVL` —— 1/7 个有
- `GetImageSize+` —— 1/7 个有
- `ImageLoader` —— 1/7 个有
- `ImageResize+` —— 1/7 个有
- `ImageStitch` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `LayerUtility: PurgeVRAM` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `RH_Nano_Banana_Image2Image` —— 1/7 个有
- `RH_Translator` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `easy positive` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 86% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 7 | 100% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler_ancestral | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 86%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
