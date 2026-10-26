---
name: image_to_image_lora_sampler_unet_14
type: Image To Image
frequency: 22
level: strong
coverage: 0.972455
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/F.2Klein提取3d立体服装_2053799596253556738.json, 图片生成/图生图/F.2Klein提取3d立体服装_2056216125565874178.json, 图片生成/图生图/F.2Klein提取3d立体服装_2057635695820369921.json, 图片生成/图生图/F.2Klein提取3d立体服装_2058364672834891778.json, 图片生成/图生图/F.2Klein提取3d立体服装_2058380006920904706.json, 图片生成/图生图/FireRed Edit艺术字风格迁移设计_2052228410910486530.json, 图片生成/图生图/FireRed Edit艺术字风格迁移设计_2059096605923565569.json, 图片生成/图生图/FireRed Edit艺术字风格迁移设计_2059435718690304002.json, 图片生成/图生图/FireRed Edit艺术字风格迁移设计_2061660098623262721.json, 图片生成/图生图/FireRed-Image-Edit1.1单图编辑换装_2031741074665902081.json, 图片生成/图生图/FireRed-Image-edit1.1单图_双图_三图编辑_2029806395092115457.json, 图片生成/图生图/FireRed-Image-edit1.1单图_双图_三图编辑_2030064414078017537.json, 图片生成/图生图/FireRed_Edit艺术字风格迁移设计_2069077798647586817.json, 图片生成/图生图/Flux2-Klein9b一键提取3d立体服装_2038251793729200129.json, 图片生成/图生图/Flux2-Klein一键提取3d立体服装_2038862090676473857.json, 图片生成/图生图/KINWING_白底图背景替换_Qwen edit_2046550050255413249.json, 图片生成/图生图/Qwenedit 2511 一键换衣_2004388430463332354.json, 图片生成/图生图/qwen 2511重新照明重打光_2059634574510092289.json, 图片生成/图生图/qwen edit2511模糊秒变高清+真实皮肤质感_2055844453260242946.json, 图片生成/图生图/qwen edit2511模糊秒变高清+真实皮肤质感_2056203314009780225.json, 图片生成/图生图/qwen2511去除光斑 移除光影_2043657856179769346.json, 视频生成/图生视频/YZ金鱼-单人InfiniteTalk官方版工作流_2113526159744004098.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_14

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/图生图/F.2Klein提取3d立体服装_2053799596253556738.json、图片生成/图生图/F.2Klein提取3d立体服装_2056216125565874178.json、图片生成/图生图/F.2Klein提取3d立体服装_2057635695820369921.json、图片生成/图生图/F.2Klein提取3d立体服装_2058364672834891778.json、图片生成/图生图/F.2Klein提取3d立体服装_2058380006920904706.json…）

- **类型**：Image To Image
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 22 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 15/22 个有
- `TextEncodeQwenImageEditPlus` —— 15/22 个有
- `ConditioningZeroOut` —— 14/22 个有
- `Int` —— 14/22 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 14/22 个有
- `Image Comparer (rgthree)` —— 10/22 个有
- `FluxKontextImageScale` —— 8/22 个有
- `Flux2KleinEditTextEncode_EditUtils` —— 7/22 个有
- `FluxKontextMultiReferenceLatentMethod` —— 6/22 个有
- `ReferenceLatent` —— 5/22 个有
- `easy cleanGpuUsed` —— 5/22 个有
- `easy imageConcat` —— 5/22 个有
- `CR Prompt Text` —— 4/22 个有
- `EmptyLatentImage` —— 2/22 个有
- `Fast Bypasser (rgthree)` —— 1/22 个有
- `ImageConcatMulti` —— 1/22 个有
- `PreviewImage` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 22 | 41% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 22 | 100% |
| 采样算法 | euler | - | 22 | 95% |
| 调度器 | simple | - | 22 | 68% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |
| 宽度 | 1920 | - | 2 | 100% |
| 高度 | 1080 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，22 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，22 个样本，一致性 95%
- 调度器 最常用 simple，22 个样本，一致性 68%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 宽度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1080，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（25/22 个样本）：Steps较低可能导致细节不足
