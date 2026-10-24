---
name: image_to_image_sampler_clip_vae_5
type: Image To Image
frequency: 33
level: strong
coverage: 1
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, RH_Translator, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/KontextNunchakuDevLora万物皮克斯风格_1944262455931338753.json, 图片生成/图生图/KontextNunchakuDevLora万物美化_1943149163196669953.json, 图片生成/图生图/KontextNunchakuDevLora人物三视图_1944263357543120898.json, 图片生成/图生图/KontextNunchakuDevLora写实艺术风格_1943145435769036801.json, 图片生成/图生图/KontextNunchakuDevLora发光粒子素描风格_1943525207695126529.json, 图片生成/图生图/KontextNunchakuDevLora吉卜力风格_1943499828590485506.json, 图片生成/图生图/KontextNunchakuDevLora孤独的王者动漫风格_1943501453111816194.json, 图片生成/图生图/KontextNunchakuDevLora拍立得相片_1944265400445992961.json, 图片生成/图生图/KontextNunchakuDevLora潦草彩铅线条插画风_1942783159161262082.json, 图片生成/图生图/KontextNunchakuDevLora火焰特效_1943526598106619905.json, 图片生成/图生图/KontextNunchakuDevLora鸟山明风格_1943504711444295681.json, 图片生成/图生图/KontextNunchakuDev万物彩铅风_1942781217336922113.json, 图片生成/图生图/KontextNunchakuDev万物毛茸茸_1942785932607033346.json, 图片生成/图生图/KontextNunchakuDev万物移除_1942788245061349377.json, 图片生成/图生图/KontextNunchakuDev喜剧复古动漫风格_1941339536565891074.json, 图片生成/图生图/KontextNunchakuDev极简主义插画_1942408948442140674.json, 图片生成/图生图/KontextNunchakuDev水粉画艺术风格_1942422462619652098.json, 图片生成/图生图/KontextNunchakuDev波普艺术风格_1942427162085625858.json, 图片生成/图生图/KontextNunchakuDev玻璃雕像_1942437081085849601.json, 图片生成/图生图/KontextNunchakuDev瑞克莫蒂动漫风格_1942412431219961857.json, 图片生成/图生图/KontextNunchakuDev立体派艺术风格_1942424438593761282.json, 图片生成/图生图/KontextNunchakuDev线条画风格_1942777046684905473.json, 图片生成/图生图/KontextNunchakuDev转绘低模_1941336591367565314.json, 图片生成/图生图/KontextNunchakuDev转绘幻想艺术_1941331496819179521.json, 图片生成/图生图/KontextNunchakuDev转绘等距艺术_1941333847969787906.json, 图片生成/图生图/KontextNunchakuDev转绘线艺_1941335193267683329.json, 图片生成/图生图/KontextNunchakuDev转绘霓虹_1941338008530612226.json, 图片生成/图生图/KontextNunchakuDev重新打光_1942783905021759489.json, 图片生成/图生图/KontextNunchakuDev铅笔素描艺术风格_1942410316838014978.json, 图片生成/图生图/KontextNunchakuDev黑白变彩色_1941328448780713986.json, 图片生成/图生图/KontextNunchakuDev黑胡桃木材质人像_1942421784010625026.json, 图片生成/图生图/flux kontext 三联图_1939285901316956162.json, 图片生成/图生图/kontextnunchakudevlora全能图片G4o同款icon头像_1943141910594666498.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_5

> 由 `engine/knowledge_consolidation` 从 33 个 workflow 归纳得出（图片生成/图生图/KontextNunchakuDevLora万物皮克斯风格_1944262455931338753.json、图片生成/图生图/KontextNunchakuDevLora万物美化_1943149163196669953.json、图片生成/图生图/KontextNunchakuDevLora人物三视图_1944263357543120898.json、图片生成/图生图/KontextNunchakuDevLora写实艺术风格_1943145435769036801.json、图片生成/图生图/KontextNunchakuDevLora发光粒子素描风格_1943525207695126529.json…）

- **类型**：Image To Image
- **样本数**：33
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 33 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `RH_Translator`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingFlux` —— 32/33 个有
- `NunchakuFluxDiTLoader` —— 32/33 个有
- `LoraLoaderModelOnly` —— 26/33 个有
- `SDXLPromptStyler` —— 19/33 个有
- `EmptySD3LatentImage` —— 6/33 个有
- `ArtistsImage_Zho` —— 4/33 个有
- `JoinStringMulti` —— 4/33 个有
- `ImageStitch` —— 2/33 个有
- `Get Image Size` —— 1/33 个有
- `UnetLoaderGGUF` —— 1/33 个有
- `easy imageScaleDownBy` —— 1/33 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 33 | 96% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 33 | 100% |
| 采样算法 | euler | - | 33 | 100% |
| 调度器 | simple | - | 33 | 85% |
| 重绘幅度 | 1 | 1 - 1 | 33 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，33 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，33 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，33 个样本，一致性 100%
- 调度器 最常用 simple，33 个样本，一致性 85%
- 重绘幅度 中位数 1，观测区间 1 - 1，33 个样本，取值集中（一致性 100%）
