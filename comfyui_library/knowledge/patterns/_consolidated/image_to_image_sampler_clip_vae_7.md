---
name: image_to_image_sampler_clip_vae_7
type: Image To Image
frequency: 25
level: strong
coverage: 0.9094
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImageConcanate, ImageStitch, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux Kontext 人物方向调整_2029096941195370498.json, 图片生成/图生图/Flux Kontext 人物方向调整｜多视角生成_1951928820335063041.json, 图片生成/图生图/Flux Kontext万物油画风新版加速版v1_1943677156033462273.json, 图片生成/图生图/Flux Kontext万物线稿提取简约加速版v1_1943677533101625345.json, 图片生成/图生图/Flux Kontext万物美式数字卡通加速版V1_1946975140393037826.json, 图片生成/图生图/Flux Kontext万物铅笔画高质量加速版v1_1946473852803407873.json, 图片生成/图生图/Flux Kontext万物铜像加速版v1_1946449382982213634.json, 图片生成/图生图/Flux Kontext万物高质量水彩画加速版v1_1943676548438196226.json, 图片生成/图生图/Flux Kontext二阶段万物老照片加速版v1(做旧，黑白，破损)_1946594162894626818.json, 图片生成/图生图/Flux Kontext同场景运镜及主体动作修改加速版v1_1946474584902393857.json, 图片生成/图生图/Flux Kontext图片编辑模型胸部变大神器一键变丰胸性感扩胸模型_2060639940156940290.json, 图片生成/图生图/Flux Kontext图片美学增强三重奏v1_1944787468988108802.json, 图片生成/图生图/Flux Kontext奇特XP人物单足加速版v1_1946451472924205058.json, 图片生成/图生图/Flux Kontext最强图像外扩加速版v1_1944793607230377986.json, 图片生成/图生图/Flux Kontext最强图像扩图_1948035581176623106.json, 图片生成/图生图/Flux Kontext毛绒毛毡玩具加速版v1_1946471882877231105.json, 图片生成/图生图/Flux Kontext深色主题人物肖像加速版v1_1946471396512788481.json, 图片生成/图生图/Flux Kontext照片做旧万物老照片加速版v1_1946474125385691137.json, 图片生成/图生图/Flux Kontext照片去油Real Skin加速版v1_1946788599365033986.json, 图片生成/图生图/Flux Kontext电影滤镜Lut加速版v1_1946442194157727746.json, 图片生成/图生图/Kontext 美颜相机 人像修复 30秒精修_1945140443552337922.json, 图片生成/图生图/kontext 一键粒子化 点云特效_1945135744891461634.json, 图片生成/图生图/一键比基尼换装_1947994655486029826.json, 图片生成/图生图/万物老照片加速版v1(做旧，黑白，破损)_2043522941861761026.json, 图片生成/图生图/人物换装迁移（kontext＋ IC Custom）_1963645388178935810.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_7

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/图生图/Flux Kontext 人物方向调整_2029096941195370498.json、图片生成/图生图/Flux Kontext 人物方向调整｜多视角生成_1951928820335063041.json、图片生成/图生图/Flux Kontext万物油画风新版加速版v1_1943677156033462273.json、图片生成/图生图/Flux Kontext万物线稿提取简约加速版v1_1943677533101625345.json、图片生成/图生图/Flux Kontext万物美式数字卡通加速版V1_1946975140393037826.json…）

- **类型**：Image To Image
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 25 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageConcanate`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImageOutput` —— 24/25 个有
- `CR Prompt Text` —— 23/25 个有
- `GoogleTranslateTextNode` —— 23/25 个有
- `LoraLoaderModelOnly` —— 23/25 个有
- `UnetLoaderGGUF` —— 23/25 个有
- `TeaCache` —— 22/25 个有
- `PDIMAGE_LongerSize` —— 17/25 个有
- `ImagePadKJ` —— 2/25 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/25 个有
- `NunchakuFluxDiTLoader` —— 2/25 个有
- `NunchakuFluxLoraLoader` —— 2/25 个有
- `easy showAnything` —— 2/25 个有
- `GetImageSize+` —— 1/25 个有
- `Image Comparer (rgthree)` —— 1/25 个有
- `JWInteger` —— 1/25 个有
- `LayerUtility: PurgeVRAM` —— 1/25 个有
- `RH_Translator` —— 1/25 个有
- `RunningHub ICCustom Loader` —— 1/25 个有
- `RunningHub ICCustom Sampler` —— 1/25 个有
- `SimpleMath+` —— 1/25 个有
- `easy imageRemBg` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 25 | 88% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 25 | 100% |
| 采样算法 | euler | - | 25 | 100% |
| 调度器 | simple | - | 25 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 25 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，25 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，25 个样本，一致性 100%
- 调度器 最常用 simple，25 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
