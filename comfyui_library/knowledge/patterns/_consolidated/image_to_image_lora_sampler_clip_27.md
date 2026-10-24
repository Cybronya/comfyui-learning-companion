---
name: image_to_image_lora_sampler_clip_27
type: Image To Image
frequency: 9
level: strong
coverage: 0.886889
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/小红书爆款3D emoji小人_1956325155729539073.json, 图片生成/图生图/新-kontext商业级印花提取工作流V2版本_1956004419567583233.json, 图片生成/图生图/新Kontext-青铜雕塑风格转绘+TEACACHE加速_1946480965322436610.json, 图片生成/图生图/最强素颜化妆上妆flux_kontext_dev_1963264724798517250.json, 图片生成/图生图/真人转动漫flux_kontext_dev_1964320638330617857.json, 图片生成/图生图/空白工作流_1977925668166062081.json, 图片生成/图生图/线稿上色｜自选风格_1948299809867345921.json, 图片生成/文生图/Kontext-LORA效果测试工作流_1942450419496857602.json, 图片生成/文生图/喜剧复古动漫风格2.0_1942402202403024898.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_27

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/小红书爆款3D emoji小人_1956325155729539073.json、图片生成/图生图/新-kontext商业级印花提取工作流V2版本_1956004419567583233.json、图片生成/图生图/新Kontext-青铜雕塑风格转绘+TEACACHE加速_1946480965322436610.json、图片生成/图生图/最强素颜化妆上妆flux_kontext_dev_1963264724798517250.json、图片生成/图生图/真人转动漫flux_kontext_dev_1964320638330617857.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 7/9 个有
- `ImageStitch` —— 6/9 个有
- `Image Comparer (rgthree)` —— 5/9 个有
- `CR Text` —— 3/9 个有
- `CR Text Replace` —— 2/9 个有
- `EmptySD3LatentImage` —— 2/9 个有
- `LoadImageOutput` —— 2/9 个有
- `RH_Captioner` —— 2/9 个有
- `CR Simple Image Compare` —— 1/9 个有
- `Display Any (rgthree)` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `ShowText` —— 1/9 个有
- `TeaCache` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 9 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，9 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
