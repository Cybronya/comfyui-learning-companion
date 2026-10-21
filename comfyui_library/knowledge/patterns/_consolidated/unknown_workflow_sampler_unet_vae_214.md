---
name: unknown_workflow_sampler_unet_vae_214
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8865
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, DualCLIPLoader, KSamplerSelect, LoadImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: TextJoin, easy positive, easy stylesSelector]
members: [图片生成/文生图/1928700813932400642.json, 图片生成/文生图/1940416147244167169.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_214

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1928700813932400642.json、图片生成/文生图/1940416147244167169.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoaderGGUF` —— 1/2 个有
- `CLIPTextEncode` —— 1/2 个有
- `CLIPTextEncodeFlux` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `LayerUtility: TextJoin` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `easy positive` —— 1/2 个有
- `easy stylesSelector` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: TextJoin、easy positive、easy stylesSelector
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
