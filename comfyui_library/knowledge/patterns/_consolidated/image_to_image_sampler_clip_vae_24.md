---
name: image_to_image_sampler_clip_vae_24
type: Image To Image
frequency: 9
level: strong
coverage: 0.919
common_nodes: [CLIPTextEncode, ConditioningZeroOut, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/kontext-gguf版单图编辑（真人转3D，真人转动漫，动漫转真人）_1989474249289158658.json, 图片生成/图生图/kontext单图工作流_1944956155041075201.json, 图片生成/图生图/kontext单图工作流_1971121957414543362.json, 图片生成/图生图/kontext单图转绘-免费-速度快-效果好_1963527482023694337.json, 图片生成/图生图/kontext去水印_1958369496044093441.json, 图片生成/图生图/kontext商业级印花提取工作流V1版本_1945098408367673345.json, 图片生成/图生图/kontext图生图(双图)故事绘本_2010263590753800193.json, 图片生成/图生图/kontext皮肤纹理真实化_1942120587915587585.json, 图片生成/图生图/工作流基础系列13-FLUX.1-Kontext编辑工作流_2012813919022227458.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_24

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/kontext-gguf版单图编辑（真人转3D，真人转动漫，动漫转真人）_1989474249289158658.json、图片生成/图生图/kontext单图工作流_1944956155041075201.json、图片生成/图生图/kontext单图工作流_1971121957414543362.json、图片生成/图生图/kontext单图转绘-免费-速度快-效果好_1963527482023694337.json、图片生成/图生图/kontext去水印_1958369496044093441.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 8/9 个有
- `UNETLoader` —— 8/9 个有
- `FluxKontextImageScale` —— 6/9 个有
- `EmptySD3LatentImage` —— 3/9 个有
- `ImageStitch` —— 3/9 个有
- `LoraLoaderModelOnly` —— 3/9 个有
- `UnetLoaderGGUF` —— 3/9 个有
- `ImageScaleToTotalPixels` —— 2/9 个有
- `DualCLIPLoaderGGUF` —— 1/9 个有
- `ETN_Translate` —— 1/9 个有
- `GetImageSize+` —— 1/9 个有
- `Image Comparer (rgthree)` —— 1/9 个有
- `LayerUtility: GetImageSize` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `Seed` —— 1/9 个有
- `Seed (rgthree)` —— 1/9 个有
- `easy promptList` —— 1/9 个有
- `workflow>UpSpeed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 9 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
