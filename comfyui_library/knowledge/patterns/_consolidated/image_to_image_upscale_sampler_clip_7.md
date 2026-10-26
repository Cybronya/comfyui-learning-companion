---
name: image_to_image_upscale_sampler_clip_7
type: Image To Image
frequency: 17
level: moderate
coverage: 0.709235
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ImpactInt, JoinStrings, KSampler, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/去ai-V1版本（人像+场景适用）_2051149008340561922.json, 图片生成/图生图/反推洗图工作流，图片去同质化免扣健康分2_2102430336633364482.json, 图片生成/图生图/图片去除Ai感_2066524004466384897.json, 图片生成/图生图/图片去除Ai感重绘放大工作流_2049669122480455682.json, 图片生成/图生图/图片反推洗图工作流，去同质化保健康分_2072580610752860161.json, 图片生成/图生图/最强还原人物真实度、去AI感_2077790045355995137.json, 图片生成/图生图/最强还原人物真实度、去AI感_2092808030168637441.json, 图片生成/图生图/最强还原人物真实度、去AI感_2093497000145805314.json, 图片生成/图生图/最强还原人物真实度、去AI感_2096456819844673537.json, 图片生成/图生图/最强还原人物真实度、去AI感_2111073643794100225.json, 图片生成/图生图/最强还原人物真实度去AI感自然修图工作流_2083006885749411842.json, 图片生成/图生图/最强还原人物真实度去AI感自然修图工作流_2083022220804321281.json, 图片生成/图生图/黄哥13期专用_2091511337003343874.json, 图片生成/文生图/qwen3反推提示词并生图_2057289354837581825.json, 图片生成/文生图/qwen3反推提示词并生图_2057720195904532481.json, 图片生成/文生图/图片去除Ai感工作流+全节点注释_2056746160630616066.json, 视频生成/图生视频/洗图加生视频_2070330640096120833.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_7

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/去ai-V1版本（人像+场景适用）_2051149008340561922.json、图片生成/图生图/反推洗图工作流，图片去同质化免扣健康分2_2102430336633364482.json、图片生成/图生图/图片去除Ai感_2066524004466384897.json、图片生成/图生图/图片去除Ai感重绘放大工作流_2049669122480455682.json、图片生成/图生图/图片反推洗图工作流，去同质化保健康分_2072580610752860161.json…）

- **类型**：Image To Image
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ImpactInt`
- `JoinStrings`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 16/17 个有
- `Qwen3_VQA` —— 16/17 个有
- `TextInput_` —— 16/17 个有
- `ImageScaleBy` —— 15/17 个有
- `ShowText|pysssss` —— 15/17 个有
- `Fast Groups Bypasser (rgthree)` —— 12/17 个有
- `Image Comparer (rgthree)` —— 12/17 个有
- `LayerUtility: PurgeVRAM` —— 11/17 个有
- `LoraLoaderModelOnly` —— 11/17 个有
- `孤海注释` —— 4/17 个有
- `CR Text` —— 3/17 个有
- `Float` —— 3/17 个有
- `PreviewImage` —— 3/17 个有
- `MemoryCleaner` —— 2/17 个有
- `easy saveText` —— 2/17 个有
- `GetNode` —— 1/17 个有
- `PrimitiveFloat` —— 1/17 个有
- `RHUploadZip` —— 1/17 个有
- `RH_RhartVideoSparkvideo20MultimodalVideo` —— 1/17 个有
- `SaveVideo` —— 1/17 个有
- `SetNode` —— 1/17 个有
- `忽略多组孤海` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 5 - 10 | 17 | 88% |
| Prompt 约束强度(CFG) | 1 | 0.9 - 2 | 17 | 77% |
| 采样算法 | euler | - | 17 | 94% |
| 调度器 | simple | - | 17 | 94% |
| 重绘幅度 | 0.7 | 0.1 - 0.7 | 17 | 76% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 5 - 10，17 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.9 - 2，17 个样本
- 采样算法 最常用 euler，17 个样本，一致性 94%
- 调度器 最常用 simple，17 个样本，一致性 94%
- 重绘幅度 中位数 0.7，观测区间 0.1 - 0.7，17 个样本
- 风险：Prompt 约束强度(CFG) 观测到 0.9，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
