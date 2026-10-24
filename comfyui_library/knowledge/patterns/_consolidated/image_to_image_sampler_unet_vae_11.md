---
name: image_to_image_sampler_unet_vae_11
type: Image To Image
frequency: 12
level: strong
coverage: 0.98275
common_nodes: [ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【阡陌】FLUX + LORA 中文提示词自动翻译 图生图工作流_1942184705607282690.json, 图片生成/图生图/【阡陌】FLUX Teacache 无损加速 图生图工作流_1944716485539319809.json, 图片生成/图生图/【阡陌】flux Schnell 图生图工作流_1944742726615355394.json, 图片生成/图生图/一键复古美式_2077623031396134914.json, 图片生成/图生图/一键扩图FluxKontext开源版=艾橘溪_1939987079931564034.json, 图片生成/图生图/人物去除+衣服提取+透明背景_1945018713423929346.json, 图片生成/图生图/全能视频S真人前置-素描Kontext_1974104968892387330.json, 图片生成/图生图/印花提取-商业级 Flux.1 Kontext_2103519336425156610.json, 图片生成/图生图/印花提取-商业级 Flux.1 Kontext_2104433739911745537.json, 图片生成/图生图/印花提取-商业级_Flux.1_Kontext_2108385501811142658.json, 图片生成/图生图/印花提取-商业级_Flux.1_Kontext_2109826006751203329.json, 图片生成/图生图/🧙Kontext完美扩图工作流【扩图LORA】🍧_1945310376504512514.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_11

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/【阡陌】FLUX + LORA 中文提示词自动翻译 图生图工作流_1942184705607282690.json、图片生成/图生图/【阡陌】FLUX Teacache 无损加速 图生图工作流_1944716485539319809.json、图片生成/图生图/【阡陌】flux Schnell 图生图工作流_1944742726615355394.json、图片生成/图生图/一键复古美式_2077623031396134914.json、图片生成/图生图/一键扩图FluxKontext开源版=艾橘溪_1939987079931564034.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 12 个 workflow 都包含：
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
- `CLIPTextEncode` —— 9/12 个有
- `LoraLoaderModelOnly` —— 9/12 个有
- `ReferenceLatent` —— 9/12 个有
- `FluxKontextImageScale` —— 7/12 个有
- `PreviewImage` —— 3/12 个有
- `ArgosTranslateCLIPTextEncodeNode` —— 2/12 个有
- `DeepTranslatorCLIPTextEncodeNode` —— 1/12 个有
- `ImageConcanate` —— 1/12 个有
- `ImagePadForOutpaint` —— 1/12 个有
- `ImagePadKJ` —— 1/12 个有
- `JWImageResizeByLongerSide` —— 1/12 个有
- `JWInteger` —— 1/12 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/12 个有
- `LayerUtility: PurgeVRAM V2` —— 1/12 个有
- `TeaCache` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 25 | 12 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 67% |
| 重绘幅度 | 1 | 0.5 - 1 | 12 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 25，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，12 个样本，取值集中（一致性 82%）
