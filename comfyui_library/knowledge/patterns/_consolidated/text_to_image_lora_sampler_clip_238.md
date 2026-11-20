---
name: text_to_image_lora_sampler_clip_238
type: Text To Image
frequency: 8
level: strong
coverage: 0.909875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/397种风格内置 Krea2照片风格迁移一键转换_2104349505163448322.json, 图片生成/图生图/AI漫剧制作｜参考图一键生成四视图 图生图分镜素材工作流_2097501947946430465.json, 图片生成/图生图/FZ-MinimaxH3参考图生成四视图｜Krea2人物角色设计_2097107184881590273.json, 图片生成/图生图/KREA-2-EDIT单图编辑V2｜短剧必备人物一致性图生图_2089436784265613313.json, 图片生成/图生图/Krea2 Edit 单图编辑｜图生图局部修改 一张图随心改_2097565811954249729.json, 图片生成/图生图/Krea2一键人物三视图加动态表情，图生图角色资产快速生成工具_2103943483949150210.json, 图片生成/图生图/Krea2一键人物三视图加动态表情｜角色设定图生图高效出图_2103666719335215105.json, 图片生成/文生图/KREA-2-EDIT单图三视图模版｜图生图角色设定生成_2089431183133331457.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_238

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/397种风格内置 Krea2照片风格迁移一键转换_2104349505163448322.json、图片生成/图生图/AI漫剧制作｜参考图一键生成四视图 图生图分镜素材工作流_2097501947946430465.json、图片生成/图生图/FZ-MinimaxH3参考图生成四视图｜Krea2人物角色设计_2097107184881590273.json、图片生成/图生图/KREA-2-EDIT单图编辑V2｜短剧必备人物一致性图生图_2089436784265613313.json、图片生成/图生图/Krea2 Edit 单图编辑｜图生图局部修改 一张图随心改_2097565811954249729.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 6/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/8 个有
- `ImageResizeKJv2` —— 2/8 个有
- `ImpactInt` —— 2/8 个有
- `MuyeTextEditOutput` —— 2/8 个有
- `ResizeImageMaskNode` —— 2/8 个有
- `Textbox` —— 2/8 个有
- `CR Prompt Text` —— 1/8 个有
- `CR Text` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `GetImageSize` —— 1/8 个有
- `Image Comparer (rgthree)` —— 1/8 个有
- `ImageScaleBy` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `easy stylesSelector` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（11/8 个样本）：Steps较低可能导致细节不足
