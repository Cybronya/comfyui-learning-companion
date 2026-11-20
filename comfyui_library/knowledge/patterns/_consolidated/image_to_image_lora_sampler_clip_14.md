---
name: image_to_image_lora_sampler_clip_14
type: Image To Image
frequency: 11
level: moderate
coverage: 0.808727
common_nodes: [CLIPLoader, CLIPTextEncode, Canny, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/Qwen Image Union Control多重控制V1_1959993171348500482.json, 图片生成/图生图/Qwen Image Union Control多重控制V1_2038786081507774465.json, 图片生成/图生图/qwen_image联合控制工作流_1991719993102512130.json, 图片生成/图生图/千问_Canny_重绘（画风一致）_1999855817111334914.json, 图片生成/图生图/图生图Qwen-Image InstantX Union ControlNet（线稿_深度_姿态）_1971187587396341761.json, 图片生成/图生图/图生图Qwen-Image InstantX Union ControlNet（线稿_深度_姿态）_2022602222256791554.json, 图片生成/图生图/图生图Qwen-Image InstantX Union ControlNet（线稿_深度_姿态）_2060578205039423490.json, 图片生成/图生图/图生图Qwen-Image_InstantX_Union_ControlNet线稿_深度_姿态_2096884116947030017.json, 图片生成/图生图/图生图Qwen-Image_InstantX_Union_ControlNet线稿_深度_姿态_2097175006064238593.json, "图片生成/文生图/InstantX_Qwen-Image-ControlNet-Union（,线稿_深度_姿态）_1961145405088186369.json", 图片生成/文生图/Qwen Image Contro控制_1960239683160715266.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_14

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen Image Union Control多重控制V1_1959993171348500482.json、图片生成/图生图/Qwen Image Union Control多重控制V1_2038786081507774465.json、图片生成/图生图/qwen_image联合控制工作流_1991719993102512130.json、图片生成/图生图/千问_Canny_重绘（画风一致）_1999855817111334914.json、图片生成/图生图/图生图Qwen-Image InstantX Union ControlNet（线稿_深度_姿态）_1971187587396341761.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Canny`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 10/11 个有
- `VAEDecode` —— 10/11 个有
- `DepthAnything_V2` —— 9/11 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 9/11 个有
- `ControlNetApplyAdvanced` —— 6/11 个有
- `ControlNetLoader` —— 6/11 个有
- `DWPreprocessor` —— 6/11 个有
- `ControlNetInpaintingAliMamaApply` —— 5/11 个有
- `ImagePadForOutpaint` —— 5/11 个有
- `ReferenceLatent` —— 5/11 个有
- `MiDaS-NormalMapPreprocessor` —— 3/11 个有
- `OpenposePreprocessor` —— 3/11 个有
- `ImpactSwitch` —— 1/11 个有
- `Int` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `PDImageResizeV2` —— 1/11 个有
- `VAEDecodeTiled` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 22 | 11 | 43% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 11 | 53% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| ControlNet 权重 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 32/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/11 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 22，11 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，11 个样本
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（32/11 个样本）：Steps较低可能导致细节不足
