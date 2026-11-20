---
name: image_to_image_lora_sampler_clip_51
type: Image To Image
frequency: 6
level: strong
coverage: 0.920333
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/服装衣物生成3D镂空图_1980917939945783297.json, 图片生成/图生图/电商产品溶图_2026942543119785985.json, 图片生成/图生图/真实皮肤质感-画质增强自然光照_Kontext-DEV-LORA_1970697389088645122.json, 图片生成/图生图/真实皮肤质感-画质增强自然光照_Kontext-DEV-LORA_1986368699110223874.json, 图片生成/图生图/美漫手绘故事_Kontext-LORA_1955150925189058561.json, 图片生成/图生图/镜头缩放主体可见_Kontext-DEV-LORA_1948295169715109889.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_51

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/服装衣物生成3D镂空图_1980917939945783297.json、图片生成/图生图/电商产品溶图_2026942543119785985.json、图片生成/图生图/真实皮肤质感-画质增强自然光照_Kontext-DEV-LORA_1970697389088645122.json、图片生成/图生图/真实皮肤质感-画质增强自然光照_Kontext-DEV-LORA_1986368699110223874.json、图片生成/图生图/美漫手绘故事_Kontext-LORA_1955150925189058561.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
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
- `ConditioningZeroOut` —— 5/6 个有
- `ShowText|pysssss` —— 5/6 个有
- `Text Multiline` —— 5/6 个有
- `ImageStitch` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `CR Simple Image Compare` —— 3/6 个有
- `TeaCache` —— 3/6 个有
- `Image Padding` —— 2/6 个有
- `EmptySD3LatentImage` —— 1/6 个有
- `GetImageSizeAndCount` —— 1/6 个有
- `ImageUpscaleWithModelBatched` —— 1/6 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/6 个有
- `LayerUtility: ImageAutoCrop V2` —— 1/6 个有
- `RH_Translator` —— 1/6 个有
- `UpscaleModelLoader` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 6 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，6 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
