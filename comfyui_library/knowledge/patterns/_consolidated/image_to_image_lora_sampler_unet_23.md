---
name: image_to_image_lora_sampler_unet_23
type: Image To Image
frequency: 19
level: strong
coverage: 0.947474
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问3D手办_1989299261110145025.json, 图片生成/图生图/千问EDIT局部修改_2048292651706884097.json, 图片生成/图生图/千问edit局部修改工作流_1954950250534506497.json, 图片生成/图生图/图生图-真人转动漫 - 真人转卡通-  真人转漫画_2062456179342798850.json, 图片生成/图生图/极速真人转动漫_2061261202520625153.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画   Q版卡通  Q版风格化_2053849545037107202.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画   Q版卡通  Q版风格化_2053877857646071809.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画   Q版卡通  Q版风格化_2053880513613582337.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画  Q版卡通  Q版风格化_2053875214815113218.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画  Q版卡通  Q版风格化_2053897627506356225.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画  Q版卡通  Q版风格化_2053900093924888577.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2059878371705843713.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2059909148455817218.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2059925156805562369.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2089746856464183297.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2096643115598831618.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2096654007803666433.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2096831045206364161.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2100329081756803073.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_23

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/千问3D手办_1989299261110145025.json、图片生成/图生图/千问EDIT局部修改_2048292651706884097.json、图片生成/图生图/千问edit局部修改工作流_1954950250534506497.json、图片生成/图生图/图生图-真人转动漫 - 真人转卡通-  真人转漫画_2062456179342798850.json、图片生成/图生图/极速真人转动漫_2061261202520625153.json…）

- **类型**：Image To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 19 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SeedVR2LoadDiTModel` —— 6/19 个有
- `SeedVR2LoadVAEModel` —— 6/19 个有
- `SeedVR2VideoUpscaler` —— 6/19 个有
- `PIP_图像联结` —— 5/19 个有
- `PreviewImage` —— 5/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/19 个有
- `TextInput_` —— 3/19 个有
- `SetLatentNoiseMask` —— 2/19 个有
- `ImpactInt` —— 1/19 个有
- `Power Lora Loader (rgthree)` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 19 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 19 | 100% |
| 采样算法 | euler | - | 19 | 100% |
| 调度器 | simple | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，19 个样本，一致性 100%
- 调度器 最常用 simple，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（19/19 个样本）：Steps较低可能导致细节不足
