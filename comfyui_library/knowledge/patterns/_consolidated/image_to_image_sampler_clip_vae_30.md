---
name: image_to_image_sampler_clip_vae_30
type: Image To Image
frequency: 7
level: strong
coverage: 0.828429
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, ImageStitch, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/啊癫 极速复杂水印自动去除_1946593965531652098.json, 图片生成/图生图/图片去水印_Kontext-Dev_Nunchaku_1943877566316838914.json, 图片生成/图生图/提取服装平铺图_1942986904318984194.json, 图片生成/图生图/真人转动漫flux_kontext_dev_1964320638330617857.json, 图片生成/图生图/空白工作流_1977925668166062081.json, 图片生成/图生图/线稿上色｜自选风格_1948299809867345921.json, 图片生成/图生图/老照片修复_Kontext-LORA版_1943506433671372802.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_30

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/啊癫 极速复杂水印自动去除_1946593965531652098.json、图片生成/图生图/图片去水印_Kontext-Dev_Nunchaku_1943877566316838914.json、图片生成/图生图/提取服装平铺图_1942986904318984194.json、图片生成/图生图/真人转动漫flux_kontext_dev_1964320638330617857.json、图片生成/图生图/空白工作流_1977925668166062081.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
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
- `FluxKontextImageScale` —— 6/7 个有
- `Image Comparer (rgthree)` —— 5/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `UNETLoader` —— 5/7 个有
- `JjkText` —— 2/7 个有
- `NunchakuFluxDiTLoader` —— 2/7 个有
- `RH_LLMAPI_NODE` —— 2/7 个有
- `ShowText|pysssss` —— 2/7 个有
- `ColorMatch` —— 1/7 个有
- `DeepTranslatorTextNode` —— 1/7 个有
- `GetNode` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `TextInputBasic` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 7 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，7 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
