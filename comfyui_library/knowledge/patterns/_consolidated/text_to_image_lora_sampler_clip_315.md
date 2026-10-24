---
name: text_to_image_lora_sampler_clip_315
type: Text To Image
frequency: 6
level: strong
coverage: 0.817333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/全能图片2角色一致四格分镜 漫剧自动分镜出图_2098848127490023425.json, 图片生成/图生图/全能图片CPT-Image-2.5官方稳定版，图生图全能处理_2111521414405775361.json, 图片生成/图生图/全能图片G 2.0去脏去噪｜精修图生图电商处理_2090660175639310337.json, 图片生成/图生图/双图服装替换工作流｜全能图片2官方稳定版_2095583561020698625.json, 图片生成/文生图/GI2.5 Sunburst文生图加图生图集合流全能图片G2.5 二合一方案_2109407073535619073.json, 图片生成/文生图/GI2.5 Sunburst文生图图生图集合流｜新奇创意一把抓，文生图图生图双模式_2100484050002735106.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_315

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/全能图片2角色一致四格分镜 漫剧自动分镜出图_2098848127490023425.json、图片生成/图生图/全能图片CPT-Image-2.5官方稳定版，图生图全能处理_2111521414405775361.json、图片生成/图生图/全能图片G 2.0去脏去噪｜精修图生图电商处理_2090660175639310337.json、图片生成/图生图/双图服装替换工作流｜全能图片2官方稳定版_2095583561020698625.json、图片生成/文生图/GI2.5 Sunburst文生图加图生图集合流全能图片G2.5 二合一方案_2109407073535619073.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/6 个有
- `MuyeTextEditOutput` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `RH_RhartImageG25OfficialTokenSunburstEdit` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `PlaySound|pysssss` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `RH_RhartImageG25OfficialTokenSunburstTextToImage` —— 2/6 个有
- `RH_RhartImageG25SunburstImageToImage` —— 2/6 个有
- `RH_RhartImageG25SunburstTextToImage` —— 2/6 个有
- `ImpactSwitch` —— 1/6 个有
- `Int` —— 1/6 个有
- `RH_Nano_Banana2_Image2Image_Batch` —— 1/6 个有
- `RH_RhartImageNG31FlashOfficialImageToImage` —— 1/6 个有
- `RH_RhartImageNProEdit` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
