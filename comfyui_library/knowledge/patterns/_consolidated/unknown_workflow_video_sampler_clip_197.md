---
name: unknown_workflow_video_sampler_clip_197
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.939
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, INTConstant, ImageResizeKJ, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, SimpleMath+, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, WanVideoNAG, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/▶WAN2.2-首尾帧加速流+马桶冲水_1998309830924361729.json, 视频生成/图生视频/▶WAN2.2-首尾帧加速流（描述词细化）_1993159656203812866.json, 视频生成/图生视频/首尾帧生成视频_2039547359687872514.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_197

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/▶WAN2.2-首尾帧加速流+马桶冲水_1998309830924361729.json、视频生成/图生视频/▶WAN2.2-首尾帧加速流（描述词细化）_1993159656203812866.json、视频生成/图生视频/首尾帧生成视频_2039547359687872514.json）

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
- `INTConstant`
- `ImageResizeKJ`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `SimpleMath+`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `WanVideoNAG`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `DF_Integer` —— 2/3 个有
- `FILM VFI` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `RH_Nano_Banana_Image2Image` —— 1/3 个有
- `SaveImage` —— 1/3 个有
- `UNETLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
