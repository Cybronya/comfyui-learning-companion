---
name: image_to_image_sampler_unet_vae_5
type: Image To Image
frequency: 26
level: moderate
coverage: 0.915423
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen+Edit+2511三图编辑_2074110282011598849.json, 图片生成/图生图/Qwen-Edit-2509-白底图转模特展示_1989690060327014401.json, 图片生成/图生图/Qwen-Edit-2509图像编辑_1981990949586903042.json, 图片生成/图生图/Qwen-Edit-2511 人物姿势模仿工作流_2091518524282990593.json, 图片生成/图生图/Qwen-Edit-2511版单图&多图融合迁移工作流2.0_2028760934268801026.json, 图片生成/图生图/Qwen-Image-2511-AnyPose用参考图实现姿势控制_2006282960210763777.json, 图片生成/图生图/Qwen-edit万能一键去水印_2077302903462785026.json, 图片生成/图生图/Qwen2511+模特姿势复刻_2003731932687048705.json, 图片生成/图生图/人物换装+换背景V2_2004104139988738050.json, 图片生成/图生图/千问Qwen+Image+Edit+2511-三图多图编辑（加速版）_2005619327858606082.json, 图片生成/图生图/可单图可多图编辑命令Qwen Image Edit-2511_2031274430206316546.json, 图片生成/图生图/换背景Qwen+Image+Edit+2511-支持单图多图编辑加速版_2007308029473071105.json, 图片生成/图生图/换装千问Qwen2511最新图像编辑换装工作流_2084112989686427649.json, 图片生成/图生图/换装千问Qwen2511最新图像编辑换装工作流_2084124102578753538.json, 图片生成/图生图/换装千问qwen2511最新图像编辑_2008133174475366401.json, 图片生成/图生图/换装千问qwen2511最新图像编辑换装千问2511_2003636475113684993.json, 图片生成/图生图/换装千问qwen2511最新图像编辑换装千问2511_2100047371999735810.json, 图片生成/图生图/换装千问qwen2511最新图像编辑换装千问2511_2100125361475506178.json, 图片生成/图生图/支持单图多图编辑融合-邻家AI大女孩_2045067988478464001.json, 图片生成/图生图/老孙AI 一键去水印qwen2511_2086304124907380737.json, 图片生成/图生图/风格转换qwen2511最新图像编辑换装千问2511追赶nano+全能图片V1(1)_2004060386825519105.json, 图片生成/文生图/测试v2_2028368389479075842.json, 平台全量/Qwen Image Edit 2511 图像编辑单图多图高清换装换背景融合洗图_2004217896568057858.json, 平台全量/最新 千问 Qwen Image Edit 2511  单图多图编辑_2003694860962021378.json, 平台全量/🦄Qwen简易姿势参考流 🎯天下无腰_2036409609656737793.json, 数字人/数字人/Qwen Image Edit 2511-多图编辑_2061638633966358529.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_5

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（图片生成/图生图/Qwen+Edit+2511三图编辑_2074110282011598849.json、图片生成/图生图/Qwen-Edit-2509-白底图转模特展示_1989690060327014401.json、图片生成/图生图/Qwen-Edit-2509图像编辑_1981990949586903042.json、图片生成/图生图/Qwen-Edit-2511 人物姿势模仿工作流_2091518524282990593.json、图片生成/图生图/Qwen-Edit-2511版单图&多图融合迁移工作流2.0_2028760934268801026.json…）

- **类型**：Image To Image
- **样本数**：26
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 26 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 25/26 个有
- `FluxKontextMultiReferenceLatentMethod` —— 21/26 个有
- `ImageConcanate` —— 19/26 个有
- `CR Text` —— 14/26 个有
- `Image Comparer (rgthree)` —— 14/26 个有
- `EmptySD3LatentImage` —— 11/26 个有
- `ImageConcatMulti` —— 11/26 个有
- `PreviewImage` —— 3/26 个有
- `DWPreprocessor` —— 2/26 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/26 个有
- `easy imageSize` —— 2/26 个有
- `AIO_Preprocessor` —— 1/26 个有
- `Anything Everywhere` —— 1/26 个有
- `ConditioningZeroOut` —— 1/26 个有
- `Int` —— 1/26 个有
- `ReferenceLatent` —— 1/26 个有
- `UnetLoaderGGUF` —— 1/26 个有
- `easy cleanGpuUsed` —— 1/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 26 | 36% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 26 | 73% |
| 采样算法 | euler | - | 26 | 96% |
| 调度器 | simple | - | 26 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 26 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 33/26 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，26 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，26 个样本
- 采样算法 最常用 euler，26 个样本，一致性 96%
- 调度器 最常用 simple，26 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，26 个样本，取值集中（一致性 100%）
- 高发问题（33/26 个样本）：Steps较低可能导致细节不足
