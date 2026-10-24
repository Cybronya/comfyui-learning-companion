---
name: image_to_image_sampler_unet_vae_38
type: Image To Image
frequency: 6
level: moderate
coverage: 0.9505
common_nodes: [CLIPLoader, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2 角色（四视图）_2091470849290362882.json, 图片生成/图生图/Krea2-edit-双图编辑_2076636562376454146.json, 图片生成/图生图/Krea2-turbo 角色四视图_2082484491444113410.json, 图片生成/图生图/krea2 服装转移 Outpaint_2079466311188566017.json, 图片生成/图生图/krea2_edit_single_ref_2076602213874626562.json, 图片生成/图生图/krea2_edit_two_ref_2076602231138377730.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_38

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Krea2 角色（四视图）_2091470849290362882.json、图片生成/图生图/Krea2-edit-双图编辑_2076636562376454146.json、图片生成/图生图/Krea2-turbo 角色四视图_2082484491444113410.json、图片生成/图生图/krea2 服装转移 Outpaint_2079466311188566017.json、图片生成/图生图/krea2_edit_single_ref_2076602213874626562.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `ResolutionSelector` —— 3/6 个有
- `ResizeImageMaskNode` —— 2/6 个有
- `CR Load LoRA` —— 1/6 个有
- `EmptyImage` —— 1/6 个有
- `EmptyLatentImage` —— 1/6 个有
- `ImageCompositeMasked` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `RMBG` —— 1/6 个有
- `SolidMask` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 6 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 6 | 44% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 512 | - | 1 | 100% |
| 高度 | 512 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，6 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，6 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
