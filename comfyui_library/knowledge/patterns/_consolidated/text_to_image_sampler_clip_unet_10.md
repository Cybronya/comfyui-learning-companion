---
name: text_to_image_sampler_clip_unet_10
type: Text To Image
frequency: 26
level: weak
coverage: 0.928538
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-瑶光版-超真实细节增强_2049457426226749441.json, 图片生成/文生图/Z-Image-瑶光版-适合人像创作_2102648327572647937.json, 图片生成/文生图/Z-Image-瑶光版-适合人像创作_2108742472506626050.json, 图片生成/文生图/Z-Image-瑶光版-适合人像创作_2110185721926602754.json, 图片生成/文生图/Z-Image基础简易文生图_2003471072429260801.json, 图片生成/文生图/Z-Image文生图基础工作流_1997889845496283138.json, 图片生成/文生图/Z-Image瑶光版文生图｜人像创作质感出片首选_2104572471079952385.json, 图片生成/文生图/Z-image Kook-写实文生图_2036359445025923074.json, 图片生成/文生图/Z-image Kook-写实文生图_2085557272251555841.json, 图片生成/文生图/Z-image Kook-写实文生图_2085561609514213377.json, 图片生成/文生图/Z-image Kook-写实文生图_2085563036080885761.json, 图片生成/文生图/Z_image角色生成【文生图】_2050492161661128706.json, 图片生成/文生图/image2.0文生图全能图像G_2086535340189380610.json, 图片生成/文生图/krea2免LORA文生图｜无需训练直接出图省心版_2111061448398041089.json, 图片生成/文生图/qwen-image-2.1官方原版｜纯净文生图像模型直出_2103085016224985090.json, 图片生成/文生图/qwen-image-2.1文生图基础款｜参数清爽开箱即用｜日常出图够用了_2102267329873801217.json, 图片生成/文生图/qwen2.1文生图基础工作流 新手友好稳定出图_2104664392800489473.json, 图片生成/文生图/qwen2.1文生图基础工作流 新手友好稳定出图_2105070911778021377.json, 图片生成/文生图/平替全能图片G图像编辑 Qwen Image 2.1生图加编辑12张参考图_2104300055376261122.json, 数字人/数字人/千问大模型驱动的数字人工作流，多功能AI生成方案_2102883846000828418.json, 数字人/数字人/千问大模型驱动的数字人工作流，多功能AI生成方案_2105115732848766978.json, 视频生成/图生视频/Qwen-Image-2.1一键扩图图生图｜写实风格扩展轻松搞定_2107980380883214337.json, 视频生成/图生视频/Qwen_Image_2.1一键图片换装图生图，人物服饰替换处理工具_2104382452906156034.json, 视频生成/图生视频/Qwen_Image_2.1图片换头换脸，一键面部替换的图生图处理工具_2106546399436431361.json, 视频生成/图生视频/Qwen_Image_2.1图片编辑工作流，简洁高效的图生图处理方案_2105520911070875649.json, 视频生成/图生视频/qwen_image2.1多图编辑进阶版｜文生图图生图自由切换｜批量改图高效_2104446242880315393.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_10

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（图片生成/文生图/Z-Image-瑶光版-超真实细节增强_2049457426226749441.json、图片生成/文生图/Z-Image-瑶光版-适合人像创作_2102648327572647937.json、图片生成/文生图/Z-Image-瑶光版-适合人像创作_2108742472506626050.json、图片生成/文生图/Z-Image-瑶光版-适合人像创作_2110185721926602754.json、图片生成/文生图/Z-Image基础简易文生图_2003471072429260801.json…）

- **类型**：Text To Image
- **样本数**：26
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 26 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 25/26 个有
- `JjkText` —— 15/26 个有
- `solarL_SaveImagesToZip` —— 15/26 个有
- `TextEncodeQwenImage21` —— 12/26 个有
- `FastFilmGrain` —— 10/26 个有
- `LayerColor: BrightnessContrastV2` —— 10/26 个有
- `QwenImage21Cache` —— 10/26 个有
- `ResolutionSelector` —— 10/26 个有
- `CR Text` —— 9/26 个有
- `ComfySwitchNode` —— 9/26 个有
- `孤海注释` —— 9/26 个有
- `LoadImage` —— 8/26 个有
- `EmptyImage` —— 6/26 个有
- `PreviewImage` —— 6/26 个有
- `BatchImagesNode` —— 5/26 个有
- `TextGenerateLTX2Prompt` —— 5/26 个有
- `SaveImageAdvanced` —— 4/26 个有
- `easy showAnything` —— 2/26 个有
- `AnyAspectRatio` —— 1/26 个有
- `GetImageSize` —— 1/26 个有
- `JDCN_StringToList` —— 1/26 个有
- `RH_RhartImageG2TextToImage` —— 1/26 个有
- `TextInput_` —— 1/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1280 | 26 | 0% |
| 高度 | 80 | 80 - 1920 | 26 | 0% |
| 采样步数 | 4 | 4 - 20 | 26 | 45% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 26 | 46% |
| 采样算法 | er_sde | - | 26 | 58% |
| 调度器 | beta | - | 26 | 58% |
| 重绘幅度 | 1 | 1 - 1 | 26 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/26 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1280，26 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，26 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 20，26 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，26 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 er_sde，26 个样本，一致性 58%
- 调度器 最常用 beta，26 个样本，一致性 58%
- 重绘幅度 中位数 1，观测区间 1 - 1，26 个样本，取值集中（一致性 100%）
- 高发问题（28/26 个样本）：Steps较低可能导致细节不足
