---
name: image_to_image_sampler_clip_unet_2
type: Image To Image
frequency: 33
level: moderate
coverage: 0.981758
common_nodes: [CLIPTextEncode, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX -Kontext开源版-万物产品设计线稿上色_1941704882602852354.json, 图片生成/图生图/FLUX Kontext-DEV开源单图参考_1938430563936047106.json, 图片生成/图生图/FLUX.1Kontext.dev-单多图测试_1939156551691067393.json, 图片生成/图生图/FLUX2Klein_写实风格转真人3DCG质感风格_极速出图_2041643301173989378.json, 图片生成/图生图/Flux Kontext De-摄影灯光调节加速版+放大（单图）_1941107885030195202.json, 图片生成/图生图/Flux Kontext Dev 开源主体换背景电商工作流_1939119172565524481.json, 图片生成/图生图/Flux Kontext Dev 开源提取线稿_1938935399077044226.json, 图片生成/图生图/Flux Kontext Dev 开源线稿上色_1938867678918725634.json, 图片生成/图生图/Flux Kontext Dev-3D建模风格加速版+放大_1944571710064742401.json, 图片生成/图生图/Flux Kontext Dev-Q版人物变写实加速版+放大（单图）_1941085269749874690.json, 图片生成/图生图/Flux Kontext Dev-一句话换装加速版+放大_1941651089550950402.json, 图片生成/图生图/Flux Kontext Dev-万物拍立得风格加速版+放大_1944571779916419073.json, 图片生成/图生图/Flux Kontext Dev-万物法相加速版+放大_1944571766952087554.json, 图片生成/图生图/Flux Kontext Dev-万物转充气玩偶加速版+放大_1944571747574140930.json, 图片生成/图生图/Flux Kontext Dev-动漫转手绘风格加速版+放大_1943475948014759938.json, 图片生成/图生图/Flux Kontext Dev-动漫转现实风格加速版+放大_1943124583442497537.json, 图片生成/图生图/Flux Kontext Dev-卡通转真人加速版+放大_1943665908873302017.json, 图片生成/图生图/Flux Kontext Dev-图像转皮克斯风格加速版+放大_1944927820898553857.json, 图片生成/图生图/Flux Kontext Dev-图片添加特效加速版+放大_1944016908414779394.json, 图片生成/图生图/Flux Kontext Dev-电影胶片质感+放大_1943661527230713858.json, 图片生成/图生图/Flux Kontext Dev-素描转真人加速版+放大_1946911282425683969.json, 图片生成/图生图/Flux Kontext Dev-线稿上色加速版+放大_1943666773826633729.json, 图片生成/图生图/Flux Kontext Dev-转粘土动漫风格加速版+放大_1948939899769630722.json, 图片生成/图生图/Flux Kontext Dev-转黑白老旧照片加速版+放大_1947228789387501569.json, 图片生成/图生图/Flux Kontext Dev-风景变漫画风格加速版+放大（单图）_1941103747567403009.json, 图片生成/图生图/Flux Kontext Dev-饰品珠宝金属精修加速版+放大_1944315412693569537.json, 图片生成/图生图/Flux Kontext Dev-马赛克消除加速版+放大_1943467504184270849.json, 图片生成/图生图/Flux Kontext Dev-高品质绘画风格转变加速版+放大_1947113753634189314.json, 图片生成/图生图/Flux Kontext Dev-黑白漫画转3D彩色漫画加速版+放大_1943957498988728321.json, 图片生成/图生图/Flux Kontext Dev一句话图生图加速版+放大（单图）_1939584231284645890.json, 图片生成/图生图/Flux Kontext Dev一句话图生图加速版+放大（双图）_1939560347982544897.json, 图片生成/图生图/Flux Kontext Dev万物消除加速版+放大（单图）_1940257498471288833.json, 图片生成/图生图/Flux Kontext Dev图片变机械风格加速版+放大（单图）_1940935206633369601.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_2

> 由 `engine/knowledge_consolidation` 从 33 个 workflow 归纳得出（图片生成/图生图/FLUX -Kontext开源版-万物产品设计线稿上色_1941704882602852354.json、图片生成/图生图/FLUX Kontext-DEV开源单图参考_1938430563936047106.json、图片生成/图生图/FLUX.1Kontext.dev-单多图测试_1939156551691067393.json、图片生成/图生图/FLUX2Klein_写实风格转真人3DCG质感风格_极速出图_2041643301173989378.json、图片生成/图生图/Flux Kontext De-摄影灯光调节加速版+放大（单图）_1941107885030195202.json…）

- **类型**：Image To Image
- **样本数**：33
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 33 个 workflow 都包含：
- `CLIPTextEncode`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 32/33 个有
- `DualCLIPLoader` —— 32/33 个有
- `ImageConcatMulti` —— 31/33 个有
- `RH_Translator` —— 31/33 个有
- `ImageStitch` —— 30/33 个有
- `Text Multiline` —— 30/33 个有
- `PMRF` —— 29/33 个有
- `NunchakuFluxDiTLoader` —— 26/33 个有
- `NunchakuFluxLoraLoader` —— 26/33 个有
- `LoraLoaderModelOnly` —— 11/33 个有
- `UnetLoaderGGUF` —— 8/33 个有
- `ShowText|pysssss` —— 5/33 个有
- `TeaCache` —— 5/33 个有
- `CR Prompt Text` —— 3/33 个有
- `MagCache` —— 3/33 个有
- `ImageResizeKJv2` —— 2/33 个有
- `CLIPLoader` —— 1/33 个有
- `ETN_Translate` —— 1/33 个有
- `GoogleTranslateTextNode` —— 1/33 个有
- `Image Comparer (rgthree)` —— 1/33 个有
- `PreviewImage` —— 1/33 个有
- `SDXLEmptyLatentSizePicker+` —— 1/33 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 30 | 33 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 33 | 100% |
| 采样算法 | euler | - | 33 | 100% |
| 调度器 | simple | - | 33 | 100% |
| 重绘幅度 | 1 | 0.99 - 1 | 33 | 100% |
| 宽度 | 832x1216 (0.68) | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/33 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 30，33 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，33 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，33 个样本，一致性 100%
- 调度器 最常用 simple，33 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.99 - 1，33 个样本，取值集中（一致性 100%）
- 高发问题（18/33 个样本）：Steps较低可能导致细节不足
