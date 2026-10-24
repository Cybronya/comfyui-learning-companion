---
name: image_to_image_sampler_clip_vae_6
type: Image To Image
frequency: 22
level: strong
coverage: 0.889364
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux Kontext超强去水印（numchaku10倍加速）_1941322884021383170.json, 图片生成/图生图/Flux kontext dev（三图版）极速电商万能融合王 指定动作换装换商品换背景_1945397369816981506.json, 图片生成/图生图/KONTEXT超级美颜，逼真皮肤纹理_1948333109749121025.json, 图片生成/图生图/Kontext Dev 人物妆容修改_1942405018597142529.json, 图片生成/图生图/Kontext Dev 模型｜重打光_1938996534883373057.json, 图片生成/图生图/Kontext Dev｜人物换衣服_1942404005945610241.json, 图片生成/图生图/Kontext [dev] 人像化妆｜一致性_1938548535325286402.json, 图片生成/图生图/Kontext [dev] 人物换衣服_1938897776589594626.json, 图片生成/图生图/Kontext [dev] 人物换装｜人物一致性_1938841329088843778.json, 图片生成/图生图/Kontext [dev] 人物表情编辑器_1939002140163821569.json, 图片生成/图生图/Kontext [dev] 卡通角色动作编辑_1938998476602855425.json, 图片生成/图生图/Kontext [dev] 图像编辑｜换背景_1938898561276764162.json, 图片生成/图生图/Kontext [dev] 图像编辑｜简易工作流_1938882018925334529.json, 图片生成/图生图/Kontext dev 人像美颜_1940743531990564865.json, 图片生成/图生图/Kontext dev 动漫转真人_1939855036945965058.json, 图片生成/图生图/Kontext dev 动漫转真人_1942399169807986689.json, 图片生成/图生图/Kontext dev 动漫转真人_1956572583183437826.json, 图片生成/图生图/Kontext 美剧恶搞之家风格_1946822314623426561.json, 图片生成/图生图/Kontext抖音图文快速版_1942169548500135937.json, 图片生成/图生图/Kontext（3D透明玻璃材质）_1946032275093942274.json, 图片生成/图生图/Kontext（国风刺绣风格）_1948667825243205633.json, 图片生成/图生图/毛线风格（Kontext Lora）_1949405488208326657.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_6

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/图生图/Flux Kontext超强去水印（numchaku10倍加速）_1941322884021383170.json、图片生成/图生图/Flux kontext dev（三图版）极速电商万能融合王 指定动作换装换商品换背景_1945397369816981506.json、图片生成/图生图/KONTEXT超级美颜，逼真皮肤纹理_1948333109749121025.json、图片生成/图生图/Kontext Dev 人物妆容修改_1942405018597142529.json、图片生成/图生图/Kontext Dev 模型｜重打光_1938996534883373057.json…）

- **类型**：Image To Image
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 22 个 workflow 都包含：
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
- `ImageStitch` —— 20/22 个有
- `EmptySD3LatentImage` —— 19/22 个有
- `UNETLoader` —— 19/22 个有
- `LoadImageOutput` —— 18/22 个有
- `PreviewImage` —— 18/22 个有
- `LoraLoaderModelOnly` —— 4/22 个有
- `TeaCache` —— 4/22 个有
- `LayerUtility: ImageReel` —— 3/22 个有
- `LayerUtility: ImageReelComposit` —— 3/22 个有
- `NunchakuFluxDiTLoader` —— 3/22 个有
- `CR Text` —— 2/22 个有
- `ImpactSwitch` —— 2/22 个有
- `RH_Translator` —— 2/22 个有
- `easy cleanGpuUsed` —— 2/22 个有
- `Bjornulf_ShowStringText` —— 1/22 个有
- `CR Simple Image Compare` —— 1/22 个有
- `ImageUpscaleWithModel` —— 1/22 个有
- `RepeatLatentBatch` —— 1/22 个有
- `UpscaleModelLoader` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 22 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 22 | 100% |
| 采样算法 | euler | - | 22 | 100% |
| 调度器 | simple | - | 22 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，22 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，22 个样本，一致性 100%
- 调度器 最常用 simple，22 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
