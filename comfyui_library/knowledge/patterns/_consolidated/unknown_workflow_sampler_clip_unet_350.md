---
name: unknown_workflow_sampler_clip_unet_350
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.839667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/【电商】Landingpage落地页图生图洗图（官方版）_1952968291545452545.json, 图片生成/图生图/【电商】中文海报风格复刻_1952970918001840130.json, 图片生成/图生图/通义千问超级反推_1985771868139466754.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_350

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/【电商】Landingpage落地页图生图洗图（官方版）_1952968291545452545.json、图片生成/图生图/【电商】中文海报风格复刻_1952970918001840130.json、图片生成/图生图/通义千问超级反推_1985771868139466754.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 2/3 个有
- `RHHiddenNodes` —— 2/3 个有
- `RH_LLMAPI_NODE` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `easy imageSize` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 3 | 80% |
| Prompt 约束强度(CFG) | 3.5 | 3.5 - 4 | 3 | 94% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 3.5 - 4，3 个样本，取值集中（一致性 94%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
