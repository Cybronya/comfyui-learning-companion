---
name: unknown_workflow_video_lora_sampler_928
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9375
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, ImageLoader, ImageResizeKJv2, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/wam2.2 remix 动态优化_2030591840105275393.json, 视频生成/图生视频/丝滑首尾帧视频生成（Wan2.2 Smooth）_2033421738389803009.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_928

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/wam2.2 remix 动态优化_2030591840105275393.json、视频生成/图生视频/丝滑首尾帧视频生成（Wan2.2 Smooth）_2033421738389803009.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `ImageLoader`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Int` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有
- `TextInput_` —— 1/2 个有
- `WanFirstLastFrameToVideo` —— 1/2 个有
- `WanFunInpaintToVideo` —— 1/2 个有
- `wanBlockSwap` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 50% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 50% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 50%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
