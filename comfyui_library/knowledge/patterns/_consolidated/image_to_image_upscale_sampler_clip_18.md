---
name: image_to_image_upscale_sampler_clip_18
type: Image To Image
frequency: 7
level: moderate
coverage: 0.842857
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LoadImage, SaveImage, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima Preview2分块放大_2033542982825152514.json, 图片生成/文生图/Anima+Aesthetic+1.1｜分块放大_2078701745957588993.json, 图片生成/文生图/Anima分块放大_2021929692445544449.json, 图片生成/文生图/Magic-Wan-V2分块超清放大_1991113618789892098.json, 图片生成/文生图/Magic-Wan-V2加速分块超清放大_1991145078443868162.json, 图片生成/文生图/Z-Image-base放大_2016768153547710466.json, 视频生成/文生视频/Anima-2.9B｜分块高清重绘_2089343542203346946.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_18

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Anima Preview2分块放大_2033542982825152514.json、图片生成/文生图/Anima+Aesthetic+1.1｜分块放大_2078701745957588993.json、图片生成/文生图/Anima分块放大_2021929692445544449.json、图片生成/文生图/Magic-Wan-V2分块超清放大_1991113618789892098.json、图片生成/文生图/Magic-Wan-V2加速分块超清放大_1991145078443868162.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `Seed (rgthree)` —— 6/7 个有
- `VAELoader` —— 6/7 个有
- `LoraLoader` —— 5/7 个有
- `Florence2Run` —— 4/7 个有
- `DownloadAndLoadFlorence2Model` —— 3/7 个有
- `WD14Tagger|pysssss` —— 3/7 个有
- `JWStringConcat` —— 2/7 个有
- `KepStringLiteral` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `ModelSamplingSD3` —— 2/7 个有
- `ClownsharKSampler_Beta` —— 1/7 个有
- `Florence2ModelLoader` —— 1/7 个有
- `ModelSamplingAuraFlow` —— 1/7 个有
- `PathchSageAttentionKJ` —— 1/7 个有
- `VAELoaderKJ` —— 1/7 个有
- `XB_UNetNameBroadcaster` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.85 | 0.85 - 0.85 | 5 | 100% |
| LoRA 文本强度 | 0.85 | 0.85 - 0.85 | 5 | 100% |
| 采样步数 | 20 | 4 - 31 | 7 | 62% |
| Prompt 约束强度(CFG) | 3 | 1 - 8 | 7 | 32% |
| 采样算法 | euler | - | 7 | 29% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 0.25 | 0.15 - 1 | 7 | 13% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 7/7 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 1/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 0.85，观测区间 0.85 - 0.85，5 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.85，观测区间 0.85 - 0.85，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 4 - 31，7 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 8，7 个样本，取值分散，一致性仅 32%
- 采样算法 最常用 euler，7 个样本，一致性 29%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 0.25，观测区间 0.15 - 1，7 个样本，取值分散，一致性仅 13%
- 高发问题（7/7 个样本）：发现KSampler但没有VAEDecode
