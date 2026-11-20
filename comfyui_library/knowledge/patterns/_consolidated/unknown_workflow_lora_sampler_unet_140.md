---
name: unknown_workflow_lora_sampler_unet_140
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.847333
common_nodes: [CLIPLoader, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, QwenImageIntegratedKSampler, SaveImage, UNETLoader, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/漫画上色 可批量处理_2070067090685517825.json, 图片生成/图生图/漫画上色 可批量处理_2070071645481558018.json, 图片生成/图生图/漫画上色（本地批量详见视频）_2020397586309451778.json, 平台全量/【阡陌】Qwen-Eidt-2511零偏移图像编辑工作流_2009167349676511233.json, 平台全量/千问Qwen-edit-2511-白模转材质_2062786868227436546.json, 平台全量/换脸工作流（无需遮罩）_2087788702478196737.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_140

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/漫画上色 可批量处理_2070067090685517825.json、图片生成/图生图/漫画上色 可批量处理_2070071645481558018.json、图片生成/图生图/漫画上色（本地批量详见视频）_2020397586309451778.json、平台全量/【阡陌】Qwen-Eidt-2511零偏移图像编辑工作流_2009167349676511233.json、平台全量/千问Qwen-edit-2511-白模转材质_2062786868227436546.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImageIntegratedKSampler`
- `SaveImage`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 3/6 个有
- `PrimitiveInt` —— 3/6 个有
- `PrimitiveStringMultiline` —— 3/6 个有
- `UnetLoaderGGUF` —— 3/6 个有
- `TextInput_` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 图生图 image-to-image | - | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | 736 | 0 - 1472 | 6 | 0% |
| 调度器 | 552 | 0 - 1104 | 6 | 0% |
| 重绘幅度 | 7.32814e+14 | 999 - 1.06505e+15 | 6 | 24% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 图生图 image-to-image，6 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 中位数 736，观测区间 0 - 1472，6 个样本，取值分散，一致性仅 0%
- 调度器 中位数 552，观测区间 0 - 1104，6 个样本，取值分散，一致性仅 0%
- 重绘幅度 中位数 7.32814e+14，观测区间 999 - 1.06505e+15，6 个样本，取值分散，一致性仅 24%
- 风险：重绘幅度 观测到 1.06505e+15，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
