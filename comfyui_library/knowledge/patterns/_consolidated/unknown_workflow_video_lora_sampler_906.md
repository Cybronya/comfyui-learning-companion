---
name: unknown_workflow_video_lora_sampler_906
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.894
common_nodes: [CLIPLoader, CLIPTextEncode, ImageLoader, Int, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SaveImage, TT_img_enc, TT_img_enc_v2, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/首尾帧V4_2000212534974181377.json, 视频生成/图生视频/（自用）Wan2.2 Smooth + Qwen VL3双参自动丝滑首尾帧V3_1982679380579237890.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_906

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/首尾帧V4_2000212534974181377.json、视频生成/图生视频/（自用）Wan2.2 Smooth + Qwen VL3双参自动丝滑首尾帧V3_1982679380579237890.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageLoader`
- `Int`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SaveImage`
- `TT_img_enc`
- `TT_img_enc_v2`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `ACE_ImageGetSize` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `DuckHideNode` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `MultiplePathsInput` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 86% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | normal | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 normal，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
