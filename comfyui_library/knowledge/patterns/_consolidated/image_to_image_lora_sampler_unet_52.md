---
name: image_to_image_lora_sampler_unet_52
type: Image To Image
frequency: 11
level: strong
coverage: 0.852727
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit 2511_2046841088454955010.json, 图片生成/图生图/Qwen-Edit 二次元转超写实真人_2019670658141134849.json, 图片生成/图生图/Qwen-Edit-2509 场景换视角工作流_2046950886362062849.json, 图片生成/图生图/Qwen-Edit-2509 测试_2003005793597288449.json, 图片生成/图生图/Qwen-Edit-2509 白底图换场景工作流_2091502540566388738.json, 图片生成/图生图/Qwen-Edit-2509 超多角度切换 LoRA_1990400053313507330.json, 图片生成/图生图/Qwen-Edit-2509-多角度切换_1990328940835336193.json, 图片生成/图生图/Qwen-Edit-2509-多角度切换_2000522237449039873.json, 图片生成/图生图/Qwen-Edit-2509_白底图换场景工作流_2097869384277643266.json, 图片生成/图生图/Qwen-Edit-2509_白底图换场景工作流_2099408627546284034.json, 图片生成/图生图/Qwen-image edit 2511 最新一图生成人物的全角度_2003698374991855618.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_52

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit 2511_2046841088454955010.json、图片生成/图生图/Qwen-Edit 二次元转超写实真人_2019670658141134849.json、图片生成/图生图/Qwen-Edit-2509 场景换视角工作流_2046950886362062849.json、图片生成/图生图/Qwen-Edit-2509 测试_2003005793597288449.json、图片生成/图生图/Qwen-Edit-2509 白底图换场景工作流_2091502540566388738.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
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
- `CFGNorm` —— 10/11 个有
- `TextEncodeQwenImageEditPlus` —— 10/11 个有
- `Image Comparer (rgthree)` —— 8/11 个有
- `ImageScaleToTotalPixels` —— 8/11 个有
- `PreviewImage` —— 8/11 个有
- `easy imageSize` —— 4/11 个有
- `ImageBlend` —— 3/11 个有
- `Mask Fill Holes` —— 3/11 个有
- `MaskToImage` —— 3/11 个有
- `Any Switch (rgthree)` —— 2/11 个有
- `CR Text` —— 2/11 个有
- `ShowText|pysssss` —— 2/11 个有
- `Text Multiline` —— 2/11 个有
- `easy promptLine` —— 2/11 个有
- `Anything Everywhere3` —— 1/11 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/11 个有
- `JjkText` —— 1/11 个有
- `LayerMask: LoadFlorence2Model` —— 1/11 个有
- `LayerUtility: Collage` —— 1/11 个有
- `Note Plus (mtb)` —— 1/11 个有
- `TextEncodeQwenImageEdit` —— 1/11 个有
- `easy imageBatchToImageList` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 11 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，11 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（23/11 个样本）：Steps较低可能导致细节不足
