---
name: unknown_workflow_upscale_sampler_clip_25
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.804
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler (Efficient), LayerFilter: HDREffects, LoadImage, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, Text Multiline, easy imageChooser]
problems: []
missing: []
members: [图片生成/图生图/一键运行：Z-IMAGE 海报生成器文生图、图生图、高清放大_1997563539177029633.json, 图片生成/文生图/一键运行：Ovis  文生图 反推 高清放大_2000064549170671618.json, 图片生成/文生图/一键运行：White_Marble-AIO 白玉工作流 反推、风格切换 、高清放大_2063094142267379714.json, 图片生成/文生图/一键运行：Z-IMAGE 文生图 图像反推，文案优化，高清放大，图像选择_1997560990004887553.json, 图片生成/文生图/一键运行：red-z-image 融合模型 反推 高清放大 文生图_1999794771981893634.json, 图片生成/文生图/一键运行：红潮 Pruned-Red-Z-image bf16 文生图 QWEN3 反推 放大_1999790696926150657.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_25

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/一键运行：Z-IMAGE 海报生成器文生图、图生图、高清放大_1997563539177029633.json、图片生成/文生图/一键运行：Ovis  文生图 反推 高清放大_2000064549170671618.json、图片生成/文生图/一键运行：White_Marble-AIO 白玉工作流 反推、风格切换 、高清放大_2063094142267379714.json、图片生成/文生图/一键运行：Z-IMAGE 文生图 图像反推，文案优化，高清放大，图像选择_1997560990004887553.json、图片生成/文生图/一键运行：red-z-image 融合模型 反推 高清放大 文生图_1999794771981893634.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler (Efficient)`
- `LayerFilter: HDREffects`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `Text Multiline`
- `easy imageChooser`

**可变部分**（部分 workflow 才有）：
- `StringFunction|pysssss` —— 5/6 个有
- `easy stylesSelector` —— 5/6 个有
- `easy textSwitch` —— 5/6 个有
- `AILab_QwenVL` —— 4/6 个有
- `CLIPLoader` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `Text Concatenate` —— 4/6 个有
- `UNETLoader` —— 4/6 个有
- `VAELoader` —— 4/6 个有
- `Anything Everywhere` —— 2/6 个有
- `CheckpointLoaderSimple` —— 2/6 个有
- `ConditioningSetTimestepRange` —— 2/6 个有
- `Qwen3_VQA` —— 2/6 个有
- `CR Seed` —— 1/6 个有
- `SeedVarianceEnhancer` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 6 - 50 | 6 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 6 | 11% |
| 采样算法 | euler_ancestral | - | 6 | 50% |
| 调度器 | sgm_uniform | - | 6 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 768 | 728 - 1080 | 6 | 85% |
| 高度 | 1024 | 1024 - 1920 | 6 | 72% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 9，观测区间 6 - 50，6 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，6 个样本，取值分散，一致性仅 11%
- 采样算法 最常用 euler_ancestral，6 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，6 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 728 - 1080，6 个样本，取值集中（一致性 85%）
- 高度 中位数 1024，观测区间 1024 - 1920，6 个样本
