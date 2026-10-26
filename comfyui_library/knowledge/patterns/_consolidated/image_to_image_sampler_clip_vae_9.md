---
name: image_to_image_sampler_clip_vae_9
type: Image To Image
frequency: 21
level: strong
coverage: 0.971571
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/F.1 KONTEXT DEV 单图版nunchaku极速电商万能改图王_1945395741722386434.json, 图片生成/图生图/F.1 Kontext dev 官方两图版 万物编辑 图片融合 换衣换背景_1943235556400914434.json, 图片生成/图生图/F.1 kontext dev三图 电商万能融合王_1943683362261204994.json, 图片生成/图生图/F.1KONTEXT 两图nunchaku极速电商融合王_1945397317442916354.json, 图片生成/图生图/FLUX -Kontext开源版-万物产品设计线稿上色_1941704882602852354.json, 图片生成/图生图/FLUX Kontext-DEV开源单图参考_1938430563936047106.json, 图片生成/图生图/FLUX Kontext四倍提速(nunchaku)提取图案加速_1950117459787472897.json, 图片生成/图生图/FLUX Kontext四倍提速（nunchaku）_1940002928692465665.json, 图片生成/图生图/FLUX_Kontext 套图2_1945908436590620674.json, 图片生成/图生图/Flux Kontext De-摄影灯光调节加速版+放大（单图）_1941107885030195202.json, 图片生成/图生图/Flux Kontext Dev-图片生成3视图加速版+放大_1942029327120941058.json, 图片生成/图生图/Flux Kontext Dev-图片转变手办加速版+放大_1943663969976352770.json, 图片生成/图生图/Flux Kontext Dev-图片转国画风格加速版+放大_1943229697700618241.json, 图片生成/图生图/Flux Kontext Dev-图片转水彩画加速版+放大_1943871375528329218.json, 图片生成/图生图/Flux Kontext Dev-图片转电影颗粒质感风格加速版+放大_1943871523440693250.json, 图片生成/图生图/Flux Kontext Dev-图片风格转绘（毛毡）加速版+放大_1943122910695342081.json, 图片生成/图生图/Flux Kontext Dev-扩图加速版+放大_1943871102491955202.json, 图片生成/图生图/Flux Kontext Dev万物转3D Chibi Style加速版+放大（单图）_1940291607579021314.json, 图片生成/图生图/Flux Kontext Dev万物转plushie毛绒风格加速版+放大（单图）_1940289618552209410.json, 图片生成/图生图/Flux Kontext Dev万物转吉卜力加速版+放大（单图）_1940569779944189954.json, 图片生成/图生图/Flux Kontext Dev二阶段换装工作流V1（提高成功率）_1939271936381992962.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_9

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/F.1 KONTEXT DEV 单图版nunchaku极速电商万能改图王_1945395741722386434.json、图片生成/图生图/F.1 Kontext dev 官方两图版 万物编辑 图片融合 换衣换背景_1943235556400914434.json、图片生成/图生图/F.1 kontext dev三图 电商万能融合王_1943683362261204994.json、图片生成/图生图/F.1KONTEXT 两图nunchaku极速电商融合王_1945397317442916354.json、图片生成/图生图/FLUX -Kontext开源版-万物产品设计线稿上色_1941704882602852354.json…）

- **类型**：Image To Image
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 20/21 个有
- `ImageStitch` —— 18/21 个有
- `RH_Translator` —— 18/21 个有
- `NunchakuFluxDiTLoader` —— 16/21 个有
- `UNETLoader` —— 16/21 个有
- `ImageConcatMulti` —— 13/21 个有
- `NunchakuFluxLoraLoader` —— 13/21 个有
- `PMRF` —— 12/21 个有
- `Text Multiline` —— 12/21 个有
- `EmptySD3LatentImage` —— 6/21 个有
- `PreviewImage` —— 4/21 个有
- `ImageConcanate` —— 3/21 个有
- `ShowText|pysssss` —— 3/21 个有
- `GoogleTranslateTextNode` —— 2/21 个有
- `ImagePadForOutpaint` —— 2/21 个有
- `ETN_Translate` —— 1/21 个有
- `ImageFlip+` —— 1/21 个有
- `ImageResizeKJv2` —— 1/21 个有
- `LoadLatent` —— 1/21 个有
- `LoraLoaderModelOnly` —— 1/21 个有
- `MZ_Flux1PartialLoad_Patch` —— 1/21 个有
- `MagCache` —— 1/21 个有
- `SaveLatent` —— 1/21 个有
- `UnetLoaderGGUF` —— 1/21 个有
- `easy showAnything` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 21 | 56% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 21 | 100% |
| 采样算法 | euler | - | 21 | 100% |
| 调度器 | simple | - | 21 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，21 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，21 个样本，一致性 100%
- 调度器 最常用 simple，21 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
