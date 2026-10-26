---
name: text_to_image_lora_sampler_clip_87
type: Text To Image
frequency: 14
level: strong
coverage: 0.863929
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1自动换头术图像编辑工作流，人像写真图生图处理工具_2108454879172849665.json, 图片生成/图生图/Qwen Image 2.1角色三视图BF16展开版，可选择保留背景图生图工具_2106504632108408834.json, 图片生成/图生图/Qwen Image2.1图生图三套夏装｜多套服装一键试穿_2108077360229732354.json, 图片生成/图生图/Qwen Image2.1自动换头术｜图像编辑换脸局部重绘利器_2108034758382018561.json, 图片生成/图生图/Qwen image 2.1三图编辑 多参考图图生图处理生成工具_2113016992780345345.json, 图片生成/图生图/Qwen image 2.1单图编辑 一张参考图图生图处理工具_2113031173294350337.json, 图片生成/图生图/Qwen image 2.1双图编辑器 两图参考图生图处理工具_2113058550032453634.json, 图片生成/图生图/Qwen image 2.1图像编辑通用版｜图生图指令改图｜听懂人话好上手_2102285690850598914.json, 图片生成/图生图/Qwen image 2.1图片编辑一号版｜图生图轻量改图首选_2112880073996062721.json, 图片生成/图生图/QwenImage2.1角色三视图生成｜bf16展开版图生图精准出图_2106197248026697729.json, 图片生成/文生图/Qwen Image 2.1 PE文生图提示词优化加速版 高质量画面直出_2109372180118200321.json, 图片生成/文生图/Qwen Image 2.1-PE 加速文生图｜提示词优化一键增强_2112477823029047298.json, 图片生成/文生图/Qwen Image 2.1-PE 提示词优化版｜文生图智能扩写_2112472087343489026.json, 图片生成/文生图/Qwen Image 2.1-PE 文生图加速版｜提示词优化出好图_2112468933998632962.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_87

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1自动换头术图像编辑工作流，人像写真图生图处理工具_2108454879172849665.json、图片生成/图生图/Qwen Image 2.1角色三视图BF16展开版，可选择保留背景图生图工具_2106504632108408834.json、图片生成/图生图/Qwen Image2.1图生图三套夏装｜多套服装一键试穿_2108077360229732354.json、图片生成/图生图/Qwen Image2.1自动换头术｜图像编辑换脸局部重绘利器_2108034758382018561.json、图片生成/图生图/Qwen image 2.1三图编辑 多参考图图生图处理生成工具_2113016992780345345.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 11/14 个有
- `PrimitiveStringMultiline` —— 10/14 个有
- `QwenImage21Cache` —— 10/14 个有
- `LoadImage` —— 8/14 个有
- `SaveImageAdvanced` —— 7/14 个有
- `PrimitiveBoolean` —— 6/14 个有
- `ResolutionSelector` —— 5/14 个有
- `PreviewImage` —— 4/14 个有
- `QwenImage21_T2IPromptRewrite` —— 4/14 个有
- `RH_QwenImagePromptEnhancer` —— 4/14 个有
- `easy showAnything` —— 4/14 个有
- `ImageCompare` —— 2/14 个有
- `Int` —— 2/14 个有
- `SDVN Load Image Url` —— 2/14 个有
- `WujiCleaner` —— 2/14 个有
- `WujiUpscaler2` —— 2/14 个有
- `easy int` —— 2/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高发问题（20/14 个样本）：Steps较低可能导致细节不足
