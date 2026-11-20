---
name: text_to_image_lora_sampler_clip_568
type: Text To Image
frequency: 3
level: strong
coverage: 0.9
common_nodes: [CLIPTextEncode, CR Text, CheckpointLoaderSimple, EmptyLatentImage, FluxGuidance, KSampler, Lora Loader Stack (rgthree), RH_LLMAPI_NODE, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/可乐-生成漫剧场景图片_2008822807001567234.json, 图片生成/文生图/可乐-角色生成图片_2008803491568947202.json, 视频生成/图生视频/维尼漫剧学院（更新版）_2000504996472946689.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_568

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/可乐-生成漫剧场景图片_2008822807001567234.json、图片生成/文生图/可乐-角色生成图片_2008803491568947202.json、视频生成/图生视频/维尼漫剧学院（更新版）_2000504996472946689.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `Lora Loader Stack (rgthree)`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `RHHiddenNodes` —— 2/3 个有
- `RH_Nano_Banana_Image2Image` —— 2/3 个有
- `RH_Translator` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_Sora2_I2V` —— 1/3 个有
- `SaveVideo` —— 1/3 个有
- `Text Multiline` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 24 | 24 - 24 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 720 | 720 - 1280 | 3 | 71% |
| 高度 | 1280 | 720 - 1280 | 3 | 76% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 24，观测区间 24 - 24，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 720，观测区间 720 - 1280，3 个样本
- 高度 中位数 1280，观测区间 720 - 1280，3 个样本
