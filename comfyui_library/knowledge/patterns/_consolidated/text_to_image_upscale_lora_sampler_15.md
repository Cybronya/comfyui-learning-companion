---
name: text_to_image_upscale_lora_sampler_15
type: Text To Image
frequency: 3
level: weak
coverage: 0.936
common_nodes: [Any Switch (rgthree), CFGNorm, CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageScaleToTotalPixels, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, PathchSageAttentionKJ, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, Text Load Line From File, Text Multiline, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy batchAnything, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen三视图多视图角色多视角｜正面侧面背面全出，人设立体呈现_2107352964183707650.json, 图片生成/图生图/Qwen角色三视图多视角生成｜一套图出全身角度，角色设计必备_2107317964277112833.json, 视频生成/图生视频/三视图_多视图_角色三视图_角色多视角图片生成_2087063594050605058.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_15

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen三视图多视图角色多视角｜正面侧面背面全出，人设立体呈现_2107352964183707650.json、图片生成/图生图/Qwen角色三视图多视角生成｜一套图出全身角度，角色设计必备_2107317964277112833.json、视频生成/图生视频/三视图_多视图_角色三视图_角色多视角图片生成_2087063594050605058.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `Text Load Line From File`
- `Text Multiline`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `solarL_SaveImagesToZip` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `RunningHub Deepcleaner` —— 1/3 个有
- `SeedVR2` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 720 | 3 | 0% |
| 高度 | 80 | 80 - 1440 | 3 | 0% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 3 | 51% |
| 采样算法 | er_sde | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 720，3 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1440，3 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，3 个样本
- 采样算法 最常用 er_sde，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
