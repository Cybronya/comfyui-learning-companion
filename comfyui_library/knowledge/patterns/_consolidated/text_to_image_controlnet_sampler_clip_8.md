---
name: text_to_image_controlnet_sampler_clip_8
type: Text To Image
frequency: 2
level: weak
coverage: 0.663
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetNode, KSampler, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-IMAGE_ControlNet控制_1996388619596210177.json, 图片生成/文生图/节点系列12-Image Color Match节点_2013504175904137217.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_8

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-IMAGE_ControlNet控制_1996388619596210177.json、图片生成/文生图/节点系列12-Image Color Match节点_2013504175904137217.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetNode`
- `KSampler`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `Anything Everywhere3` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有
- `easy imageColorMatch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 13 | - | 2 | 77% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 50% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1128 | - | 2 | 64% |
| 高度 | 1152 | - | 2 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 13，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 50%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1128，样本不足，未给区间，2 个样本
- 高度 中位数 1152，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
