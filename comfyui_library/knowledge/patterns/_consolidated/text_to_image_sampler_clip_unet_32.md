---
name: text_to_image_sampler_clip_unet_32
type: Text To Image
frequency: 11
level: moderate
coverage: 0.924909
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/5.其他类型-6.NSF+-09.Z-image生图002.Z-image批量文生图.json_2021966315602317313.json, 图片生成/文生图/Anima Turbo 10-Step｜10步极速文生图_2075555632480079873.json, 图片生成/文生图/Anima强大的动漫文生图turbo高速版_2061065103197425666.json, 图片生成/文生图/Kook_Flux_klein_亚洲人像_2019704034847891458.json, 图片生成/文生图/Krea-2 高真实感与卓越美学文生图_2069624809176256513.json, 图片生成/文生图/LH-DMT版本-2.生图片类-029.Z-image智能改词文生图-NF_2016493278639693826.json, 图片生成/文生图/Z-IMAGE高清超强生图_1995183324647841794.json, 图片生成/文生图/Zimage-turbo保暖内衣_2051484069925531650.json, 图片生成/文生图/krea2+z_image+boogu模型测试对比_2069616764018843650.json, 图片生成/文生图/z-image手动+反推+高清超强生图_1995144168718655490.json, 图片生成/文生图/zimage+krea2+boogu三模型对比_2069599329727373314.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_32

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/5.其他类型-6.NSF+-09.Z-image生图002.Z-image批量文生图.json_2021966315602317313.json、图片生成/文生图/Anima Turbo 10-Step｜10步极速文生图_2075555632480079873.json、图片生成/文生图/Anima强大的动漫文生图turbo高速版_2061065103197425666.json、图片生成/文生图/Kook_Flux_klein_亚洲人像_2019704034847891458.json、图片生成/文生图/Krea-2 高真实感与卓越美学文生图_2069624809176256513.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 9/11 个有
- `ImpactInt` —— 8/11 个有
- `String Literal` —— 8/11 个有
- `easy showAnything` —— 8/11 个有
- `CR Prompt List` —— 7/11 个有
- `LoadImage` —— 6/11 个有
- `CR Text` —— 5/11 个有
- `Dapao_LlamaCaption` —— 4/11 个有
- `Dapao_LlamaCaptionOptions` —— 4/11 个有
- `RegexReplace` —— 4/11 个有
- `LoraLoaderModelOnly` —— 3/11 个有
- `easy cleanGpuUsed` —— 3/11 个有
- `GetImageSize` —— 2/11 个有
- `LayerUtility: ImageReel` —— 2/11 个有
- `LayerUtility: ImageReelComposit` —— 2/11 个有
- `Qwen3VL_Advanced` —— 2/11 个有
- `ShowText|pysssss` —— 2/11 个有
- `UltimateSDUpscale` —— 2/11 个有
- `UpscaleModelLoader` —— 2/11 个有
- `easy anythingIndexSwitch` —— 2/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `ProcessString` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 720 - 1280 | 11 | 78% |
| 高度 | 1280 | 720 - 1920 | 11 | 78% |
| 采样步数 | 9 | 4 - 15 | 11 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.1 | 11 | 97% |
| 采样算法 | euler | - | 11 | 36% |
| 调度器 | simple | - | 11 | 64% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 720 - 1280，11 个样本
- 高度 中位数 1280，观测区间 720 - 1920，11 个样本
- 采样步数 中位数 9，观测区间 4 - 15，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.1，11 个样本，取值集中（一致性 97%）
- 采样算法 最常用 euler，11 个样本，一致性 36%
- 调度器 最常用 simple，11 个样本，一致性 64%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（13/11 个样本）：Steps较低可能导致细节不足
