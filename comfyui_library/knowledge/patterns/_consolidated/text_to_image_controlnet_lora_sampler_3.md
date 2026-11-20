---
name: text_to_image_controlnet_lora_sampler_3
type: Text To Image
frequency: 7
level: strong
coverage: 0.894571
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, ImageResize+, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/【线稿提取】图片转绘速写线稿图生成_1938480251531886594.json, 图片生成/图生图/【高清漫画】真人模特转绘漫画风格_1909111109171687426.json, 图片生成/图生图/一键美漫转绘_1927538995205398529.json, 图片生成/图生图/一键转线稿-傲雪AIGC_1980952157593714689.json, 图片生成/图生图/图片一键转线稿_1892157113735536641.json, 图片生成/图生图/图片提取转绘线稿图_1942499808412119041.json, 图片生成/图生图/真人照片物体平面矢量风格插图转绘_1928472489205309441.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_3

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/【线稿提取】图片转绘速写线稿图生成_1938480251531886594.json、图片生成/图生图/【高清漫画】真人模特转绘漫画风格_1909111109171687426.json、图片生成/图生图/一键美漫转绘_1927538995205398529.json、图片生成/图生图/一键转线稿-傲雪AIGC_1980952157593714689.json、图片生成/图生图/图片一键转线稿_1892157113735536641.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `ImageResize+`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `BNK_CLIPTextEncodeAdvanced` —— 6/7 个有
- `FaceDetailer` —— 5/7 个有
- `UltralyticsDetectorProvider` —— 5/7 个有
- `LineArtPreprocessor` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `Joy_caption_two` —— 2/7 个有
- `Joy_caption_two_load` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `PlaySound|pysssss` —— 1/7 个有
- `SAMLoader` —— 1/7 个有
- `easy imageColorMatch` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 7 | 100% |
| Prompt 约束强度(CFG) | 5 | 5 - 7 | 7 | 83% |
| 采样算法 | euler_ancestral | - | 7 | 57% |
| 调度器 | normal | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 512 | 512 - 768 | 7 | 84% |
| 高度 | 512 | 512 - 1024 | 7 | 69% |
| ControlNet 权重 | 0.8 | 0.5 - 1 | 7 | 78% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 7，7 个样本，取值集中（一致性 83%）
- 采样算法 最常用 euler_ancestral，7 个样本，一致性 57%
- 调度器 最常用 normal，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 768，7 个样本，取值集中（一致性 84%）
- 高度 中位数 512，观测区间 512 - 1024，7 个样本
- ControlNet 权重 中位数 0.8，观测区间 0.5 - 1，7 个样本
