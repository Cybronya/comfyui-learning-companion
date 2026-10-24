---
name: text_to_image_lora_sampler_clip_198
type: Text To Image
frequency: 9
level: strong
coverage: 0.900667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image2.1产品融图工作流｜图生图电商商品合成_2108396388856975362.json, 图片生成/图生图/Qwen-image2.1产品融图，图生图商品场景一键合成_2110481620418514946.json, 图片生成/图生图/Qwen-image2.1人像多角度生成｜图生图一套多机位素材_2104545126759620610.json, 图片生成/图生图/Qwen-image2.1角色多角度lora，图生图同一角色随心转面_2112301019328761857.json, 图片生成/图生图/万能电商商品溶图Qwen Image 2.1 产品图融合自然过渡_2108648107725643777.json, 图片生成/图生图/万能电商商品溶图Qwen Image 2.1手动版 产品图融合手动控制_2108704910568153090.json, 图片生成/图生图/万能电商商品溶图Qwen-Image-2.1｜手动版重新打光_2108453301376339970.json, 视频生成/文生视频/Qwen Image 2.1商品主体任意溶图40步质量加Viggle加速双路线工作流，图生视频_2108276276401360897.json, 视频生成/文生视频/Qwen Image2.1商品主体任意溶图｜40步质量+Viggle加速双路线_2108053287957262337.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_198

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen-image2.1产品融图工作流｜图生图电商商品合成_2108396388856975362.json、图片生成/图生图/Qwen-image2.1产品融图，图生图商品场景一键合成_2110481620418514946.json、图片生成/图生图/Qwen-image2.1人像多角度生成｜图生图一套多机位素材_2104545126759620610.json、图片生成/图生图/Qwen-image2.1角色多角度lora，图生图同一角色随心转面_2112301019328761857.json、图片生成/图生图/万能电商商品溶图Qwen Image 2.1 产品图融合自然过渡_2108648107725643777.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 8/9 个有
- `CR Prompt Text` —— 5/9 个有
- `FastCanvas` —— 5/9 个有
- `ImageScaleToTotalPixels` —— 5/9 个有
- `ImageUpscaleWithModel` —— 5/9 个有
- `KSamplerAdvanced` —— 5/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/9 个有
- `UpscaleModelLoader` —— 5/9 个有
- `FastCanvasTool` —— 4/9 个有
- `CR Text Concatenate` —— 3/9 个有
- `InspyrenetRembg` —— 3/9 个有
- `PreviewImage` —— 3/9 个有
- `FluxGuidance` —— 2/9 个有
- `Image Rembg (Remove Background)` —— 2/9 个有
- `ImageCropper` —— 2/9 个有
- `SaveImageAdvanced` —— 2/9 个有
- `TTP_Expand_And_Mask` —— 2/9 个有
- `Int` —— 1/9 个有
- `QwenMultiangleCameraNode` —— 1/9 个有
- `YYZPack_yyz_canvasnodeTool` —— 1/9 个有
- `easy promptList` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
