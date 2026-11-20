---
name: unknown_workflow_lora_sampler_unet_46
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.85325
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus_lrzjason, Textbox, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/002.Qwen编辑之王014.证件照生成+排版_2034655195208097794.json, 图片生成/图生图/002.Qwen编辑之王015.证件照快速生成_2034656163802914818.json, 图片生成/图生图/Qwen-image-Edit新版三图编辑_1971599377657688065.json, 图片生成/图生图/Qwen-image-Edit新版双图万物迁移_1971595548304338946.json, 图片生成/图生图/Qwen-image-Edit新版双图编辑人物姿态参考_1971504055640080386.json, 图片生成/图生图/一键证件照_2073052703089053697.json, 图片生成/图生图/证件照-自动剪切-高清放大_2067458008455671810.json, 图片生成/图生图/证件照-自动剪切-高清放大_2084170366376828929.json, 图片生成/图生图/证件照-自动剪切-高清放大_2096498580654743553.json, 图片生成/图生图/证件照-自动剪切-高清放大_2096801265585049601.json, 图片生成/图生图/证件照生产+自动剪切+高清放大_1998995992928210946.json, 平台全量/证件照生成_1996125281284997122.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_46

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/002.Qwen编辑之王014.证件照生成+排版_2034655195208097794.json、图片生成/图生图/002.Qwen编辑之王015.证件照快速生成_2034656163802914818.json、图片生成/图生图/Qwen-image-Edit新版三图编辑_1971599377657688065.json、图片生成/图生图/Qwen-image-Edit新版双图万物迁移_1971595548304338946.json、图片生成/图生图/Qwen-image-Edit新版双图编辑人物姿态参考_1971504055640080386.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `Textbox`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 11/12 个有
- `ImageStitch` —— 10/12 个有
- `AddBackgroundNode` —— 8/12 个有
- `HivisionLayOutNode` —— 8/12 个有
- `HivisionNode` —— 8/12 个有
- `LaterProcessNode` —— 8/12 个有
- `PreviewImage` —— 8/12 个有
- `ZHHivisionParamsNode` —— 8/12 个有
- `SeedVR2LoadDiTModel` —— 6/12 个有
- `SeedVR2LoadVAEModel` —— 6/12 个有
- `SeedVR2VideoUpscaler` —— 6/12 个有
- `easy cleanGpuUsed` —— 6/12 个有
- `DWPreprocessor` —— 1/12 个有
- `GetNode` —— 1/12 个有
- `SetNode` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 12 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
