---
name: unknown_workflow_video_upscale_lora_4
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.737833
common_nodes: [Anything Everywhere, CLIPLoader, CLIPTextEncode, ClownsharKSampler_Beta, EmptyHunyuanLatentVideo, ImageScaleBy, ImageUpscaleWithModel, LayerFilter: AddGrain, ModelSamplingSD3, PathchSageAttentionKJ, Power Lora Loader (rgthree), SaveImage, String, StringConcatenate, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, WanVideoNAG]
problems: []
missing: []
members: [图片生成/文生图/Wan2.2+真实摄影+8K高清_1994707638271217666.json, 图片生成/文生图/Wan2.2真实摄影_1994369665260457985.json, 图片生成/文生图/Wan2.2超真实摄影-Instareal+Lenovo【LORA】_1960338805641441282.json, 图片生成/文生图/商K-真实摄影Wan2.2_1982596622628593665.json, 数字人/数字人/Wan2.2真实摄影-Instareal+Lenovo_1979374680974987266.json, 视频生成/图生视频/Wan2.2真实摄影-Instareal+Lenovo_1958396927266209793.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_4

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Wan2.2+真实摄影+8K高清_1994707638271217666.json、图片生成/文生图/Wan2.2真实摄影_1994369665260457985.json、图片生成/文生图/Wan2.2超真实摄影-Instareal+Lenovo【LORA】_1960338805641441282.json、图片生成/文生图/商K-真实摄影Wan2.2_1982596622628593665.json、数字人/数字人/Wan2.2真实摄影-Instareal+Lenovo_1979374680974987266.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 6 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPLoader`
- `CLIPTextEncode`
- `ClownsharKSampler_Beta`
- `EmptyHunyuanLatentVideo`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `LayerFilter: AddGrain`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `Power Lora Loader (rgthree)`
- `SaveImage`
- `String`
- `StringConcatenate`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `Image Comparer (rgthree)` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `Text Multiline` —— 5/6 个有
- `Int` —— 1/6 个有
- `Joy_caption_two` —— 1/6 个有
- `Joy_caption_two_load` —— 1/6 个有
- `LoadImage` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `RH_Translator` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `easy textSwitch` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | beta57 | - | 6 | 83% |
| Prompt 约束强度(CFG) | 12 | 3 - 12 | 6 | 68% |
| 采样算法 | 4 | -1 - 4 | 6 | 41% |
| 调度器 | 1 | 0.3 - 1 | 6 | 70% |
| 重绘幅度 | 3.5 | 2 - 3.5 | 6 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 beta57，6 个样本，一致性 83%
- Prompt 约束强度(CFG) 中位数 12，观测区间 3 - 12，6 个样本
- 采样算法 中位数 4，观测区间 -1 - 4，6 个样本，取值分散，一致性仅 41%
- 调度器 中位数 1，观测区间 0.3 - 1，6 个样本
- 重绘幅度 中位数 3.5，观测区间 2 - 3.5，6 个样本，取值集中（一致性 83%）
- 风险：重绘幅度 观测到 3.5，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
