---
name: unknown_workflow_video_sampler_clip_187
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.936333
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSampler, LoadImage, RIFE VFI, UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine, WanImageToVideo, WanVideoTeaCacheKJ]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/Wan2.1官方基础图生视频_2000497535640797186.json, 视频生成/图生视频/wan2.1_image_to_video(native nodes)_1903708781744656386.json, 视频生成/图生视频/wan2.1万相1080P60帧图生视频官方工作流版（提示词优化+高清放大+插帧）_1916481916541796354.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_187

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.1官方基础图生视频_2000497535640797186.json、视频生成/图生视频/wan2.1_image_to_video(native nodes)_1903708781744656386.json、视频生成/图生视频/wan2.1万相1080P60帧图生视频官方工作流版（提示词优化+高清放大+插帧）_1916481916541796354.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `KSampler`
- `LoadImage`
- `RIFE VFI`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `WanVideoTeaCacheKJ`

**可变部分**（部分 workflow 才有）：
- `Int` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ModelSamplingSD3` —— 2/3 个有
- `SkipLayerGuidanceWanVideo` —— 2/3 个有
- `UpscaleImageByUsingModel` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `ImageResizeKJ` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 3 | 84% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 3/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，3 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：发现KSampler但没有VAEDecode
