---
name: image_to_image_sampler_clip_vae_8
type: Image To Image
frequency: 22
level: strong
coverage: 0.860636
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/47qushuiyinwanmei_2050116000095453185.json, 图片生成/反推提示词/56wusunqushuiyin_2051290949149569025.json, 图片生成/图生图/(自用)去水印文字效果最佳+高清无损放大_2051996438422405121.json, 图片生成/图生图/20s去水印_2056912950182633473.json, 图片生成/图生图/Kontext Dev 模型｜重打光_1938996534883373057.json, 图片生成/图生图/Kontext Dev｜人物换衣服_1942404005945610241.json, 图片生成/图生图/Kontext [dev] 人像化妆｜一致性_1938548535325286402.json, 图片生成/图生图/Kontext [dev] 人物换衣服_1938897776589594626.json, 图片生成/图生图/Kontext [dev] 人物换装｜人物一致性_1938841329088843778.json, 图片生成/图生图/Kontext [dev] 人物表情编辑器_1939002140163821569.json, 图片生成/图生图/Kontext [dev] 卡通角色动作编辑_1938998476602855425.json, 图片生成/图生图/Kontext [dev] 图像编辑｜换背景_1938898561276764162.json, 图片生成/图生图/Kontext [dev] 图像编辑｜简易工作流_1938882018925334529.json, 图片生成/图生图/Kontext dev 人像美颜_1940743531990564865.json, 图片生成/图生图/Kontext dev 动漫转真人_1939855036945965058.json, 图片生成/图生图/Kontext dev 动漫转真人_1942399169807986689.json, 图片生成/图生图/Kontext dev 动漫转真人_1956572583183437826.json, 图片生成/图生图/Kontext 美剧恶搞之家风格_1946822314623426561.json, 图片生成/图生图/SeedVR2.5-去水印修复放大（有用）_2013859487152607234.json, 图片生成/图生图/kontext参考蒙版涂抹消除增加元素_1940288167415300097.json, 图片生成/图生图/去水印文字效果最佳+高清无损放大 zip_2052044034285285377.json, 图片生成/图生图/无损去图片水印，还原图片原本画质，ai去水印_2027795592591712258.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_8

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/反推提示词/47qushuiyinwanmei_2050116000095453185.json、图片生成/反推提示词/56wusunqushuiyin_2051290949149569025.json、图片生成/图生图/(自用)去水印文字效果最佳+高清无损放大_2051996438422405121.json、图片生成/图生图/20s去水印_2056912950182633473.json、图片生成/图生图/Kontext Dev 模型｜重打光_1938996534883373057.json…）

- **类型**：Image To Image
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageStitch` —— 21/22 个有
- `PreviewImage` —— 21/22 个有
- `UNETLoader` —— 19/22 个有
- `FluxKontextImageScale` —— 18/22 个有
- `EmptySD3LatentImage` —— 16/22 个有
- `LoadImageOutput` —— 16/22 个有
- `NunchakuFluxDiTLoader` —— 4/22 个有
- `SeedVR2LoadDiTModel` —— 4/22 个有
- `SeedVR2LoadVAEModel` —— 4/22 个有
- `SeedVR2VideoUpscaler` —— 4/22 个有
- `ImageResize+` —— 3/22 个有
- `ImageScaleBy` —— 3/22 个有
- `Color` —— 1/22 个有
- `HAIGC_SaveImagesToZip` —— 1/22 个有
- `InvertMask` —— 1/22 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/22 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/22 个有
- `RTXVideoSuperResolution` —— 1/22 个有
- `easy cleanGpuUsed` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 22 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 22 | 100% |
| 采样算法 | euler | - | 22 | 100% |
| 调度器 | simple | - | 22 | 95% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，22 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，22 个样本，一致性 100%
- 调度器 最常用 simple，22 个样本，一致性 95%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
