---
name: unknown_workflow_lora_sampler_clip_193
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.444
common_nodes: [Anything Everywhere, BasicScheduler, CLIPLoader, CLIPTextEncode, ClownOptions_ExtraOptions_Beta, ClownsharKSampler_Beta, ClownsharkChainsampler_Beta, EmptyLatentImage, GetNode, Image Comparer (rgthree), ImageStitch, LoraLoaderModelOnly, PreviewImage, PrimitiveFloat, ResizeImageMaskNode, ResolutionSelector, SaveImage, Seed (rgthree), SetNode, SharkOptions_Beta, SigmasPreview, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine]
problems: []
missing: []
members: [图片生成/文生图/Krea 2 深度探索：从控制结果，到控制过程 _ Controlling the Generati_2078072383788896258.json, 图片生成/文生图/Krea_2_深度探索_从控制结果，到控制过程_Controlling_the_Generati_2080936885467312130.json, 视频生成/图生视频/Krea+2+深度探索：从控制结果，到控制过程+_+Controlling+the+Generati_2088072723561009153.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_193

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Krea 2 深度探索：从控制结果，到控制过程 _ Controlling the Generati_2078072383788896258.json、图片生成/文生图/Krea_2_深度探索_从控制结果，到控制过程_Controlling_the_Generati_2080936885467312130.json、视频生成/图生视频/Krea+2+深度探索：从控制结果，到控制过程+_+Controlling+the+Generati_2088072723561009153.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：44%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ClownOptions_ExtraOptions_Beta`
- `ClownsharKSampler_Beta`
- `ClownsharkChainsampler_Beta`
- `EmptyLatentImage`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageStitch`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveFloat`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `SharkOptions_Beta`
- `SigmasPreview`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |
| 采样步数 | bong_tangent | - | 3 | 100% |
| Prompt 约束强度(CFG) | 2 | 2 - 2 | 3 | 100% |
| 采样算法 | -1 | -1 - -1 | 3 | 100% |
| 调度器 | 1 | 1 - 1 | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 采样步数 最常用 bong_tangent，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 2，观测区间 2 - 2，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 -1，观测区间 -1 - -1，3 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
