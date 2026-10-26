---
name: image_to_image_lora_sampler_unet_29
type: Image To Image
frequency: 15
level: strong
coverage: 0.923133
common_nodes: [CLIPLoader, EmptySD3LatentImage, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/krea2_编辑_2082011860395712513.json, 图片生成/图生图/krea2_角色三视图生成_2090342017615351809.json, 图片生成/图生图/krea2单图编辑单图洗图换图片元素改图改元素洗图神器_2089670581288525826.json, 图片生成/图生图/krea2换装编辑工作流换衣服模特换装人物换衣换装图片工作流_2089668090056499201.json, 图片生成/图生图/krea2身份保持换装_2080169764953088001.json, 图片生成/图生图/krea2，四视图_2095382343082135554.json, 图片生成/图生图/opsv-krea2-2refs_2080246504194928641.json, 图片生成/图生图/pipi-krea2单图编辑工作流_2081650003457691649.json, 图片生成/图生图/pipi-krea2换装编辑工作流_2081382750556348418.json, 图片生成/图生图/▶▷MiniMaxH3辅助四视图生成流-k2_2090275044734889985.json, 图片生成/图生图/▶▷MiniMaxH3辅助四视图生成流-k2_2091066864536481794.json, 图片生成/图生图/一张图辅助四视图生成流_2093273969200816130.json, 图片生成/图生图/四视图_2093977191204872193.json, 图片生成/文生图/Krea2-双图编辑_完美替换_2089961180281532417.json, 图片生成/文生图/Krea2-局部重绘_移除_2089978434125647873.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_29

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/krea2_编辑_2082011860395712513.json、图片生成/图生图/krea2_角色三视图生成_2090342017615351809.json、图片生成/图生图/krea2单图编辑单图洗图换图片元素改图改元素洗图神器_2089670581288525826.json、图片生成/图生图/krea2换装编辑工作流换衣服模特换装人物换衣换装图片工作流_2089668090056499201.json、图片生成/图生图/krea2身份保持换装_2080169764953088001.json…）

- **类型**：Image To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 15 个 workflow 都包含：
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
- `ImageResizeKJv2` —— 12/15 个有
- `Label (rgthree)` —— 7/15 个有
- `PreviewImage` —— 6/15 个有
- `ResolutionSelector` —— 4/15 个有
- `String Literal` —— 4/15 个有
- `Seed (rgthree)` —— 3/15 个有
- `ImageScaleToTotalPixels` —— 2/15 个有
- `PrimitiveStringMultiline` —— 2/15 个有
- `CR Prompt Text` —— 1/15 个有
- `DrawMaskOnImage` —— 1/15 个有
- `GetImageSize+` —— 1/15 个有
- `JjkText` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 12 | 15 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.2 | 15 | 95% |
| 采样算法 | euler | - | 15 | 93% |
| 调度器 | simple | - | 15 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 12，15 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.2，15 个样本，取值集中（一致性 95%）
- 采样算法 最常用 euler，15 个样本，一致性 93%
- 调度器 最常用 simple，15 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
