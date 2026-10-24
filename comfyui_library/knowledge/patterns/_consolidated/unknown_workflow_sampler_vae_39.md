---
name: unknown_workflow_sampler_vae_39
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9075
common_nodes: [BasicGuider, BasicScheduler, KSamplerSelect, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX文生图 无损超级加速版 nunchaku_1937516933006671873.json, 图片生成/文生图/F拉斯_2075877608994201601.json, 图片生成/文生图/NunChaku超级加速1秒1张图1K Flux抽卡工作流_1915461235243159553.json, 图片生成/文生图/Nunchaku Krea文生图_1951252739424727041.json, 图片生成/文生图/Nunchaku-flux.1-Krea-dev-文生图-自动提示词-8步出图_1954524753786761217.json, 图片生成/文生图/nunchaku-flux.1-dev & flux.1 krea-dev-8步快速出图-自动提示词_1954518475970625537.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_39

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/FLUX文生图 无损超级加速版 nunchaku_1937516933006671873.json、图片生成/文生图/F拉斯_2075877608994201601.json、图片生成/文生图/NunChaku超级加速1秒1张图1K Flux抽卡工作流_1915461235243159553.json、图片生成/文生图/Nunchaku Krea文生图_1951252739424727041.json、图片生成/文生图/Nunchaku-flux.1-Krea-dev-文生图-自动提示词-8步出图_1954524753786761217.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `KSamplerSelect`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 5/6 个有
- `EmptyLatentImage` —— 5/6 个有
- `NunchakuFluxLoraLoader` —— 4/6 个有
- `FluxGuidance` —— 3/6 个有
- `ModelSamplingFlux` —— 3/6 个有
- `PreviewImage` —— 2/6 个有
- `RH_LLMAPI_NODE` —— 2/6 个有
- `RH_Translator` —— 2/6 个有
- `ShowText|pysssss` —— 2/6 个有
- `CLIPTextEncodeFlux` —— 1/6 个有
- `CR Overlay Text` —— 1/6 个有
- `EmptySD3LatentImage` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `SDVN Translate` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 784 - 1024 | 5 | 90% |
| 高度 | 1024 | 1024 - 1600 | 5 | 78% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 784 - 1024，5 个样本，取值集中（一致性 90%）
- 高度 中位数 1024，观测区间 1024 - 1600，5 个样本
