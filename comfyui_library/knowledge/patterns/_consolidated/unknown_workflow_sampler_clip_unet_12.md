---
name: unknown_workflow_sampler_clip_unet_12
type: Unknown Workflow
frequency: 20
level: weak
coverage: 0.9654
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image-turbo-fp8 基础文生图_1994352646947475457.json, 图片生成/文生图/Z-image_zimage_文生图工作流_2019697317217046529.json, 图片生成/文生图/Z-image一键美女文生图_2023344603134431233.json, 图片生成/文生图/Z-image文生图18×流_2013868687253573633.json, 图片生成/文生图/Z-image瑜伽舞蹈动作控制_2025505912990994434.json, 图片生成/文生图/Z-image真实文生图_2027593525369507841.json, 图片生成/文生图/Z-image真实文生图_2096478812799328257.json, 图片生成/文生图/Z-image真实文生图无限制_2021242393848188929.json, 图片生成/文生图/Z-image高中女生校服丝袜写真_2025507598744690689.json, 图片生成/文生图/Z-image鬼术妖臀蜜桃臀_2027414828809199617.json, 图片生成/文生图/ZImage+LoRA文生图+VAE增加细节1_2084738891352993793.json, 图片生成/文生图/ZImage+LoRA文生图_2018160063252271106.json, 图片生成/文生图/ZImageBase文生图亮亮丝袜美女_2063529324246036482.json, 图片生成/文生图/ZImageBase文生图美女丝袜_2064861858766614530.json, 图片生成/文生图/ZImage女神_2063571918896328705.json, 图片生成/文生图/danotebook-qwen-image-2512_2062470910413725697.json, 图片生成/文生图/image_qwen_image2512_2006758711385133057.json, 图片生成/文生图/image_qwen_image2512_grid_scene_2006770240398565377.json, 图片生成/文生图/性感情趣内衣亮亮丝袜_2024871763326275585.json, 图片生成/文生图/本地专用 Z-Image 文生图_2005279973143445506.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_12

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/文生图/Z-image-turbo-fp8 基础文生图_1994352646947475457.json、图片生成/文生图/Z-image_zimage_文生图工作流_2019697317217046529.json、图片生成/文生图/Z-image一键美女文生图_2023344603134431233.json、图片生成/文生图/Z-image文生图18×流_2013868687253573633.json、图片生成/文生图/Z-image瑜伽舞蹈动作控制_2025505912990994434.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `VAELoader` —— 19/20 个有
- `LoraLoaderModelOnly` —— 17/20 个有
- `CompressImages` —— 6/20 个有
- `DuckHideNode` —— 3/20 个有
- `INTConstant` —— 2/20 个有
- `AV_VAELoader` —— 1/20 个有
- `ConditioningZeroOut` —— 1/20 个有
- `easy bookmark` —— 1/20 个有
- `孤海注释` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 50 | 20 | 5% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 20 | 70% |
| 采样算法 | euler | - | 20 | 95% |
| 调度器 | simple | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 50，20 个样本，取值分散，一致性仅 5%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，20 个样本
- 采样算法 最常用 euler，20 个样本，一致性 95%
- 调度器 最常用 simple，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（20/20 个样本）：Steps较低可能导致细节不足
