---
name: unknown_workflow_lora_sampler_unet_211
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.914333
common_nodes: [CLIPLoader, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Moss_Image_EDIT 图像编辑工作流_2113950613439606785.json, 图片生成/图生图/小红书 FireRed-Image-Edit-1.1 换装_2030083792521662465.json, 视频生成/图生视频/MOSS_CharRef_角色参考生图_2114383277577560065.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_211

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Moss_Image_EDIT 图像编辑工作流_2113950613439606785.json、图片生成/图生图/小红书 FireRed-Image-Edit-1.1 换装_2030083792521662465.json、视频生成/图生视频/MOSS_CharRef_角色参考生图_2114383277577560065.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `MOSSImageOstrisEditModelPatch` —— 2/3 个有
- `SkipLayerGuidanceDiTSimple` —— 2/3 个有
- `TextEncodeMOSSImageOstrisEdit` —— 2/3 个有
- `EmptyFlux2LatentImage` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `TextEncodeQwenImageEditPlus` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 8 - 50 | 3 | 42% |
| Prompt 约束强度(CFG) | 3 | 1 - 3 | 3 | 60% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 772 | - | 2 | 66% |
| 高度 | 768 | - | 2 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 8 - 50，3 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 772，样本不足，未给区间，2 个样本
- 高度 中位数 768，样本不足，未给区间，2 个样本
