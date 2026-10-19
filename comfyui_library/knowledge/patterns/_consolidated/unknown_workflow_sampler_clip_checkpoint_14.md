---
name: unknown_workflow_sampler_clip_checkpoint_14
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.663333
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSamplerAdvanced, SaveImage, VAEDecode]
problems: []
missing: []
members: [comfyui-workflow-templates-json/sdxl_refiner_prompt_example.json, comfyui-workflow-templates-json/sdxl_simple_example.json, 图片生成/文生图/1946739229718405122.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_14

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（comfyui-workflow-templates-json/sdxl_refiner_prompt_example.json、comfyui-workflow-templates-json/sdxl_simple_example.json、图片生成/文生图/1946739229718405122.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `SaveImage`
- `VAEDecode`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1024 | 3 | 72% |
| 高度 | 1024 | 512 - 1024 | 3 | 72% |
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 25 | 20 - 25 | 3 | 90% |
| 采样算法 | 8 | 8 - 8 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | normal | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1024，3 个样本
- 高度 中位数 1024，观测区间 512 - 1024，3 个样本
- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 25，观测区间 20 - 25，3 个样本，取值集中（一致性 90%）
- 采样算法 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 normal，3 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 25，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
