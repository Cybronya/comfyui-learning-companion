---
name: unknown_workflow_sampler_clip_checkpoint_21
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7475
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSamplerAdvanced, SaveImage, VAEDecode]
problems: []
missing: []
members: [comfyui-workflow-templates-json/sdxl_refiner_prompt_example.json, comfyui-workflow-templates-json/sdxl_simple_example.json, 图片生成/文生图/简单文生图_1946739229718405122.json, 图片生成/文生图/超酷炫魔法瓶_2056664936935411713.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_21

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（comfyui-workflow-templates-json/sdxl_refiner_prompt_example.json、comfyui-workflow-templates-json/sdxl_simple_example.json、图片生成/文生图/简单文生图_1946739229718405122.json、图片生成/文生图/超酷炫魔法瓶_2056664936935411713.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1024 | 4 | 67% |
| 高度 | 768 | 512 - 1024 | 4 | 67% |
| 采样步数 | fixed | - | 4 | 50% |
| Prompt 约束强度(CFG) | 22.5 | 20 - 25 | 4 | 89% |
| 采样算法 | 8 | 5.7 - 8 | 4 | 87% |
| 调度器 | euler | - | 4 | 75% |
| 重绘幅度 | normal | - | 4 | 75% |
| LoRA 模型强度 | 0.7 | - | 1 | 100% |
| LoRA 文本强度 | 0.5 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1024，4 个样本
- 高度 中位数 768，观测区间 512 - 1024，4 个样本
- 采样步数 最常用 fixed，4 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 22.5，观测区间 20 - 25，4 个样本，取值集中（一致性 89%）
- 采样算法 中位数 8，观测区间 5.7 - 8，4 个样本，取值集中（一致性 87%）
- 调度器 最常用 euler，4 个样本，一致性 75%
- 重绘幅度 最常用 normal，4 个样本，一致性 75%
- 风险：Prompt 约束强度(CFG) 观测到 25，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
