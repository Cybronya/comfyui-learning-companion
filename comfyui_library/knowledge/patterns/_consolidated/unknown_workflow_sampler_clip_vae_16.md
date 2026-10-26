---
name: unknown_workflow_sampler_clip_vae_16
type: Unknown Workflow
frequency: 11
level: weak
coverage: 0.830636
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/image_qwen_Image_2512_2018879224546856962.json, 图片生成/文生图/image_qwen_image_1953087441538322434.json, 图片生成/文生图/image_qwen_image_distill-10步蒸馏版_1960503206273085442.json, 图片生成/文生图/image_qwen_image文生图80 年代香港街景_1960500241579520002.json, 图片生成/文生图/image_qwen_image文生图_1984457132592480258.json, 图片生成/文生图/nucnhaku-qwen-image_1966414867236368386.json, 图片生成/文生图/nunchaku qwen加速文生图_1964600749260947457.json, 图片生成/文生图/nunchaku-qwen-image with lora_2073405156171018242.json, 图片生成/文生图/qwen出图对比（4步vs8步）_1955869888814436354.json, 图片生成/文生图/z-image base 插画 文生图 工作流_2028391930756866049.json, 图片生成/文生图/z-image base 插画 文生图 工作流_2028716736136089602.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_16

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/image_qwen_Image_2512_2018879224546856962.json、图片生成/文生图/image_qwen_image_1953087441538322434.json、图片生成/文生图/image_qwen_image_distill-10步蒸馏版_1960503206273085442.json、图片生成/文生图/image_qwen_image文生图80 年代香港街景_1960500241579520002.json、图片生成/文生图/image_qwen_image文生图_1984457132592480258.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 7/11 个有
- `LoraLoaderModelOnly` —— 5/11 个有
- `NunchakuQwenImageDiTLoader` —— 4/11 个有
- `CFGNorm` —— 2/11 个有
- `easy clearCacheAll` —— 2/11 个有
- `EmptyImage` —— 1/11 个有
- `HAIGC_SaveImagesToZip` —— 1/11 个有
- `NunchakuQwenImageLoraStackV3` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 36 | 11 | 29% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 11 | 35% |
| 采样算法 | euler | - | 11 | 82% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 36，11 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，11 个样本，取值分散，一致性仅 35%
- 采样算法 最常用 euler，11 个样本，一致性 82%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（6/11 个样本）：Steps较低可能导致细节不足
