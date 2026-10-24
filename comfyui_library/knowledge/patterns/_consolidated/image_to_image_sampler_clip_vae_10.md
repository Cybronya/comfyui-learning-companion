---
name: image_to_image_sampler_clip_vae_10
type: Image To Image
frequency: 15
level: strong
coverage: 0.910467
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImageConcanate, ImageStitch, KSampler, LoadImage, LoadImageOutput, PreviewImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Kontext最强图像扩图_1948035581176623106.json, 图片生成/图生图/Flux Kontext电影质感（黑客帝国-胶片颗粒，青绿色，低饱和）加速版v1_1943612914513158145.json, 图片生成/图生图/Flux Kontext绝对角度万物正视图加速版v1_1946434790629498882.json, 图片生成/图生图/Flux Kontext胖妹妹福音变苗条v1_1945370923623174145.json, 图片生成/图生图/Flux Kontext衣服提取商品白底图加速版v1（换装前置）_1946477302638080001.json, 图片生成/图生图/Flux Kontext长曝光风格加速版v1_1946471702076223490.json, 图片生成/图生图/Flux Kontext高分辨率修复Highres加速版v1_1944790783922720769.json, 图片生成/图生图/Flux Kontext高品质优化风加速版V1_1946972757789290498.json, 图片生成/图生图/Flux Kontext黏土动画风格加速版v1_1948655673111392257.json, 图片生成/图生图/Kontext  动漫3D PVC 玩偶_1947866211100045314.json, 图片生成/图生图/Kontext  动漫铅笔线稿生成_1947864523493490690.json, 图片生成/图生图/Kontext + 打光 LoRA｜高质量打光工作流_1942579813515505666.json, 图片生成/图生图/Kontext Dev 昭和动漫风_1942582074488631297.json, 图片生成/图生图/Kontext 电影质感_1943908526999867394.json, 图片生成/图生图/人物换装迁移（kontext＋ IC Custom）_1963645388178935810.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_10

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/Flux Kontext最强图像扩图_1948035581176623106.json、图片生成/图生图/Flux Kontext电影质感（黑客帝国-胶片颗粒，青绿色，低饱和）加速版v1_1943612914513158145.json、图片生成/图生图/Flux Kontext绝对角度万物正视图加速版v1_1946434790629498882.json、图片生成/图生图/Flux Kontext胖妹妹福音变苗条v1_1945370923623174145.json、图片生成/图生图/Flux Kontext衣服提取商品白底图加速版v1（换装前置）_1946477302638080001.json…）

- **类型**：Image To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageConcanate`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `LoadImageOutput`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 14/15 个有
- `GoogleTranslateTextNode` —— 14/15 个有
- `LoraLoaderModelOnly` —— 13/15 个有
- `UnetLoaderGGUF` —— 13/15 个有
- `PDIMAGE_LongerSize` —— 10/15 个有
- `TeaCache` —— 9/15 个有
- `MagCache` —— 3/15 个有
- `NunchakuFluxDiTLoader` —— 3/15 个有
- `NunchakuFluxLoraLoader` —— 3/15 个有
- `EmptySD3LatentImage` —— 2/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/15 个有
- `GetImageSize+` —— 1/15 个有
- `ImagePadKJ` —— 1/15 个有
- `JWImageResize` —— 1/15 个有
- `LayerUtility: PurgeVRAM` —— 1/15 个有
- `RH_Translator` —— 1/15 个有
- `RunningHub ICCustom Loader` —— 1/15 个有
- `RunningHub ICCustom Sampler` —— 1/15 个有
- `SimpleMath+` —— 1/15 个有
- `easy imageRemBg` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 15 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | simple | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 simple，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
