---
name: unknown_workflow_lora_sampler_unet_261
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.87
common_nodes: [CLIPLoader, EmptyLatentImage, GetImageSize, ImageScaleToTotalPixels, ImageStitch, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, easy float]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_Edit_2511-新版双图编辑姿势迁移工作流_2005190961670090753.json, 图片生成/图生图/Qwen_Edit_2511-新版双图编辑模特换装工作流_2005192162713239554.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_261

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen_Edit_2511-新版双图编辑姿势迁移工作流_2005190961670090753.json、图片生成/图生图/Qwen_Edit_2511-新版双图编辑模特换装工作流_2005192162713239554.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy float`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 768 | - | 2 | 100% |
| 采样步数 | 6 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta57 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta57，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
