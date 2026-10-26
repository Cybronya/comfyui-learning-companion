---
name: text_to_image_lora_sampler_clip_100
type: Text To Image
frequency: 13
level: strong
coverage: 0.883154
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, EmptySD3LatentImage, JjkText, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2单图双图局部重绘图像编辑工作流，图生图精准区域处理工具_2106100322811863041.json, 图片生成/图生图/Krea2四视图角色设定表-图生图工作流zip版_2087343455298211842.json, 图片生成/图生图/Krea2四视图资产库生成 人物角色图生图处理工具_2114098850569998338.json, 图片生成/图生图/Krea2图生图四视图角色资产库｜简易版4视图 图生图建角色档案_2104081597220868098.json, 图片生成/图生图/Krea2改图扩图多合一工作流｜局部重绘图生图处理_2097526511334154241.json, 图片生成/图生图/Krea2改图扩图多合一｜局部重绘图生图处理_2092369295241207810.json, 图片生成/图生图/Krea2资产库角色四视图 动漫角色分镜生成出图工具_2098707532436041730.json, 图片生成/图生图/Krea2资产库角色四视图 角色一致性图生图处理工具_2114097366662991874.json, 图片生成/图生图/Krea2资产库角色四视图 角色设计图生图处理工具_2113391188228268034.json, 图片生成/图生图/Krea2资产库角色四视图｜一致性角色设定图生图_2094940042543325186.json, 图片生成/图生图/Krea2资产库角色四视图｜角色一致性人物图生图_2114062123566452738.json, 图片生成/图生图/Krea2资产库角色四视图｜角色设计图生图生成_2092355126718722050.json, 图片生成/文生图/Krea2局部重绘移除｜精准无缝融合文生图图生图_2090464406776926210.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_100

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Krea2单图双图局部重绘图像编辑工作流，图生图精准区域处理工具_2106100322811863041.json、图片生成/图生图/Krea2四视图角色设定表-图生图工作流zip版_2087343455298211842.json、图片生成/图生图/Krea2四视图资产库生成 人物角色图生图处理工具_2114098850569998338.json、图片生成/图生图/Krea2图生图四视图角色资产库｜简易版4视图 图生图建角色档案_2104081597220868098.json、图片生成/图生图/Krea2改图扩图多合一工作流｜局部重绘图生图处理_2097526511334154241.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
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
- `PreviewImage` —— 11/13 个有
- `AddLabel` —— 9/13 个有
- `GetImageSize` —— 9/13 个有
- `ImageConcatMulti` —— 9/13 个有
- `ImageResizeKJv2` —— 9/13 个有
- `DrawMaskOnImage` —— 4/13 个有
- `GetImageSize+` —— 4/13 个有
- `ImageScaleToTotalPixels` —— 4/13 个有
- `PrimitiveStringMultiline` —— 4/13 个有
- `Seed (rgthree)` —— 4/13 个有
- `AnyBooleanSwitch` —— 2/13 个有
- `ImagePadForOutpaint` —— 2/13 个有
- `ImpactConditionalBranch` —— 2/13 个有
- `PrimitiveFloat` —— 2/13 个有
- `easy boolean` —— 2/13 个有
- `Fast Groups Bypasser (rgthree)` —— 1/13 个有
- `HAIGC_SaveImagesToZip` —— 1/13 个有
- `ResolutionSelector` —— 1/13 个有

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
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
