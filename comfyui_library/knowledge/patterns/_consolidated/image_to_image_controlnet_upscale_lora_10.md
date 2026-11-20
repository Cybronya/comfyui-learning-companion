---
name: image_to_image_controlnet_upscale_lora_10
type: Image To Image
frequency: 3
level: moderate
coverage: 0.597
common_nodes: [CR Prompt Text, Combine Tiles, ControlNetApplyAdvanced, ControlNetLoader, Display UI, Divide Image and Select Tile, Divide and Conquer Algorithm, Fast Groups Bypasser (rgthree), Fast Groups Muter (rgthree), Florence2ModelLoader, Florence2Run, GetNode, Image Comparer (rgthree), JWImageResizeByShorterSide, KSampler, Latent Noise Injection, LoadImage, Power Lora Loader (rgthree), PreviewImage, SaveImage, SetNode, UpscaleModelLoader, VAEDecode, VAEEncode, VHS_LoadVideoFFmpeg, easy promptConcat]
problems: []
missing: []
members: [图片生成/图生图/SDXL细化去除纹理噪点_2063527982848897026.json, 平台全量/04-SDXL细化去除纹理噪点_2062849936726777857.json, 平台全量/flux1的分区放大重绘真实lora_2062510592581259265.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_lora_10

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/SDXL细化去除纹理噪点_2063527982848897026.json、平台全量/04-SDXL细化去除纹理噪点_2062849936726777857.json、平台全量/flux1的分区放大重绘真实lora_2062510592581259265.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Prompt Text`
- `Combine Tiles`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `Display UI`
- `Divide Image and Select Tile`
- `Divide and Conquer Algorithm`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Muter (rgthree)`
- `Florence2ModelLoader`
- `Florence2Run`
- `GetNode`
- `Image Comparer (rgthree)`
- `JWImageResizeByShorterSide`
- `KSampler`
- `Latent Noise Injection`
- `LoadImage`
- `Power Lora Loader (rgthree)`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VHS_LoadVideoFFmpeg`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `BNK_CLIPTextEncodeAdvanced` —— 2/3 个有
- `CLIPSetLastLayer` —— 2/3 个有
- `CheckpointLoaderSimple` —— 2/3 个有
- `ColorCorrect` —— 2/3 个有
- `ColorMatch` —— 2/3 个有
- `TTPlanet_TileGF_Preprocessor` —— 2/3 个有
- `CLIPTextEncodeFlux` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `DualCLIPLoader` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `TeaCache` —— 1/3 个有
- `UNETLoader` —— 1/3 个有
- `VAELoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.4 | 0.4 - 0.9 | 3 | 58% |
| 采样步数 | 30 | 20 - 30 | 3 | 82% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 3 | 65% |
| 采样算法 | dpmpp_3m_sde | - | 3 | 67% |
| 调度器 | exponential | - | 3 | 67% |
| 重绘幅度 | 0.6 | 0.6 - 0.9 | 3 | 80% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.4，观测区间 0.4 - 0.9，3 个样本
- 采样步数 中位数 30，观测区间 20 - 30，3 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 dpmpp_3m_sde，3 个样本，一致性 67%
- 调度器 最常用 exponential，3 个样本，一致性 67%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 0.9，3 个样本
