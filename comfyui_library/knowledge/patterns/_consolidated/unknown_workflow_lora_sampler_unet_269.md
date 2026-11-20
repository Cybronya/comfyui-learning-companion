---
name: unknown_workflow_lora_sampler_unet_269
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.774667
common_nodes: [1hew_TextListToString, CLIPLoader, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, QwenMultiangleCameraNode, SaveImage, UNETLoader, VAEDecode, VAELoader, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/多角度自由生成_2043851163468046338.json, 图片生成/图生图/精准批量生成多角度图_2026491700318838785.json, 平台全量/最热Qwen2511+柯基大佬的镜头控制插件= 超强一致性无限多角度（任何物体都可）_2010187784581029890.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_269

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/多角度自由生成_2043851163468046338.json、图片生成/图生图/精准批量生成多角度图_2026491700318838785.json、平台全量/最热Qwen2511+柯基大佬的镜头控制插件= 超强一致性无限多角度（任何物体都可）_2010187784581029890.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `1hew_TextListToString`
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenMultiangleCameraNode`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `List of strings [Crystools]` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/3 个有
- `easy imageSize` —— 2/3 个有
- `DF_Get_image_size` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `QwenEditAdaptiveLongestEdge` —— 1/3 个有
- `QwenEditConfigPreparer` —— 1/3 个有
- `Text List Concatenate` —— 1/3 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 1/3 个有
- `easy promptList` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1280 | 512 - 1280 | 3 | 65% |
| 高度 | 720 | 512 - 720 | 3 | 85% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，观测区间 512 - 1280，3 个样本
- 高度 中位数 720，观测区间 512 - 720，3 个样本，取值集中（一致性 85%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
