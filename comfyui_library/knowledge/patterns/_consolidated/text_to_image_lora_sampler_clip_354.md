---
name: text_to_image_lora_sampler_clip_354
type: Text To Image
frequency: 5
level: strong
coverage: 0.8734
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen image 2.1多图编辑 多张输入精准改图_2105016159463632898.json, 图片生成/图生图/千问Image2.1图像编辑不偏移版，自动优化提示词可抠图商品换背景工具_2103564372319760385.json, 图片生成/图生图/抠图工作流 精准主体识别透明背景生成一键搞定_2105393800863637505.json, 图片生成/文生图/千问Image2.1文生图中文海报自动扩写提示词可抠图，文生图多合一工具_2103561269214277633.json, 图片生成/文生图/微小字体不崩坏 千问image2.1创意海报文生图_2104312640167305218.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_354

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/qwen image 2.1多图编辑 多张输入精准改图_2105016159463632898.json、图片生成/图生图/千问Image2.1图像编辑不偏移版，自动优化提示词可抠图商品换背景工具_2103564372319760385.json、图片生成/图生图/抠图工作流 精准主体识别透明背景生成一键搞定_2105393800863637505.json、图片生成/文生图/千问Image2.1文生图中文海报自动扩写提示词可抠图，文生图多合一工具_2103561269214277633.json、图片生成/文生图/微小字体不崩坏 千问image2.1创意海报文生图_2104312640167305218.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
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
- `QwenPERewriteT8` —— 4/5 个有
- `ResolutionSelector` —— 4/5 个有
- `SaveImageAdvanced` —— 4/5 个有
- `ShowText|pysssss` —— 4/5 个有
- `Text Multiline` —— 4/5 个有
- `ComfySwitchNode` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `Seed (rgthree)` —— 3/5 个有
- `XinbaoImageStandardizer` —— 3/5 个有
- `QwenImage21Cache` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `ImpactInt` —— 1/5 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/5 个有
- `RunningHub SeedXPro Translator` —— 1/5 个有
- `easy imageScaleDownToSize` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
