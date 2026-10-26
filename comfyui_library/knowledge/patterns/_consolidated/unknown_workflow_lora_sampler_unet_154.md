---
name: unknown_workflow_lora_sampler_unet_154
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9396
common_nodes: [AddLabel, CLIPLoader, CR Prompt Text, Fast Groups Bypasser (rgthree), INTConstant, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, QwenImageIntegratedKSampler, SaveImage, UNETLoader, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑 VS qwen_2030611704802971649.json, 图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑 VS qwen_2030612012606169089.json, 图片生成/图生图/小红书FireRed-Image-edit1.1多图编辑 vs qwen_2030612111793065986.json, 图片生成/图生图/小红书FireRed-Image-edit1.1多图编辑 vs qwen_2044369995022475265.json, 图片生成/图生图/超好用🔥小红书多图编辑-使用简单丝滑_2046877239186300930.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_154

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑 VS qwen_2030611704802971649.json、图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑 VS qwen_2030612012606169089.json、图片生成/图生图/小红书FireRed-Image-edit1.1多图编辑 vs qwen_2030612111793065986.json、图片生成/图生图/小红书FireRed-Image-edit1.1多图编辑 vs qwen_2044369995022475265.json、图片生成/图生图/超好用🔥小红书多图编辑-使用简单丝滑_2046877239186300930.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `AddLabel`
- `CLIPLoader`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `QwenImageIntegratedKSampler`
- `SaveImage`
- `UNETLoader`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 图生图 image-to-image | - | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | 1472 | 1472 - 1472 | 5 | 100% |
| 调度器 | 1104 | 1104 - 1104 | 5 | 100% |
| 重绘幅度 | 7.92762e+14 | 6.1076e+14 - 9.94435e+14 | 5 | 82% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 图生图 image-to-image，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1472，观测区间 1472 - 1472，5 个样本，取值集中（一致性 100%）
- 调度器 中位数 1104，观测区间 1104 - 1104，5 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 7.92762e+14，观测区间 6.1076e+14 - 9.94435e+14，5 个样本，取值集中（一致性 82%）
- 风险：重绘幅度 观测到 9.94435e+14，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
