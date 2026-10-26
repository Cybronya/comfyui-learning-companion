---
name: image_to_image_sampler_clip_vae_11
type: Image To Image
frequency: 20
level: moderate
coverage: 0.89275
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX图生图，重绘，修复工作流_1915242265982205954.json, 图片生成/图生图/Flux Kontext Dev电商产品精修_1944057754137006081.json, 图片生成/图生图/Flux Kontext一键变大_1967443728325599233.json, 图片生成/图生图/Flux Kontext一键胸部变大神器 图片编辑模型胸部变大神器 变丰胸性感扩胸模型_2061421685408100353.json, 图片生成/图生图/Flux Kontext万物Logo融合Place It加速版v1_1946420363637219330.json, 图片生成/图生图/Flux Kontext万物sumsage动漫风加速版v1_1946450507353481217.json, 图片生成/图生图/Flux Kontext万物大理石雕塑加速版v1_1946436183197147137.json, 图片生成/图生图/Flux Kontext万物折纸风小清新加速版v1_1946442386803449857.json, 图片生成/图生图/Flux Kontext万物抽象色块风格加速版v1_1944784222865248258.json, 图片生成/图生图/Flux Kontext万物新海诚风格加速版v1_1946442556256186370.json, 图片生成/图生图/Flux Kontext万物日系动漫化加速版v1_1946450052674150402.json, 图片生成/图生图/Flux Kontext万物极简风提取线稿简笔画v1_1944780233847263233.json, 图片生成/图生图/Flux Kontext万物迁移Put it here加速版v1_1946742400083746817.json, 图片生成/图生图/Flux Kontext万物迁移Put it here加速版v4.2_1965934624595709954.json, 图片生成/图生图/Flux Kontext人物换头Place It加速版v1_1946407823179964418.json, 图片生成/图生图/Flux Kontext图像参考追色_1946826407948218369.json, 图片生成/图生图/Flux Kontext手持商品融合Place It加速版v1_1946422520510574594.json, 图片生成/图生图/Flux Kontext昏暗光线主体背景融合Fuse It加速版v1_1946424727658196993.json, 图片生成/图生图/【电商】产品手持+模特替换_1955441814003073025.json, 图片生成/图生图/🦖手持商品融合_1947540209770582017.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_11

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/FLUX图生图，重绘，修复工作流_1915242265982205954.json、图片生成/图生图/Flux Kontext Dev电商产品精修_1944057754137006081.json、图片生成/图生图/Flux Kontext一键变大_1967443728325599233.json、图片生成/图生图/Flux Kontext一键胸部变大神器 图片编辑模型胸部变大神器 变丰胸性感扩胸模型_2061421685408100353.json、图片生成/图生图/Flux Kontext万物Logo融合Place It加速版v1_1946420363637219330.json…）

- **类型**：Image To Image
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 19/20 个有
- `FluxKontextImageScale` —— 19/20 个有
- `LoraLoaderModelOnly` —— 19/20 个有
- `ReferenceLatent` —— 19/20 个有
- `UnetLoaderGGUF` —— 19/20 个有
- `PreviewImage` —— 18/20 个有
- `TeaCache` —— 18/20 个有
- `ImageConcanate` —— 17/20 个有
- `ImageStitch` —— 17/20 个有
- `PDIMAGE_LongerSize` —— 16/20 个有
- `CR Prompt Text` —— 15/20 个有
- `GoogleTranslateTextNode` —— 15/20 个有
- `LoadImageOutput` —— 15/20 个有
- `FastCanvas` —— 9/20 个有
- `FastCanvasTool` —— 9/20 个有
- `RMBG` —— 9/20 个有
- `TTP_Expand_And_Mask` —— 8/20 个有
- `ImageCropper` —— 6/20 个有
- `Image Comparer (rgthree)` —— 3/20 个有
- `ShowText|pysssss` —— 2/20 个有
- `CR Text` —— 1/20 个有
- `DeepTranslatorTextNode` —— 1/20 个有
- `JjkText` —— 1/20 个有
- `LatentUpscale` —— 1/20 个有
- `RHHiddenNodes` —— 1/20 个有
- `RH_LLMAPI_NODE` —— 1/20 个有
- `RH_Translator` —— 1/20 个有
- `Text Concatenate (JPS)` —— 1/20 个有
- `TextInputBasic` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 21 | 20 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 20 | 60% |
| 采样算法 | euler | - | 20 | 100% |
| 调度器 | simple | - | 20 | 95% |
| 重绘幅度 | 1 | 0.55 - 1 | 20 | 90% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 21，20 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，20 个样本
- 采样算法 最常用 euler，20 个样本，一致性 100%
- 调度器 最常用 simple，20 个样本，一致性 95%
- 重绘幅度 中位数 1，观测区间 0.55 - 1，20 个样本，取值集中（一致性 90%）
