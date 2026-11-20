---
name: image_to_image_sampler_clip_vae_19
type: Image To Image
frequency: 12
level: strong
coverage: 0.926917
common_nodes: [CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImageStitch, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/红潮版弱审查Flux Kontext Dev图像编辑V1（换装前置）_1939170724722434050.json, 图片生成/图生图/（Flux Kontext Dev Change to nothing V1（换装前置）_1940801587570962434.json, 图片生成/图生图/（自用）Flux Kontext Dev 19500步V1（换装前置）_1943283028309254145.json, 图片生成/图生图/（自用）Flux Kontext Dev JD3强化版V1（可变姿势）（换装前置）_1940454348533166081.json, 图片生成/图生图/（自用）Flux Kontext Dev Unlock V1（换装前置）_1940800414864535554.json, 图片生成/图生图/（自用）Flux Kontext Dev V1（Nunchaku） （换装前置）_1940337496180064258.json, 图片生成/图生图/（自用）Flux Kontext Dev万物进食V1（学习版）_1943557653316444162.json, 图片生成/图生图/（自用）Flux Kontext Dev动漫V1（换装前置）_1942754180102557698.json, 图片生成/图生图/（自用）Flux Kontext Dev胸肌调整V1（Nunchaku）_1939731118046547970.json, 图片生成/文生图/Flux+Kontext+快速出图（Nunchaku）基础工作流_1968134912584876033.json, 平台全量/Flux Kontext Dev真人转动漫Limbus风格_1945286636521365506.json, 视频生成/图生视频/Flux Kontext Dev极简主义风格加速版v1_1941888370622754818.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_19

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/红潮版弱审查Flux Kontext Dev图像编辑V1（换装前置）_1939170724722434050.json、图片生成/图生图/（Flux Kontext Dev Change to nothing V1（换装前置）_1940801587570962434.json、图片生成/图生图/（自用）Flux Kontext Dev 19500步V1（换装前置）_1943283028309254145.json、图片生成/图生图/（自用）Flux Kontext Dev JD3强化版V1（可变姿势）（换装前置）_1940454348533166081.json、图片生成/图生图/（自用）Flux Kontext Dev Unlock V1（换装前置）_1940800414864535554.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImageOutput` —— 11/12 个有
- `LoraLoaderModelOnly` —— 11/12 个有
- `EmptySD3LatentImage` —— 10/12 个有
- `GoogleTranslateTextNode` —— 10/12 个有
- `LoadLatent` —— 9/12 个有
- `MagCache` —— 9/12 个有
- `SaveLatent` —— 9/12 个有
- `UnetLoaderGGUF` —— 8/12 个有
- `PreviewImage` —— 7/12 个有
- `NunchakuFluxDiTLoader` —— 6/12 个有
- `NunchakuFluxLoraLoader` —— 5/12 个有
- `ImageConcanate` —— 3/12 个有
- `easy showAnything` —— 3/12 个有
- `UNETLoader` —— 2/12 个有
- `GoogleTranslator` —— 1/12 个有
- `ImageScaleToTotalPixels` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 15 - 20 | 12 | 93% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 15 - 20，12 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
