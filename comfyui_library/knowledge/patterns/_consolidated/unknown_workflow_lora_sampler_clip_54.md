---
name: unknown_workflow_lora_sampler_clip_54
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.883667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [CR Text]
members: [图片生成/文生图/1988974782064496641.json, 图片生成/文生图/FLUX 2-文生图_1993499987302612994.json, 图片生成/文生图/FLUX2 文生图-text to image_1993525496059281410.json, 图片生成/文生图/flux文生图(自用）_1891744030592774146.json, 图片生成/文生图/flux文生图（厨房风格模型 含例子示例整理）20260114_2011004615533268994.json, 图片生成/文生图/文生图（厨房风格模型）_2000758286930542594.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_54

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1988974782064496641.json、图片生成/文生图/FLUX 2-文生图_1993499987302612994.json、图片生成/文生图/FLUX2 文生图-text to image_1993525496059281410.json、图片生成/文生图/flux文生图(自用）_1891744030592774146.json、图片生成/文生图/flux文生图（厨房风格模型 含例子示例整理）20260114_2011004615533268994.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 5/6 个有
- `UNETLoader` —— 5/6 个有
- `CR Text` —— 4/6 个有
- `DualCLIPLoader` —— 4/6 个有
- `EmptySD3LatentImage` —— 4/6 个有
- `ModelSamplingFlux` —— 4/6 个有
- `CLIPLoader` —— 2/6 个有
- `EmptyLatentImage` —— 2/6 个有
- `SeedVR2` —— 2/6 个有
- `SeedVR2BlockSwap` —— 2/6 个有
- `SeedVR2ExtraArgs` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `LoadImage` —— 1/6 个有
- `NunchakuFluxDiTLoader` —— 1/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text
