---
name: unknown_workflow_lora_sampler_unet_226
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.786
common_nodes: [CLIPLoader, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, PrimitiveInt, PrimitiveStringMultiline, QwenImageIntegratedKSampler, SaveImage, UNETLoader, UnetLoaderGGUF, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/漫画上色 可批量处理_2070067090685517825.json, 图片生成/图生图/漫画上色 可批量处理_2070071645481558018.json, 图片生成/图生图/漫画上色（本地批量详见视频）_2020397586309451778.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_226

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/漫画上色 可批量处理_2070067090685517825.json、图片生成/图生图/漫画上色 可批量处理_2070071645481558018.json、图片生成/图生图/漫画上色（本地批量详见视频）_2020397586309451778.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `QwenImageIntegratedKSampler`
- `SaveImage`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 图生图 image-to-image | - | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | 1472 | 1472 - 1472 | 3 | 100% |
| 调度器 | 1104 | 1104 - 1104 | 3 | 100% |
| 重绘幅度 | 1.05203e+15 | 9.21455e+14 - 1.06505e+15 | 3 | 94% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 图生图 image-to-image，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1472，观测区间 1472 - 1472，3 个样本，取值集中（一致性 100%）
- 调度器 中位数 1104，观测区间 1104 - 1104，3 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1.05203e+15，观测区间 9.21455e+14 - 1.06505e+15，3 个样本，取值集中（一致性 94%）
- 风险：重绘幅度 观测到 1.06505e+15，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
