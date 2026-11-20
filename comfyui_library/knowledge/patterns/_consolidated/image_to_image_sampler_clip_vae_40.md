---
name: image_to_image_sampler_clip_vae_40
type: Image To Image
frequency: 4
level: moderate
coverage: 0.8935
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, NunchakuFluxDiTLoader, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/nunchaku-flux.1-kontext-dev-8步快速t生成三视图_1942909354280435713.json, 图片生成/图生图/nunchaku-flux.1-kontext-dev-8步快速出图_1942473442157342721.json, 图片生成/图生图/nunchaku-flux.1-kontext-dev-扩图-8步快速出图_1954878812870754306.json, 图片生成/图生图/【全能图片G4o同款】Flux Kontext 图像编辑加速版_1948192407916544002.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_40

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/nunchaku-flux.1-kontext-dev-8步快速t生成三视图_1942909354280435713.json、图片生成/图生图/nunchaku-flux.1-kontext-dev-8步快速出图_1942473442157342721.json、图片生成/图生图/nunchaku-flux.1-kontext-dev-扩图-8步快速出图_1954878812870754306.json、图片生成/图生图/【全能图片G4o同款】Flux Kontext 图像编辑加速版_1948192407916544002.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_Translator` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `PreviewImage` —— 2/4 个有
- `RH_LLMAPI_NODE` —— 2/4 个有
- `easy imageConcat` —— 2/4 个有
- `ImagePadForOutpaint` —— 1/4 个有
- `ImageUpscaleWithModel` —— 1/4 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 343 | 4 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 343，4 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 343，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
