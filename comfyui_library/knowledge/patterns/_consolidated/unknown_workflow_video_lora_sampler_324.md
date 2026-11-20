---
name: unknown_workflow_video_lora_sampler_324
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.973125
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstMiddleLastFrameToVideo]
problems: []
missing: []
members: [视频生成/图生视频/首尾帧SmoothMix-V2.0_1977014698942046209.json, 视频生成/图生视频/首尾帧_多帧视频生成_SmoothMix2.0_2020439963401195521.json, 视频生成/图生视频/首尾帧图生视频流畅版_2079086796184571905.json, 视频生成/图生视频/首尾帧整理版  wan2.2 wan22  图生视频   视频生成_2078764896707244034.json, 视频生成/图生视频/首尾帧整理版  wan2.2 wan22  图生视频   视频生成_2087965953232556033.json, 视频生成/图生视频/首尾帧新版本   wan2.2 wan22  图生视频   视频生成_2078441258510536706.json, 视频生成/图生视频/首尾帧视频生成_多帧视频生成_SmoothMix2.0_2020867158913323009.json, 视频生成/图生视频/首尾帧视频生成_多帧视频生成_SmoothMix2.0_2046411920428769281.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_324

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/首尾帧SmoothMix-V2.0_1977014698942046209.json、视频生成/图生视频/首尾帧_多帧视频生成_SmoothMix2.0_2020439963401195521.json、视频生成/图生视频/首尾帧图生视频流畅版_2079086796184571905.json、视频生成/图生视频/首尾帧整理版  wan2.2 wan22  图生视频   视频生成_2078764896707244034.json、视频生成/图生视频/首尾帧整理版  wan2.2 wan22  图生视频   视频生成_2087965953232556033.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstMiddleLastFrameToVideo`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 2/8 个有
- `SetNode` —— 2/8 个有
- `ImageConcatMulti` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `easy float` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 8 | 100% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | simple | - | 8 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，8 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 simple，8 个样本，一致性 50%
