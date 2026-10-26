---
name: text_to_image_lora_sampler_clip_391
type: Text To Image
frequency: 5
level: strong
coverage: 0.8562
common_nodes: [Anything Everywhere3, ApplyFBCacheOnModel, Bjornulf_FreeVRAM, CFGZeroStarAndInit, CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, EmptyLatentImage, FluxGuidance, Int, KSampler, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, SaveImage, ShowText|pysssss, TextInput_, UNETLoader, VAEDecode, VAELoader, easy forLoopEnd, easy forLoopStart, easy seed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/cos自拍_1919987623421743105.json, 图片生成/图生图/公孙离自拍_1920419864220209153.json, 图片生成/图生图/梦见月自拍_1920439776271601666.json, 图片生成/图生图/花火cos_1918976114239410178.json, 图片生成/图生图/躺地拍照2_1918867851929915393.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_391

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/cos自拍_1919987623421743105.json、图片生成/图生图/公孙离自拍_1920419864220209153.json、图片生成/图生图/梦见月自拍_1920439776271601666.json、图片生成/图生图/花火cos_1918976114239410178.json、图片生成/图生图/躺地拍照2_1918867851929915393.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `Anything Everywhere3`
- `ApplyFBCacheOnModel`
- `Bjornulf_FreeVRAM`
- `CFGZeroStarAndInit`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `Int`
- `KSampler`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `SaveImage`
- `ShowText|pysssss`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Molmo7BDbnb` —— 4/5 个有
- `Fast Groups Muter (rgthree)` —— 2/5 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/5 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 720 - 1920 | 5 | 66% |
| 高度 | 1920 | 1080 - 1920 | 5 | 77% |
| 采样步数 | 35 | 35 - 35 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 720 - 1920，5 个样本
- 高度 中位数 1920，观测区间 1080 - 1920，5 个样本
- 采样步数 中位数 35，观测区间 35 - 35，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
