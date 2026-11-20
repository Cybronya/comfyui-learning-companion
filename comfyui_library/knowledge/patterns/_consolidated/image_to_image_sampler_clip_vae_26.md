---
name: image_to_image_sampler_clip_vae_26
type: Image To Image
frequency: 9
level: strong
coverage: 0.726889
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, ImageStitch, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/啊癫 极速复杂水印自动去除_1946593965531652098.json, 图片生成/图生图/图片去水印_Kontext-Dev_Nunchaku_1943877566316838914.json, 图片生成/图生图/提取服装平铺图_1942986904318984194.json, 图片生成/图生图/真人转动漫flux_kontext_dev_1964320638330617857.json, 图片生成/图生图/空白工作流_1977925668166062081.json, 图片生成/图生图/线稿上色｜自选风格_1948299809867345921.json, 图片生成/图生图/老照片修复_Kontext-LORA版_1943506433671372802.json, 平台全量/医美丰胸_内衣模特_1952288831506731010.json, 平台全量/暗黑金属【kontext】_1952298476732387329.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_26

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/啊癫 极速复杂水印自动去除_1946593965531652098.json、图片生成/图生图/图片去水印_Kontext-Dev_Nunchaku_1943877566316838914.json、图片生成/图生图/提取服装平铺图_1942986904318984194.json、图片生成/图生图/真人转动漫flux_kontext_dev_1964320638330617857.json、图片生成/图生图/空白工作流_1977925668166062081.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 8/9 个有
- `Image Comparer (rgthree)` —— 7/9 个有
- `LoraLoaderModelOnly` —— 7/9 个有
- `PreviewImage` —— 7/9 个有
- `UNETLoader` —— 7/9 个有
- `JjkText` —— 4/9 个有
- `ShowText|pysssss` —— 4/9 个有
- `GetNode` —— 3/9 个有
- `SetNode` —— 3/9 个有
- `CR Simple Image Compare` —— 2/9 个有
- `GoogleTranslator` —— 2/9 个有
- `ImageResizeKJv2` —— 2/9 个有
- `LayerUtility: ImageBlend` —— 2/9 个有
- `NunchakuFluxDiTLoader` —— 2/9 个有
- `RHHiddenNodes` —— 2/9 个有
- `RH_LLMAPI_NODE` —— 2/9 个有
- `RepeatLatentBatch` —— 2/9 个有
- `Text To Image (mtb)` —— 2/9 个有
- `ColorMatch` —— 1/9 个有
- `DeepTranslatorTextNode` —— 1/9 个有
- `TextInputBasic` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 9 | 64% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
