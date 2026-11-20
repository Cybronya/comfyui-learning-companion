---
name: text_to_image_lora_sampler_clip_445
type: Text To Image
frequency: 4
level: strong
coverage: 0.9465
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageBatchMulti, KSampler, LoadImage, ModelSamplingAuraFlow, RunningHub_ZImageI2L_Loader, RunningHub_ZImageI2L_LoraGenerator, RunningHub_ZImageI2L_Saver, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Z-Image Base  多图生Lora_2018605832035897346.json, 图片生成/图生图/Z-Image Base I2L 图生Lora（官方维护中）_2016860599078096898.json, 图片生成/图生图/Z-image-base五张图一个lora训练流可下载_2016878382465683457.json, 图片生成/文生图/Z-image-base i2L 3分钟图生Lora_2073309025671933953.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_445

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Z-Image Base  多图生Lora_2018605832035897346.json、图片生成/图生图/Z-Image Base I2L 图生Lora（官方维护中）_2016860599078096898.json、图片生成/图生图/Z-image-base五张图一个lora训练流可下载_2016878382465683457.json、图片生成/文生图/Z-image-base i2L 3分钟图生Lora_2073309025671933953.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageBatchMulti`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `RunningHub_ZImageI2L_Loader`
- `RunningHub_ZImageI2L_LoraGenerator`
- `RunningHub_ZImageI2L_Saver`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `LoraLoader` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `PreviewAny` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 976 | 768 - 1184 | 4 | 79% |
| 高度 | 1408 | 1280 - 1536 | 4 | 91% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 50 | 50 - 50 | 4 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 4 | 100% |
| 采样算法 | res_multistep | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 976，观测区间 768 - 1184，4 个样本
- 高度 中位数 1408，观测区间 1280 - 1536，4 个样本，取值集中（一致性 91%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 50，观测区间 50 - 50，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
