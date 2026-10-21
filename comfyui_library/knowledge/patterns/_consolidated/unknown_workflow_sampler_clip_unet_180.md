---
name: unknown_workflow_sampler_clip_unet_180
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.94
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1970786088950374402.json, 图片生成/文生图/FLUX批量生成小红书涨粉美女_1884421093896372225.json, 图片生成/文生图/文生图_FLUX_FP16+Teacache_1893650144414351362.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_180

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1970786088950374402.json、图片生成/文生图/FLUX批量生成小红书涨粉美女_1884421093896372225.json、图片生成/文生图/文生图_FLUX_FP16+Teacache_1893650144414351362.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 2/3 个有
- `EmptyImage` —— 1/3 个有
- `LoraLoader|pysssss` —— 1/3 个有
- `ModelSamplingFlux` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `ReferenceLatent` —— 1/3 个有
- `TeaCacheForImgGen` —— 1/3 个有
- `VAEEncode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1.72 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
