---
name: unknown_workflow_lora_sampler_checkpoint_15
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8795
common_nodes: [CheckpointLoaderSimple, GetImageSize, GrowMaskWithBlur, Image Comparer (rgthree), ImageScale, ImageScaleToMaxDimension, LoadImage, LoraLoaderModelOnly, QwenImageIntegratedKSampler, ResizeMask, SaveImage, SetLatentNoiseMask, Text, VAEDecode, VAEEncode, easy int]
problems: []
missing: []
members: ["图片生成/图生图/QwenEdit 2511aio23单图万物局部重绘,零偏移_2036713079777529857.json", 图片生成/图生图/QwenEdit 局部重绘（绝对无偏移）_2036703161758519297.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_checkpoint_15

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/QwenEdit 2511aio23单图万物局部重绘,零偏移_2036713079777529857.json、图片生成/图生图/QwenEdit 局部重绘（绝对无偏移）_2036703161758519297.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `GetImageSize`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageScale`
- `ImageScaleToMaxDimension`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImageIntegratedKSampler`
- `ResizeMask`
- `SaveImage`
- `SetLatentNoiseMask`
- `Text`
- `VAEDecode`
- `VAEEncode`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `SetNode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 图生图 image-to-image | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | 0 | - | 2 | 100% |
| 调度器 | 0 | - | 2 | 100% |
| 重绘幅度 | 9.10769e+14 | - | 2 | 95% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 图生图 image-to-image，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 0，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 0，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 9.10769e+14，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- 风险：重绘幅度 观测到 9.59268e+14，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
