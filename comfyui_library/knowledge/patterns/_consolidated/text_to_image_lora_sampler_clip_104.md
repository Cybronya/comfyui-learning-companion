---
name: text_to_image_lora_sampler_clip_104
type: Text To Image
frequency: 13
level: strong
coverage: 0.885692
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageResizeKJv2, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/krea2四视图生成流加强版｜角色设定图生图_2095213399323004929.json, 图片生成/图生图/一分钟极速换脸｜图生图局部重绘一键出片生成_2090149383538036738.json, 图片生成/图生图/一分钟极速换脸｜图生图局部重绘一键出片生成_2090615604003827713.json, 图片生成/图生图/一分钟极速换脸｜图生图局部重绘一键出片生成_2090631125050937346.json, 图片生成/图生图/上传参考图生成角色四视图 Krea2资产库简易版_2104321390848598018.json, 图片生成/图生图/上传图片一键生成四视图【短剧资产专用】_2096435540651503618.json, 图片生成/图生图/单图编辑图片处理｜pipi-krea2换装图生图_2095582778946580482.json, 图片生成/图生图/四视图生成加强版｜krea2图生图角色设计_2095493686284079106.json, 图片生成/图生图/四视图角色设定表｜Krea2一键生成角色一致性设计_2090897661913292802.json, 图片生成/图生图/四视图角色资产库｜Krea2分镜出图图生图生成_2095118168535687170.json, 图片生成/图生图/四视图角色资产库｜Krea2分镜出图角色设计图生图_2092611870934003713.json, 图片生成/图生图/换装编辑一键处理｜pipi-krea2图生图工作流_2095581266308591618.json, 图片生成/图生图/真实人与漫剧角色四视图｜角色一致性设定图生成_2095964023656370177.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_104

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/krea2四视图生成流加强版｜角色设定图生图_2095213399323004929.json、图片生成/图生图/一分钟极速换脸｜图生图局部重绘一键出片生成_2090149383538036738.json、图片生成/图生图/一分钟极速换脸｜图生图局部重绘一键出片生成_2090615604003827713.json、图片生成/图生图/一分钟极速换脸｜图生图局部重绘一键出片生成_2090631125050937346.json、图片生成/图生图/上传参考图生成角色四视图 Krea2资产库简易版_2104321390848598018.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 10/13 个有
- `Krea2EditGroundedEncode` —— 10/13 个有
- `Krea2EditModelPatch` —— 10/13 个有
- `PreviewImage` —— 10/13 个有
- `孤海注释` —— 10/13 个有
- `Image Comparer (rgthree)` —— 5/13 个有
- `ReferenceLatent` —— 5/13 个有
- `AddLabel` —— 4/13 个有
- `GetImageSize` —— 4/13 个有
- `ImageConcatMulti` —— 4/13 个有
- `EmptyFlux2LatentImage` —— 3/13 个有
- `ColorMatchV2` —— 2/13 个有
- `ConditioningZeroOut` —— 2/13 个有
- `String Literal` —— 2/13 个有
- `easy loraStack` —— 2/13 个有
- `easy loraStackApply` —— 2/13 个有
- `GetNode` —— 1/13 个有
- `SetNode` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（18/13 个样本）：Steps较低可能导致细节不足
