---
name: image_to_image_sampler_clip_vae_22
type: Image To Image
frequency: 9
level: strong
coverage: 0.918333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext单姿势图直接出图_1944080635831128065.json, 图片生成/图生图/Kontext去水印史上最强去除水印——水印移除King（watermark killer）_1941296156943216642.json, 图片生成/图生图/Kontext图像编辑工作流_1986390332885630978.json, 图片生成/图生图/Kontext老照片修复上色（高度还原，一键成片）极速版_2034265635953315841.json, 图片生成/图生图/kontext一句话编辑_2009592730074222594.json, 图片生成/图生图/kontext老照片修复工作流_2079953891206189058.json, 图片生成/图生图/一致性dev版本_1945764160510554113.json, 图片生成/图生图/万物一键转换——亚克力立架_1946941574536421378.json, 图片生成/图生图/万物一键转换——绒毛玩偶_1946954844869681154.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_22

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Kontext单姿势图直接出图_1944080635831128065.json、图片生成/图生图/Kontext去水印史上最强去除水印——水印移除King（watermark killer）_1941296156943216642.json、图片生成/图生图/Kontext图像编辑工作流_1986390332885630978.json、图片生成/图生图/Kontext老照片修复上色（高度还原，一键成片）极速版_2034265635953315841.json、图片生成/图生图/kontext一句话编辑_2009592730074222594.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 9 个 workflow 都包含：
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
- `FluxKontextImageScale` —— 8/9 个有
- `UNETLoader` —— 7/9 个有
- `Image Comparer (rgthree)` —— 6/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `RepeatLatentBatch` —— 4/9 个有
- `DeepTranslatorTextNode` —— 3/9 个有
- `NunchakuFluxDiTLoader` —— 3/9 个有
- `PreviewImage` —— 3/9 个有
- `easy imageRemBg` —— 3/9 个有
- `Fast Bypasser (rgthree)` —— 2/9 个有
- `ImpactInt` —— 2/9 个有
- `easy imageScaleDownToSize` —— 2/9 个有
- `AIO_Preprocessor` —— 1/9 个有
- `ImpactSwitch` —— 1/9 个有
- `NunchakuFluxLoraLoader` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 9 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，9 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
