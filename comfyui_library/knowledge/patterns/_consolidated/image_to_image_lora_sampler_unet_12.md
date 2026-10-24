---
name: image_to_image_lora_sampler_unet_12
type: Image To Image
frequency: 23
level: strong
coverage: 0.908348
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, QwenMultiangleCameraNode, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键五视图+可控多镜头（Qwen Multiangle Camera）_2010989708263821313.json, 图片生成/图生图/万物自由多机位镜头控制_2036392111184023554.json, 图片生成/图生图/任意角度取景_2009631099705630721.json, 图片生成/图生图/任意角度取景_2012172038881943553.json, 图片生成/图生图/任意角度取景_2033799661676400641.json, 图片生成/图生图/分镜多自定义角度生成_2011331871963095042.json, 图片生成/图生图/千问2511 人像多角度自由切换_2021416167709085698.json, 图片生成/图生图/千问2511 多角度自由切换自由选择（感谢柯基大佬）_2009793140919635969.json, 图片生成/图生图/千问2511 无限多角度 镜头控制+镜头选择（电商漫剧制作者必备）_2013106286111498241.json, 图片生成/图生图/千问2511+人像多角度自由切换_2084591767961292802.json, 图片生成/图生图/千问人物多角度生成_2026162988079652866.json, "图片生成/图生图/图生图+Qwen+Edit+2511+镜头多角度控制,一张图片变换多个角度_2063879329695756290.json", 图片生成/图生图/场景生成多视角_2013145425766780929.json, 图片生成/图生图/场景生成多视角_2101477990000582658.json, 图片生成/图生图/多角度切换相机控制 复刻场景 Qwen 人物产品多角度_2069217388083634178.json, 图片生成/图生图/多角度多视角批量出图_2011269248949161985.json, 图片生成/图生图/多角度自由切换（感谢柯基大佬）_2009912734170750977.json, 图片生成/图生图/多角度自由切换（感谢柯基大佬）_2011610163345625089.json, 图片生成/图生图/多角度镜头选择版本_2009891554516799489.json, 图片生成/图生图/手动控制镜头3d camera qwen 2511人物场景多角度镜头控制镜头选择10秒出图_2011705037017325569.json, 图片生成/图生图/手动控制镜头3d camera qwen 2511人物场景多角度镜头控制镜头选择（柯基大佬版）_2010169381770240002.json, 图片生成/图生图/手动控制镜头3d camera qwen 2511人物场景多角度镜头控制镜头选择（柯基大佬版）_2037411672662478850.json, 视频生成/图生视频/QWEN imageEdit拍摄视角选择器_2010896559696777218.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_12

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（图片生成/图生图/一键五视图+可控多镜头（Qwen Multiangle Camera）_2010989708263821313.json、图片生成/图生图/万物自由多机位镜头控制_2036392111184023554.json、图片生成/图生图/任意角度取景_2009631099705630721.json、图片生成/图生图/任意角度取景_2012172038881943553.json、图片生成/图生图/任意角度取景_2033799661676400641.json…）

- **类型**：Image To Image
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 23 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `QwenMultiangleCameraNode`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 20/23 个有
- `easy promptList` —— 20/23 个有
- `PreviewImage` —— 6/23 个有
- `AspectRatio` —— 1/23 个有
- `Bookmark (rgthree)` —— 1/23 个有
- `Compare` —— 1/23 个有
- `Int` —— 1/23 个有
- `InversionDemoLazySwitch` —— 1/23 个有
- `PlaySound|pysssss` —— 1/23 个有
- `TT_img_enc` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 23 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 23 | 100% |
| 采样算法 | euler | - | 23 | 100% |
| 调度器 | simple | - | 23 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，23 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，23 个样本，一致性 100%
- 调度器 最常用 simple，23 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 高发问题（23/23 个样本）：Steps较低可能导致细节不足
