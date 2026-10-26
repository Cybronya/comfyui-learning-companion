---
name: image_to_image_sampler_clip_vae_12
type: Image To Image
frequency: 18
level: strong
coverage: 0.909722
common_nodes: [CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImageConcanate, ImageStitch, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Kontext平面_人台服装生成电商模特图V1（Lora加强版）_1939312985770999809.json, 图片生成/图生图/Flux Kontext电商模特图_1939937418273267714.json, 图片生成/图生图/Flux Kontext电影质感（黑客帝国-胶片颗粒，青绿色，低饱和）加速版v1_1943612914513158145.json, 图片生成/图生图/Flux Kontext绝对角度万物正视图加速版v1_1946434790629498882.json, 图片生成/图生图/Flux Kontext胖妹妹福音变苗条v1_1945370923623174145.json, 图片生成/图生图/Flux Kontext衣服提取商品白底图加速版v1（换装前置）_1946477302638080001.json, 图片生成/图生图/Flux Kontext长曝光风格加速版v1_1946471702076223490.json, 图片生成/图生图/Flux Kontext高分辨率修复Highres加速版v1_1944790783922720769.json, 图片生成/图生图/Flux Kontext高品质优化风加速版V1_1946972757789290498.json, 图片生成/图生图/Flux Kontext黏土动画风格加速版v1_1948655673111392257.json, 图片生成/图生图/Flux+Kontext-高清还原（Nunchaku）_1968246375500664834.json, 图片生成/图生图/Kontext  动漫3D PVC 玩偶_1947866211100045314.json, 图片生成/图生图/Kontext  动漫铅笔线稿生成_1947864523493490690.json, 图片生成/图生图/Kontext + 打光 LoRA｜高质量打光工作流_1942579813515505666.json, 图片生成/图生图/Kontext Dev 昭和动漫风_1942582074488631297.json, 图片生成/图生图/Kontext 电影质感_1943908526999867394.json, 图片生成/图生图/Kontext-万能转换工作流_1949413979264843777.json, 图片生成/图生图/去人取衣生成服装产品3D白底图_1941798227840757762.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_12

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/Flux Kontext平面_人台服装生成电商模特图V1（Lora加强版）_1939312985770999809.json、图片生成/图生图/Flux Kontext电商模特图_1939937418273267714.json、图片生成/图生图/Flux Kontext电影质感（黑客帝国-胶片颗粒，青绿色，低饱和）加速版v1_1943612914513158145.json、图片生成/图生图/Flux Kontext绝对角度万物正视图加速版v1_1946434790629498882.json、图片生成/图生图/Flux Kontext胖妹妹福音变苗条v1_1945370923623174145.json…）

- **类型**：Image To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageConcanate`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GoogleTranslateTextNode` —— 16/18 个有
- `LoadImageOutput` —— 15/18 个有
- `LoraLoaderModelOnly` —— 13/18 个有
- `UnetLoaderGGUF` —— 13/18 个有
- `PDIMAGE_LongerSize` —— 10/18 个有
- `TeaCache` —— 8/18 个有
- `NunchakuFluxDiTLoader` —— 5/18 个有
- `NunchakuFluxLoraLoader` —— 5/18 个有
- `MagCache` —— 4/18 个有
- `UNETLoader` —— 4/18 个有
- `EmptySD3LatentImage` —— 3/18 个有
- `PMRF` —— 3/18 个有
- `RHHiddenNodes` —— 2/18 个有
- `Fast Groups Bypasser (rgthree)` —— 1/18 个有
- `ImageConcatMulti` —— 1/18 个有
- `JWImageResize` —— 1/18 个有
- `SUPIR_Upscale` —— 1/18 个有
- `ShowText` —— 1/18 个有
- `ShowText|pysssss` —— 1/18 个有
- `Text Multiline` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 18 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | simple | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 simple，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
