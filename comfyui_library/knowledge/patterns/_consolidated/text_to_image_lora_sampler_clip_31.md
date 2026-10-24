---
name: text_to_image_lora_sampler_clip_31
type: Text To Image
frequency: 22
level: strong
coverage: 0.902
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetNode, ImageScaleToTotalPixels, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SetNode, TTResolutionSelector, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy anythingIndexSwitch, easy int]
problems: []
missing: []
members: [图片生成/文生图/Krea2+Klein双采-国漫-一斩苍穹-凌清寒-第一套【syqiangk】_2086814976962031617.json, 图片生成/文生图/Krea2+Klein双采-国漫-一斩苍穹-寒鸦-第一套【syqiangk】_2085913545149079553.json, 图片生成/文生图/Krea2+Klein双采-国漫-光阴之外-灵儿-第一套【syqiangk】_2077043620032630785.json, 图片生成/文生图/Krea2+Klein双采-国漫-光阴之外-苏见秋-第一套【syqiangk】_2082478834116554754.json, 图片生成/文生图/Krea2+Klein双采-国漫-凡人修仙传-南宫婉-新建模-第一套【syqiangk】_2075978633625300994.json, 图片生成/文生图/Krea2+Klein双采-国漫-凡人修仙传-南宫阙-第一套【syqiangk】_2078147529719504897.json, 图片生成/文生图/Krea2+Klein双采-国漫-吞噬星空-星幻王-第一套【syqiangk】_2041908781411471361.json, 图片生成/文生图/Krea2+Klein双采-国漫-吞噬星空-溟莲之主-第一套【syqiangk】_2080260967069478914.json, 图片生成/文生图/Krea2+Klein双采-国漫-大主宰-清衍静-第一套【syqiangk】_2074899453416394754.json, 图片生成/文生图/Krea2+Klein双采-国漫-大主宰-灵溪-第一套【syqiangk】_2079577200193523713.json, 图片生成/文生图/Krea2+Klein双采-国漫-师兄啊师兄-云霄-黑化版【syqiangk】_2085398499084038145.json, 图片生成/文生图/Krea2+Klein双采-国漫-择日飞升-青壁-第一套【syqiangk】_2086873516091203586.json, 图片生成/文生图/Krea2+Klein双采-国漫-斗破苍穹-药灵-第一套【syqiangk】_2082101399822888961.json, 图片生成/文生图/Krea2+Klein双采-国漫-枯骨成仙-苏千荷-第一套【syqiangk】_2084295242433519617.json, 图片生成/文生图/Krea2+Klein双采-国漫-枯骨成仙-苏梦瑶-第一套【syqiangk】_2081412397172084737.json, 图片生成/文生图/Krea2+Klein双采-国漫-沧元图-长乐(大越皇后)-第一套【syqiangk】_2076711849927729154.json, 图片生成/文生图/Krea2+Klein双采-国漫-沧元图-长乐(大越皇后)-第二套【syqiangk】_2080276212844421121.json, 图片生成/文生图/Krea2+Klein双采-国漫-深空彼岸-燕清妍-第一套【syqiangk】_2085035661463220225.json, 图片生成/文生图/Krea2+Klein双采-国漫-逆天邪神-楚月婵-年番第一套【syqiangk】_2083403282608910338.json, 图片生成/文生图/Krea2+Klein双采-国漫-逆天邪神-苍月公主-年番第二套【syqiangk】_2083178016846467074.json, 图片生成/文生图/Krea2+Klein双采-游戏-永劫无间-甘璇-第一套【syqiangk】_2075979084965957634.json, 图片生成/文生图/Krea2+Klein双采-韩漫-美丽新世界-金美庭-第一套【syqiangk】_2083572001037443074.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_31

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/文生图/Krea2+Klein双采-国漫-一斩苍穹-凌清寒-第一套【syqiangk】_2086814976962031617.json、图片生成/文生图/Krea2+Klein双采-国漫-一斩苍穹-寒鸦-第一套【syqiangk】_2085913545149079553.json、图片生成/文生图/Krea2+Klein双采-国漫-光阴之外-灵儿-第一套【syqiangk】_2077043620032630785.json、图片生成/文生图/Krea2+Klein双采-国漫-光阴之外-苏见秋-第一套【syqiangk】_2082478834116554754.json、图片生成/文生图/Krea2+Klein双采-国漫-凡人修仙传-南宫婉-新建模-第一套【syqiangk】_2075978633625300994.json…）

- **类型**：Text To Image
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 22 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetNode`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy int`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | 16 - 16 | 22 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 22 | 100% |
| 采样算法 | euler_ancestral | - | 22 | 100% |
| 调度器 | simple | - | 22 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |
| 宽度 | 512 | 512 - 512 | 22 | 100% |
| 高度 | 512 | 512 - 512 | 22 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 16，观测区间 16 - 16，22 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，22 个样本，一致性 100%
- 调度器 最常用 simple，22 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，22 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，22 个样本，取值集中（一致性 100%）
