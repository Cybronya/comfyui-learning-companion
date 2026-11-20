---
name: text_to_image_lora_sampler_clip_99
type: Text To Image
frequency: 13
level: weak
coverage: 0.891308
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfySwitchNode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, QwenImage21SageAttentionT8, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux3人像完美一致性图像编辑V1_2111090153166036993.json, 图片生成/图生图/Flux3人像完美一致性图像编辑V1_2114185496237797377.json, 图片生成/图生图/Qwen-Image 2.1多图编辑T8加速版｜批量改图效率翻倍_2113515421499478017.json, 图片生成/图生图/Remove模型Qwen Image 2.1 PE姿势编辑工作流，人物类特效擦除图生图_2106895128467173377.json, 图片生成/图生图/稳定加速版Qwen Image 2.1 PE姿势编辑 人物姿态精准控制_2109389400659554306.json, 图片生成/图生图/超级加速版Qwen Image 2.1 PE图像编辑工作流，图生图图像处理方案_2108287006626369538.json, 图片生成/文生图/Flux3人像完美一致性-多图图像编辑_2111145894010773506.json, 图片生成/文生图/Flux3人像完美一致性，多图图像编辑反推提示词_2111512061292404738.json, 图片生成/文生图/Qwen Image 2.1 PE文生图工作流，人像写真海报制作文本到图像方案_2107215861605031937.json, 图片生成/文生图/Qwen Image 2.1 PE文生图工作流，高质量文本到图像生成方案_2106466665084055554.json, 图片生成/文生图/Qwen Image 2.1 加速PE加in 版，文生图速度翻倍_2110472226297442305.json, 图片生成/文生图/（稳定加速版）Qwen Image 2.1 PE文生图｜快且稳的高质量出图_2104581684481060865.json, 视频生成/图生视频/Qwen_Image_2.1_加速PE加in_版，文生图速度翻倍_2113110553781686274.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_99

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Flux3人像完美一致性图像编辑V1_2111090153166036993.json、图片生成/图生图/Flux3人像完美一致性图像编辑V1_2114185496237797377.json、图片生成/图生图/Qwen-Image 2.1多图编辑T8加速版｜批量改图效率翻倍_2113515421499478017.json、图片生成/图生图/Remove模型Qwen Image 2.1 PE姿势编辑工作流，人物类特效擦除图生图_2106895128467173377.json、图片生成/图生图/稳定加速版Qwen Image 2.1 PE姿势编辑 人物姿态精准控制_2109389400659554306.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `QwenImage21SageAttentionT8`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `easy showAnything` —— 11/13 个有
- `JjkText` —— 10/13 个有
- `LoadImage` —— 10/13 个有
- `QwenImage21Cache` —— 10/13 个有
- `solarL_SaveImagesToZip` —— 10/13 个有
- `孤海注释` —— 10/13 个有
- `QwenPERewriteT8` —— 9/13 个有
- `KSamplerSelect` —— 8/13 个有
- `ManualSigmas` —— 8/13 个有
- `SamplerCustomAdvanced` —— 8/13 个有
- `QwenImage21BlockCacheT8` —— 7/13 个有
- `QwenImage21SpectrumT8` —— 7/13 个有
- `RandomNoise` —— 7/13 个有
- `BasicGuider` —— 4/13 个有
- `ConcatTextOfUtils` —— 4/13 个有
- `EmptyFlux2LatentImage` —— 4/13 个有
- `LoraLoaderBypassModelOnly` —— 4/13 个有
- `ReferenceMultiLatent` —— 4/13 个有
- `CFGGuider` —— 3/13 个有
- `PreviewImage` —— 2/13 个有
- `EmptyImage` —— 1/13 个有
- `LTXVConcatAVLatent` —— 1/13 个有
- `LTXVSeparateAVLatent` —— 1/13 个有
- `VAEEncode` —— 1/13 个有
- `VHS_VideoCombine` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 13 | 0% |
| 高度 | 80 | 80 - 1024 | 13 | 0% |
| 采样步数 | 4 | 4 - 8 | 13 | 66% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 13 | 60% |
| 采样算法 | er_sde | - | 13 | 77% |
| 调度器 | beta | - | 13 | 77% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，13 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，13 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 8，13 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，13 个样本
- 采样算法 最常用 er_sde，13 个样本，一致性 77%
- 调度器 最常用 beta，13 个样本，一致性 77%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（14/13 个样本）：Steps较低可能导致细节不足
