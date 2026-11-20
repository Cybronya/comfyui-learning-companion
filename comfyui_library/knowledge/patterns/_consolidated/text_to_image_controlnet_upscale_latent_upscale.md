---
name: text_to_image_controlnet_upscale_latent_upscale
type: Text To Image
frequency: 8
level: weak
coverage: 0.809125
common_nodes: [AV_ControlNetPreprocessor, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, FaceDetailer, ImageUpscaleWithModel, JoinStringMulti, KSampler, KSampler (Efficient), LatentUpscaleBy, LoadImage, LoraLoader, Power Lora Loader (rgthree), PreviewAny, PreviewImage, PrimitiveStringMultiline, SaveImage, UNETLoader, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Anima转ill二次元图生图｜脸部修复+高清放大一步到位_2097139772992090113.json, 图片生成/图生图/Anima转ill动漫图生图｜修复糊脸再放大，二次元画质救星_2097143100274733058.json, 图片生成/图生图/Anima转ill图生图+脸部修复+放大算法_2096961420385673218.json, 图片生成/图生图/Anima转ill图生图+脸部修复+放大算法_2096982814603440129.json, 图片生成/图生图/Anima转ill图生图+脸部修复+放大算法_2097114436237619202.json, 图片生成/图生图/Anima转ill图生图｜二次元动漫角色脸部修复加放大算法_2097576587389657089.json, 平台全量/anima转ill二次元x现实混合风格_2096522959333711873.json, 平台全量/anima转ill混合风格｜二次元与写实一键融合_2097167631794139138.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_latent_upscale

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Anima转ill二次元图生图｜脸部修复+高清放大一步到位_2097139772992090113.json、图片生成/图生图/Anima转ill动漫图生图｜修复糊脸再放大，二次元画质救星_2097143100274733058.json、图片生成/图生图/Anima转ill图生图+脸部修复+放大算法_2096961420385673218.json、图片生成/图生图/Anima转ill图生图+脸部修复+放大算法_2096982814603440129.json、图片生成/图生图/Anima转ill图生图+脸部修复+放大算法_2097114436237619202.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 8 个 workflow 都包含：
- `AV_ControlNetPreprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `FaceDetailer`
- `ImageUpscaleWithModel`
- `JoinStringMulti`
- `KSampler`
- `KSampler (Efficient)`
- `LatentUpscaleBy`
- `LoadImage`
- `LoraLoader`
- `Power Lora Loader (rgthree)`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `SaveImage`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScale` —— 6/8 个有
- `WD14Tagger|pysssss` —— 6/8 个有
- `JjkText` —— 4/8 个有
- `LoraLoaderModelOnly` —— 4/8 个有
- `solarL_SaveImagesToZip` —— 4/8 个有
- `孤海注释` —— 4/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 424 | 80 - 1024 | 8 | 16% |
| 高度 | 808 | 80 - 1536 | 8 | 10% |
| ControlNet 权重 | 0.75 | 0.75 - 1 | 8 | 87% |
| 采样步数 | 17 | 4 - 30 | 8 | 24% |
| Prompt 约束强度(CFG) | 4.5 | 4 - 5 | 8 | 92% |
| 采样算法 | er_sde | - | 8 | 62% |
| 调度器 | beta | - | 8 | 50% |
| 重绘幅度 | 0.85 | 0.25 - 1 | 8 | 49% |
| LoRA 模型强度 | 0.6 | 0.2 - 0.6 | 8 | 65% |
| LoRA 文本强度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 424，观测区间 80 - 1024，8 个样本，取值分散，一致性仅 16%
- 高度 中位数 808，观测区间 80 - 1536，8 个样本，取值分散，一致性仅 10%
- ControlNet 权重 中位数 0.75，观测区间 0.75 - 1，8 个样本，取值集中（一致性 87%）
- 采样步数 中位数 17，观测区间 4 - 30，8 个样本，取值分散，一致性仅 24%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4 - 5，8 个样本，取值集中（一致性 92%）
- 采样算法 最常用 er_sde，8 个样本，一致性 62%
- 调度器 最常用 beta，8 个样本，一致性 50%
- 重绘幅度 中位数 0.85，观测区间 0.25 - 1，8 个样本，取值分散，一致性仅 49%
- LoRA 模型强度 中位数 0.6，观测区间 0.2 - 0.6，8 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（4/8 个样本）：Steps较低可能导致细节不足
