---
name: unknown_workflow_upscale_sampler_clip_5
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.814
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler (Efficient), LayerFilter: HDREffects, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, StringFunction|pysssss, easy imageChooser, easy stylesSelector]
problems: []
missing: []
members: [图片生成/文生图/一键运行：White_Marble-AIO 白玉工作流 反推、风格切换 、高清放大_2063094142267379714.json, 图片生成/文生图/一键运行：Z-IMAGE 文生图 图像反推，文案优化，高清放大，图像选择_1997560990004887553.json, 图片生成/文生图/一键运行：red-z-image 融合模型 反推 高清放大 文生图_1999794771981893634.json, 图片生成/文生图/一键运行：z-imgae 最简文生图 洗图  高清放大_1997558973375135745.json, 图片生成/文生图/一键运行：红潮 Pruned-Red-Z-image bf16 文生图 QWEN3 反推 放大_1999790696926150657.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_5

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/一键运行：White_Marble-AIO 白玉工作流 反推、风格切换 、高清放大_2063094142267379714.json、图片生成/文生图/一键运行：Z-IMAGE 文生图 图像反推，文案优化，高清放大，图像选择_1997560990004887553.json、图片生成/文生图/一键运行：red-z-image 融合模型 反推 高清放大 文生图_1999794771981893634.json、图片生成/文生图/一键运行：z-imgae 最简文生图 洗图  高清放大_1997558973375135745.json、图片生成/文生图/一键运行：红潮 Pruned-Red-Z-image bf16 文生图 QWEN3 反推 放大_1999790696926150657.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler (Efficient)`
- `LayerFilter: HDREffects`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `StringFunction|pysssss`
- `easy imageChooser`
- `easy stylesSelector`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/5 个有
- `ShowText|pysssss` —— 4/5 个有
- `Text Multiline` —— 4/5 个有
- `easy textSwitch` —— 4/5 个有
- `AILab_QwenVL` —— 3/5 个有
- `CLIPLoader` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `Text Concatenate` —— 3/5 个有
- `UNETLoader` —— 3/5 个有
- `VAELoader` —— 3/5 个有
- `CheckpointLoaderSimple` —— 2/5 个有
- `Anything Everywhere` —— 1/5 个有
- `CR Seed` —— 1/5 个有
- `ConditioningSetTimestepRange` —— 1/5 个有
- `Qwen3_VQA` —— 1/5 个有
- `SeedVarianceEnhancer` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 6 - 10 | 5 | 79% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | dpmpp_2m | - | 5 | 40% |
| 调度器 | sgm_uniform | - | 5 | 40% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 768 | 768 - 1080 | 5 | 85% |
| 高度 | 1024 | 1024 - 1920 | 5 | 70% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 9，观测区间 6 - 10，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，5 个样本，一致性 40%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 1080，5 个样本，取值集中（一致性 85%）
- 高度 中位数 1024，观测区间 1024 - 1920，5 个样本
