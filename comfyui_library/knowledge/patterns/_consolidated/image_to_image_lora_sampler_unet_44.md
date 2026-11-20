---
name: image_to_image_lora_sampler_unet_44
type: Image To Image
frequency: 13
level: moderate
coverage: 0.899
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen edit 2511 多角度生成_2032063580392136705.json, 图片生成/图生图/Qwen edit 2511单图多角度 短剧 动漫 专用_2041503056172425217.json, 图片生成/图生图/Qwen edit 2511单图多角度_2010230488669102081.json, 图片生成/图生图/Qwen-edit-2511-去水印_2005123694177517569.json, 图片生成/图生图/Qwen-edit-2511-无限扩图（简化版）_2005999334229495810.json, 图片生成/图生图/单图多角度_2073899870544551938.json, 图片生成/图生图/废片光影重构影楼艺术照_2036626776293646338.json, 图片生成/图生图/扩图 - Qwen-Image-Edit-2511_2039543264075849730.json, 图片生成/图生图/扩图，上下左右自定义尺寸，超快_2018966865443295233.json, 平台全量/4k超清图像放大 图像扩图 高清人像放大去AI感 增加皮肤纹理 去瑕疵，图像一键高清放大_2017853783908290562.json, 平台全量/图像无痕扩图  4k超清图像放大 高清人像放大去AI感 增加皮肤纹理 去瑕疵，图像一键高清放大_2020762500739899393.json, 平台全量/扩图 - Qwen-Image-Edit-2511_1946765641052221442.json, 平台全量/扩图 - Qwen-Image-Edit-2511_2021381262027526145.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_44

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Qwen edit 2511 多角度生成_2032063580392136705.json、图片生成/图生图/Qwen edit 2511单图多角度 短剧 动漫 专用_2041503056172425217.json、图片生成/图生图/Qwen edit 2511单图多角度_2010230488669102081.json、图片生成/图生图/Qwen-edit-2511-去水印_2005123694177517569.json、图片生成/图生图/Qwen-edit-2511-无限扩图（简化版）_2005999334229495810.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ReferenceLatent` —— 12/13 个有
- `ConditioningZeroOut` —— 10/13 个有
- `Image Comparer (rgthree)` —— 10/13 个有
- `ConstrainImage|pysssss` —— 7/13 个有
- `PreviewImage` —— 7/13 个有
- `ImagePadKJ` —— 6/13 个有
- `FluxKontextImageScale` —— 5/13 个有
- `QwenMultiangleCameraNode` —— 4/13 个有
- `PreviewAny` —— 3/13 个有
- `Fast Groups Bypasser (rgthree)` —— 2/13 个有
- `RH_Nano_Banana2_Image2Image` —— 2/13 个有
- `DapaoImagePadDirectionNode` —— 1/13 个有
- `PlaySound|pysssss` —— 1/13 个有
- `ShowText|pysssss` —— 1/13 个有
- `图像缩放V2_孤海` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 13 | 36% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 92% |
| 调度器 | simple | - | 13 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，13 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 92%
- 调度器 最常用 simple，13 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（7/13 个样本）：Steps较低可能导致细节不足
