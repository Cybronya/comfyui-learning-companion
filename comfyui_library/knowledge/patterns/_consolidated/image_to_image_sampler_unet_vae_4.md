---
name: image_to_image_sampler_unet_vae_4
type: Image To Image
frequency: 28
level: strong
coverage: 0.907571
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键氛围打光_2011310291442733057.json, 图片生成/图生图/一键生成15副姿势图动漫，真人_1990075137741516801.json, 图片生成/图生图/一键生成人物不同姿态_1987670680714022914.json, 图片生成/图生图/一键生成人物穿搭_1991670602532659201.json, 图片生成/图生图/万物自由多机位镜头控制_2036392111184023554.json, 图片生成/图生图/九个视角 人物道具 场景视角 加速版_2034191846393520129.json, 图片生成/图生图/任意角度取景_2009631099705630721.json, 图片生成/图生图/任意角度取景_2012172038881943553.json, 图片生成/图生图/任意角度取景_2033799661676400641.json, 图片生成/图生图/任意角度更换_2019449492507992065.json, 图片生成/图生图/分镜多自定义角度生成_2011331871963095042.json, 图片生成/图生图/千问2511 人像多角度自由切换_2021416167709085698.json, 图片生成/图生图/千问2511 多角度自由切换自由选择（感谢柯基大佬）_2009793140919635969.json, 图片生成/图生图/千问2511 无限多角度 镜头控制+镜头选择（电商漫剧制作者必备）_2013106286111498241.json, 图片生成/图生图/千问2511+人像多角度自由切换_2084591767961292802.json, 图片生成/图生图/千问人物多角度生成_2026162988079652866.json, 图片生成/图生图/可视化灯光调节(重打光lora强化版)_2021046893047980033.json, 图片生成/图生图/图像人物重新打光电商商品打精修千问模型plus_2077283170759827458.json, 图片生成/图生图/图像重打光 Qwen2511_2036012882982346753.json, 图片生成/图生图/图像重打光 Qwen2511_2076938070133395457.json, 图片生成/图生图/图像重打光_Qwen2511_2083573156970852354.json, 图片生成/图生图/图像重打光_Qwen2511_2095782087520514050.json, 图片生成/图生图/图像重打光_Qwen2511_2096073652218449921.json, "图片生成/图生图/图生图+Qwen+Edit+2511+镜头多角度控制,一张图片变换多个角度_2063879329695756290.json", 图片生成/图生图/多角度自由切换（感谢柯基大佬）_2009912734170750977.json, 图片生成/图生图/多角度自由切换（感谢柯基大佬）_2011610163345625089.json, 图片生成/图生图/自由调节镜头视角无极选择器Qwen2511+image+edit_2034454761310785538.json, 图片生成/文生图/三图参考生成组合_1993498915181969409.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_4

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（图片生成/图生图/一键氛围打光_2011310291442733057.json、图片生成/图生图/一键生成15副姿势图动漫，真人_1990075137741516801.json、图片生成/图生图/一键生成人物不同姿态_1987670680714022914.json、图片生成/图生图/一键生成人物穿搭_1991670602532659201.json、图片生成/图生图/万物自由多机位镜头控制_2036392111184023554.json…）

- **类型**：Image To Image
- **样本数**：28
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 28 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 27/28 个有
- `EmptySD3LatentImage` —— 26/28 个有
- `FluxKontextMultiReferenceLatentMethod` —— 24/28 个有
- `easy showAnything` —— 23/28 个有
- `QwenMultiangleCameraNode` —— 16/28 个有
- `easy promptList` —— 15/28 个有
- `QwenMultiangleLightningNode` —— 8/28 个有
- `PathchSageAttentionKJ` —— 3/28 个有
- `PrimitiveStringMultiline` —— 3/28 个有
- `RHHiddenNodes` —— 2/28 个有
- `CompressImages` —— 1/28 个有
- `DeepTranslatorTextNode` —— 1/28 个有
- `PreviewAny` —— 1/28 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 28 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 28 | 100% |
| 采样算法 | euler | - | 28 | 100% |
| 调度器 | simple | - | 28 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 28 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/28 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，28 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，28 个样本，一致性 100%
- 调度器 最常用 simple，28 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 高发问题（28/28 个样本）：Steps较低可能导致细节不足
