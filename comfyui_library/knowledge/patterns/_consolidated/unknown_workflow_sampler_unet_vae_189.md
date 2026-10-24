---
name: unknown_workflow_sampler_unet_vae_189
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8258
common_nodes: [CLIPLoader, Image Comparer (rgthree), KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2026版Klein溶图专用【一致性强】_2047118708908232706.json, 图片生成/图生图/4步极速_真人转3D动漫_Flux2-Klein_2035916830765752321.json, 图片生成/图生图/KLEIN+BFS换头升级_2029476056725458945.json, 图片生成/图生图/qwen_image_edit 一键溶图（保留细节）_1968723830762086401.json, 图片生成/图生图/小红书开源FireRed Image Edit 1.1最强一键换装_2031672315548798977.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_189

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2026版Klein溶图专用【一致性强】_2047118708908232706.json、图片生成/图生图/4步极速_真人转3D动漫_Flux2-Klein_2035916830765752321.json、图片生成/图生图/KLEIN+BFS换头升级_2029476056725458945.json、图片生成/图生图/qwen_image_edit 一键溶图（保留细节）_1968723830762086401.json、图片生成/图生图/小红书开源FireRed Image Edit 1.1最强一键换装_2031672315548798977.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `Anything Everywhere3` —— 3/5 个有
- `GetImageSize` —— 3/5 个有
- `PainterFluxImageEdit` —— 3/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `ImageScaleToTotalPixels` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `ModelSamplingAuraFlow` —— 2/5 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 2/5 个有
- `AILab_QwenVL` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 5 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
