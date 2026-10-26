---
name: image_to_image_sampler_clip_vae_5
type: Image To Image
frequency: 34
level: strong
coverage: 0.979441
common_nodes: [CLIPTextEncode, ConditioningZeroOut, FluxGuidance, FluxKontextImageScale, ImageConcatMulti, KSampler, LoadImage, ReferenceLatent, SaveImage, Text Multiline, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX2Klein_写实风格转真人3DCG质感风格_极速出图_2041643301173989378.json, 图片生成/图生图/Flux Kontext Dev 开源主体换背景电商工作流_1939119172565524481.json, 图片生成/图生图/Flux Kontext Dev 开源提取线稿_1938935399077044226.json, 图片生成/图生图/Flux Kontext Dev 开源线稿上色_1938867678918725634.json, 图片生成/图生图/Flux Kontext Dev-3D建模风格加速版+放大_1944571710064742401.json, 图片生成/图生图/Flux Kontext Dev-Q版人物变写实加速版+放大（单图）_1941085269749874690.json, 图片生成/图生图/Flux Kontext Dev-一句话换装加速版+放大_1941651089550950402.json, 图片生成/图生图/Flux Kontext Dev-万物拍立得风格加速版+放大_1944571779916419073.json, 图片生成/图生图/Flux Kontext Dev-万物法相加速版+放大_1944571766952087554.json, 图片生成/图生图/Flux Kontext Dev-万物转充气玩偶加速版+放大_1944571747574140930.json, 图片生成/图生图/Flux Kontext Dev-动漫转手绘风格加速版+放大_1943475948014759938.json, 图片生成/图生图/Flux Kontext Dev-动漫转现实风格加速版+放大_1943124583442497537.json, 图片生成/图生图/Flux Kontext Dev-卡通转真人加速版+放大_1943665908873302017.json, 图片生成/图生图/Flux Kontext Dev-图像转皮克斯风格加速版+放大_1944927820898553857.json, 图片生成/图生图/Flux Kontext Dev-图片添加特效加速版+放大_1944016908414779394.json, 图片生成/图生图/Flux Kontext Dev-电影胶片质感+放大_1943661527230713858.json, 图片生成/图生图/Flux Kontext Dev-素描转真人加速版+放大_1946911282425683969.json, 图片生成/图生图/Flux Kontext Dev-线稿上色加速版+放大_1943666773826633729.json, 图片生成/图生图/Flux Kontext Dev-转粘土动漫风格加速版+放大_1948939899769630722.json, 图片生成/图生图/Flux Kontext Dev-转黑白老旧照片加速版+放大_1947228789387501569.json, 图片生成/图生图/Flux Kontext Dev-风景变漫画风格加速版+放大（单图）_1941103747567403009.json, 图片生成/图生图/Flux Kontext Dev-饰品珠宝金属精修加速版+放大_1944315412693569537.json, 图片生成/图生图/Flux Kontext Dev-马赛克消除加速版+放大_1943467504184270849.json, 图片生成/图生图/Flux Kontext Dev-高品质绘画风格转变加速版+放大_1947113753634189314.json, 图片生成/图生图/Flux Kontext Dev-黑白漫画转3D彩色漫画加速版+放大_1943957498988728321.json, 图片生成/图生图/Flux Kontext Dev一句话图像编辑V3（单图）_1938371380234620929.json, 图片生成/图生图/Flux Kontext Dev一句话图像编辑V3（双图）_1938399471682387969.json, 图片生成/图生图/Flux Kontext Dev一句话图生图+放大（双图）_1938849049141563393.json, 图片生成/图生图/Flux Kontext Dev一句话图生图加速版+放大（单图）_1939584231284645890.json, 图片生成/图生图/Flux Kontext Dev一句话图生图加速版+放大（双图）_1939560347982544897.json, 图片生成/图生图/Flux Kontext Dev万物消除加速版+放大（单图）_1940257498471288833.json, 图片生成/图生图/Flux Kontext Dev双人互动脸部一致性增强加速版V0.5_1940000386315096066.json, 图片生成/图生图/Flux Kontext Dev图片变机械风格加速版+放大（单图）_1940935206633369601.json, 图片生成/图生图/Flux1 Kontext put it v4.2_1971140729403805698.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_5

> 由 `engine/knowledge_consolidation` 从 34 个 workflow 归纳得出（图片生成/图生图/FLUX2Klein_写实风格转真人3DCG质感风格_极速出图_2041643301173989378.json、图片生成/图生图/Flux Kontext Dev 开源主体换背景电商工作流_1939119172565524481.json、图片生成/图生图/Flux Kontext Dev 开源提取线稿_1938935399077044226.json、图片生成/图生图/Flux Kontext Dev 开源线稿上色_1938867678918725634.json、图片生成/图生图/Flux Kontext Dev-3D建模风格加速版+放大_1944571710064742401.json…）

- **类型**：Image To Image
- **样本数**：34
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 34 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageConcatMulti`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `Text Multiline`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 33/34 个有
- `RH_Translator` —— 33/34 个有
- `ImageStitch` —— 31/34 个有
- `UNETLoader` —— 31/34 个有
- `PMRF` —— 29/34 个有
- `NunchakuFluxDiTLoader` —— 25/34 个有
- `NunchakuFluxLoraLoader` —— 25/34 个有
- `LoraLoaderModelOnly` —— 15/34 个有
- `UnetLoaderGGUF` —— 12/34 个有
- `ShowText|pysssss` —— 8/34 个有
- `MagCache` —— 6/34 个有
- `TeaCache` —— 6/34 个有
- `CR Prompt Text` —— 3/34 个有
- `CLIPLoader` —— 1/34 个有
- `FastCanvas` —— 1/34 个有
- `FastCanvasTool` —— 1/34 个有
- `GoogleTranslateTextNode` —— 1/34 个有
- `Image Comparer (rgthree)` —— 1/34 个有
- `LayerMask: PersonMaskUltra V2` —— 1/34 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 8 - 20 | 34 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 34 | 100% |
| 采样算法 | euler | - | 34 | 100% |
| 调度器 | simple | - | 34 | 100% |
| 重绘幅度 | 1 | 0.99 - 1 | 34 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/34 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 8 - 20，34 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，34 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，34 个样本，一致性 100%
- 调度器 最常用 simple，34 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.99 - 1，34 个样本，取值集中（一致性 100%）
- 高发问题（17/34 个样本）：Steps较低可能导致细节不足
