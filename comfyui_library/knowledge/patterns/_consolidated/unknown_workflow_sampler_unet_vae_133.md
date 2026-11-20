---
name: unknown_workflow_sampler_unet_vae_133
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.635778
common_nodes: [CFGNorm, CLIPLoader, EmptySD3LatentImage, KSampler, LoadImage, ModelSamplingAuraFlow, PrimitiveInt, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/3图合成 Qwen Edit Plus=艾橘溪_1971910795636436994.json, 图片生成/图生图/3图合成 Qwen Edit Plus_2079458318413811714.json, 图片生成/图生图/Qwen Image Edit-自动换装_1976472822258208769.json, 图片生成/图生图/Qwen Image Edit生图技巧，一键生成模特多角度照片，去除光斑_过曝_欠曝修复_1988508745347022850.json, 图片生成/图生图/QwenImageEdit2509_多角度 + 重打光高级工作流_1987821026287529985.json, 图片生成/图生图/QwenImageEdit2509人物场景多角度 + 重打光_1988078364290428930.json, 图片生成/图生图/QwenImageEdit_多角度 + 光线修复_1988474472032329730.json, 图片生成/图生图/Qwen全V3自动换装_1996559699203989505.json, 平台全量/Qwen Edit 2509 完美自动换装_1977250843630161922.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_133

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/3图合成 Qwen Edit Plus=艾橘溪_1971910795636436994.json、图片生成/图生图/3图合成 Qwen Edit Plus_2079458318413811714.json、图片生成/图生图/Qwen Image Edit-自动换装_1976472822258208769.json、图片生成/图生图/Qwen Image Edit生图技巧，一键生成模特多角度照片，去除光斑_过曝_欠曝修复_1988508745347022850.json、图片生成/图生图/QwenImageEdit2509_多角度 + 重打光高级工作流_1987821026287529985.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PrimitiveInt`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 8/9 个有
- `LayerUtility: PurgeVRAM` —— 8/9 个有
- `LoraLoaderModelOnly` —— 8/9 个有
- `SetNode` —— 8/9 个有
- `ImageResizeKJv2` —— 5/9 个有
- `TextEncodeQwenImageEdit` —— 5/9 个有
- `FloatConstant` —— 4/9 个有
- `Image Comparer (rgthree)` —— 4/9 个有
- `ImageScaleToTotalPixels` —— 4/9 个有
- `Text Multiline` —— 4/9 个有
- `ImageAndMaskPreview` —— 3/9 个有
- `LayerMask: SegformerB2ClothesUltra` —— 3/9 个有
- `LayerUtility: ImageRemoveAlpha` —— 3/9 个有
- `PreviewImage` —— 2/9 个有
- `Anything Everywhere3` —— 1/9 个有
- `JjkText` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `LoraLoader` —— 1/9 个有
- `MaskToImage` —— 1/9 个有
- `SeedVR2` —— 1/9 个有
- `SeedVR2BlockSwap` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 8 | 9 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 56% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 8，9 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
