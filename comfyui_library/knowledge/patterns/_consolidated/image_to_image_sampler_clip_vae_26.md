---
name: image_to_image_sampler_clip_vae_26
type: Image To Image
frequency: 6
level: strong
coverage: 0.856833
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, NunchakuFluxDiTLoader, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext Presets官方预设模板发（懒人福音）_1944392404331843585.json, 图片生成/图生图/Kontext nunchaku单图编辑_1939898967906029569.json, 图片生成/图生图/Nunchaku-FLUX加速改图_1942403095311626241.json, 图片生成/图生图/nunchaku-flux.1-kontext-dev-8步快速t生成三视图_1942909354280435713.json, 图片生成/图生图/nunchaku-flux.1-kontext-dev-8步快速出图_1942473442157342721.json, 图片生成/图生图/图片去水印_Kontext-Dev_Nunchaku_1943877566316838914.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_26

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Kontext Presets官方预设模板发（懒人福音）_1944392404331843585.json、图片生成/图生图/Kontext nunchaku单图编辑_1939898967906029569.json、图片生成/图生图/Nunchaku-FLUX加速改图_1942403095311626241.json、图片生成/图生图/nunchaku-flux.1-kontext-dev-8步快速t生成三视图_1942909354280435713.json、图片生成/图生图/nunchaku-flux.1-kontext-dev-8步快速出图_1942473442157342721.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/6 个有
- `RH_LLMAPI_NODE` —— 5/6 个有
- `ShowText|pysssss` —— 5/6 个有
- `FluxKontextImageScale` —— 3/6 个有
- `ImageStitch` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `JjkText` —— 2/6 个有
- `RH_Translator` —— 2/6 个有
- `ColorMatch` —— 1/6 个有
- `DeepTranslatorTextNode` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有
- `LoadKontextPresets` —— 1/6 个有
- `RepeatLatentBatch` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
