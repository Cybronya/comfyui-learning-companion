---
name: image_to_image_lora_sampler_unet_16
type: Image To Image
frequency: 20
level: strong
coverage: 0.927
common_nodes: [CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【Qwen Edit 2511】多姿势多角度套图生成-场景人物一致性（真人略油）_2004162954566246402.json, 图片生成/图生图/一键生成15副姿势图动漫，真人_1990075137741516801.json, 图片生成/图生图/人物一致性-多表情_2012765224817922050.json, 图片生成/图生图/任意切换角度Qwen Edit 2511_2010623696456650753.json, 图片生成/图生图/任意角度取景_2009631099705630721.json, 图片生成/图生图/任意角度取景_2012172038881943553.json, 图片生成/图生图/任意角度取景_2033799661676400641.json, 图片生成/图生图/任意角度更换_2019449492507992065.json, 图片生成/图生图/分镜多自定义角度生成_2011331871963095042.json, 图片生成/图生图/千问2511 人像多角度自由切换_2021416167709085698.json, 图片生成/图生图/千问2511 多角度自由切换自由选择（感谢柯基大佬）_2009793140919635969.json, 图片生成/图生图/千问2511 无限多角度 镜头控制+镜头选择（电商漫剧制作者必备）_2013106286111498241.json, 图片生成/图生图/千问2511+人像多角度自由切换_2084591767961292802.json, 图片生成/图生图/千问人物多角度生成_2026162988079652866.json, 图片生成/图生图/图像多角度旋转 最新Qwen Image Edit 2511_2056978603925135361.json, "图片生成/图生图/图生图+Qwen+Edit+2511+镜头多角度控制,一张图片变换多个角度_2063879329695756290.json", 图片生成/图生图/多角度自由切换（感谢柯基大佬）_2009912734170750977.json, 图片生成/图生图/多角度自由切换（感谢柯基大佬）_2011610163345625089.json, 图片生成/图生图/手动控制镜头3d camera qwen 2511人物场景多角度镜头控制镜头选择（柯基大佬版）_2010169381770240002.json, 图片生成/图生图/手动控制镜头3d camera qwen 2511人物场景多角度镜头控制镜头选择（柯基大佬版）_2037411672662478850.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_16

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/【Qwen Edit 2511】多姿势多角度套图生成-场景人物一致性（真人略油）_2004162954566246402.json、图片生成/图生图/一键生成15副姿势图动漫，真人_1990075137741516801.json、图片生成/图生图/人物一致性-多表情_2012765224817922050.json、图片生成/图生图/任意切换角度Qwen Edit 2511_2010623696456650753.json、图片生成/图生图/任意角度取景_2009631099705630721.json…）

- **类型**：Image To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 18/20 个有
- `ModelSamplingAuraFlow` —— 18/20 个有
- `FluxKontextMultiReferenceLatentMethod` —— 17/20 个有
- `QwenMultiangleCameraNode` —— 17/20 个有
- `EmptySD3LatentImage` —— 16/20 个有
- `easy showAnything` —— 15/20 个有
- `easy promptList` —— 12/20 个有
- `RHHiddenNodes` —— 4/20 个有
- `easy cleanGpuUsed` —— 4/20 个有
- `ConditioningZeroOut` —— 2/20 个有
- `PreviewImage` —— 2/20 个有
- `PrimitiveInt` —— 2/20 个有
- `CompressImages` —— 1/20 个有
- `DeepTranslatorTextNode` —— 1/20 个有
- `Int` —— 1/20 个有
- `TT_img_enc` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 20 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 20 | 100% |
| 采样算法 | euler | - | 20 | 90% |
| 调度器 | simple | - | 20 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，20 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，20 个样本，一致性 90%
- 调度器 最常用 simple，20 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（20/20 个样本）：Steps较低可能导致细节不足
