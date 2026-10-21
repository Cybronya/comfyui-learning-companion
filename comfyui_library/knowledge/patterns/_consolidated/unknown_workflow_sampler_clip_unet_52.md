---
name: unknown_workflow_sampler_clip_unet_52
type: Unknown Workflow
frequency: 10
level: weak
coverage: 0.9297
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio, easy clearCacheAll]
members: [图片生成/文生图/1955060284899692545.json, 图片生成/文生图/1955160402595233794.json, 图片生成/文生图/1955444251107606530.json, 图片生成/文生图/1955869888814436354.json, 图片生成/文生图/1985959773130633217.json, 图片生成/文生图/AI模特文生图_2005619684131172353.json, 图片生成/文生图/Qwen-Image ComfyUI原生工作流_2027264283821744129.json, 图片生成/文生图/Qwen-Image一键生成不知火舞真实版_2042047842927255553.json, 图片生成/文生图/Qwen2512腿精巨长腿背影杀腿部调节_2019638224775290882.json, 图片生成/文生图/Z Image 文生图_1993906798906327041.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_52

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/1955060284899692545.json、图片生成/文生图/1955160402595233794.json、图片生成/文生图/1955444251107606530.json、图片生成/文生图/1955869888814436354.json、图片生成/文生图/1985959773130633217.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 9/10 个有
- `CompressImages` —— 2/10 个有
- `ImageUpscaleWithModel` —— 2/10 个有
- `UpscaleModelLoader` —— 2/10 个有
- `VAEEncode` —— 2/10 个有
- `Image Comparer (rgthree)` —— 1/10 个有
- `ImageScaleBy` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/10 个有
- `PathchSageAttentionKJ` —— 1/10 个有
- `Text` —— 1/10 个有
- `easy clearCacheAll` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10.5 | 4 - 30 | 10 | 44% |
| Prompt 约束强度(CFG) | 1.5 | 1 - 4 | 10 | 46% |
| 采样算法 | euler | - | 10 | 90% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 0.1 - 1 | 10 | 58% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10.5，观测区间 4 - 30，10 个样本，取值分散，一致性仅 44%
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1 - 4，10 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 euler，10 个样本，一致性 90%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 0.1 - 1，10 个样本
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio、easy clearCacheAll
