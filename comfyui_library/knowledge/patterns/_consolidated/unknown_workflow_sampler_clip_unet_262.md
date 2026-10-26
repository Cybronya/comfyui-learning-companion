---
name: unknown_workflow_sampler_clip_unet_262
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8618
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Image Comparer (rgthree), KSamplerAdvanced, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Z-Image全自动洗图_1999031680910417921.json, 图片生成/图生图/krea.2局部重绘PS版本_2105581533611511809.json, 图片生成/图生图/krea.2局部重绘PS版本_2108367394333872130.json, 图片生成/图生图/krea.2局部重绘（PS版本）_2070875464536776706.json, 图片生成/图生图/蓝佬klein调色工作流_2055123937016729601.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_262

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Z-Image全自动洗图_1999031680910417921.json、图片生成/图生图/krea.2局部重绘PS版本_2105581533611511809.json、图片生成/图生图/krea.2局部重绘PS版本_2108367394333872130.json、图片生成/图生图/krea.2局部重绘（PS版本）_2070875464536776706.json、图片生成/图生图/蓝佬klein调色工作流_2055123937016729601.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSamplerAdvanced`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `Int` —— 3/5 个有
- `PreviewImage` —— 2/5 个有
- `Anything Everywhere` —— 1/5 个有
- `CR Simple Image Compare` —— 1/5 个有
- `LatentBlend` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `MemoryCleaner` —— 1/5 个有
- `Qwen3_VQA` —— 1/5 个有
- `ReferenceLatent` —— 1/5 个有
- `ShowAnything|Mie` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 80% |
| Prompt 约束强度(CFG) | 8 | 4 - 13 | 5 | 65% |
| 采样算法 | 1 | 1 - 1.5 | 5 | 82% |
| 调度器 | euler_ancestral | - | 5 | 60% |
| 重绘幅度 | sgm_uniform | - | 5 | 60% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4 - 13，5 个样本
- 采样算法 中位数 1，观测区间 1 - 1.5，5 个样本，取值集中（一致性 82%）
- 调度器 最常用 euler_ancestral，5 个样本，一致性 60%
- 重绘幅度 最常用 sgm_uniform，5 个样本，一致性 60%
- 风险：Prompt 约束强度(CFG) 观测到 13，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
