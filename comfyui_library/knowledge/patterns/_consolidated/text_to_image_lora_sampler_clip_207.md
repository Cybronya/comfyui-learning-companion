---
name: text_to_image_lora_sampler_clip_207
type: Text To Image
frequency: 9
level: strong
coverage: 0.851556
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1自动换头术图像编辑工作流，人像写真图生图处理工具_2108454879172849665.json, 图片生成/图生图/Qwen Image 2.1角色三视图BF16展开版，可选择保留背景图生图工具_2106504632108408834.json, 图片生成/图生图/Qwen Image 2.1角色资产四视图极速版，4步8步加速图生图方案_2103944948725927937.json, 图片生成/图生图/Qwen Image2.1自动换头术｜图像编辑换脸局部重绘利器_2108034758382018561.json, 图片生成/图生图/Qwen image 2.1三图编辑 多参考图图生图处理生成工具_2113016992780345345.json, 图片生成/图生图/Qwen image 2.1单图编辑 一张参考图图生图处理工具_2113031173294350337.json, 图片生成/图生图/Qwen image 2.1双图编辑器 两图参考图生图处理工具_2113058550032453634.json, 图片生成/图生图/Qwen image 2.1图片编辑一号版｜图生图轻量改图首选_2112880073996062721.json, 图片生成/图生图/QwenImage2.1角色三视图生成｜bf16展开版图生图精准出图_2106197248026697729.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_207

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1自动换头术图像编辑工作流，人像写真图生图处理工具_2108454879172849665.json、图片生成/图生图/Qwen Image 2.1角色三视图BF16展开版，可选择保留背景图生图工具_2106504632108408834.json、图片生成/图生图/Qwen Image 2.1角色资产四视图极速版，4步8步加速图生图方案_2103944948725927937.json、图片生成/图生图/Qwen Image2.1自动换头术｜图像编辑换脸局部重绘利器_2108034758382018561.json、图片生成/图生图/Qwen image 2.1三图编辑 多参考图图生图处理生成工具_2113016992780345345.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 7/9 个有
- `ComfySwitchNode` —— 6/9 个有
- `PrimitiveStringMultiline` —— 6/9 个有
- `ImageCompare` —— 2/9 个有
- `Int` —— 2/9 个有
- `PrimitiveBoolean` —— 2/9 个有
- `SDVN Load Image Url` —— 2/9 个有
- `SaveImageAdvanced` —— 2/9 个有
- `WujiCleaner` —— 2/9 个有
- `WujiUpscaler2` —— 2/9 个有
- `easy int` —— 2/9 个有
- `GetNode` —— 1/9 个有
- `SetNode` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（12/9 个样本）：Steps较低可能导致细节不足
