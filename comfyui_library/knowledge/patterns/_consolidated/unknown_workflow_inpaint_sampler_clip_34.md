---
name: unknown_workflow_inpaint_sampler_clip_34
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.962429
common_nodes: [CLIPTextEncode, DifferentialDiffusion, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/Flux图像外扩-低显卡快速扩图-效果好_1923926047077617666.json, 平台全量/Flux局部重绘_1929065368663527425.json, 平台全量/【新】flux fill outpaint example_1859960427764649985.json, 平台全量/【新】局部重绘-tal_1953424953905434625.json, 平台全量/【最新强化】Fill-OneReward局部重绘_1987041185166503937.json, 平台全量/【阡陌】Flux Fill一键去水印工作流_1909468961539563522.json, 平台全量/【阡陌】可输中文FLUX高清无痕局部重绘工作流_1902738092468645890.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_34

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/Flux图像外扩-低显卡快速扩图-效果好_1923926047077617666.json、平台全量/Flux局部重绘_1929065368663527425.json、平台全量/【新】flux fill outpaint example_1859960427764649985.json、平台全量/【新】局部重绘-tal_1953424953905434625.json、平台全量/【最新强化】Fill-OneReward局部重绘_1987041185166503937.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 5/7 个有
- `UNETLoader` —— 5/7 个有
- `DeepTranslatorTextNode` —— 2/7 个有
- `DualCLIPLoaderGGUF` —— 2/7 个有
- `GrowMaskWithBlur` —— 2/7 个有
- `ImagePadForOutpaint` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `UnetLoaderGGUF` —— 2/7 个有
- `ViewText` —— 2/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `RH_Translator` —— 1/7 个有
- `RepeatImageBatch` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 7 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 6.97 | 7 | 18% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | normal | - | 7 | 43% |
| 重绘幅度 | 1 | 0.8 - 1 | 7 | 93% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，7 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6.97，7 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 normal，7 个样本，一致性 43%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，7 个样本，取值集中（一致性 93%）
