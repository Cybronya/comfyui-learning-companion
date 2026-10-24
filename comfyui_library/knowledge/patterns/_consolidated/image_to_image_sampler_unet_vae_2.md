---
name: image_to_image_sampler_unet_vae_2
type: Image To Image
frequency: 19
level: moderate
coverage: 0.948632
common_nodes: [CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物国风风格化_2110252503370653697.json, 图片生成/图生图/人物场景多视图一键生成_2014235660437164034.json, 图片生成/图生图/人物替换2.0影视二创换人qwen2511最新图像编辑换装千问2511追赶+全能图片V1_2005243921284431874.json, 图片生成/图生图/人物电商万物换背景优化版本qwen2511_2066095762181808129.json, 图片生成/图生图/人物视角转换_2009456601119334402.json, 图片生成/图生图/人物视角转换_2065426763504775169.json, 图片生成/图生图/任意切换角度Qwen Edit 2511_2010623696456650753.json, 图片生成/图生图/全方位多视角调节图片_2077676206090182658.json, 图片生成/图生图/全量qwen edit 2512单图多角度编辑工作流_2068339692986265601.json, 图片生成/图生图/剪辑必备-去水印qwen2511_2085741599010676737.json, 图片生成/图生图/去水印qwen2511图像编辑_2085425004350631937.json, 图片生成/图生图/去水印qwen2511最新图像编辑_2046215955486871553.json, 图片生成/图生图/去水印qwen2511最新图像编辑_2077306954288029698.json, 图片生成/图生图/去水印qwen2511最新图像编辑换装千问2511追赶+全能图片V1(2)_2004758081252847618.json, 图片生成/图生图/去水印qwen2511最新图像编辑换装千问2511追赶+全能图片V1_2053656485862887425.json, 图片生成/图生图/可视化摄像机角度调节，一键生成图像多视角_2004504081580388354.json, 图片生成/图生图/图像多角度旋转 最新Qwen Image Edit 2511_2056978603925135361.json, 图片生成/图生图/图片去水印-Qwen2511-Lighting-速度快-效果好_2021029263138365441.json, 图片生成/图生图/图片去水印-Qwen2511-无角标出图_2079924667032363010.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_2

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/人物国风风格化_2110252503370653697.json、图片生成/图生图/人物场景多视图一键生成_2014235660437164034.json、图片生成/图生图/人物替换2.0影视二创换人qwen2511最新图像编辑换装千问2511追赶+全能图片V1_2005243921284431874.json、图片生成/图生图/人物电商万物换背景优化版本qwen2511_2066095762181808129.json、图片生成/图生图/人物视角转换_2009456601119334402.json…）

- **类型**：Image To Image
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
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
- `FluxKontextMultiReferenceLatentMethod` —— 18/19 个有
- `LoraLoaderModelOnly` —— 18/19 个有
- `CFGNorm` —— 17/19 个有
- `ImageScaleToTotalPixels` —— 16/19 个有
- `CR Text` —— 10/19 个有
- `ImageConcanate` —— 10/19 个有
- `QwenMultiangleCameraNode` —— 8/19 个有
- `easy promptList` —— 4/19 个有
- `CustomAddLabel` —— 2/19 个有
- `Label (rgthree)` —— 2/19 个有
- `PrimitiveInt` —— 2/19 个有
- `ShowText|pysssss` —— 2/19 个有
- `easy cleanGpuUsed` —— 2/19 个有
- `FluxKontextImageScale` —— 1/19 个有
- `Image Comparer (rgthree)` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 19 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 19 | 42% |
| 采样算法 | euler | - | 19 | 100% |
| 调度器 | simple | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，19 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，19 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 euler，19 个样本，一致性 100%
- 调度器 最常用 simple，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（19/19 个样本）：Steps较低可能导致细节不足
