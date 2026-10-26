---
name: unknown_workflow_lora_sampler_clip_22
type: Unknown Workflow
frequency: 14
level: weak
coverage: 0.9565
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-Image-文生图4步3秒一张图_1955060284899692545.json, 图片生成/文生图/Qwen-Image-生成角色三视图_1966728561858162689.json, 图片生成/文生图/Qwen-Image_1971395682378661889.json, 图片生成/文生图/Qwen-Image文生图古风女生_1953303428673040385.json, 图片生成/文生图/Qwen-Image文生图水墨人物_1953747187043848193.json, 图片生成/文生图/Qwen-Image文生图能吃苦_1953318467875295234.json, 图片生成/文生图/Qwen-Image文生图花和尚_1953307722135572481.json, 图片生成/文生图/Qwen-Image文生图（lora基础使用工作流）_1954190525895196674.json, 图片生成/文生图/Qwen-Image的8步加速_1954463793558515714.json, 图片生成/文生图/Qwen-image 8步极速生图_1954559302579187713.json, 图片生成/文生图/Qwen-image-2512 文生图_2009132641324376066.json, 图片生成/文生图/Qwen-image中式插画_1965257014656028674.json, 图片生成/文生图/Qwen-text-360_2080631673103937538.json, 图片生成/文生图/工作流基础系列8-QwenImage2512文生图工作流-基础向讲解此工作流_2044339209980354561.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_22

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Qwen-Image-文生图4步3秒一张图_1955060284899692545.json、图片生成/文生图/Qwen-Image-生成角色三视图_1966728561858162689.json、图片生成/文生图/Qwen-Image_1971395682378661889.json、图片生成/文生图/Qwen-Image文生图古风女生_1953303428673040385.json、图片生成/文生图/Qwen-Image文生图水墨人物_1953747187043848193.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEEncode` —— 3/14 个有
- `ImageUpscaleWithModel` —— 2/14 个有
- `PreviewImage` —— 2/14 个有
- `UpscaleModelLoader` —— 2/14 个有
- `Image Comparer (rgthree)` —— 1/14 个有
- `ImageScaleBy` —— 1/14 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/14 个有
- `LayerUtility: PurgeVRAM V2` —— 1/14 个有
- `PrimitiveStringMultiline` —— 1/14 个有
- `Seed (rgthree)` —— 1/14 个有
- `easy positive` —— 1/14 个有
- `easy promptList` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 25 | 14 | 41% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 14 | 47% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 79% |
| 重绘幅度 | 1 | 0.1 - 1 | 14 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 25，14 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，14 个样本，取值分散，一致性仅 47%
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 79%
- 重绘幅度 中位数 1，观测区间 0.1 - 1，14 个样本
- 高发问题（24/14 个样本）：Steps较低可能导致细节不足
