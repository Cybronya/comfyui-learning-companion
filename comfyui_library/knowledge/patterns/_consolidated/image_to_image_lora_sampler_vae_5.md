---
name: image_to_image_lora_sampler_vae_5
type: Image To Image
frequency: 17
level: strong
coverage: 0.672
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/B6、图像编辑 千问2.5 GGUF - 和风_1992879635685855234.json, 图片生成/图生图/Ban_Qwen-动漫转写实真人V2版_1988231591057121281.json, 图片生成/图生图/Ban_Qwen-艺术摄影图片重打光_1988243660754042882.json, 图片生成/图生图/Edit-2509-光线迁移优化模型_2000043637197205506.json, 图片生成/图生图/FireRed-Image-Edit-1.0 老照片修复重新上色_2026822786328563714.json, 图片生成/图生图/NGS风格转bjd融光_2082671756535492609.json, 图片生成/图生图/NGS风格转bjd融光_2085195450470191106.json, 图片生成/图生图/Qwen 2511 史上最强-动漫转写实真人正式版_2013133142546194434.json, 图片生成/图生图/Qwen2511-真人转动漫_2014909381707567105.json, 图片生成/图生图/【推荐，动漫转真人快速版】动漫转写实真人2511-高还原_2017655194384867330.json, 图片生成/图生图/万物转厚涂梦幻动漫风格_2511（风格重绘）_2012103777167347714.json, 图片生成/图生图/动漫转真人高还原_2067296922406313986.json, 图片生成/图生图/史上最强-动漫转写实真人2511AnythingtoRealCharacters正式版-高还原_2088249983240851458.json, 图片生成/图生图/史上最强-动漫转写实真人2511（AnythingtoRealCharacters）正式版-高还原_2009527411641159681.json, 图片生成/图生图/小红书 FireRed image-Edit-1.1 老照片修复重新上色_2033805219217281026.json, 图片生成/图生图/效果最好-动漫转写实真人2511（高还原）_2014551974833819650.json, 平台全量/Qwen Edit Plus 模特换装_1970455977734643713.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_5

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/B6、图像编辑 千问2.5 GGUF - 和风_1992879635685855234.json、图片生成/图生图/Ban_Qwen-动漫转写实真人V2版_1988231591057121281.json、图片生成/图生图/Ban_Qwen-艺术摄影图片重打光_1988243660754042882.json、图片生成/图生图/Edit-2509-光线迁移优化模型_2000043637197205506.json、图片生成/图生图/FireRed-Image-Edit-1.0 老照片修复重新上色_2026822786328563714.json…）

- **类型**：Image To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 17 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 16/17 个有
- `TextEncodeQwenImageEditPlus` —— 16/17 个有
- `UNETLoader` —— 16/17 个有
- `TextEncodeQwenImageEdit` —— 14/17 个有
- `GetNode` —— 13/17 个有
- `SetNode` —— 13/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/17 个有
- `FluxKontextMultiReferenceLatentMethod` —— 10/17 个有
- `ImageScaleToTotalPixels` —— 7/17 个有
- `Image Comparer (rgthree)` —— 3/17 个有
- `ReferenceLatent` —— 2/17 个有
- `Seed Generator` —— 2/17 个有
- `Text` —— 2/17 个有
- `Anything Everywhere` —— 1/17 个有
- `ImageConcanate` —— 1/17 个有
- `Int` —— 1/17 个有
- `PreviewImage` —— 1/17 个有
- `UnetLoaderGGUF` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 9 | 17 | 64% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 17 | 100% |
| 采样算法 | euler | - | 17 | 100% |
| 调度器 | simple | - | 17 | 88% |
| 重绘幅度 | 1 | 0.8 - 1 | 17 | 93% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 9，17 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，17 个样本，一致性 100%
- 调度器 最常用 simple，17 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，17 个样本，取值集中（一致性 93%）
- 高发问题（17/17 个样本）：Steps较低可能导致细节不足
