---
name: unknown_workflow_video_sampler_clip_109
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7542
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageResizeKJv2, KSamplerAdvanced, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo]
problems: []
missing: []
members: [图片生成/图生图/WAN2.2 smooth超流畅质感加速激版首尾帧  支持_1995812290379264002.json, 视频生成/图生视频/Remix-V3.0-首尾帧视频_2033895649091002370.json, 视频生成/图生视频/WAN2.2 RemixV2超高动态艺术激版首尾帧  可加速_1996163879166263297.json, 视频生成/图生视频/WAN2.2 RemixV2首尾帧动态_2017121557004423170.json, 视频生成/图生视频/wan2212-SmoothMix首尾帧视频生成_1983512316119588865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_109

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/WAN2.2 smooth超流畅质感加速激版首尾帧  支持_1995812290379264002.json、视频生成/图生视频/Remix-V3.0-首尾帧视频_2033895649091002370.json、视频生成/图生视频/WAN2.2 RemixV2超高动态艺术激版首尾帧  可加速_1996163879166263297.json、视频生成/图生视频/WAN2.2 RemixV2首尾帧动态_2017121557004423170.json、视频生成/图生视频/wan2212-SmoothMix首尾帧视频生成_1983512316119588865.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 4/5 个有
- `INTConstant` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `wanBlockSwap` —— 4/5 个有
- `ImageConcatMulti` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `RIFE VFI` —— 3/5 个有
- `easy clearCacheAll` —— 3/5 个有
- `SimpleMath+` —— 2/5 个有
- `Anything Everywhere` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `TT_img_enc` —— 1/5 个有
- `YANC.MultilineString` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 80% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler_ancestral | - | 5 | 80% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，5 个样本，一致性 80%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
