---
name: image_to_image_lora_sampler_unet_127
type: Image To Image
frequency: 6
level: strong
coverage: 0.901167
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit 2509模特换装工作流_2003380174030868482.json, 图片生成/图生图/Qwen Image Edit  三图融合_1962314713319325698.json, 图片生成/图生图/Qwen-Image-Edit 2509：冬日萌宠童话，一键入画，定格魔法瞬间！_1987879653480271873.json, 图片生成/图生图/Qwen-Image-Edit图像编辑丨千问图像编辑_1959825512598286338.json, 图片生成/图生图/Qwen_2511_千问一键多图融合参考自动拼接工作流_2003800899795468290.json, 平台全量/千问Edit Plus模特换装_1982289708539625474.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_127

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen Edit 2509模特换装工作流_2003380174030868482.json、图片生成/图生图/Qwen Image Edit  三图融合_1962314713319325698.json、图片生成/图生图/Qwen-Image-Edit 2509：冬日萌宠童话，一键入画，定格魔法瞬间！_1987879653480271873.json、图片生成/图生图/Qwen-Image-Edit图像编辑丨千问图像编辑_1959825512598286338.json、图片生成/图生图/Qwen_2511_千问一键多图融合参考自动拼接工作流_2003800899795468290.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
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
- `CR Text` —— 4/6 个有
- `Image Comparer (rgthree)` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `TextEncodeQwenImageEditPlus` —— 4/6 个有
- `TextEncodeQwenImageEdit` —— 3/6 个有
- `CR Text Concatenate` —— 2/6 个有
- `ImageScale` —— 2/6 个有
- `PIP_图像联结` —— 2/6 个有
- `String` —— 2/6 个有
- `GetImageSize+` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `RH_Captioner` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 6 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
