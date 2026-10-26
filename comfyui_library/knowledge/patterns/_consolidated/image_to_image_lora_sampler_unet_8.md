---
name: image_to_image_lora_sampler_unet_8
type: Image To Image
frequency: 29
level: moderate
coverage: 0.971172
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2511-儿童涂鸦风格转绘-小宣喧-RH_2007047125556797442.json, 图片生成/图生图/Qwen2511-阿凡达风格-小宣喧-RH_2008411628018081793.json, 图片生成/图生图/QwenEdit2511-Q版角色-小宣喧-RH_2006747284024860673.json, 图片生成/图生图/RH-PSAPI插件用-_图生图edit2511_2068683270535081985.json, 图片生成/图生图/qwen Edit 2511 单图编辑_2051921199571193858.json, 图片生成/图生图/qwen2511一键换衣千问图像编辑换装_2060331107287134210.json, 图片生成/图生图/qwen_image_edit_2511_2004461710926901250.json, 图片生成/图生图/一键完美图片去水印TextEncode QwenlmageEdit2511_1988876685514772482.json, 图片生成/图生图/一键换衣千问qwen2511最新图像编辑换装千问2511_2034603108478754818.json, 图片生成/图生图/一键换装工作流，无需遮罩_2096447517775978497.json, 图片生成/图生图/人物替换2.0影视二创换人qwen2511最新图像编辑换装千问2511追赶+全能图片V1_2005243921284431874.json, 图片生成/图生图/人物电商万物换背景优化版本qwen2511_2066095762181808129.json, 图片生成/图生图/剪辑必备-去水印qwen2511_2085741599010676737.json, 图片生成/图生图/去水印qwen2511图像编辑_2085425004350631937.json, 图片生成/图生图/去水印qwen2511最新图像编辑_2046215955486871553.json, 图片生成/图生图/去水印qwen2511最新图像编辑_2077306954288029698.json, 图片生成/图生图/去水印qwen2511最新图像编辑换装千问2511追赶+全能图片V1(2)_2004758081252847618.json, 图片生成/图生图/去水印qwen2511最新图像编辑换装千问2511追赶+全能图片V1_2053656485862887425.json, 图片生成/图生图/图片去水印-Qwen2511-Lighting-速度快-效果好_2021029263138365441.json, 图片生成/图生图/图片去水印-Qwen2511-无角标出图_2079924667032363010.json, 图片生成/图生图/换背景Qwen+Image+Edit+2511-支持单图多图编辑加速版_2007308029473071105.json, 图片生成/图生图/换装千问Qwen2511最新图像编辑换装工作流_2084112989686427649.json, 图片生成/图生图/换装千问Qwen2511最新图像编辑换装工作流_2084124102578753538.json, 图片生成/图生图/换装千问qwen2511最新图像编辑_2008133174475366401.json, 图片生成/图生图/换装千问qwen2511最新图像编辑换装千问2511_2003636475113684993.json, 图片生成/图生图/换装千问qwen2511最新图像编辑换装千问2511_2100047371999735810.json, 图片生成/图生图/换装千问qwen2511最新图像编辑换装千问2511_2100125361475506178.json, 图片生成/图生图/老孙AI 一键去水印qwen2511_2086304124907380737.json, 图片生成/图生图/课程演示-去水印_2075540632856260610.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_8

> 由 `engine/knowledge_consolidation` 从 29 个 workflow 归纳得出（图片生成/图生图/Qwen2511-儿童涂鸦风格转绘-小宣喧-RH_2007047125556797442.json、图片生成/图生图/Qwen2511-阿凡达风格-小宣喧-RH_2008411628018081793.json、图片生成/图生图/QwenEdit2511-Q版角色-小宣喧-RH_2006747284024860673.json、图片生成/图生图/RH-PSAPI插件用-_图生图edit2511_2068683270535081985.json、图片生成/图生图/qwen Edit 2511 单图编辑_2051921199571193858.json…）

- **类型**：Image To Image
- **样本数**：29
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 29 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 28/29 个有
- `CR Text` —— 26/29 个有
- `SaveImage` —— 26/29 个有
- `ImageScaleToTotalPixels` —— 25/29 个有
- `ImageConcanate` —— 22/29 个有
- `ImageStitch` —— 4/29 个有
- `ImageResize+` —— 3/29 个有
- `KOOK_SaveJPGImage` —— 3/29 个有
- `CustomAddLabel` —— 2/29 个有
- `Image Comparer (rgthree)` —— 2/29 个有
- `Label (rgthree)` —— 2/29 个有
- `CR SDXL Aspect Ratio` —— 1/29 个有
- `ImpactSwitch` —— 1/29 个有
- `easy imageScaleDownToSize` —— 1/29 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 25 | 29 | 20% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 29 | 100% |
| 采样算法 | euler | - | 29 | 100% |
| 调度器 | simple | - | 29 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 29 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/29 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 25，29 个样本，取值分散，一致性仅 20%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，29 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，29 个样本，一致性 100%
- 调度器 最常用 simple，29 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，29 个样本，取值集中（一致性 100%）
- 高发问题（28/29 个样本）：Steps较低可能导致细节不足
