---
name: unknown_workflow_sampler_clip_vae_11
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.830167
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [easy seed, CR Text, ImageSmartSharpen+, Note Plus (mtb)]
members: [图片生成/文生图/1928999965027155970.json, 图片生成/文生图/1936219766145323010.json, 图片生成/文生图/1940292234132766721.json, 图片生成/文生图/1941002485245100033.json, 图片生成/文生图/1951074575276814337.json, 图片生成/文生图/1951091883130953729.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_11

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1928999965027155970.json、图片生成/文生图/1936219766145323010.json、图片生成/文生图/1940292234132766721.json、图片生成/文生图/1941002485245100033.json、图片生成/文生图/1951074575276814337.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `UNETLoader` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `FluxGuidance` —— 3/6 个有
- `Int` —— 3/6 个有
- `Any Switch (rgthree)` —— 2/6 个有
- `DeepTranslatorTextNode` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `ModelSamplingFlux` —— 2/6 个有
- `Note Plus (mtb)` —— 2/6 个有
- `RH_LLMAPI_NODE` —— 2/6 个有
- `ShowText|pysssss` —— 2/6 个有
- `UnetLoaderGGUF` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `CFGZeroStar` —— 1/6 个有
- `ImageSmartSharpen+` —— 1/6 个有
- `easy seed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | 512 - 1440 | 6 | 63% |
| 高度 | 768 | 512 - 1024 | 6 | 73% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 896，观测区间 512 - 1440，6 个样本
- 高度 中位数 768，观测区间 512 - 1024，6 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：easy seed、CR Text、ImageSmartSharpen+、Note Plus (mtb)
