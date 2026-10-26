---
name: image_to_image_lora_sampler_unet_27
type: Image To Image
frequency: 16
level: weak
coverage: 0.954
common_nodes: [CLIPLoader, EmptySD3LatentImage, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/KREA2单图编辑_2080462222530269186.json, 图片生成/图生图/KREA2单图编辑_2081928738899582977.json, 图片生成/图生图/KREA2单图编辑_2081978225579876353.json, 图片生成/图生图/KREA2单图编辑_2082041955021840385.json, 图片生成/图生图/KREA2单图编辑_2088660756677087234.json, 图片生成/图生图/KREA2单图编辑_2091742157894934530.json, 图片生成/图生图/Krea 2 Edit v1.2 多图编辑_2080148248815296513.json, 图片生成/图生图/Krea 2 Identity Edit V1.2单图像编辑_2079587821911887874.json, 图片生成/图生图/Krea 2 Identity Edit V1.2单图像编辑_2080549019234947073.json, 图片生成/图生图/Krea 2 Identity Edit V1.2双图换脸_2080552275218620418.json, 图片生成/图生图/Krea 2 Identity Edit V1.2双图换脸（贞贞版）_2080235403289907202.json, 图片生成/图生图/Krea 2 Identity Edit 单图像编辑_2075066679314436098.json, 图片生成/图生图/Krea 2 Identity Edit双图像参考编辑_2075068977293905921.json, 图片生成/图生图/Krea2 双图换脸 Identity-Edit_2080622882840997889.json, 图片生成/图生图/Krea2 双图换脸或全身替换 Identity-Edit_2081906852874506242.json, 图片生成/图生图/krea2_edit_2参考图编辑_2077198129690140673.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_27

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/KREA2单图编辑_2080462222530269186.json、图片生成/图生图/KREA2单图编辑_2081928738899582977.json、图片生成/图生图/KREA2单图编辑_2081978225579876353.json、图片生成/图生图/KREA2单图编辑_2082041955021840385.json、图片生成/图生图/KREA2单图编辑_2088660756677087234.json…）

- **类型**：Image To Image
- **样本数**：16
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `EmptySD3LatentImage`
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

**可变部分**（部分 workflow 才有）：
- `TextInput_` —— 14/16 个有
- `Float` —— 12/16 个有
- `ResizeImageMaskNode` —— 10/16 个有
- `ResolutionSelector` —— 9/16 个有
- `GetImageSize` —— 8/16 个有
- `ImageConcanate` —— 6/16 个有
- `Label (rgthree)` —— 2/16 个有
- `PreviewImage` —— 2/16 个有
- `RMBG` —— 2/16 个有
- `easy imageConcat` —— 2/16 个有
- `ImageResizeKJv2` —— 1/16 个有
- `ImageScaleBy` —— 1/16 个有
- `RH_Translator` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 40 | 16 | 26% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 16 | 47% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 40，16 个样本，取值分散，一致性仅 26%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，16 个样本，取值分散，一致性仅 47%
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
