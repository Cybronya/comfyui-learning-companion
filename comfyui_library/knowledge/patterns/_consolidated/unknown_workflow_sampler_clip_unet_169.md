---
name: unknown_workflow_sampler_clip_unet_169
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.99225
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSamplerAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/墨沫白皙质感Z -Image工作流_2067629087857926145.json, 图片生成/文生图/大洋IP形象的应用_2063092530673184769.json, 图片生成/文生图/文生图  z-image-turbo_2054380645274660866.json, 图片生成/文生图/文生图片_2061325270497456129.json, 图片生成/文生图/文生图片（Z-image)_2077687725708374017.json, 图片生成/文生图/文生图（解禁模型）：z-image-turbo_2054196239780065281.json, 图片生成/文生图/文生图（解禁模型）：z-image-turbo_2057705249091178498.json, 图片生成/文生图/超自然人像生成：qwen-image-2512加Z-image双采样器文生图_2022543014375198722.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_169

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/墨沫白皙质感Z -Image工作流_2067629087857926145.json、图片生成/文生图/大洋IP形象的应用_2063092530673184769.json、图片生成/文生图/文生图  z-image-turbo_2054380645274660866.json、图片生成/文生图/文生图片_2061325270497456129.json、图片生成/文生图/文生图片（Z-image)_2077687725708374017.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/8 个有
- `CR Text` —— 2/8 个有
- `Any Switch (rgthree)` —— 1/8 个有
- `ImpactInt` —— 1/8 个有
- `VAEEncode` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy promptList` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 972 | 720 - 1920 | 8 | 67% |
| 高度 | 1536 | 720 - 1920 | 8 | 74% |
| 采样步数 | randomize | - | 8 | 88% |
| Prompt 约束强度(CFG) | 9 | 9 - 10 | 8 | 95% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler_ancestral | - | 8 | 62% |
| 重绘幅度 | sgm_uniform | - | 8 | 62% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 972，观测区间 720 - 1920，8 个样本
- 高度 中位数 1536，观测区间 720 - 1920，8 个样本
- 采样步数 最常用 randomize，8 个样本，一致性 88%
- Prompt 约束强度(CFG) 中位数 9，观测区间 9 - 10，8 个样本，取值集中（一致性 95%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，8 个样本，一致性 62%
- 重绘幅度 最常用 sgm_uniform，8 个样本，一致性 62%
