---
name: image_to_image_sampler_clip_vae_4
type: Image To Image
frequency: 37
level: strong
coverage: 0.904973
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/20s去水印_2056912950182633473.json, 图片生成/图生图/CG迷-Kontext dev多图融合标准工作流_1938582981999316993.json, 图片生成/图生图/F.1 KONTEXT DEV 单图版nunchaku极速电商万能改图王_1945395741722386434.json, 图片生成/图生图/F.1 Kontext dev 官方两图版 万物编辑 图片融合 换衣换背景_1943235556400914434.json, 图片生成/图生图/F.1 kontext dev三图 电商万能融合王_1943683362261204994.json, 图片生成/图生图/F.1KONTEXT 两图nunchaku极速电商融合王_1945397317442916354.json, 图片生成/图生图/FLUX Kontext dev 图生图工作流_1946449845256089601.json, 图片生成/图生图/FLUX Kontext四倍提速(nunchaku)提取图案加速_1950117459787472897.json, 图片生成/图生图/FLUX Kontext四倍提速（nunchaku）_1940002928692465665.json, 图片生成/图生图/Flux Kontext Dev 10倍三重加速（Nunchaku）_1939491330919735298.json, 图片生成/图生图/Flux Kontext Dev 22种风格转绘_1939856959657185281.json, 图片生成/图生图/Flux Kontext Dev 22种风格转绘加速稳定版V1（Nunchaku）_1939713012859052033.json, 图片生成/图生图/Flux Kontext Dev 22种风格转绘加速稳定版V1（Nunchaku）_1940754613035495426.json, 图片生成/图生图/Flux Kontext Dev万物大头娃娃V1（Nunchaku）_1939706542520504322.json, 图片生成/图生图/Flux Kontext Dev万物打光LORA实验版V1（Nunchaku）_1939748318878863361.json, 图片生成/图生图/Flux Kontext Dev万物昭和动漫风（Nunchaku）_1940464547004313602.json, 图片生成/图生图/Flux Kontext Dev万物毛毡风（Nunchaku）_1940461545933664257.json, 图片生成/图生图/Flux Kontext Dev万物消除LORA稳定版V1（Nunchaku）_1939727401398276097.json, 图片生成/图生图/Flux Kontext Dev万物特殊像素动漫V1.1（Nunchaku）_1939698283822682113.json, 图片生成/图生图/Flux Kontext Dev万物穿黑色乳胶衣换装V1（Nunchaku）_1939678966276132866.json, 图片生成/图生图/Flux Kontext Dev万物西蓝花发型V1（Nunchaku）_1939693410351489026.json, 图片生成/图生图/Flux Kontext Dev万物赛博机械化V1（Nunchaku）_1939700410850385921.json, 图片生成/图生图/Flux Kontext Dev万物转手绘复古动漫（Nunchaku）_1940463589205454849.json, 图片生成/图生图/Flux Kontext Dev万物转绘可爱轻像素风（Nunchaku）_1940464478230310914.json, 图片生成/图生图/Flux Kontext Dev万物高质量吉卜力转绘（Nunchaku）_1940450894993403906.json, 图片生成/图生图/Flux Kontext Dev人物方向调整LORA加强版（Nunchaku）_1940464465148276737.json, 图片生成/图生图/Flux Kontext Dev人脸缩放（Nunchaku）_1940441962178654209.json, 图片生成/图生图/Flux Kontext Dev光腿神器脱丝袜V1（Nunchaku）_1939695799502544897.json, 图片生成/图生图/Flux Kontext Dev动漫转真人dtpr风格（Nunchaku）_1940444736761262081.json, 图片生成/图生图/Flux Kontext Dev图像模糊变高清修复V1（j即插即用，修复迭代损失）_1940442151652323329.json, 图片生成/图生图/Flux Kontext Dev扁平化动漫风格转绘V1（Nunchaku）_1939697504759750658.json, 图片生成/图生图/Flux Kontext Dev手绘风4视图（Nunchaku）_1940445748691447810.json, 图片生成/图生图/Flux Kontext Dev手部修复（Nunchaku）_1941544818873102338.json, 图片生成/图生图/Flux Kontext Dev摄影打光调色（Nunchaku）_1941519235963318274.json, 图片生成/图生图/Flux Kontext Dev脚部修复（Nunchaku）_1941539755584864258.json, 图片生成/图生图/Flux Kontext 人物方向调整_2029096941195370498.json, 图片生成/图生图/Flux Kontext 人物方向调整｜多视角生成_1951928820335063041.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_4

> 由 `engine/knowledge_consolidation` 从 37 个 workflow 归纳得出（图片生成/图生图/20s去水印_2056912950182633473.json、图片生成/图生图/CG迷-Kontext dev多图融合标准工作流_1938582981999316993.json、图片生成/图生图/F.1 KONTEXT DEV 单图版nunchaku极速电商万能改图王_1945395741722386434.json、图片生成/图生图/F.1 Kontext dev 官方两图版 万物编辑 图片融合 换衣换背景_1943235556400914434.json、图片生成/图生图/F.1 kontext dev三图 电商万能融合王_1943683362261204994.json…）

- **类型**：Image To Image
- **样本数**：37
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 37 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
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
- `ImageStitch` —— 35/37 个有
- `EmptySD3LatentImage` —— 33/37 个有
- `NunchakuFluxDiTLoader` —— 33/37 个有
- `PreviewImage` —— 33/37 个有
- `LoadImageOutput` —— 29/37 个有
- `CR Prompt Text` —— 28/37 个有
- `GoogleTranslateTextNode` —— 28/37 个有
- `ImageConcanate` —— 28/37 个有
- `NunchakuFluxLoraLoader` —— 27/37 个有
- `RH_Translator` —— 6/37 个有
- `UNETLoader` —— 4/37 个有
- `easy promptConcat` —— 4/37 个有
- `ImpactSwitch` —— 3/37 个有
- `JWInteger` —— 3/37 个有
- `RHHiddenNodes` —— 3/37 个有
- `ShowText` —— 3/37 个有
- `easy showAnything` —— 3/37 个有
- `DeepTranslatorTextNode` —— 1/37 个有
- `ImageFlip+` —— 1/37 个有
- `LoraLoaderModelOnly` —— 1/37 个有
- `PrimitiveStringMultiline` —— 1/37 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 37 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 37 | 100% |
| 采样算法 | euler | - | 37 | 100% |
| 调度器 | simple | - | 37 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 37 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/37 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，37 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，37 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，37 个样本，一致性 100%
- 调度器 最常用 simple，37 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，37 个样本，取值集中（一致性 100%）
