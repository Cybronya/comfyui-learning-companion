---
name: unknown_workflow_sampler_clip_unet_67
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.941538
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/超强文生图Z-image-base_2016185060738732034.json, 图片生成/文生图/超真实文生图 Z-image  zimage   自然真实 没AI感_2046109081471029250.json, 图片生成/文生图/超真实文生图_2044746798295687169.json, 图片生成/文生图/通义千问 Qwen-image文生图丨中文渲染系列出图_1953691322731429889.json, 图片生成/文生图/通义千问Qwen-image文生图_1953143788371906562.json, 图片生成/文生图/通义千问Qwen-image文生图：媲美即梦出图_1952728050552270850.json, 图片生成/文生图/通义千问Qwen-文生图-8步出图_1959478057306370049.json, 图片生成/文生图/造相-Z-Image-Turbo-文生图工作流_2052340397992624130.json, 图片生成/文生图/阿清的AI模特文生图_2000461829648379906.json, 图片生成/文生图/陶器工作流_2071425077450727425.json, 图片生成/文生图/静帧画面工作流_2025778505488801793.json, 图片生成/文生图/黑森林Flux2文生图_1993588775534133249.json, 视频生成/图生视频/自己用：Qwen-Image +Lora_1955581722751483906.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_67

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/超强文生图Z-image-base_2016185060738732034.json、图片生成/文生图/超真实文生图 Z-image  zimage   自然真实 没AI感_2046109081471029250.json、图片生成/文生图/超真实文生图_2044746798295687169.json、图片生成/文生图/通义千问 Qwen-image文生图丨中文渲染系列出图_1953691322731429889.json、图片生成/文生图/通义千问Qwen-image文生图_1953143788371906562.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 12/13 个有
- `ConditioningZeroOut` —— 5/13 个有
- `LoraLoaderModelOnly` —— 5/13 个有
- `CR Text` —— 3/13 个有
- `FluxResolutionNode` —— 2/13 个有
- `CR SDXL Aspect Ratio` —— 1/13 个有
- `Image Filter Adjustments` —— 1/13 个有
- `LoraLoader` —— 1/13 个有
- `PrimitiveStringMultiline` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 50 | 13 | 42% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 13 | 51% |
| 采样算法 | euler | - | 13 | 77% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 50，13 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，13 个样本
- 采样算法 最常用 euler，13 个样本，一致性 77%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
