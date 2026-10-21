---
name: text_to_image_controlnet_sampler_clip_3
type: Text To Image
frequency: 3
level: strong
coverage: 0.847667
common_nodes: [AIO_Preprocessor, CLIPTextEncode, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, LoadImage, PreviewImage, SaveImage, SetUnionControlNetType, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, ttN concat]
members: [图片生成/文生图/01_参考生图_2074230063763116033.json, 图片生成/文生图/1915206472983318529.json, 图片生成/文生图/1977917454909329410.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/01_参考生图_2074230063763116033.json、图片生成/文生图/1915206472983318529.json、图片生成/文生图/1977917454909329410.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DF_Image_scale_to_side` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageGenResolutionFromImage` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `DifferentialDiffusion` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `NunchakuFluxDiTLoader` —— 1/3 个有
- `NunchakuFluxLoraLoader` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `VAEEncode` —— 1/3 个有
- `ttN concat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 采样步数 | 25 | 25 - 30 | 3 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 800 | 720 - 800 | 3 | 95% |
| 高度 | 1024 | 1024 - 1280 | 3 | 89% |
| ControlNet 权重 | 0.8 | 0.6 - 0.8 | 3 | 87% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 30，3 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 800，观测区间 720 - 800，3 个样本，取值集中（一致性 95%）
- 高度 中位数 1024，观测区间 1024 - 1280，3 个样本，取值集中（一致性 89%）
- ControlNet 权重 中位数 0.8，观测区间 0.6 - 0.8，3 个样本，取值集中（一致性 87%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、ttN concat
