---
name: image_to_image_lora_sampler_clip_29
type: Image To Image
frequency: 10
level: strong
coverage: 0.8947
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, TeaCache, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图片胸部变大神器 Flux Kontext一键变大胸_2015768410298261506.json, 图片生成/图生图/图片胸部增强神器 一键变丰胸放大，优化美女身材_2051213394669252609.json, 图片生成/图生图/完美丰胸一键运行_1981197400008196098.json, 图片生成/图生图/真实皮肤质感-画质增强自然光照_Kontext-DEV-LORA_1970697389088645122.json, 图片生成/图生图/真实皮肤质感-画质增强自然光照_Kontext-DEV-LORA_1986368699110223874.json, 图片生成/图生图/镜头缩放主体可见_Kontext-DEV-LORA_1948295169715109889.json, 平台全量/Kontext一键拍立得手持摄影（添加lora方案）_1948216099287498754.json, 平台全量/LORA真实皮肤质感-画质增强自然光照_2031910810020225025.json, 平台全量/人像去AI感皮肤质感光影调整_1964897682265358338.json, 平台全量/真实皮肤质感-画质增强自然光照_Kontext-DEV-LORA_1947884468544647169.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_29

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/图片胸部变大神器 Flux Kontext一键变大胸_2015768410298261506.json、图片生成/图生图/图片胸部增强神器 一键变丰胸放大，优化美女身材_2051213394669252609.json、图片生成/图生图/完美丰胸一键运行_1981197400008196098.json、图片生成/图生图/真实皮肤质感-画质增强自然光照_Kontext-DEV-LORA_1970697389088645122.json、图片生成/图生图/真实皮肤质感-画质增强自然光照_Kontext-DEV-LORA_1986368699110223874.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `TeaCache`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 9/10 个有
- `ImageStitch` —— 9/10 个有
- `PreviewImage` —— 9/10 个有
- `CR Simple Image Compare` —— 8/10 个有
- `Text Multiline` —— 7/10 个有
- `UNETLoader` —— 7/10 个有
- `ShowText|pysssss` —— 6/10 个有
- `Image Padding` —— 5/10 个有
- `Image Comparer (rgthree)` —— 3/10 个有
- `UnetLoaderGGUF` —— 3/10 个有
- `ImageConcanate` —— 2/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `Primitive string multiline [Crystools]` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 10 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
