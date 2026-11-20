---
name: unknown_workflow_sampler_unet_vae_67
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.703286
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/KD_Qwen-Image-2.1-PE-文生图-提示词优化-加速版_2115349965794009089.json, 图片生成/文生图/QWEN IMAGE 2.1 文生图，带提示词增强_2103073606212341761.json, 图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2108811508326166529.json, 图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2109545902754066433.json, 图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2109573850085281794.json, 图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2111996327927312386.json, 图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2112074578649509889.json, 图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2112076292018495489.json, 图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2112081176390361090.json, 图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2112091885144727554.json, 图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2112093934708150274.json, 图片生成/文生图/Qwen Image2.1文生图（LTX2提示词扩写）2609_2106051218907942913.json, 图片生成/文生图/image_qwen_image_2_1_t2i_2101968376938717186.json, 视频生成/文生视频/Qwen_image_2.1_文生图_2104447797318733826.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_67

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/KD_Qwen-Image-2.1-PE-文生图-提示词优化-加速版_2115349965794009089.json、图片生成/文生图/QWEN IMAGE 2.1 文生图，带提示词增强_2103073606212341761.json、图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2108811508326166529.json、图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2109545902754066433.json、图片生成/文生图/Qwen Image 2.1-PE-文生图-提示词优化-加速版_2109573850085281794.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 12/14 个有
- `ComfySwitchNode` —— 11/14 个有
- `SaveImageAdvanced` —— 11/14 个有
- `easy showAnything` —— 11/14 个有
- `LoraLoaderModelOnly` —— 10/14 个有
- `PreviewImage` —— 10/14 个有
- `PrimitiveBoolean` —— 10/14 个有
- `RH_QwenImagePromptEnhancer` —— 10/14 个有
- `QwenImage21_T2IPromptRewrite` —— 9/14 个有
- `TextGenerateLTX2Prompt` —— 4/14 个有
- `PreviewAny` —— 3/14 个有
- `EmptyImage` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 14 | 14% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 14 | 100% |
| 高度 | 1024 | 1024 - 1024 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，14 个样本，取值分散，一致性仅 14%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，14 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，14 个样本，取值集中（一致性 100%）
- 高发问题（10/14 个样本）：Steps较低可能导致细节不足
