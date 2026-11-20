---
name: unknown_workflow_lora_sampler_clip_49
type: Unknown Workflow
frequency: 9
level: weak
coverage: 0.904556
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-Image-8步和4步对比_1955503632722661377.json, 图片生成/文生图/Qwen-Image-GGUF-Q4KS-4步极速生图_1955586331033288705.json, 图片生成/文生图/Qwen-Image-GGUF-Q4KS-4步极速生图_1970690059521454082.json, 图片生成/文生图/Z-image-base+lora文生图工作流_2016716307059707905.json, 图片生成/文生图/Z-image-base+lora文生图工作流_2058729767695904769.json, 图片生成/文生图/danotebook-qwen-image-2512_2062470910413725697.json, 图片生成/文生图/image_qwen_image2512_2006758711385133057.json, 图片生成/文生图/image_qwen_image2512_grid_scene_2006770240398565377.json, 图片生成/文生图/z-image滑块系列文生图_2057114517376688130.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_49

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Qwen-Image-8步和4步对比_1955503632722661377.json、图片生成/文生图/Qwen-Image-GGUF-Q4KS-4步极速生图_1955586331033288705.json、图片生成/文生图/Qwen-Image-GGUF-Q4KS-4步极速生图_1970690059521454082.json、图片生成/文生图/Z-image-base+lora文生图工作流_2016716307059707905.json、图片生成/文生图/Z-image-base+lora文生图工作流_2058729767695904769.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 8/9 个有
- `UNETLoader` —— 7/9 个有
- `easy seed` —— 4/9 个有
- `INTConstant` —— 2/9 个有
- `String Literal` —— 2/9 个有
- `UnetLoaderGGUF` —— 2/9 个有
- `AddLabel` —— 1/9 个有
- `ImageConcanate` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 28 | 9 | 12% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 9 | 12% |
| 采样算法 | euler | - | 9 | 78% |
| 调度器 | simple | - | 9 | 78% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 27/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 28，9 个样本，取值分散，一致性仅 12%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，9 个样本，取值分散，一致性仅 12%
- 采样算法 最常用 euler，9 个样本，一致性 78%
- 调度器 最常用 simple，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（27/9 个样本）：Steps较低可能导致细节不足
