---
name: text_to_image_sampler_clip_vae_27
type: Text To Image
frequency: 5
level: moderate
coverage: 0.9276
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, ImageStitch, KSampler, LoadImage, RH_Translator, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux Kontext Dev-去除马赛克_1938440441555804162.json, 图片生成/图生图/Flux Kontext Dev-手办多视图加速版+放大_1942760110571892737.json, 图片生成/图生图/Flux Kontext Dev图像转绘-动漫转真人_1940010138121998337.json, 图片生成/图生图/Kontext 动漫转真人｜LoRA 版本_1947612612328677378.json, 图片生成/图生图/flux kontext dev 单图 双图 三图 三合一 nunchaku加速版_1937433957573279745.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_27

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux Kontext Dev-去除马赛克_1938440441555804162.json、图片生成/图生图/Flux Kontext Dev-手办多视图加速版+放大_1942760110571892737.json、图片生成/图生图/Flux Kontext Dev图像转绘-动漫转真人_1940010138121998337.json、图片生成/图生图/Kontext 动漫转真人｜LoRA 版本_1947612612328677378.json、图片生成/图生图/flux kontext dev 单图 双图 三图 三合一 nunchaku加速版_1937433957573279745.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `RH_Translator`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ShowText|pysssss` —— 4/5 个有
- `Text Multiline` —— 4/5 个有
- `NunchakuFluxDiTLoader` —— 3/5 个有
- `NunchakuFluxLoraLoader` —— 3/5 个有
- `RepeatLatentBatch` —— 3/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `Text Concatenate` —— 2/5 个有
- `UNETLoader` —— 2/5 个有
- `FluxResolutionNode` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `ImpactSwitch` —— 1/5 个有
- `Int Literal` —— 1/5 个有
- `LayerUtility: BooleanOperatorV2` —— 1/5 个有
- `PMRF` —— 1/5 个有
- `easy ifElse` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1536 | 5 | 66% |
| 高度 | 1024 | 512 - 1536 | 5 | 61% |
| 采样步数 | 20 | 8 - 20 | 5 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1536，5 个样本
- 高度 中位数 1024，观测区间 512 - 1536，5 个样本
- 采样步数 中位数 20，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
