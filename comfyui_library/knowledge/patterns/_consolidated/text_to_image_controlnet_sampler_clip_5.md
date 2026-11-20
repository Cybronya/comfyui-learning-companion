---
name: text_to_image_controlnet_sampler_clip_5
type: Text To Image
frequency: 8
level: moderate
coverage: 0.903625
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, ImageResize+, KSampler, LoadImage, PreviewImage, SaveImage, VAEDecode, Zoe-DepthMapPreprocessor]
problems: []
missing: []
members: [图片生成/图生图/10s照片转色彩头像_1891801702159298561.json, 图片生成/文生图/文生图+CN_Depth_Openpose_1778002614114390018.json, 平台全量/51艺术字体海报设计_1782645766683144193.json, 平台全量/520海报制作_1791296386277429250.json, 平台全量/人物角色三视图_1777882936469622785.json, 平台全量/劳动节艺术字体海报设计_1782611984517214210.json, 平台全量/水彩画头像转换器_1804030744862908418.json, 平台全量/端午海报制作_1790938867180883969.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_5

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/10s照片转色彩头像_1891801702159298561.json、图片生成/文生图/文生图+CN_Depth_Openpose_1778002614114390018.json、平台全量/51艺术字体海报设计_1782645766683144193.json、平台全量/520海报制作_1791296386277429250.json、平台全量/人物角色三视图_1777882936469622785.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `ImageResize+`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `Zoe-DepthMapPreprocessor`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 7/8 个有
- `VAEEncode` —— 7/8 个有
- `IPAdapter` —— 6/8 个有
- `IPAdapterUnifiedLoader` —— 6/8 个有
- `UpscaleModelLoader` —— 6/8 个有
- `LoraLoader` —— 5/8 个有
- `Canny` —— 4/8 个有
- `DWPreprocessor` —— 3/8 个有
- `ImageCrop` —— 2/8 个有
- `GetImageSize+` —— 1/8 个有
- `Image Overlay` —— 1/8 个有
- `ImageBlur` —— 1/8 个有
- `OpenposePreprocessor` —— 1/8 个有
- `Upscale Model Loader` —— 1/8 个有
- `WD14Tagger|pysssss` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.8 | 0.5 - 1 | 8 | 79% |
| 采样步数 | 25 | 20 - 30 | 8 | 80% |
| Prompt 约束强度(CFG) | 8 | 6.99 - 8 | 8 | 96% |
| 采样算法 | dpmpp_2m | - | 8 | 50% |
| 调度器 | karras | - | 8 | 100% |
| 重绘幅度 | 0.6 | 0.38 - 1 | 8 | 70% |
| 宽度 | 800 | 768 - 1024 | 8 | 88% |
| 高度 | 1044 | 768 - 1064 | 8 | 91% |
| LoRA 模型强度 | 0.35 | 0.2 - 0.4 | 5 | 75% |
| LoRA 文本强度 | 1 | 0.35 - 1 | 5 | 70% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.8，观测区间 0.5 - 1，8 个样本
- 采样步数 中位数 25，观测区间 20 - 30，8 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 6.99 - 8，8 个样本，取值集中（一致性 96%）
- 采样算法 最常用 dpmpp_2m，8 个样本，一致性 50%
- 调度器 最常用 karras，8 个样本，一致性 100%
- 重绘幅度 中位数 0.6，观测区间 0.38 - 1，8 个样本
- 宽度 中位数 800，观测区间 768 - 1024，8 个样本，取值集中（一致性 88%）
- 高度 中位数 1044，观测区间 768 - 1064，8 个样本，取值集中（一致性 91%）
- LoRA 模型强度 中位数 0.35，观测区间 0.2 - 0.4，5 个样本
- LoRA 文本强度 中位数 1，观测区间 0.35 - 1，5 个样本
