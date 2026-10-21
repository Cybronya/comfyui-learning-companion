---
name: unknown_workflow_upscale_sampler_clip_8
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.81525
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler (Efficient), LayerFilter: HDREffects, LoadImage, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, StringFunction|pysssss, Text Concatenate, Text Multiline, VAELoader, easy imageChooser, easy stylesSelector]
problems: []
missing: []
members: [图片生成/文生图/一键运行：Nunchaku Z-Image 文生图 动态提示词，反推，扩写，图像选择，高清放大_2005169988224905218.json, 图片生成/文生图/一键运行：Ovis  文生图 反推 高清放大_2000064549170671618.json, 图片生成/文生图/一键运行：Wz_image 文生图工作流（尺寸修改，反推，扩写，图像选择，高清放大、图片压缩）_2009910255966232578.json, 图片生成/文生图/一键运行：z-image 完整版（图片反推、高清放大、提示词扩写、动态提示词、高清压缩）_2002582226669826049.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_8

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/一键运行：Nunchaku Z-Image 文生图 动态提示词，反推，扩写，图像选择，高清放大_2005169988224905218.json、图片生成/文生图/一键运行：Ovis  文生图 反推 高清放大_2000064549170671618.json、图片生成/文生图/一键运行：Wz_image 文生图工作流（尺寸修改，反推，扩写，图像选择，高清放大、图片压缩）_2009910255966232578.json、图片生成/文生图/一键运行：z-image 完整版（图片反推、高清放大、提示词扩写、动态提示词、高清压缩）_2002582226669826049.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler (Efficient)`
- `LayerFilter: HDREffects`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `Text Concatenate`
- `Text Multiline`
- `VAELoader`
- `easy imageChooser`
- `easy stylesSelector`

**可变部分**（部分 workflow 才有）：
- `CR Text Input Switch (4 way)` —— 3/4 个有
- `DPMagicPrompt` —— 3/4 个有
- `EmptyLatentImage` —— 3/4 个有
- `KOOK_ImageCompression` —— 3/4 个有
- `KOOK_SaveJPGImage` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `PromptExpand` —— 3/4 个有
- `SeedVarianceEnhancer` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `NunchakuZImageDiTLoader` —— 2/4 个有
- `Anything Everywhere` —— 1/4 个有
- `ConditioningSetTimestepRange` —— 1/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `ResolutionMaster` —— 1/4 个有
- `easy textSwitch` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 50 | 4 | 8% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 4 | 13% |
| 采样算法 | euler_ancestral | - | 4 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 768 | 728 - 768 | 3 | 98% |
| 高度 | 1200 | 1024 - 1200 | 3 | 93% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 50，4 个样本，取值分散，一致性仅 8%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，4 个样本，取值分散，一致性仅 13%
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 728 - 768，3 个样本，取值集中（一致性 98%）
- 高度 中位数 1200，观测区间 1024 - 1200，3 个样本，取值集中（一致性 93%）
