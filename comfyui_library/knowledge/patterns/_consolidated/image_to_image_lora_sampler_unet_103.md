---
name: image_to_image_lora_sampler_unet_103
type: Image To Image
frequency: 6
level: strong
coverage: 0.811167
common_nodes: [CLIPLoader, EmptySD3LatentImage, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2四视图生成流（参考图生成）2608_2096849439011991554.json, 图片生成/图生图/Krea2图生图四视图角色资产库（简易版4视图）_2103785269098008577.json, 图片生成/图生图/Krea2角色设定表（四视图）一键生成_2089486554589908993.json, 图片生成/图生图/krea2生成角色卡4视图_2083418547585376257.json, 图片生成/图生图/全新虚拟试衣！Krea 2 Outfit Transfer 双参考图编辑 ComfyUI 工作流_2080954078280114177.json, 图片生成/图生图/漫剧（四视图）_2090381002257555458.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_103

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Krea2四视图生成流（参考图生成）2608_2096849439011991554.json、图片生成/图生图/Krea2图生图四视图角色资产库（简易版4视图）_2103785269098008577.json、图片生成/图生图/Krea2角色设定表（四视图）一键生成_2089486554589908993.json、图片生成/图生图/krea2生成角色卡4视图_2083418547585376257.json、图片生成/图生图/全新虚拟试衣！Krea 2 Outfit Transfer 双参考图编辑 ComfyUI 工作流_2080954078280114177.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `GetImageSize` —— 4/6 个有
- `AddLabel` —— 3/6 个有
- `ImageConcatMulti` —— 3/6 个有
- `孤海注释` —— 2/6 个有
- `GetNode` —— 1/6 个有
- `ImageScaleBy` —— 1/6 个有
- `ResizeImageMaskNode` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `TTResolutionSelector` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 6 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，6 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
