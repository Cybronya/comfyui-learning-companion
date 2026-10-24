---
name: unknown_workflow_sampler_unet_vae_195
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.79
common_nodes: [CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, 孤海注释]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1 精准扩图V2.0｜扩展比例(25%)｜扩展大小(300像素)｜图片比例(16_9)_2104416668545015809.json, 图片生成/图生图/Qwen Image 2.1 精准扩图｜扩展25%｜扩展300像素｜扩展为16_9_2104146400111054849.json, 图片生成/图生图/Qwen image 2.1 二合一工作流｜万物移除+局部重绘_2104111069567471617.json, 图片生成/图生图/Qwen_image_2.1_二合一工作流｜万物移除+局部重绘_2108746327097171969.json, 图片生成/图生图/Qwen_image_2.1_二合一工作流｜万物移除+局部重绘_2110191490327736321.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_195

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 精准扩图V2.0｜扩展比例(25%)｜扩展大小(300像素)｜图片比例(16_9)_2104416668545015809.json、图片生成/图生图/Qwen Image 2.1 精准扩图｜扩展25%｜扩展300像素｜扩展为16_9_2104146400111054849.json、图片生成/图生图/Qwen image 2.1 二合一工作流｜万物移除+局部重绘_2104111069567471617.json、图片生成/图生图/Qwen_image_2.1_二合一工作流｜万物移除+局部重绘_2108746327097171969.json、图片生成/图生图/Qwen_image_2.1_二合一工作流｜万物移除+局部重绘_2110191490327736321.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `DrawMaskOnImage` —— 4/5 个有
- `ImpactSwitch` —— 4/5 个有
- `Int` —— 4/5 个有
- `CR Prompt Text` —— 3/5 个有
- `Mask Fill Holes` —— 3/5 个有
- `孤海外补画板按方向` —— 2/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `Switch any [Crystools]` —— 1/5 个有
- `easy imageSizeByLongerSide` —— 1/5 个有
- `easy int` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
