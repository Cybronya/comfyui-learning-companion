---
name: unknown_workflow_upscale_sampler_clip_45
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.813333
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, CR Text Input Switch (4 way), ConditioningZeroOut, DPMagicPrompt, KOOK_ImageCompression, KOOK_SaveJPGImage, KSampler (Efficient), LayerFilter: HDREffects, LoadImage, PreviewImage, PromptExpand, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SeedVarianceEnhancer, ShowText|pysssss, StringFunction|pysssss, Text Concatenate, Text Multiline, VAELoader, easy imageChooser, easy stylesSelector]
problems: []
missing: []
members: [图片生成/文生图/一键运行：Nunchaku Z-Image 文生图 动态提示词，反推，扩写，图像选择，高清放大_2005169988224905218.json, 图片生成/文生图/一键运行：Wz_image 文生图工作流（尺寸修改，反推，扩写，图像选择，高清放大、图片压缩）_2009910255966232578.json, 图片生成/文生图/一键运行：z-image 完整版（图片反推、高清放大、提示词扩写、动态提示词、高清压缩）_2002582226669826049.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_45

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/一键运行：Nunchaku Z-Image 文生图 动态提示词，反推，扩写，图像选择，高清放大_2005169988224905218.json、图片生成/文生图/一键运行：Wz_image 文生图工作流（尺寸修改，反推，扩写，图像选择，高清放大、图片压缩）_2009910255966232578.json、图片生成/文生图/一键运行：z-image 完整版（图片反推、高清放大、提示词扩写、动态提示词、高清压缩）_2002582226669826049.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Input Switch (4 way)`
- `ConditioningZeroOut`
- `DPMagicPrompt`
- `KOOK_ImageCompression`
- `KOOK_SaveJPGImage`
- `KSampler (Efficient)`
- `LayerFilter: HDREffects`
- `LoadImage`
- `PreviewImage`
- `PromptExpand`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SeedVarianceEnhancer`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `Text Concatenate`
- `Text Multiline`
- `VAELoader`
- `easy imageChooser`
- `easy stylesSelector`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `NunchakuZImageDiTLoader` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `ResolutionMaster` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 9 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1200 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 9，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1200，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
