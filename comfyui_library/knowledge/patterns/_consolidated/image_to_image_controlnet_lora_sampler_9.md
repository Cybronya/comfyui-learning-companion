---
name: image_to_image_controlnet_lora_sampler_9
type: Image To Image
frequency: 3
level: moderate
coverage: 0.880333
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CR Text, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, ImageScale, KSampler, LoadImage, LoraLoader, PreviewImage, SaveImage, ShowText|pysssss, Text List, Text List to Text, VAEDecode, VAEEncode, WD14Tagger|pysssss]
problems: []
missing: []
members: [图片生成/图生图/2D 转 3D 形象 ｜一键生图系列_1905621624433856514.json, 平台全量/2D转欧美卡通风格_1817495730629292033.json, 平台全量/像素画风丨风格转换v3.2_1938071151103119361.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_9

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2D 转 3D 形象 ｜一键生图系列_1905621624433856514.json、平台全量/2D转欧美卡通风格_1817495730629292033.json、平台全量/像素画风丨风格转换v3.2_1938071151103119361.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `ImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `Text List`
- `Text List to Text`
- `VAEDecode`
- `VAEEncode`
- `WD14Tagger|pysssss`

**可变部分**（部分 workflow 才有）：
- `VAELoader` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `ControlNetLoaderAdvanced` —— 1/3 个有
- `DepthAnything_V2` —— 1/3 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/3 个有
- `FaceDetailer` —— 1/3 个有
- `LatentUpscaleBy` —— 1/3 个有
- `RepeatLatentBatch` —— 1/3 个有
- `SAMLoader` —— 1/3 个有
- `UltimateSDUpscale` —— 1/3 个有
- `UltralyticsDetectorProvider` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | 0.55 - 0.7 | 3 | 89% |
| 采样步数 | 20 | 18 - 28 | 3 | 80% |
| Prompt 约束强度(CFG) | 4.5 | 3 - 7.5 | 3 | 63% |
| 采样算法 | dpmpp_2m_sde_gpu | - | 3 | 33% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 0.8 | 0.78 - 1 | 3 | 88% |
| LoRA 模型强度 | 0.55 | 0.4 - 1.2 | 3 | 52% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.7，观测区间 0.55 - 0.7，3 个样本，取值集中（一致性 89%）
- 采样步数 中位数 20，观测区间 18 - 28，3 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 3 - 7.5，3 个样本
- 采样算法 最常用 dpmpp_2m_sde_gpu，3 个样本，一致性 33%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 0.8，观测区间 0.78 - 1，3 个样本，取值集中（一致性 88%）
- LoRA 模型强度 中位数 0.55，观测区间 0.4 - 1.2，3 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
