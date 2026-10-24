---
name: text_to_image_sampler_clip_vae_33
type: Text To Image
frequency: 3
level: moderate
coverage: 0.900667
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/nunchaku-flux-kontext_1980175881677213697.json, 图片生成/图生图/角色一致性4格漫画生成｜Kontext Dev_1948258403920556033.json, 图片生成/文生图/Nunchaku加速_FLUX_Kontext_lora_1911961603980623874.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_33

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/nunchaku-flux-kontext_1980175881677213697.json、图片生成/图生图/角色一致性4格漫画生成｜Kontext Dev_1948258403920556033.json、图片生成/文生图/Nunchaku加速_FLUX_Kontext_lora_1911961603980623874.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 2/3 个有
- `FluxGuidance` —— 2/3 个有
- `ImageStitch` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `NunchakuFluxDiTLoader` —— 2/3 个有
- `RH_Translator` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `DifferentialDiffusion` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `NunchakuFluxLoraLoader` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `UNETLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 16 - 20 | 3 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.3 - 1 | 3 | 57% |
| 宽度 | 768 | 512 - 1024 | 3 | 73% |
| 高度 | 1024 | 512 - 1536 | 3 | 59% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 16 - 20，3 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，3 个样本
- 宽度 中位数 768，观测区间 512 - 1024，3 个样本
- 高度 中位数 1024，观测区间 512 - 1536，3 个样本
