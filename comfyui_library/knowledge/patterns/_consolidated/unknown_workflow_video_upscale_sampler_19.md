---
name: unknown_workflow_video_upscale_sampler_19
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.934
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, Int, KSampler, LoadImage, ModelSamplingSD3, RIFE VFI, SkipLayerGuidanceWanVideo, UNETLoader, UpscaleImageByUsingModel, UpscaleModelLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine, WanImageToVideo, WanVideoTeaCacheKJ]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/2000497535640797186.json, 视频生成/图生视频/1916481916541796354.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_19

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2000497535640797186.json、视频生成/图生视频/1916481916541796354.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `Int`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `RIFE VFI`
- `SkipLayerGuidanceWanVideo`
- `UNETLoader`
- `UpscaleImageByUsingModel`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `WanVideoTeaCacheKJ`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 6 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
