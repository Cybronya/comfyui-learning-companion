---
name: image_to_image_sampler_clip_unet_9
type: Image To Image
frequency: 2
level: weak
coverage: 0.8005
common_nodes: [CLIPTextEncode, DualCLIPLoader, KSampler, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed]
members: [图片生成/文生图/1950930994167742465.json, 图片生成/文生图/1963796521585299457.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_9

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1950930994167742465.json、图片生成/文生图/1963796521585299457.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 22% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.65 | - | 2 | 77% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 0.8 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 22%
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.65，样本不足，未给区间，2 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、easy cleanGpuUsed
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
