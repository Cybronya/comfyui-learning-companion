---
name: unknown_workflow_ipadapter_sampler_clip_2
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7125
common_nodes: [CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, DetailTransfer, Fast Bypasser (rgthree), FreeU_V2, GetNode, ICLightConditioning, IPAdapterAdvanced, IPAdapterUnifiedLoader, Image Comparer (rgthree), ImageCASharpening+, KSampler (Efficient), LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, LoadAndApplyICLightUnet, LoadImage, SaveImage, SetNode, VAEDecode, VAEEncode, easy negative, easy positive, easy seed, easy showAnything, easy stylesSelector]
problems: []
missing: []
members: [图片生成/图生图/PS高阶-光影优化_1922110524610265090.json, 图片生成/图生图/PS高阶-光影自动优化（个人原创）_1911626362736836610.json]
source: knowledge_consolidation
---

# unknown_workflow_ipadapter_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/PS高阶-光影优化_1922110524610265090.json、图片生成/图生图/PS高阶-光影自动优化（个人原创）_1911626362736836610.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DetailTransfer`
- `Fast Bypasser (rgthree)`
- `FreeU_V2`
- `GetNode`
- `ICLightConditioning`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `KSampler (Efficient)`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `SaveImage`
- `SetNode`
- `VAEDecode`
- `VAEEncode`
- `easy negative`
- `easy positive`
- `easy seed`
- `easy showAnything`
- `easy stylesSelector`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 1/2 个有
- `Prompts Everywhere` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.7 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
