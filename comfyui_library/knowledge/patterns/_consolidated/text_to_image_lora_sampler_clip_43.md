---
name: text_to_image_lora_sampler_clip_43
type: Text To Image
frequency: 19
level: strong
coverage: 0.878842
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/姿势提取工作流，配合分镜流使用的图生图人体姿态分析工具_2103535118508978178.json, 图片生成/图生图/官方稳定版全能图片｜G2.0图生图处理直出_2092759621646766081.json, 图片生成/图生图/室内效果图分阶修复专家｜精修图生图 老房子秒变样板间_2105510590549676033.json, 图片生成/图生图/小红书电商换装实战｜FireRed-Image-Edit服饰图生图_2101241575685836802.json, 图片生成/图生图/换装商用级高清方案，高度一致性图生图呈现_2111239332995616769.json, 图片生成/图生图/换装换衣电商服装展示小红书 FireRed Image Edit工作流_2105073990086778881.json, 图片生成/图生图/换装换衣电商服装展示小红书FireRed Image Edit 服装展示方案_2109427654737879042.json, 图片生成/图生图/换装换衣电商服装展示小红书FireRed Image Edit 服装展示方案_2109429147910103042.json, 图片生成/图生图/换装换衣电商服装展示小红书FireRed Image Edit工作流，服饰图生图换装工具_2107618127231143937.json, 图片生成/图生图/电商双图服装试穿换装工作流，图生图电商服装展示搭配预览工具_2106074131702829057.json, 图片生成/图生图/电商换装双图服装试穿 图生图处理工具_2100664711040823297.json, 图片生成/图生图/电商换装换衣展示｜FireRed-Image-Edit小红书图生图_2095951997458538497.json, 图片生成/图生图/电商服装一键换装展示 图生图虚拟试衣工具_2098852784799043585.json, 图片生成/图生图/电商服装一键换装展示 图生图虚拟试衣工具_2099600628573102082.json, 图片生成/图生图/电商服装一键换装展示 虚拟试衣图生图工具_2099948523428073473.json, 图片生成/图生图/电商服装一键换装展示_虚拟试衣图生图工具_2101225437476245506.json, 图片生成/图生图/电商服装一键换装展示流｜换衣服换款式一步到位，上新图不用拍_2099419761980567554.json, 图片生成/图生图/电商服装展示小红书换装｜FireRed-Image-Edit换衣图生图_2095584350510338049.json, 图片生成/图生图/电商服装展示换衣｜FireRed-Image-Edit小红书图生图_2090922615786528769.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_43

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/姿势提取工作流，配合分镜流使用的图生图人体姿态分析工具_2103535118508978178.json、图片生成/图生图/官方稳定版全能图片｜G2.0图生图处理直出_2092759621646766081.json、图片生成/图生图/室内效果图分阶修复专家｜精修图生图 老房子秒变样板间_2105510590549676033.json、图片生成/图生图/小红书电商换装实战｜FireRed-Image-Edit服饰图生图_2101241575685836802.json、图片生成/图生图/换装商用级高清方案，高度一致性图生图呈现_2111239332995616769.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 18/19 个有
- `PreviewImage` —— 17/19 个有
- `ConditioningZeroOut` —— 16/19 个有
- `PIP_图像联结` —— 16/19 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 16/19 个有
- `LayerUtility: ImageReel` —— 8/19 个有
- `LayerUtility: ImageReelComposit` —— 8/19 个有
- `Image Comparer (rgthree)` —— 5/19 个有
- `EmptyImage` —— 2/19 个有
- `AIO_Preprocessor` —— 1/19 个有
- `ConstrainResolution` —— 1/19 个有
- `ImageResizeKJv2` —— 1/19 个有
- `ImageScaleToTotalPixels` —— 1/19 个有
- `RH_RhartImageG25SunburstImageToImage` —— 1/19 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 19 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 19 | 100% |
| 采样算法 | er_sde | - | 19 | 100% |
| 调度器 | beta | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |
| 宽度 | 80 | 80 - 80 | 19 | 100% |
| 高度 | 80 | 80 - 80 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 32/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，19 个样本，一致性 100%
- 调度器 最常用 beta，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高发问题（32/19 个样本）：Steps较低可能导致细节不足
