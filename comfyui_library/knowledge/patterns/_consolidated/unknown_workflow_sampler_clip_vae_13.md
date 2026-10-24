---
name: unknown_workflow_sampler_clip_vae_13
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.88125
common_nodes: [CLIPTextEncode, ConditioningZeroOut, KSampler, RH_Translator, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux.1-Krea-Dev文生图 nuchaku加速版_1951464859126976513.json, 图片生成/文生图/FLUX Krea  基础工作流（NUNCHAKU加速）_1952660935905357826.json, 图片生成/文生图/FLUX-krea Nunchaku  加速文生图_1951668271105912833.json, 图片生成/文生图/Flux.1-Krea-Dev文生图-去AI味-真实质感_1950961660334899201.json, 图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1950931756763521026.json, 图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1956944111003688962.json, 图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1986360219359969282.json, 图片生成/文生图/Flux.1-Krea-Dev文生图_1951846909747122177.json, 图片生成/文生图/My_T2I_Workflow_1951132729087864833.json, 图片生成/文生图/Nunchaku-Flux.1-Krea-Dev文生图-逼真质感【两张】_1951508454584340482.json, 图片生成/文生图/Nunchaku极速版本-Flux.1-Krea-Dev文生图-无AI味逼真质感_1951205710673719298.json, 图片生成/文生图/【最新】Flux Krea 文生图｜高质量模型_1951117515063762945.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_13

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Flux.1-Krea-Dev文生图 nuchaku加速版_1951464859126976513.json、图片生成/文生图/FLUX Krea  基础工作流（NUNCHAKU加速）_1952660935905357826.json、图片生成/文生图/FLUX-krea Nunchaku  加速文生图_1951668271105912833.json、图片生成/文生图/Flux.1-Krea-Dev文生图-去AI味-真实质感_1950961660334899201.json、图片生成/文生图/Flux.1-Krea-Dev文生图-无AI味逼真质感_1950931756763521026.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `RH_Translator`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 11/12 个有
- `DualCLIPLoader` —— 11/12 个有
- `Text Multiline` —— 10/12 个有
- `easy showAnything` —— 10/12 个有
- `UNETLoader` —— 9/12 个有
- `NunchakuFluxDiTLoader` —— 5/12 个有
- `Primitive integer [Crystools]` —— 3/12 个有
- `NunchakuFluxLoraLoader` —— 2/12 个有
- `EmptySD3LatentImage` —— 1/12 个有
- `FluxGuidance` —— 1/12 个有
- `NunchakuTextEncoderLoader` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 20 | 12 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 20，12 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
