---
name: unknown_workflow_sampler_clip_unet_62
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.937769
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Klein批量去除水印9B版_2012709119131652097.json, 图片生成/图生图/Flux2 Klein｜1 图像编辑（终极版V3：角色一致性，保留角色全身特征）_2052041548086427649.json, 图片生成/图生图/Flux2 klein kv高速图片编辑_2040977793638469634.json, 图片生成/图生图/Flux2+Klein9b服装提取3d+移除褶皱_2020468089401384961.json, 图片生成/图生图/Flux2-Klein-9B-人物换头_2012775113048989698.json, 图片生成/图生图/Flux2-Klein-9B-材质替换_2012772305113456641.json, 图片生成/图生图/Flux2-Klein-9B衣服迁移(偏色修正版)_2012342283487678465.json, 图片生成/图生图/Flux2-Klein-动作迁移_2012197021490356226.json, 图片生成/图生图/Flux2-Klein-衣服迁移_2012194675712593921.json, 图片生成/图生图/Flux2-Klein9b 万能提取服装_2025975423003271170.json, 图片生成/图生图/flux_特征转换iden_transfer_v3_2051150744098754562.json, 图片生成/图生图/产品图与美妆精修_2053373828482519041.json, 图片生成/图生图/任意图片转“手持自拍”_2052670657846099969.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_62

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein批量去除水印9B版_2012709119131652097.json、图片生成/图生图/Flux2 Klein｜1 图像编辑（终极版V3：角色一致性，保留角色全身特征）_2052041548086427649.json、图片生成/图生图/Flux2 klein kv高速图片编辑_2040977793638469634.json、图片生成/图生图/Flux2+Klein9b服装提取3d+移除褶皱_2020468089401384961.json、图片生成/图生图/Flux2-Klein-9B-人物换头_2012775113048989698.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 12/13 个有
- `Image Comparer (rgthree)` —— 9/13 个有
- `FluxKontextImageScale` —— 7/13 个有
- `ImageScaleToTotalPixels` —— 6/13 个有
- `LoraLoaderModelOnly` —— 4/13 个有
- `PreviewImage` —— 4/13 个有
- `YC Color Match` —— 3/13 个有
- `IdentityFeatureTransferV3` —— 2/13 个有
- `FluxKVCache` —— 1/13 个有
- `HAIGC_LoadImagesFromZip` —— 1/13 个有
- `HAIGC_SaveImagesToZip` —— 1/13 个有
- `ImageConcatenate_UTK` —— 1/13 个有
- `ImageFromBatch+` —— 1/13 个有
- `ImageListToBatch+` —— 1/13 个有
- `OpenposePreprocessor` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
