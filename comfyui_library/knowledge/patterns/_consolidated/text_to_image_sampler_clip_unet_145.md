---
name: text_to_image_sampler_clip_unet_145
type: Text To Image
frequency: 5
level: strong
coverage: 0.9236
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, Qwen3_VQA, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image 人物提示词优化+图片反推_1996440578021801985.json, 图片生成/文生图/Z-image+Qwen3 图像反推_1993867190606692353.json, 图片生成/文生图/Z-image-电商产品摄影-提示词优化框架_1996428997665898497.json, 图片生成/文生图/Z-image，文生图新王，秒级出图，洗图工具_1995432469656690689.json, 图片生成/文生图/【gen全能视频Si】z-image欧美复古胶片风lora_1995801362824835073.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_145

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Z-image 人物提示词优化+图片反推_1996440578021801985.json、图片生成/文生图/Z-image+Qwen3 图像反推_1993867190606692353.json、图片生成/文生图/Z-image-电商产品摄影-提示词优化框架_1996428997665898497.json、图片生成/文生图/Z-image，文生图新王，秒级出图，洗图工具_1995432469656690689.json、图片生成/文生图/【gen全能视频Si】z-image欧美复古胶片风lora_1995801362824835073.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `Qwen3_VQA`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `LayerUtility: PurgeVRAM` —— 3/5 个有
- `CR Prompt Text` —— 2/5 个有
- `LazySwitchKJ` —— 2/5 个有
- `Text Multiline` —— 2/5 个有
- `easy promptReplace` —— 2/5 个有
- `AspectRatio` —— 1/5 个有
- `GroupSwitcher` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `PurgeVRAM_UTK` —— 1/5 个有
- `StringConcatenate` —— 1/5 个有
- `easy int` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1080 | 5 | 97% |
| 高度 | 1536 | 1024 - 1920 | 5 | 73% |
| 采样步数 | 10 | 10 - 10 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1080，5 个样本，取值集中（一致性 97%）
- 高度 中位数 1536，观测区间 1024 - 1920，5 个样本
- 采样步数 中位数 10，观测区间 10 - 10，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
