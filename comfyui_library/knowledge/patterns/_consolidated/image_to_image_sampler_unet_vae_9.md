---
name: image_to_image_sampler_unet_vae_9
type: Image To Image
frequency: 16
level: moderate
coverage: 0.932438
common_nodes: [ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【阡陌】FLUX + LORA 中文提示词自动翻译 图生图工作流_1942184705607282690.json, 图片生成/图生图/【阡陌】FLUX Teacache 无损加速 图生图工作流_1944716485539319809.json, 图片生成/图生图/【阡陌】FLUX krea 图生图工作流_1951526547859648513.json, 图片生成/图生图/【阡陌】flux Schnell 图生图工作流_1944742726615355394.json, 图片生成/图生图/一键复古美式_2077623031396134914.json, 图片生成/图生图/一键扩图FluxKontext开源版=艾橘溪_1939987079931564034.json, 图片生成/图生图/人像光影融合-MAGIC-K-V1_2096507439083511809.json, 图片生成/图生图/人像光影融合-MAGIC-K-V1_2096864329248362497.json, 图片生成/图生图/人物一键卸妆与素颜还原_2060237604842467329.json, 图片生成/图生图/图像高精度去水印与无损修复_2057742605227741185.json, 图片生成/图生图/运营图风格转换_2000487206320041985.json, 图片生成/图生图/🦖光影融合工作流_1958791734731960321.json, 平台全量/Kontext 一句话改变图像视角_1938549142723743746.json, 平台全量/Kontext 一句话模特换装_1938510030557896705.json, 平台全量/Kontext 一句话风格参考_1938482092009545729.json, 平台全量/Q-特效脸（扭曲）_1957443773041143810.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_9

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/【阡陌】FLUX + LORA 中文提示词自动翻译 图生图工作流_1942184705607282690.json、图片生成/图生图/【阡陌】FLUX Teacache 无损加速 图生图工作流_1944716485539319809.json、图片生成/图生图/【阡陌】FLUX krea 图生图工作流_1951526547859648513.json、图片生成/图生图/【阡陌】flux Schnell 图生图工作流_1944742726615355394.json、图片生成/图生图/一键复古美式_2077623031396134914.json…）

- **类型**：Image To Image
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 16 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 13/16 个有
- `LoraLoaderModelOnly` —— 12/16 个有
- `ReferenceLatent` —— 12/16 个有
- `Image Comparer (rgthree)` —— 7/16 个有
- `easy positive` —— 6/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/16 个有
- `PreviewImage` —— 4/16 个有
- `ArgosTranslateCLIPTextEncodeNode` —— 2/16 个有
- `DeepTranslatorCLIPTextEncodeNode` —— 1/16 个有
- `ImagePadForOutpaint` —— 1/16 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/16 个有
- `RHHiddenNodes` —— 1/16 个有
- `TeaCache` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 30 | 16 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 16 | 100% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 69% |
| 重绘幅度 | 1 | 0.5 - 1 | 16 | 84% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 30，16 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 69%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，16 个样本，取值集中（一致性 84%）
