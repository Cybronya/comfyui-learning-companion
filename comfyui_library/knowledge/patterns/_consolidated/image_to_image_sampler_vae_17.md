---
name: image_to_image_sampler_vae_17
type: Image To Image
frequency: 9
level: moderate
coverage: 0.944889
common_nodes: [ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【阡陌】FLUX + LORA 中文提示词自动翻译 图生图工作流_1942184705607282690.json, 图片生成/图生图/【阡陌】FLUX Teacache 无损加速 图生图工作流_1944716485539319809.json, 图片生成/图生图/【阡陌】FLUX krea 图生图工作流_1951526547859648513.json, 图片生成/图生图/【阡陌】flux Schnell 图生图工作流_1944742726615355394.json, 图片生成/图生图/一键复古美式_2077623031396134914.json, 图片生成/图生图/一键扩图FluxKontext开源版=艾橘溪_1939987079931564034.json, 图片生成/图生图/人物一键卸妆与素颜还原_2060237604842467329.json, 图片生成/图生图/冰爷老杨简单溶图-提前PS（省钱版）_1966078677220061185.json, 图片生成/图生图/完美丰胸一键运行_1981197400008196098.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_17

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/【阡陌】FLUX + LORA 中文提示词自动翻译 图生图工作流_1942184705607282690.json、图片生成/图生图/【阡陌】FLUX Teacache 无损加速 图生图工作流_1944716485539319809.json、图片生成/图生图/【阡陌】FLUX krea 图生图工作流_1951526547859648513.json、图片生成/图生图/【阡陌】flux Schnell 图生图工作流_1944742726615355394.json、图片生成/图生图/一键复古美式_2077623031396134914.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 9 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 8/9 个有
- `CLIPTextEncode` —— 6/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `ReferenceLatent` —— 5/9 个有
- `PreviewImage` —— 4/9 个有
- `Image Comparer (rgthree)` —— 3/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/9 个有
- `ArgosTranslateCLIPTextEncodeNode` —— 2/9 个有
- `TeaCache` —— 2/9 个有
- `easy cleanGpuUsed` —— 2/9 个有
- `CR Simple Image Compare` —— 1/9 个有
- `DeepTranslatorCLIPTextEncodeNode` —— 1/9 个有
- `DetailTransfer` —— 1/9 个有
- `ImagePadForOutpaint` —— 1/9 个有
- `Primitive string multiline [Crystools]` —— 1/9 个有
- `Seed (rgthree)` —— 1/9 个有
- `Text Concatenate` —— 1/9 个有
- `Text Multiline` —— 1/9 个有
- `UnetLoaderGGUF` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 30 | 9 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | normal | - | 9 | 44% |
| 重绘幅度 | 1 | 0.5 - 1 | 9 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 30，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 normal，9 个样本，一致性 44%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，9 个样本
