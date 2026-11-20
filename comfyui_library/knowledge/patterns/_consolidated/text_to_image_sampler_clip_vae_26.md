---
name: text_to_image_sampler_clip_vae_26
type: Text To Image
frequency: 5
level: moderate
coverage: 0.8404
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/nunchaku-flux-kontext_1980175881677213697.json, 图片生成/图生图/角色一致性4格漫画生成｜Kontext Dev_1948258403920556033.json, 图片生成/文生图/Nunchaku加速_FLUX_Kontext_lora_1911961603980623874.json, 平台全量/Flux Kontext Dev一句话图像编辑V3（单图）_1940660424188784641.json, 平台全量/Flux kontext(产品精修)_1945381157318086657.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_26

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/nunchaku-flux-kontext_1980175881677213697.json、图片生成/图生图/角色一致性4格漫画生成｜Kontext Dev_1948258403920556033.json、图片生成/文生图/Nunchaku加速_FLUX_Kontext_lora_1911961603980623874.json、平台全量/Flux Kontext Dev一句话图像编辑V3（单图）_1940660424188784641.json、平台全量/Flux kontext(产品精修)_1945381157318086657.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `FluxGuidance` —— 4/5 个有
- `NunchakuFluxDiTLoader` —— 4/5 个有
- `Anything Everywhere` —— 3/5 个有
- `Anything Everywhere3` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `GetNode` —— 3/5 个有
- `RH_Translator` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `ImageResize+` —— 2/5 个有
- `ImageStitch` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `TextInput_` —— 2/5 个有
- `CR Text Replace` —— 1/5 个有
- `DifferentialDiffusion` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `NunchakuFluxLoraLoader` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `UNETLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 16 - 20 | 5 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 0.3 - 1 | 5 | 67% |
| 宽度 | 1024 | 512 - 1536 | 5 | 65% |
| 高度 | 1280 | 512 - 1536 | 5 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 16 - 20，5 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，5 个样本
- 宽度 中位数 1024，观测区间 512 - 1536，5 个样本
- 高度 中位数 1280，观测区间 512 - 1536，5 个样本
