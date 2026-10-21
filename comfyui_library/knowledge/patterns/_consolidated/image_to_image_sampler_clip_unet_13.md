---
name: image_to_image_sampler_clip_unet_13
type: Image To Image
frequency: 3
level: strong
coverage: 1
common_nodes: [CLIPTextEncode, FluxGuidance, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux2图像编辑工作流_1993535727956852738.json, 图片生成/文生图/Flux2洗图加速版_1994693315876560898.json, 视频生成/图生视频/1937024075837640705.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_13

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Flux2图像编辑工作流_1993535727956852738.json、图片生成/文生图/Flux2洗图加速版_1994693315876560898.json、视频生成/图生视频/1937024075837640705.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `ReferenceLatent` —— 2/3 个有
- `DualCLIPLoader` —— 1/3 个有
- `FluxKontextImageScale` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `ModelPatchTorchSettings` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.46 - 1 | 3 | 69% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.46 - 1，3 个样本
