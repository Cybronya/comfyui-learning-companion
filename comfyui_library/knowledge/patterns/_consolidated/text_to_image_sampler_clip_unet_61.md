---
name: text_to_image_sampler_clip_unet_61
type: Text To Image
frequency: 10
level: weak
coverage: 0.8631
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Anima aesthetic-v11-全底模test-测试工作流_2079220135235252226.json, 图片生成/图生图/Anima base-v11｜10步极速文生图_2079165843375738882.json, 图片生成/文生图/2029928001101635585.json, 图片生成/文生图/Anima aesthetic-v11_2080189925386964993.json, 图片生成/文生图/Anima_V10-Turbo 10-Step｜10步极速文生图_2079037824149573634.json, 图片生成/文生图/Anima强大的动漫文生图turbo高速版_2061065103197425666.json, 图片生成/文生图/Boogu-Image Turbo 文生图 VS Zimage-turbo_2069035083775963138.json, 图片生成/文生图/Ernie-Image最强生图模型+全节点注释_2046103239707332609.json, 图片生成/文生图/Krea2 文生图_2071762623535861761.json, 图片生成/文生图/Nunchaku Z-Image文生图_2005466390012329986.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_61

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Anima aesthetic-v11-全底模test-测试工作流_2079220135235252226.json、图片生成/图生图/Anima base-v11｜10步极速文生图_2079165843375738882.json、图片生成/文生图/2029928001101635585.json、图片生成/文生图/Anima aesthetic-v11_2080189925386964993.json、图片生成/文生图/Anima_V10-Turbo 10-Step｜10步极速文生图_2079037824149573634.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 7/10 个有
- `LoraLoaderModelOnly` —— 6/10 个有
- `ConditioningZeroOut` —— 5/10 个有
- `FluxResolutionNode` —— 3/10 个有
- `PDRatioSelector` —— 3/10 个有
- `ModelSamplingAuraFlow` —— 2/10 个有
- `XB_UNetNameBroadcaster` —— 2/10 个有
- `CFGNorm` —— 1/10 个有
- `Image Comparer (rgthree)` —— 1/10 个有
- `LoadImage` —— 1/10 个有
- `NunchakuZImageDiTLoader` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 25 | 10 | 43% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 10 | 50% |
| 采样算法 | euler | - | 10 | 90% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 848 | 512 - 1080 | 10 | 70% |
| 高度 | 512 | 248 - 1920 | 10 | 33% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 25，10 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，10 个样本
- 采样算法 最常用 euler，10 个样本，一致性 90%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 848，观测区间 512 - 1080，10 个样本
- 高度 中位数 512，观测区间 248 - 1920，10 个样本，取值分散，一致性仅 33%
- 高发问题（11/10 个样本）：Steps较低可能导致细节不足
