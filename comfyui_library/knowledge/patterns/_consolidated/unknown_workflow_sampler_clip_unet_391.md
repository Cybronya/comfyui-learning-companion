---
name: unknown_workflow_sampler_clip_unet_391
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.905
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingSD3, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/WAN2.2文生图_1953166220825718786.json, 图片生成/文生图/Wan2.2文生图_1949897867035107330.json, 图片生成/文生图/Wan2.2文生图最优实现_1950849465034940417.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_391

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/WAN2.2文生图_1953166220825718786.json、图片生成/文生图/Wan2.2文生图_1949897867035107330.json、图片生成/文生图/Wan2.2文生图最优实现_1950849465034940417.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingSD3`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyHunyuanLatentVideo` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `String Literal` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 3.5 | 3 | 56% |
| 采样算法 | heun | - | 3 | 33% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 0.5 | 0.3 - 1 | 3 | 51% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 3.5，3 个样本
- 采样算法 最常用 heun，3 个样本，一致性 33%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 0.5，观测区间 0.3 - 1，3 个样本
