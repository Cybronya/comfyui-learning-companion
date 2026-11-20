---
name: unknown_workflow_lora_sampler_clip_367
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9205
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, Text Concatenate, UNETLoader, VAEDecode, VAELoader, ttN text]
problems: []
missing: []
members: [平台全量/Flux 漫改二次元_1843928040714752002.json, 平台全量/[FLUX] Chrometype Logo_1864576775337492481.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_367

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Flux 漫改二次元_1843928040714752002.json、平台全量/[FLUX] Chrometype Logo_1864576775337492481.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `ttN text`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 1/2 个有
- `Image Overlay` —— 1/2 个有
- `Image Size to Number` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `JWIntegerSub` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
