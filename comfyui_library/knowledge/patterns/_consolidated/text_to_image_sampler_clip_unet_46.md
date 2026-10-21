---
name: text_to_image_sampler_clip_unet_46
type: Text To Image
frequency: 9
level: moderate
coverage: 0.769333
common_nodes: [CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, EmptyLatentImage, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [Text Multiline, CR SDXL Aspect Ratio, CR Text Replace, LayerUtility: ColorImage V2, LayerUtility: ImageCombineAlpha]
members: [图片生成/文生图/1952896951139430401.json, 图片生成/文生图/1952902120161931266.json, 图片生成/文生图/1952909468277346306.json, 图片生成/文生图/1953685065354149889.json, 图片生成/文生图/1954723873654763521.json, 图片生成/文生图/1958426605657997313.json, 图片生成/文生图/1963795542739603457.json, 图片生成/文生图/Qwen-lmage 官方版文生图  支持中文字体_1990708737994350594.json, 图片生成/文生图/Qwen-lmage 文生图 支持中文字体_2063400027611033601.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_46

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1952896951139430401.json、图片生成/文生图/1952902120161931266.json、图片生成/文生图/1952909468277346306.json、图片生成/文生图/1953685065354149889.json、图片生成/文生图/1954723873654763521.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 8/9 个有
- `RH_Captioner` —— 8/9 个有
- `Textbox` —— 8/9 个有
- `Int` —— 7/9 个有
- `CR Text Replace` —— 1/9 个有
- `GetRandomIntegerInRange` —— 1/9 个有
- `ImageToMask` —— 1/9 个有
- `ImpactStringSelector` —— 1/9 个有
- `LayerUtility: ColorImage V2` —— 1/9 个有
- `LayerUtility: ImageCombineAlpha` —— 1/9 个有
- `LoraLoaderModelOnly` —— 1/9 个有
- `RH_LLMAPI_NODE` —— 1/9 个有
- `Text Multiline` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 9 | 80% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 9 | 72% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 512 | 512 - 1328 | 9 | 57% |
| 高度 | 512 | 512 - 1328 | 9 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，9 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 1328，9 个样本
- 高度 中位数 512，观测区间 512 - 1328，9 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline、CR SDXL Aspect Ratio、CR Text Replace、LayerUtility: ColorImage V2、LayerUtility: ImageCombineAlpha
